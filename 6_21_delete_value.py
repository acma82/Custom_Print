import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()
tbl.title_bg  = 90
tbl.title_bold = True
tbl.title_italic = True
tbl.title_align = cp.Align.CENTER


people = [\
      ["Names",  "Lasts",   "Age"],
      ["Pancho", "Melti",    50  ],
      ["Javier", "Nangy",    32  ],
      ["Melony", "Archi",    40  ],
      ["Jose",   "Valvimar", 18  ]]
tbl.title_msg = " Original People List "
tbl.print_fancy_format(people)

print(f"{cp.set_font(1,23,231)} Delete age item on header with case_sensitive=False, update=True. {cp.reset_font()}")
new_people = pylo.delete_value(data=people, value="age", case_sensitive=False, update=True)
print(new_people)
print(f"{cp.set_font(1,23,231)} Original {cp.reset_font()}")
print(people)

cp.ins_newline(2)


print(f"{cp.set_font(1,23,231)} Delete 3 case_sensitive=False, update=False. {cp.reset_font()}")
numbers = [[11,[10,3],12,3],[14,15,3],[12,3,3]]
new_numbers = pylo.delete_value(numbers, 3, False, False)
print("3 is gone: ",new_numbers)
print("Original : ",numbers)