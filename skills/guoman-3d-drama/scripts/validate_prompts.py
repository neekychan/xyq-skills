#!/usr/bin/env python3
"""Validate a pending visual generation batch. Never submits or edits media."""

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

STYLE_ANCHOR = "国漫3D渲染风格，高清3D渲染，高亮、低对比、轻雾化、柔光滤镜效果，高精度三维建模，细腻渲染，东方奇幻动画美术风格。"
VISUAL_KINDS = {"image", "image_edit", "video", "video_edit", "video_extend"}
VIDEO_KINDS = {"video", "video_edit", "video_extend"}
ASSET_KINDS = {"character", "scene", "prop", "keyframe", "frame", "video", "reference"}
SOURCES = {"project_generated", "user_provided", "user_designated"}
STATUSES = {"planned", "drafted", "generated", "accepted", "rejected", "stale"}
PURPOSE_KINDS = {
    "identity": {"character", "reference"},
    "costume": {"character", "reference"},
    "layout": {"scene", "frame", "reference"},
    "prop": {"prop", "reference"},
    "continuity": {"frame", "video", "keyframe"},
    "keyframe": {"keyframe"},
}


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate(data, base_dir):
    errors = []

    def fail(where, message):
        errors.append({"at": where, "message": message})

    def ids(value, where):
        if not isinstance(value, list) or not all(nonempty(x) for x in value):
            fail(where, "应为非空字符串 ID 的数组（允许空数组）。")
            return []
        if len(value) != len(set(value)):
            fail(where, "ID 重复。")
        return value

    if not isinstance(data, dict):
        return [{"at": "$", "message": "清单顶层必须是对象。"}]
    project = data.get("project")
    if not isinstance(project, dict):
        fail("project", "缺少项目对象。")
        project = {}
    scope = project.get("scope")
    if not nonempty(scope):
        fail("project.scope", "必须明确本次制作范围。")
    core_ids = ids(project.get("core_asset_ids"), "project.core_asset_ids")
    skip = project.get("skip_asset_images", {"enabled": False})
    skip_enabled = False
    if not isinstance(skip, dict) or not isinstance(skip.get("enabled"), bool):
        fail("project.skip_asset_images", "必须包含布尔 enabled。")
    elif skip["enabled"]:
        if not nonempty(skip.get("user_instruction")) or skip.get("scope") != scope:
            fail("project.skip_asset_images", "跳过出图须登记真实用户原话，且范围与当前 scope 一致。")
        else:
            skip_enabled = True

    asset_list = data.get("assets")
    if not isinstance(asset_list, list):
        fail("assets", "必须为资产数组。")
        asset_list = []
    assets = {}
    parents = {}
    for i, asset in enumerate(asset_list):
        where = f"assets[{i}]"
        if not isinstance(asset, dict) or not nonempty(asset.get("id")):
            fail(where, "资产必须为带非空 id 的对象。")
            continue
        aid = asset["id"]
        if aid in assets:
            fail(where, f"资产 ID 重复：{aid}")
        assets[aid] = asset
        if asset.get("kind") not in tuple(ASSET_KINDS):
            fail(where, "未知资产 kind。")
        if asset.get("source") not in tuple(SOURCES):
            fail(where, "资产来源不允许；禁止内置或外部风格图。")
        if asset.get("status") not in tuple(STATUSES):
            fail(where, "未知资产 status。")
        if not isinstance(asset.get("style_verified"), bool):
            fail(where, "style_verified 必须为真实验收后的布尔值。")
        parents[aid] = ids(asset.get("source_asset_ids", []), where + ".source_asset_ids")
        if asset.get("status") == "accepted":
            locator = asset.get("locator")
            if not nonempty(locator):
                fail(where, "accepted 资产缺少实际 locator。")
                continue
            try:
                uri = urlsplit(locator)
                if not uri.scheme or uri.scheme == "file":
                    path = Path(unquote(uri.path) if uri.scheme else locator).expanduser()
                    if not path.is_absolute():
                        path = base_dir / path
                    if not path.is_file() or path.stat().st_size == 0:
                        fail(where, f"本地资产文件不存在或为空：{locator}")
            except (ValueError, OSError) as exc:
                fail(where, f"无法读取 locator：{exc}")

    def require_asset(aid, where, style=False):
        asset = assets.get(aid)
        if asset is None:
            fail(where, f"未登记资产：{aid}")
            return
        if asset.get("status") != "accepted":
            fail(where, f"资产未验收或已失效：{aid}")
        if style and asset.get("style_verified") is not True:
            fail(where, f"资产未通过本风格验收：{aid}")

    visited = set()

    def check_lineage(aid, trail):
        if aid in trail:
            fail("assets.source_asset_ids", f"来源链有循环：{' -> '.join(trail + [aid])}")
            return
        if aid in visited:
            return
        for parent in parents.get(aid, []):
            if parent not in assets:
                fail(f"assets.{aid}.source_asset_ids", f"来源资产未登记：{parent}")
            else:
                check_lineage(parent, trail + [aid])
        visited.add(aid)

    for aid in assets:
        check_lineage(aid, [])
    for aid in core_ids:
        if aid not in assets:
            fail("project.core_asset_ids", f"核心资产未登记：{aid}")
        elif assets[aid].get("kind") not in ("character", "scene", "prop"):
            fail("project.core_asset_ids", f"核心资产应为角色、场景或道具图：{aid}")

    prompt_list = data.get("visual_prompts")
    if not isinstance(prompt_list, list) or not prompt_list:
        fail("visual_prompts", "必须有至少一条本次待提交视觉 prompt。")
        prompt_list = []
    seen = set()
    for i, item in enumerate(prompt_list):
        where = f"visual_prompts[{i}]"
        if not isinstance(item, dict):
            fail(where, "prompt 记录必须为对象。")
            continue
        pid = item.get("id")
        if not nonempty(pid):
            fail(where, "缺少非空 prompt id。")
        elif pid in seen:
            fail(where, f"prompt ID 重复：{pid}")
        else:
            seen.add(pid)
        kind = item.get("kind")
        if not isinstance(kind, str):
            kind = None
        if kind not in VISUAL_KINDS:
            fail(where, "未知视觉任务 kind；音频、纯截帧和转码不放入此列表。")
        prompt = item.get("prompt")
        if not isinstance(prompt, str) or not prompt.startswith(STYLE_ANCHOR):
            fail(where + ".prompt", "固定锚定词必须从第一个字符起逐字出现。")
        else:
            if prompt.count(STYLE_ANCHOR) != 1:
                fail(where + ".prompt", "固定锚定词应出现一次，不重复堆叠。")
            if not prompt[len(STYLE_ANCHOR):].strip():
                fail(where + ".prompt", "只有风格锚定词，缺少实际画面描述。")
        required = ids(item.get("required_asset_ids"), where + ".required_asset_ids")
        refs = item.get("references")
        if not isinstance(refs, list):
            fail(where + ".references", "必须为实际附件引用数组，文生图可为空。")
            refs = []
        direct_ids = []
        for j, ref in enumerate(refs):
            rw = f"{where}.references[{j}]"
            if not isinstance(ref, dict) or not nonempty(ref.get("asset_id")):
                fail(rw, "引用必须指定已登记 asset_id。")
                continue
            aid = ref["asset_id"]
            direct_ids.append(aid)
            purpose = ref.get("purpose")
            if not isinstance(purpose, str) or purpose not in PURPOSE_KINDS:
                fail(rw, "引用用途不允许；不能使用 style 或隐式风格参考。")
            elif aid in assets and assets[aid].get("kind") not in tuple(PURPOSE_KINDS[purpose]):
                fail(rw, "引用用途与资产 kind 不兼容。")
            require_asset(aid, rw, style=kind in VIDEO_KINDS)

        covered = set()

        def cover(aid):
            if aid in covered:
                return
            covered.add(aid)
            require_asset(aid, where + ".lineage")
            for parent in parents.get(aid, []):
                cover(parent)

        for aid in direct_ids:
            cover(aid)
        for aid in required:
            require_asset(aid, where + ".required_asset_ids", style=kind in VIDEO_KINDS)
            if aid not in covered:
                fail(where, f"必需资产未被实际绑定或未包含在关键帧来源链：{aid}")
        if kind == "image_edit" and not direct_ids:
            fail(where, "图像编辑必须绑定实际输入图。")
        if kind not in VIDEO_KINDS:
            continue
        if not skip_enabled:
            if not core_ids:
                fail(where, "视频前必须列齐本范围核心资产；没有跳过资产图的明确记录。")
            for aid in core_ids:
                require_asset(aid, where + ".core_assets", style=True)
        mode = item.get("binding_mode")
        if mode == "text_only":
            if not skip_enabled or refs or required:
                fail(where, "text_only 仅适用于明确跳过资产图、且无图像引用与必需图像绑定的任务。")
        elif mode == "single_keyframe":
            if len(refs) != 1 or len(direct_ids) != 1:
                fail(where, "单首帧模式必须只绑定一张已验收的单画面关键帧。")
            elif assets.get(direct_ids[0], {}).get("kind") != "keyframe" or refs[0].get("purpose") != "keyframe":
                fail(where, "首帧必须标为 keyframe，不能直接使用三视图/场景四宫格。")
        elif mode == "multi_reference":
            if not direct_ids:
                fail(where, "多参考视频必须有实际绑定。")
        else:
            fail(where, "视频必须指定有效 binding_mode。")
        if kind in {"video_edit", "video_extend"} and not any(
            assets.get(aid, {}).get("kind") == "video" for aid in direct_ids
        ):
            fail(where, "视频编辑/延长必须引用实际源视频。")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        path = args.manifest.expanduser().resolve()
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        errors = validate(data, path.parent)
    except (OSError, ValueError, RecursionError) as exc:
        print(json.dumps({"ok": False, "input_error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    count = len(data.get("visual_prompts", [])) if isinstance(data, dict) and isinstance(data.get("visual_prompts"), list) else 0
    print(json.dumps({"ok": not errors, "checked_prompts": count, "errors": errors}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
