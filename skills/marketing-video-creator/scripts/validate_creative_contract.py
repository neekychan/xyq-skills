#!/usr/bin/env python3
"""Deterministic pre-script checks for adaptive fusion, execution, and localization.

Input is one JSON object from a file path or stdin. Exit 0 means the
contract may proceed; exit 1 returns a list of plain-language problem
descriptions (Chinese) telling the reader exactly what to fix.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


LOCKED_AUTHORITIES = {"locked_by_user"}
THAI_CAST_VALUES = {"thai", "thai_local", "thailand_local"}
NON_PHYSICAL_OBJECT_STATES = {"digital", "virtual", "brand", "数字/虚拟", "品牌本身"}
HOOK_CARRIERS = {
    "spoken_line",
    "on_screen_text",
    "self_evident_visual",
    "distinctive_sound",
}
SILENT_OPENING_AUTHORITIES = {
    "user_locked_asmr",
    "user_locked_visual_hook",
    "user_locked_sound_hook",
}


def _norm(value: Any) -> str:
    return str(value or "").strip().lower()


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _selling_point_limit(duration: float) -> int:
    if duration <= 0:
        return 0
    if duration <= 8:
        return 1
    if duration <= 20:
        return 2
    if duration <= 30:
        return 3
    if duration <= 45:
        return 4
    if duration <= 60:
        return 5
    return max(5, int((duration + 14) // 15))


def validate_contract(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    sku_lock = contract.get("current_sku_lock") or {}
    if not sku_lock:
        errors.append("缺少 current_sku_lock（当前 SKU 锁定）：必须先锁定本次要拍的确切 SKU 形态。")
    elif _as_list(sku_lock.get("unresolved_conflicts")):
        errors.append("current_sku_lock 里还有未解决的冲突（unresolved_conflicts 非空）：先把 SKU 冲突消解掉再继续。")

    selected_program = contract.get("selected_content_program")
    program_lock = contract.get("program_lock") or {}
    if not selected_program:
        errors.append("缺少 selected_content_program（选定的内容方案）：必须先确定用哪一个内容方向。")
    if not program_lock:
        errors.append("缺少 program_lock（内容方案锁定）：选定方案后必须把它锁进 program_lock。")
    else:
        if _norm(program_lock.get("selected_content_program")) != _norm(selected_program):
            errors.append("program_lock 里的 selected_content_program 和顶层 selected_content_program 不一致：两者必须指向同一个方案。")
        source_coverage = program_lock.get("source_coverage") or {}
        if any(
            not source_coverage.get(field)
            for field in ("exact_sku_form", "duration_fit", "evidence_basis")
        ):
            errors.append("program_lock.source_coverage 不完整：exact_sku_form（确切 SKU 形态）、duration_fit（时长适配）、evidence_basis（证据依据）三项都必须有内容。")
        if not program_lock.get("main_proof_loop"):
            errors.append("program_lock 缺 main_proof_loop（主证明闭环）：必须写清主证明是怎么闭环的。")
        if float(program_lock.get("minimum_main_proof_seconds") or 0) <= 0:
            errors.append("program_lock.minimum_main_proof_seconds（主证明最短秒数）必须是正数。")
        if float(program_lock.get("auxiliary_seconds") or 0) > 1.2:
            errors.append("短视频里辅助信息秒数超标：program_lock.auxiliary_seconds 不能超过 1.2 秒。")
        if program_lock.get("ending_in_task") is not True:
            errors.append("program_lock.ending_in_task 必须为 true：结尾必须落在真实任务里，不能是静态定妆。")

    hook_claims = {_norm(item) for item in _as_list(contract.get("hook_claims"))}
    proof_answer_shot = contract.get("proof_answer_shot")

    if hook_claims and not proof_answer_shot:
        errors.append("开头抛了 hook_claims（钩子主张/悬念）却没有 proof_answer_shot（兑现镜头）:开头挖的坑后面必须有画面兑现。")

    if contract.get("sku_eligibility") is False:
        errors.append("选定方案和当前 SKU 冲突（sku_eligibility=false）:换方案或换 SKU。")
    if contract.get("asset_eligibility") is False:
        errors.append("选定方案缺少所需的素材/证据（asset_eligibility=false）:补齐素材证据或换方案。")
    if _as_list(contract.get("eligibility_conflicts")):
        errors.append("选定方案还有未解决的适配冲突（eligibility_conflicts 非空）:先消解再继续。")

    adaptive = contract.get("adaptive_fusion") or {}
    adaptive_required_fields = (
        "product_specific_tension",
        "opening_event",
        "opening_state",
        "product_causal_action",
        "proof_state",
        "end_state",
    )
    missing_adaptive = [field for field in adaptive_required_fields if not adaptive.get(field)]
    if missing_adaptive:
        errors.append(
            "adaptive_fusion（融合创意规格）缺少必填状态字段："
            + "、".join(missing_adaptive)
            + "。这些字段描述从开场到结尾的商品因果状态链，缺一不可。"
        )

    selected_modules = adaptive.get("selected_modules") or {}
    module_effects = adaptive.get("module_observable_effects") or {}
    module_cn = {"hook": "Hook（钩子）", "play": "Play（玩法）", "style": "Style（风格）"}
    for module in ("hook", "play", "style"):
        if bool(selected_modules.get(module)) and not module_effects.get(module):
            errors.append(
                f"选用了 {module_cn[module]} 模块，却没在 module_observable_effects 里写它的可观察落点：选用的每个模块都要有具体可见的落地效果。"
            )
    if bool(selected_modules.get("style")) and not adaptive.get("style_modulation"):
        errors.append("选用了 Style（风格）模块却没写 style_modulation（风格执行调制）：风格必须落到具体执行手法上。")
    if bool(adaptive.get("generic_template_skin_only")):
        errors.append("adaptive_fusion 只是给通用模板换皮（generic_template_skin_only=true）:必须真正重新编译成本商品的因果链，不能套壳。")

    human = contract.get("human_performance") or {}
    if bool(human.get("required")):
        required_human_fields = (
            "trigger_source",
            "observable_response",
            "action_intent",
            "result_response",
        )
        if any(not human.get(field) for field in required_human_fields):
            errors.append("有真人出镜（human_performance.required=true）时必须写清因果可观察表演：trigger_source（触发源）、observable_response（可见反应）、action_intent（动作意图）、result_response（结果反应）四项都要有。")
        if bool(human.get("emotion_labels_only")):
            errors.append("真人表演只写了情绪标签（emotion_labels_only=true）:必须改写成可拍摄的具体行为，不能只写“开心/惊讶”这类抽象情绪词。")

    spectacle = contract.get("spectacle_causality") or {}
    if bool(spectacle.get("required")):
        required_spectacle_fields = (
            "spectacle_mechanism",
            "product_relevant_force",
            "visible_effect_on_character_or_task",
            "counteraction_or_progression",
            "handoff_to_proof",
        )
        if any(not spectacle.get(field) for field in required_spectacle_fields):
            errors.append("奇观钩子（spectacle_causality.required=true）必须写清商品因果状态变化：spectacle_mechanism（奇观机制）、product_relevant_force（与商品相关的作用力）、visible_effect_on_character_or_task（对人物或任务的可见影响）、counteraction_or_progression（反作用或推进）、handoff_to_proof（交接到证明）五项都要有。")

    platform = _norm(contract.get("platform"))
    is_short_form_platform = "抖音" in platform or "tiktok" in platform
    duration = float(contract.get("duration_seconds") or 0)

    content_budget = contract.get("content_budget") or {}
    if duration > 0 and not content_budget:
        errors.append("缺少 content_budget（内容预算）：给定时长后必须规划卖点预算。")
    elif content_budget:
        main_points = int(content_budget.get("main_selling_points", 0))
        supporting_points = int(content_budget.get("supporting_selling_points", 0))
        auxiliary_beats = int(content_budget.get("auxiliary_information_beats", 0))
        active_ids = _as_list(content_budget.get("active_selling_point_ids"))
        if main_points != 1:
            errors.append(f"主卖点数量必须恰好是 1（当前 main_selling_points={main_points}）:一条视频只能有一个主卖点。")
        if main_points + supporting_points > _selling_point_limit(duration):
            errors.append(
                f"卖点总数超出时长预算：{duration:g} 秒最多允许 {_selling_point_limit(duration)} 个卖点，"
                f"当前主+辅共 {main_points + supporting_points} 个。"
            )
        if active_ids and len(active_ids) != main_points + supporting_points:
            errors.append(
                f"active_selling_point_ids 数量（{len(active_ids)}）和预算里主+辅卖点数（{main_points + supporting_points}）对不上。"
            )
        if 0 < duration <= 15 and auxiliary_beats > 2:
            errors.append(f"15 秒内辅助信息节拍超标：auxiliary_information_beats 最多 2，当前 {auxiliary_beats}。")

    object_state = _norm(sku_lock.get("object_state") or "physical")
    if object_state not in NON_PHYSICAL_OBJECT_STATES:
        entity = contract.get("product_entity_contract") or {}
        if not entity:
            errors.append("实体商品必须提供 product_entity_contract（商品实体合同）:用来锁定商品的数量、身份锚点和逐镜实体台账。")
        else:
            instance_budget = int(entity.get("instance_budget", 0))
            authority = _norm(entity.get("multi_instance_authority") or "none")
            signature = _as_list(entity.get("immutable_signature"))
            shots = _as_list(entity.get("shot_entity_ledger"))
            if instance_budget < 1:
                errors.append("product_entity_contract.instance_budget（商品实例数上限）必须是正数。")
            if instance_budget > 1 and authority == "none":
                errors.append("允许多个商品实例（instance_budget>1）却没有授权（multi_instance_authority=none）:多件同款商品同framing需要显式授权。")
            if len(signature) < 2:
                errors.append("商品身份锚点不足：immutable_signature（不可变外观特征）至少要有 2 个，才能保证跨镜不串味。")
            if not shots:
                errors.append("实体商品缺少 shot_entity_ledger（逐镜实体台账）:每个镜头出现几件商品、怎么拿都要登记。")
            for shot in shots:
                if not isinstance(shot, dict):
                    errors.append("shot_entity_ledger 里有格式错误的条目（不是对象）。")
                    continue
                count = int(shot.get("instance_count", 0))
                if count > instance_budget:
                    errors.append(f"某镜头商品实例数（{count}）超过 instance_budget（{instance_budget}）。")
                if count > 1 and authority == "none":
                    errors.append("某镜头出现多件同款商品却没有 multi_instance_authority 授权。")
                interactions = _as_list(shot.get("high_risk_interactions"))
                if len(interactions) > 1:
                    errors.append("某镜头堆叠了多个高风险商品交互（high_risk_interactions>1）:一个镜头里别同时做多个易穿帮的商品动作。")
                if interactions and not (
                    shot.get("left_hand_job") or shot.get("right_hand_job")
                ):
                    errors.append("某镜头有商品交互却没写左右手分工（left_hand_job / right_hand_job）:高风险交互要明确哪只手做什么。")
                similar_objects = _as_list(shot.get("other_similar_objects"))
                for item in similar_objects:
                    if not isinstance(item, dict) or not item.get("name") or not item.get("role"):
                        errors.append("某镜头里出现了含糊的相似物体（other_similar_objects 缺 name 或 role）:同框相似物要写清名字和作用，避免和商品混淆。")
                        break
                occlusion = float(shot.get("occlusion_ratio") or 0)
                if (occlusion > 0.4 or bool(shot.get("handoff_or_flip"))) and (
                    shot.get("reanchor_after_occlusion") is not True
                ):
                    errors.append("某镜头遮挡过半或有交接/翻转后没有重新锚定商品（reanchor_after_occlusion 未置 true）:遮挡后要重新确认还是同一件商品。")

    if is_short_form_platform and 0 < duration <= 20:
        execution = contract.get("short_form_execution") or {}
        first_event_at = float(execution.get("first_event_at_seconds", 999))
        product_task_at = float(execution.get("product_in_real_task_at_seconds", 999))
        beats = int(execution.get("effective_visual_beats", 0))
        native_scores = _as_list(execution.get("native_scores"))

        if first_event_at > 0.5:
            errors.append(f"短视频首帧没有有效事件：first_event_at_seconds 必须 ≤ 0.5 秒，当前 {first_event_at:g}。")

        opening = contract.get("opening_hook_contract") or {}
        if not opening:
            errors.append("短视频必须提供 opening_hook_contract（开场钩子合同）。")
        else:
            carrier = _norm(opening.get("hook_carrier"))
            first_information_at = float(
                opening.get("first_information_at_seconds", 999)
            )
            legible_at = float(
                opening.get("viewer_can_name_problem_or_desire_by_seconds", 999)
            )
            unframed_silence = float(opening.get("unframed_silence_seconds") or 0)
            silence_authority = _norm(opening.get("silent_opening_authority") or "none")
            if carrier not in HOOK_CARRIERS:
                errors.append("opening_hook_contract.hook_carrier（钩子信息载体）无效：必须是 spoken_line（口播）、on_screen_text（画面文字）、self_evident_visual（自明视觉）或 distinctive_sound（标志性声音）之一。")
            if first_information_at > 0.5:
                errors.append(f"开场信息出现太晚：first_information_at_seconds 必须 ≤ 0.5 秒，当前 {first_information_at:g}。")
            if legible_at > 1.0:
                errors.append(f"观众读不懂开场问题/欲望：viewer_can_name_problem_or_desire_by_seconds 必须 ≤ 1.0 秒，当前 {legible_at:g}。")
            if (
                unframed_silence > 0.4
                and silence_authority not in SILENT_OPENING_AUTHORITIES
            ):
                errors.append("未经授权的开场留白：unframed_silence_seconds 超过 0.4 秒且没有 silent_opening_authority 授权。")
            if carrier == "spoken_line" and not opening.get("spoken_hook"):
                errors.append("hook_carrier 是 spoken_line（口播）却没写 spoken_hook（口播钩子台词）。")
            if carrier == "on_screen_text" and not opening.get("on_screen_hook"):
                errors.append("hook_carrier 是 on_screen_text（画面文字）却没写 on_screen_hook（画面钩子文字）。")
            if carrier == "self_evident_visual" and not opening.get(
                "visible_contrast_or_consequence"
            ):
                errors.append("hook_carrier 是 self_evident_visual（自明视觉）却没写 visible_contrast_or_consequence（可见的对比或后果）。")
            if carrier == "distinctive_sound" and not opening.get(
                "distinctive_sound_and_causal_result"
            ):
                errors.append("hook_carrier 是 distinctive_sound（标志性声音）却没写 distinctive_sound_and_causal_result（标志性声音及其因果结果）。")

        if product_task_at > 3.0:
            errors.append(f"商品没在 3 秒内进入真实任务：product_in_real_task_at_seconds 必须 ≤ 3.0 秒，当前 {product_task_at:g}。")
        if bool(execution.get("static_product_intro")):
            errors.append("static_product_intro=true：静态摆拍式商品亮相不算原生执行，商品要在真实使用中出场。")
        if duration <= 15 and not 5 <= beats <= 8:
            errors.append(f"15 秒内视频需要 5-8 个有效视觉节拍，当前 effective_visual_beats={beats}。")
        if len(native_scores) != 8:
            errors.append(f"原生执行评分必须是 8 项，当前 native_scores 有 {len(native_scores)} 项。")
        else:
            parsed_scores = [int(score) for score in native_scores]
            if any(score < 0 or score > 2 for score in parsed_scores):
                errors.append("native_scores 每项必须是 0-2 分。")
            elif 0 in parsed_scores or sum(parsed_scores) < 12:
                errors.append(f"原生执行评分不达标：不能有 0 分项，且总分要 ≥ 12（当前总分 {sum(parsed_scores)}）。")
        if execution.get("platform_execution_floor_preserved") is not True:
            errors.append("short_form_execution.platform_execution_floor_preserved 必须为 true：不能为了创意牺牲平台执行底线。")
        if not execution.get("style_native_adapter"):
            errors.append("短视频缺 style_native_adapter（风格原生适配器）:风格要用平台原生的方式落地。")
        speech = contract.get("speech_rhythm_contract") or {}
        if not speech:
            errors.append("短视频必须提供 speech_rhythm_contract（语速节奏合同）。")
        elif _norm(speech.get("language")) in {"zh", "中文", "chinese"}:
            profile = _norm(speech.get("profile"))
            target_rate = float(speech.get("target_rate") or 0)
            max_rate = float(speech.get("max_rate") or 0)
            if profile == "douyin_native" and not 5.5 <= target_rate <= 6.5:
                errors.append(f"抖音原生中文语速超出范围：target_rate 应在 5.5-6.5 字/秒，当前 {target_rate:g}。")
            if max_rate > 7.2:
                errors.append(f"口播语速上限超过人类短视频天花板：max_rate 不能超过 7.2 字/秒，当前 {max_rate:g}。")
            for line in _as_list(speech.get("line_budgets")):
                if isinstance(line, dict) and float(line.get("rate") or 0) > max_rate:
                    errors.append("有台词的语速超过了自己声明的 max_rate 上限。")
        if float(execution.get("main_proof_seconds") or 0) < float(
            program_lock.get("minimum_main_proof_seconds") or 0
        ):
            errors.append(
                f"主证明时长不足：short_form_execution.main_proof_seconds（{execution.get('main_proof_seconds')}）"
                f"低于 program_lock.minimum_main_proof_seconds（{program_lock.get('minimum_main_proof_seconds')}）。"
            )

        scene_sequence = [_norm(item) for item in _as_list(execution.get("scene_sequence"))]
        circular_locked = bool(execution.get("user_locked_circular_structure"))
        seen: set[str] = set()
        previous = ""
        for scene in scene_sequence:
            if not scene or scene == previous:
                previous = scene or previous
                continue
            if scene in seen and not circular_locked:
                errors.append("短视频里出现了场景回访（离开某场景后又切回去）:短视频禁止回访旧场景，除非用户锁定了环形结构。")
                break
            seen.add(scene)
            previous = scene

    localization = contract.get("localization") or {}
    market = _norm(localization.get("target_market"))
    spoken_language = _norm(localization.get("spoken_language"))
    authority = _norm(localization.get("character_reference_authority"))
    cast = _norm(localization.get("cast_localization"))
    thai_default = market in {"thailand", "泰国"} or (
        spoken_language in {"thai", "泰语"} and "tiktok" in platform
    )
    if thai_default and authority not in LOCKED_AUTHORITIES and cast not in THAI_CAST_VALUES:
        errors.append("面向泰国市场/泰语内容默认要用泰国本地化选角：localization.cast_localization 需设为泰国本地演员，或由用户显式锁定其它选角（character_reference_authority=locked_by_user）。")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("contract", nargs="?", help="JSON contract path; stdin when omitted")
    args = parser.parse_args()

    if args.contract:
        payload = Path(args.contract).read_text(encoding="utf-8")
    else:
        payload = sys.stdin.read()

    contract = json.loads(payload)
    errors = validate_contract(contract)
    result = {"ok": not errors, "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
