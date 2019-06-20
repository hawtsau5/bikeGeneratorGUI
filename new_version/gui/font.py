import sys
import bimpy

font_dir = "new_version/gui/font/"
af = bimpy.add_font_from_file_ttf

class Fonts:
    def load_all_fonts(self):
        print("Loading Fonts...", end="     \r", file=sys.stderr)
        self.fonts = [
            {
                "bold"           : af(font_dir + "Bold.ttf", i),
                "bold_cond"      : af(font_dir + "BoldCondensed.ttf", i),
                "bold_ital"      : af(font_dir + "BoldItalic.ttf", i),
                "cond"           : af(font_dir + "Condensed.ttf", i),
                "ext_bold_ital"  : af(font_dir + "ExtraBoldItalic.ttf", i),
                "ital"           : af(font_dir + "Italic.ttf", i),
                "light"          : af(font_dir + "Light.ttf", i),
                "light_ital"     : af(font_dir + "LightItalic.ttf", i),
                "medium"         : af(font_dir + "Medium.ttf", i),
                "ult_light"      : af(font_dir + "UltraLight.ttf", i),
                "ult_light_ital" : af(font_dir + "UltraLightItalic.ttf", i),
                "yu"             : af(font_dir + "Yu.ttf", i),
                "inserat"        : af(font_dir + "Inserat.otf", i)
            } 
            for i in range(66)
        ]