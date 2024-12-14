import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()
tbl.bg_title = 90
tbl.bold_title = True
tbl.align_title = cp.Align.LEFT

#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
l1 = [1,5,8,4]
l2 = [[99,97,98,100]]
res = pylo.merge(list_1=l1, list_2=l2, posi=2, merge_by=pylo.Appending.COLUMNS)
print("re: ",res)
print("l1: ",l1)
print("l1: ",l2)

#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
# The main idea how to use it.
l4 = ["Country", "MEX", "USA", "CAN",  "SAL"]

l5 = [["Names",  "Lasts",   "Age"],
      ["Pancho", "Melti",    50  ],
      ["Javier", "Nangy",    32  ],
      ["Melony", "Archi",    40  ],
      ["Jose",   "Valvimar", 18  ]]

l6 = [["Country", "MEX",  "USA",  "CAN",  "SAL"],
      ["Code",    "012",  "234",  "781"        ]]
#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
resr = pylo.merge(list_1=l5, list_2=l6, posi=2, merge_by=pylo.Appending.ROWS)
tbl.msg_title = " Appending l6 as ROWS to l5 "
tbl.print_fancy_format(resr)

#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
resc = pylo.merge(list_1=l5, list_2=l6, posi=2, merge_by=pylo.Appending.COLUMNS)
print(resc)
tbl.msg_title = " Appending l6 as COLUMNS to l5 "
tbl.print_fancy_format(resc)
print(resc)

#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
tbl.msg_title = " Appending l4 as COLUMNS to l5 "
res = pylo.add_col(data=l5, col_data=l4, posi=2)
tbl.print_fancy_format(res)

#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
l7 = []
for n in reversed(l6): l7.append(n)
tbl.msg_title = " Appending l6 as COLUMNS to l5 REVERSE "
res = pylo.merge(list_1=l5, list_2=l7, posi=2, merge_by=pylo.Appending.COLUMNS)
tbl.print_fancy_format(res)
print(res)
#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
final = pylo.number(data=res, start_number=1, id_txt="ID", renumber=False, update=False)
tbl.print_fancy_format(final)

print(res)
