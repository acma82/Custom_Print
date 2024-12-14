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



classes_methods = [["Header 1","Header 2",     "Header 3",              "Header 4"            ],
                   ["Cursor",  "FontStyle",    "FancyMessage",          "FancyFormat"         ],
                   ["jumpTo",  "start_style",  "print_fancy_message",   "print_fancy_format"  ],
                   ["jumpxy",  "stop_style",   "print_fancy_note",      "reset_fancy_format"  ],
                   ["moveTo",  "print_style",  "----             ",      "----             "  ],
                   ["movexy",  "reset_style",  "----             ",      "----             "  ]]

result = pylo.number(classes_methods,start_number=1, id_txt="N", renumber=False, update=False)
tbl.print_fancy_format(result)
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(classes_methods)


print(f"{cp.ins_chr(n=80, unicode="-")}")
lst = [["name","last","age"],["Miguel","AC",40],["Pedro","Alvarez",20],["Jose","Waka"]]
result = pylo.number(lst,start_number=1, id_txt="Tb")
tbl.print_fancy_format(result)
print(lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,23,231)} Original list {cp.reset_font()}")
lst = [["name","last","age"],["Miguel","AC",40],["Pedro","Alvarez",20],["Jose","Waka","d"]]
print("Original", lst)

print(f"{cp.set_font(1,23,231)} Case 1 adding the enumeration to the list {cp.reset_font()}")
result = pylo.number(data=lst,start_number=1,id_txt="**", renumber=False, update=False)
print("result",result)
print("Original", lst)


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
print(lst)
result = pylo.number(data=lst, start_number=1, id_txt="id",renumber=False, update=True)
print(result)
print(lst)
