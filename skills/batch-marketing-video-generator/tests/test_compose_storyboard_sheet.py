import importlib.util
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

from PIL import Image


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "compose_storyboard_sheet.py"
SPEC = importlib.util.spec_from_file_location("compose_storyboard_sheet", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ReplacementImageTests(unittest.TestCase):
    def test_overlays_single_image_after_seedream_grid_split(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            grid_path = temp / "grid.png"
            replacement_path = temp / "shot-02-v2.png"
            grid = Image.new("RGB", (300, 300), "black")
            colors = ["#110000", "#220000", "#330000", "#440000", "#550000"]
            for index, color in enumerate(colors):
                left = (index % 3) * 100
                top = (index // 3) * 100
                grid.paste(Image.new("RGB", (100, 100), color), (left, top))
            grid.save(grid_path)
            Image.new("RGB", (40, 120), "#abcdef").save(replacement_path)

            args = Namespace(
                grid_image=grid_path,
                grid_images=None,
                grid_rows=3,
                grid_cols=3,
                grid_margin=0,
                grid_gap=0,
                grid_trim_ratio=0,
                grid_shot_counts=[5],
                images=None,
            )
            manifest = {
                "shots": [
                    {"number": 1},
                    {"number": 2, "replacement_image": str(replacement_path)},
                    {"number": 3},
                    {"number": 4},
                    {"number": 5},
                ]
            }

            original, source_mode = MODULE.source_images(args, manifest)
            resolved, replaced = MODULE.apply_replacement_images(
                original, manifest["shots"], "contain"
            )

            self.assertEqual(source_mode, "grid")
            self.assertEqual(replaced, [2])
            self.assertEqual(resolved[1].size, original[1].size)
            self.assertEqual(resolved[1].getpixel((50, 50)), (171, 205, 239))
            self.assertEqual(resolved[0].getpixel((50, 50)), (17, 0, 0))
            self.assertEqual(resolved[2].getpixel((50, 50)), (51, 0, 0))

    def test_replaces_multiple_images_at_original_sizes_with_contain(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            portrait = temp / "portrait.png"
            landscape = temp / "landscape.png"
            Image.new("RGB", (20, 100), "#ff0000").save(portrait)
            Image.new("RGB", (100, 20), "#00ff00").save(landscape)

            base = [
                Image.new("RGB", (120, 80), "#111111"),
                Image.new("RGB", (90, 150), "#222222"),
                Image.new("RGB", (64, 64), "#333333"),
            ]
            shots = [
                {"number": 1, "replacement_image": str(portrait)},
                {"number": 2, "replacement_image": str(landscape)},
                {"number": 3},
            ]

            resolved, replaced = MODULE.apply_replacement_images(base, shots, "contain")

            self.assertEqual(replaced, [1, 2])
            self.assertEqual([image.size for image in resolved], [image.size for image in base])
            self.assertEqual(resolved[0].getpixel((60, 40)), (255, 0, 0))
            self.assertEqual(resolved[0].getpixel((0, 0)), (23, 27, 29))
            self.assertEqual(resolved[1].getpixel((45, 75)), (0, 255, 0))
            self.assertIs(resolved[2], base[2])

    def test_cover_fills_original_size_without_stretching_canvas(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            replacement_path = Path(temp_dir) / "replacement.png"
            Image.new("RGB", (30, 120), "#336699").save(replacement_path)
            base = [Image.new("RGB", (160, 90), "black")]

            resolved, replaced = MODULE.apply_replacement_images(
                base,
                [{"number": 7, "replacement_image": str(replacement_path)}],
                "cover",
            )

            self.assertEqual(replaced, [7])
            self.assertEqual(resolved[0].size, (160, 90))
            self.assertEqual(resolved[0].getpixel((0, 0)), (51, 102, 153))

    def test_updated_speaker_line_is_used_in_annotation_fields(self):
        fields = dict(
            MODULE.annotation_fields(
                {
                    "visual": "新版画面",
                    "transition": "切入下一镜",
                    "audio": "新版音效",
                    "voiceover": "小林｜对白｜你看这里。；阿美｜对白｜果然更干净。",
                }
            )
        )

        self.assertEqual(
            fields["有声内容"],
            "小林｜对白｜你看这里。；阿美｜对白｜果然更干净。",
        )


class DividerSemanticsTests(unittest.TestCase):
    @staticmethod
    def shot(number):
        return {
            "number": number,
            "timecode": "00:00-00:01",
            "shot_size": "中景",
            "purpose": "展示商品",
            "visual": "角色展示商品",
            "transition": "直接切换",
            "audio": "轻音乐",
            "voiceover": "旁白｜旁白｜介绍商品。",
        }

    def compose(self, temp, ratio):
        output = temp / f"sheet-{ratio.replace(':', '-')}.png"
        result = MODULE.compose_sheet(
            [Image.new("RGB", (320, 180), "#aa0000"), Image.new("RGB", (320, 180), "#00aa00")],
            [self.shot(1), self.shot(2)],
            {"整体说明": "分隔线语义测试"},
            output,
            MODULE.resolve_font(None),
            "cover",
            None,
            "individual",
            ratio,
        )
        return Image.open(output).convert("RGB"), result

    def test_landscape_uses_thick_horizontal_shot_divider_and_thin_vertical_content_divider(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            sheet, result = self.compose(Path(temp_dir), "16:9")
            divider = (48, 56, 60)
            frame_width, row_height = result["frame_size"]

            self.assertEqual(sheet.getpixel((10, row_height - 5)), divider)
            self.assertEqual(sheet.getpixel((10, row_height + 4)), divider)
            self.assertNotEqual(sheet.getpixel((10, row_height - 6)), divider)
            self.assertNotEqual(sheet.getpixel((10, row_height + 5)), divider)

            self.assertEqual(sheet.getpixel((frame_width - 3, 200)), divider)
            self.assertEqual(sheet.getpixel((frame_width + 2, 200)), divider)
            self.assertNotEqual(sheet.getpixel((frame_width - 4, 200)), divider)
            self.assertNotEqual(sheet.getpixel((frame_width + 3, 200)), divider)

    def test_portrait_uses_thick_vertical_shot_divider_and_thin_horizontal_content_divider(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            sheet, result = self.compose(Path(temp_dir), "9:16")
            divider = (48, 56, 60)
            card_width, frame_height = result["frame_size"]
            start_x = (sheet.width - (2 * card_width)) // 2
            shot_boundary = start_x + card_width

            self.assertEqual(sheet.getpixel((shot_boundary - 5, 200)), divider)
            self.assertEqual(sheet.getpixel((shot_boundary + 4, 200)), divider)
            self.assertNotEqual(sheet.getpixel((shot_boundary - 6, 200)), divider)
            self.assertNotEqual(sheet.getpixel((shot_boundary + 5, 200)), divider)

            content_x = start_x + 200
            self.assertEqual(sheet.getpixel((content_x, frame_height - 3)), divider)
            self.assertEqual(sheet.getpixel((content_x, frame_height + 2)), divider)
            self.assertNotEqual(sheet.getpixel((content_x, frame_height - 4)), divider)
            self.assertNotEqual(sheet.getpixel((content_x, frame_height + 3)), divider)


if __name__ == "__main__":
    unittest.main()
