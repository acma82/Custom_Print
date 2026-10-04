import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

tbl.title_bg  = 90
tbl.title_bold = True
tbl.title_italic = True
tbl.title_align  = cp.Align.LEFT

#-----------------------------------------------------------------------------------------
methods = [\
    ["Cursor",  "FontStyle"  ,  "FancyFormat"       ],
    ["jumpTo",  "start_style",  "print_fancy_format"],
    ["jumpxy",  "stop_style" ,  "reset_fancy_format"],
    ["moveTo",  "print_style"                       ],
    ["movexy"]]

people = [\
      ["Names",  "Lasts",   "Age", "A"],
      ["Pancho", "Melti",    50,   "1"],
      ["Javier", "Nangy",    32,   "2"],
      ["Melony", "Archi",    40,   "3"],
      ["Jose",   "Valvimar", 18,   "4"]]

tbl.title_msg = " List 1: Methods "
tbl.print_fancy_format(methods)

tbl.title_msg = " List 2: People "
tbl.print_fancy_format(people)


tbl.adj_space = 1
tbl.title_msg = " Merge List 2 to List 1 as COLUMNS posi = 8 "
merge_cols = pylo.merge(list_1=methods, list_2=people, posi=8, merge_by=pylo.Appending.COLUMNS) 

tbl.print_fancy_format(merge_cols)

tbl.title_msg = " Merge List 2 to List 1 as ROWS posi = -1 "
merge_rows = pylo.merge(list_1=methods, list_2=people, posi=-8, merge_by=pylo.Appending.ROWS)
tbl.print_fancy_format(merge_rows)



# # lista1 = ["hello", "adios"]
# lista1 = [["hello", "adios"]]
# lista1 = [["hello"], ["adios"]]

# lista2 = ["heaven", "hell"]
# # lista2 = [["heaven", "hell"]]
# # lista2 = [["heaven"], ["hell"]]
# tbl.title_msg = " Merge List people to List methods as COLUMNS posi=8 "

# merge_rows = pylo.merge(list_1=lista1, list_2=lista2, posi=8, merge_by=pylo.Appending.COLUMNS)
# tbl.print_fancy_format(merge_rows)
# print(merge_rows)

tbl.title_msg = " Merge List 2 to List 1 as ROWS posi = 2 "
merge_rows = pylo.merge(list_1=methods, list_2=people, posi=2, merge_by=pylo.Appending.ROWS)
tbl.print_fancy_format(merge_rows)




