import fancyprint as fp
lst = fp.FancyFormat()
drw = fp.Draw()
crs = fp.Cursor()

drw.arrow()

print("  |-->")

lst.align_data=fp.Align.CENTER
lst.align_header = fp.Align.CENTER
lst.horizontal_separator_line_on = True
lst.horizontal_line_under_header_on = True

lst1 = [["A","B","C"],["10","8","7"],["0","4","-7"],["-1","-2","7"]]
lst.print_fancy_format(lst1,fp.Line_Style.SQUARE_BRACKETS)
lst2 = ["Vector Uno 3D"]
lst.print_fancy_format(lst2,fp.Line_Style.SQUARE_BRACKETS)

print("\u254E")
print("\u2574")