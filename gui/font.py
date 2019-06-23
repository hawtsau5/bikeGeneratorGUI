import sys
import bimpy

font_dir = "gui/font/"
af = bimpy.add_font_from_file_ttf

class Fonts:
    def load_all_fonts(self):
        print("Loading Fonts...", end="     \r", file=sys.stderr)
        self.fonts = [
            {
                "cond"           : af(font_dir + "Condensed.ttf", i),
                "ext_bold_ital"  : af(font_dir + "ExtraBoldItalic.ttf", i)
            } 
            for i in range(12, 60)
        ]