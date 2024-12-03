'''
To enumerate a list, it has to be a list with rows and cols as a table.
Otherwise, it will be ignored.
'''

import custom_print as cp
pylo = cp.PyLO()
tbl = cp.FancyFormat()

lst = [["Names","last","Ages"],[5,5,4],[1,2,3],[9,9,9],[0,1,1]]
result = pylo.enumarate_list(lst)
tbl.print_fancy_format(result)  # Using the Default values (data=result, start_number=0, id_txt="id")



classes_methods_fancyprint = [["Header 1","Header 2",     "Header 3",              "Header 4"            ],
                              ["Cursor",  "FontStyle",    "FancyMessage",          "FancyFormat"         ],
                              ["jumpTo",  "start_style",  "print_fancy_message",   "print_fancy_format"  ],
                              ["jumpxy",  "stop_style",   "print_fancy_note",      "reset_fancy_format"  ],
                              ["moveTo",  "print_style",  "----             ",      "----             "  ],
                              ["movexy",  "reset_style",  "----             ",      "----             "  ]]

result = pylo.enumarate_list(classes_methods_fancyprint,start_number=1, id_txt="N")
tbl.print_fancy_format(result)


lst = [["name","last","age"],["Miguel","AC",40],["Pedro","Alvarez",20],["Jose","Waka"]]
result = pylo.enumarate_list(lst,start_number=1, id_txt="Tb")
print(result)
tbl.print_fancy_format(result)