'''
To enumerate a list, it has to be a list with rows and cols as a table.
Otherwise, it will be ignored.
'''

import custom_print as cp
pylo = cp.PyLO()
tbl = cp.FancyFormat()

lst = [["Names","last","Ages"],[5,5,4],[1,2,3],[9,9,9],[0,1,1]]
result = pylo.number(lst)
tbl.print_fancy_format(result)  # Using the Default values (data=result, start_number=0, id_txt="id")



classes_methods_fancyprint = [["Header 1","Header 2",     "Header 3",              "Header 4"            ],
                              ["Cursor",  "FontStyle",    "FancyMessage",          "FancyFormat"         ],
                              ["jumpTo",  "start_style",  "print_fancy_message",   "print_fancy_format"  ],
                              ["jumpxy",  "stop_style",   "print_fancy_note",      "reset_fancy_format"  ],
                              ["moveTo",  "print_style",  "----             ",      "----             "  ],
                              ["movexy",  "reset_style",  "----             ",      "----             "  ]]

result = pylo.number(classes_methods_fancyprint,start_number=1, id_txt="N")
tbl.print_fancy_format(result)


print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")

lst = [["name","last","age"],["Miguel","AC",40],["Pedro","Alvarez",20],["Jose","Waka"]]
result = pylo.number(lst,start_number=1, id_txt="Tb")
print(result)
tbl.print_fancy_format(result)



print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,23,231)} Original list {cp.reset_font()}")
lst = [["name","last","age"],["Miguel","AC",40],["Pedro","Alvarez",20],["Jose","Waka"]]
print("Original")
print(lst)

print(f"{cp.set_font(1,23,231)} Case 1 adding the enumeration to the list {cp.reset_font()}")
result = pylo.number(lst,1)
print("result")
print(result)


print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,23,231)} Case 2 Adding KAYLA to the new list {cp.reset_font()}")
result.insert(1,[999, "KAYLA", "ACBD",  12,  1234 ])
print(result)

print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")


print(f"{cp.set_font(1,23,231)} renumerating and saving the result in the same list {cp.reset_font()}")
new_result = pylo.number(result, 1, "id", True, True)
print(new_result)
print(result)

print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")

lst = [["name"],["Miguel"],["Pedro"],["Jose"]]
# lst = [["name","last"],["Miguel","AC"],["Pedro","Alvarez"],["Jose","Waka"]]
# lst = [["name","last","age"],["Miguel","AC",40],["Pedro","Alvarez",20],["Jose","Waka"]]
print(lst)
result = pylo.number(data=lst, start_number=1, id_txt="id",renumber=False, update=False)
print(result)

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Get List Type                                                                                                                                      -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _get_list_type(my_list):
    if not isinstance(my_list, list):
        return "incorrect_variable_type"                # [Not a List] Case 0
    #-------------------------------------------------------------------------------------------------------------------------------------------------

    if len(my_list) == 0:
        return "empty_list"                             # []    Case 1

    #-------------------------------------------------------------------------------------------------------------------------------------------------

    if len(my_list) == 1:
        if isinstance(my_list[0], list):
            if len(my_list[0]) > 1:
                return "multiple_items_one_row"           # [[1,2,3]]   Case 5
            else:
                return "one_item_one_row"                 # [[1]]  Case 4
        else:
            return "one_item_no_row"                      # [1]   Case 2

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    if len(my_list) > 1:
        items = 0; rows = 0
        for n in my_list:
            if not isinstance(n, list):
                items = 1
            else:
                rows = 1

        if (items ==  1 and rows == 0):
            return "multiple_items_no_row"              #  [1,2,3]                      Case 3
        elif (items == 0 and rows == 1):
            return  "multiple_items_multiple_rows"      # [[1],[4],[7]]                 Case 6
                                                        # [[1,2,3],[4,5,6],[7,8,9]]     Case 6
                                                        # [[1],[1,2,3],[5,4,7,8]]       Case 6
                                                        # any combination of this is    Case 6
                                                        # [[1,2,3],[[2],3,4],[5,[6,7]]] Case 6
        else:
            return "mix_items"                          # [5,6,[1,2,3],[1,0,3]]         Case 7
                                                        # [[1,2],[1,2,[1]],[1,2,3]]     Case 7
                                                        # any combination of this is    Case 7

