import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

tbl.bg_title = 90
tbl.align_title = cp.Align.LEFT
tbl.bg_title = 1
tbl.msg_title = " Adding list_6 as cols in list_5 at the end "

#-----------------------------------------------------------------------------------
list_5  = [["Header_1","Header_2","Header_3"],
          ["R1_C1","R1_C2","R1_C3"],
          ["R2_C1","R2_C2","R2_C3"]]

list_6 = [["R3_C1","R3_C2","R3_C3"],
          ["R4_C1","R4_C2","R4_C3"]]

for rows in range(len(list_6)):
    list_5_6 = pylo.add_col(data=list_5, new_col_data=list_6[rows], col_posi=len(list_5[0]))

tbl.print_fancy_format(list_5_6)
print(list_5_6)

#-----------------------------------------------------------------------------------
tbl.msg_title = " Adding the row numbers "
pylo.number(data=list_5_6, start_number=1, id_txt="ID", renumber=False, update=True)
tbl.print_fancy_format(list_5_6)

#-----------------------------------------------------------------------------------
tmp = [0,"RC","RRC","RRCC","RRRCC","RRRCCC"]
list_5_6.append(tmp)
tbl.msg_title = " Adding a new row "
tbl.print_fancy_format(list_5_6)

#-----------------------------------------------------------------------------------
pylo.number(data=list_5_6, start_number=1, id_txt="ID", renumber=True, update=True)
tbl.msg_title = " renumerating the rows "
tbl.print_fancy_format(list_5_6)
