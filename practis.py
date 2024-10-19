import fancyprint as fp
lista = fp.FancyFormat()
crs = fp.Cursor()
pen = fp.Pen()

# pen.bg_draw_line = 14
# pen.fg_draw_line = 0
# pen.bold_draw_line = True



pen.draw_line(size=25, layout=fp.Layout.HORIZONTAL, tail="\N{BLACK CIRCLE}",\
               body=fp.Unicode.EM_DASH, head="\u21FE")#head=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT)


pen.draw_line(size=5,layout=fp.Layout.HORIZONTAL)
print()
pen.draw_line(size=10, layout=fp.Layout.VERTICAL, tail=fp.Unicode.BLACK_UP_POINTING_TRIANGLE, body="\u2502", head=fp.Unicode.BLACK_DOWN_POINTING_TRIANGLE)


print(fp.set_font(1,14,0))
print("\N{BLACK CIRCLE}")
print(fp.reset_font())
# Box Drawings
# Geometric Shapes
# Miscellaneous Symbols

print(f"\u2014{fp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE}")



