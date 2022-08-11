import colorsys as cs


def color_correct(input_color, hue=0.0, sat=1.0, val=0.0):
    r, g, b = (float(i) / 255 for i in input_color)
    h, s, v = cs.rgb_to_hsv(r, g, b)
    color = cs.hsv_to_rgb(h + hue, sat, v * val)
    c = tuple(int(i * 255) for i in color)
    return f"rgb({c[0]},{c[1]},{c[2]})"


print(color_correct((10, 10, 10), hue=0.4, sat=1, val=0.4))


class OGenericStyleSheet:
    def __init__(self, corner_radius=15, font='gill', font_style='',
                 font_size=15, padding=(3, 3), margin=(3, 3)):
        self.corner_radius = corner_radius
        self.padding = padding
        self.margin = margin
        self.base_color = (0, 100, 200)
        self.main_bg_color = color_correct(self.base_color, sat=0.1, val=0.15)
        self.button_color = color_correct(self.base_color, sat=0.9, val=0.5)
        self.button_color_hover = color_correct(self.base_color, sat=1.0, val=0.6)
        self.button_color_click = color_correct(self.base_color, sat=0.8, val=1.2)
        self.font_color_main = color_correct((255, 255, 255), val=0.6, sat=0.0)
        self.fonts_dict = dict(arial="Arial", verdana="Verdana",
                               helvetica="Helvetica", tahoma="Tahoma",
                               trebuchet="Trebuchet MS", newroman="Times New Roman",
                               gill="Gill Sans", georgia="Georgia",
                               garamond="Garamond", courier="Courier New")

        self.font = self.fonts_dict[font]
        self.font_size = font_size
        self.font_style = font_style

    def padding_and_margin(self):
        out = (f"padding: {self.padding[0]}px {self.padding[1]}px;"
               f"margin: {self.margin[0]}px {self.margin[1]}px;")
        return out

    def flat_and_hover(self):
        out = f"""*{{font: {self.font_size}pt {self.font};
color: {self.font_color_main};
border-radius: {self.corner_radius}px;
{self.padding_and_margin()}
background: {self.button_color};}}
*:hover{{background: {self.button_color_hover};}}
*:pressed{{background: {self.button_color_click};}}
"""
        return out

    def simple_with_bg(self):
        out = f"""
font: {self.font_size}pt {self.font};
color: {self.font_color_main};
background: {self.button_color};
border-radius: {self.corner_radius}px;
{self.padding_and_margin()}
"""
        return out

    def simple_no_bg(self):
        out = f"""
font: {self.font_size}pt {self.font};
color: {self.font_color_main};
{self.padding_and_margin()}
"""
        return out
