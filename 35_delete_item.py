import source.custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()
tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True
tbl.align_title = cp.Align.CENTER


people = [\
      ["Names",  "Lasts",   "Age"],
      ["Pancho", "Melti",    50  ],
      ["Javier", "Nangy",    32  ],
      ["Melony", "Archi",    40  ],
      ["Jose",   "Valvimar", 18  ]]
tbl.msg_title = " Original People List "
tbl.print_fancy_format(people)

print(f"{cp.set_font(1,23,231)} Delete age item on header with case_sensitive=False. {cp.reset_font()}")
new_people = pylo.delete_item(data=people, ref="age", case_sensitive=False, update=True)
print(new_people)
print(f"{cp.set_font(1,23,231)} update=True {cp.reset_font()}")
print(people)

cp.ins_newline(2)

numbers = [[11,[10,3],12,3],[14,15,3],[12,3,3]]
new_numbers = pylo.delete_item(numbers, 3, False, False)
print("3 is gone: ",new_numbers)
print("Original : ",numbers)