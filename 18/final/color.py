# getting the colors for the Hirst painting

import colorgram  # type: ignore

rgb_colors = []
colors = colorgram.extract('demo.jpeg' , 35)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)