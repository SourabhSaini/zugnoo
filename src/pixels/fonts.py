from rgbmatrix import graphics


class Font:
    def __init__(self):
        self.font = graphics.Font()

        self.font_features = {
                'xxxlargeb': { 'x': 9, 'y': 15, 'extra': 'B'},
                'xxlargeb': { 'x': 8, 'y': 13, 'extra': 'B'},
                'xxlarge': { 'x': 8, 'y': 13, 'extra': ''},
                'xlargeb': { 'x': 7, 'y': 14, 'extra': 'B'},
                'xlarge': { 'x': 7, 'y': 14, 'extra': ''},
                'largeb': { 'x': 6, 'y': 13, 'extra': 'B'},
                'large': { 'x': 6, 'y': 12, 'extra': ''},
                'medium': { 'x': 5, 'y': 8, 'extra': ''},
                'small': { 'x': 5, 'y': 7, 'extra': '' },
                'xsmall': { 'x': 4, 'y': 6, 'extra': '' },
        }

    def features(self, size):
        return self.font_features[size]

    def file(self, size):
        return self.get_font_file(self.features(size))

    def get_font_file(self, size):
        font_path = f"fonts/{size['x']}x{size['y']}{size['extra']}.bdf"
        self.font.LoadFont(font_path)
        return self.font

