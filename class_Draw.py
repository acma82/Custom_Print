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
lst.print_fancy_format(lst1,fp.Line_Style.SQR_BRACKETS)
lst2 = ["Vector Uno 3D"]
lst.print_fancy_format(lst2,fp.Line_Style.SQR_BRACKETS)

print("\u254E")
print("\u2574")

print(fp.set_font(1,11,21)+ " Python is " + fp.set_font(0,1) +\
       " Wonderful."+fp.reset_font())


# print(fp.set_font(blinking=True) + "Hello" + fp.reset_font())

lst.print_fancy_format("Miguel",fp.Line_Style.DASH)


def str2list(my_str):
   tempo_list = []
   for n in my_str:
      tempo_list.append(n)

   #tempo_list.append(my_str)
   return tempo_list


dato = str2list("Miguel")
print(dato)