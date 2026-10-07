import custom_print as cp
pylo = cp.PyLO()

# lst = [["1454545454"],["Migue"], ["acma"], ["Miguelito"]]       # multiple_items_multiple_rows  -> works
# lst = [["Migue","44545454", "acma", "Miguelito"]]         # multiple_items_one_row  -> works

# lst = [["Python",  "th",  "on"],       # 0.  Letters
#         [True,  True,  True ],         # 1.  Bold
#         [152,   115,   202  ],         # 2.  bg
#         [16,    177,    23  ],         # 3.  Fg
#         [22,     33,    10  ],         # 11. left_space
#         [21,     33,    11  ],         # 12. middle_space
#         [24,     33,     1  ]]         # 13. right_space

lst = ["acma2",4787878,"Migue", "acma", "Miguelito"]         # multiple_items_no_row   ->  works


print()
print(f"{cp.set_font(1,202,231)} padding_list = pylo.padding_list(data=lst, align=cp.Align.JUSTIFY, {cp.reset_font()}\n"\
      f"{cp.set_font(1,202,231)} padding_size=1, left_pad=4, right_pad=1)                           {cp.reset_font()}\n")

padding_list = pylo.padding_list(data=lst, align=cp.Align.JUSTIFY, padding_size=1, left_pad=4, right_pad=1)
print(padding_list)
