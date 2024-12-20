import source.source.custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

tbl.bg_title = 90
tbl.align_title = cp.Align.LEFT

#------------------------------------------------------------------------------
# Adding list_2 as one col in list_1
tbl.msg_title = " List_1 "
list_1 = [["Header_1","Header_2"],["R1_C1","R1_C2"], ["R2_C1","R2_C2"]]
tbl.print_fancy_format(list_1)

tbl.msg_title = " List_2 to be added to List_1 as Col, pos=1 "
list_2 = ["New_Header",   "New_Row_Col",  "New_Row_Col"]
tbl.print_fancy_format(list_2)

tbl.msg_title = " New Complete List_1_2 "
list_1_2 = pylo.add_col(data=list_1, col_data=list_2, posi=1)
tbl.print_fancy_format(list_1_2)


#------------------------------------------------------------------------------
# Adding the list_4 as more Rows in list_3
list_3 = [["Header_1","Header_2","Header_3"],
          ["R1_C1","R1_C2","R1_C3"],
          ["R2_C1","R2_C2","R2_C3"]]

list_4 = [["R3_C1","R3_C2","R3_C3"],
          ["R4_C1","R4_C2","R4_C3"]]

for row in range(len(list_4)): list_3.append(list_4[row])

tbl.bg_title = 23; tbl.msg_title = " Adding list_4 as rows in list_3 "
tbl.print_fancy_format(list_3)


#------------------------------------------------------------------------------
# Adding list_6 as columns in list_5
tbl.bg_title = 1
tbl.msg_title = " Adding list_6 as cols in list_5 at the end "

list_5  = [["Header_1","Header_2","Header_3"],
           ["R1_C1",   "R1_C2",   "R1_C3"],
           ["R2_C1",   "R2_C2",   "R2_C3"]]

list_6 = [["R3_C1","R3_C2","R3_C3"],
          ["R4_C1","R4_C2","R4_C3"]]
tmp = list_5
for rows in range(len(list_6)):
    tmp = pylo.add_col(data=tmp, col_data=list_6[rows], posi=1)#len(list_5[0]))


list_5_6 = pylo.add_col(data=list_5, col_data=list_6[0], posi=1)#len(list_5[0]))
result = pylo.add_col(data=list_5_6, col_data=list_6[1], posi=1)#len(list_5[0]))
# tbl.print_fancy_format(tmp)
tbl.print_fancy_format(result)

print(list_5)
print(list_6)
print(result)

# print(list_5_6)
# print(result)

# list_5_6_2 = list_5
# for row in list_6:
#     list_5_6_2.append(row)
# tbl.print_fancy_format(list_5_6_2)