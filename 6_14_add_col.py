import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

tbl.title_bg = 90
tbl.title_align = cp.Align.LEFT

#------------------------------------------------------------------------------
# Adding list_2 as one col in list_1
tbl.title_msg = " List_1 "
list_1 = [["Header_1","Header_2"],["R1_C1","R1_C2"], ["R2_C1","R2_C2"]]
tbl.print_fancy_format(list_1)

tbl.title_msg = " List_2 to be added to List_1 as Col, pos=1 "
list_2 = ["New_Header",   "New_Row_Col",  "New_Row_Col"]
tbl.print_fancy_format(list_2)

tbl.title_msg = " New Complete List_1_2 "
tbl.footnote_msg = " data=list_1, col_data=list_2, posi=1 "
list_1_2 = pylo.add_col(data=list_1, col_data=list_2, posi=1)
tbl.print_fancy_format(list_1_2)
tbl.footnote_msg = ""

#------------------------------------------------------------------------------
# Adding list_4 as columns in list_3
cp.ins_newline(2)
tbl.title_msg = ""
tbl.title_bg = 1

tbl.title_msg = " List 3 "
list_3  = [["Header_1","Header_2","Header_3"],
           ["R1_C1",   "R1_C2",   "R1_C3"],
           ["R2_C1",   "R2_C2",   "R2_C3"]]
tbl.print_fancy_format(list_3)

tbl.title_msg = " List 4 "
list_4 = [["R3_C1","R3_C2","R3_C3"],
          ["R4_C1","R4_C2","R4_C3"]]
tbl.print_fancy_format(list_4)

# add cols into another list merge in horizontal
tmp = list_3
for rows in range(len(list_4)):
    tmp = pylo.add_col(data=tmp, col_data=list_4[rows], posi=len(tmp)+1)

tbl.print_fancy_format(tmp, cp.Line_Style.DOUBLE_LINE)

tmp = list_3
for rows in range(len(list_4)):
    tmp = pylo.add_col(data=tmp, col_data=list_4[rows], posi=len(tmp))

tbl.print_fancy_format(tmp, cp.Line_Style.DOUBLE_LINE)


