from PIL import Image


class PaletteMaker:

    def hex_to_rgb(self, value):
        """Return (red, green, blue) for the color given as #rrggbb."""
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    def rgb_to_hex(self, red, green, blue):
        """Return color as #rrggbb for the given color values."""
        return '#%02x%02x%02x' % (red, green, blue)

    def analyze_image(self, image):
        img = Image.open(image)
        img = img.quantize(colors=4, kmeans=4).convert('RGB')
        n_dom_colors = 4
        dom_colors = sorted(img.getcolors(2 ** 24), reverse=True)[:n_dom_colors]
        extracted_tuples = [item[1] for item in dom_colors]
        hex_list = []
        for rbg_tuple in extracted_tuples:
            hex = self.rgb_to_hex(*rbg_tuple)
            print(hex)
            hex_list.append(hex)
        return hex_list

    def get_hex_codes(self, extracted_tuples):
        hex_list = []
        for rbg_tuple in extracted_tuples:
            hex = self.rgb_to_hex(*rbg_tuple)
            print(hex)
            hex_list.append(hex)
            return hex_list
