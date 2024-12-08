import copy
import custom_print as cp

tbl = cp.FancyFormat()
pylo = cp.PyLO()

list_1 = [["Header 1", "Header 2", "Header 3"],
          ["Datito 1", "Datito 2", "Datito 3"],
          ["Datito 4", "Datito 5", "Datito 6"]]

list_2 = [["Header 1", "Header 2", "Header 3"],
          ["Datito 1", "Datito 2", "Datito 3"],
          ["Datito 4", "Datito 5", "Datito 6"]]

tbl.print_fancy_format(list_1)

#-----------------------------------------------------------------------------------------
# Merge Horizontally                                                                    --
#-----------------------------------------------------------------------------------------
result_h = []
l_col = len(list_2)
list_2_transpose = pylo.transpose(list_2)

for n in range(len(list_2[0])):
    result_h = pylo.add_col(list_1, list_2_transpose[n], col_ref=l_col)
    l_col += 1

tbl.print_fancy_format(result_h)


#-----------------------------------------------------------------------------------------
# Merge Vertically                                                                      --
#-----------------------------------------------------------------------------------------
list_1 = [["Header 1", "Header 2", "Header 3"],
          ["Datito 1", "Datito 2", "Datito 3"],
          ["Datito 4", "Datito 5", "Datito 6"]]

list_2 = [["Header 1", "Header 2", "Header 3"],
          ["Datito 1", "Datito 2", "Datito 3"],
          ["Datito 4", "Datito 5", "Datito 6"]]

result_v = list_1

for row in list_2:
    result_v.append(row)

tbl.print_fancy_format(result_v)


#-----------------------------------------------------------------------------------------
# grep                                                                                  --
#-----------------------------------------------------------------------------------------
def grep(data:list, ref:int|str)->list:
    grep_list = [] 
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == ref:
                grep_list.append([row, col, ref])
    if len(grep_list) > 0:
        grep_list.insert(0, ["Row","Col","Ref"])
    else:
        grep_list.insert(0, ["Row", "Col",  "Ref"])
        grep_list.append(["None","None", ref])

    return grep_list



list_1 = [["Header 1", "Header 2", "Header 3"],
          ["Datito 1", "Datito 2", "Datito 3"],
          ["Datito 4", "Datito 5", "Datito 6"],
          ["Datito 1", "Datito 2", "Datito 1"]]

result = grep(list_1, 3)
tbl.print_fancy_format(result)



