import source.custom_print as cp
pylo = cp.PyLO()

tbl  = cp.FancyFormat()
tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True
tbl.align_title = cp.Align.CENTER

#         0           1          2            3         4
l1 = [["Names",    "Lasts",    "Ages",  "Department", "AWeb"    ],
      ["Miguel",   "AC",       40,         "EE",      "uno"     ],
      ["Tyler",    "Hig",      35,         "ECE",     "dos"     ],
      ["Alex",     "Call",     38,         "EE",      "tres"    ],
      ["Matt",     "Armaci",   40,         "CS",      "cuatro"  ]]



result = pylo.sort_cols(l1, "ascending", False)
tbl.msg_title = " Ascending Order ";    tbl.print_fancy_format(result)
tbl.msg_title = " Original List ";      tbl.print_fancy_format(l1)


result = pylo.sort_cols(l1, "descending", False)
tbl.msg_title = " Descending Order ";     tbl.print_fancy_format(result)
tbl.msg_title = " Original List ";        tbl.print_fancy_format(l1)

result = pylo.sort_cols(data=l1, sort_type=[4,0,1,3,2], update=True)
tbl.msg_title = " Order by List Reference ";     tbl.print_fancy_format(result)
tbl.msg_title = " Original List ";               tbl.print_fancy_format(l1)


result = pylo.sort_cols(data=l1, sort_type=pylo.Order.ASCENDING, update=False)
result = pylo.sort_cols(data=l1, sort_type=pylo.Order.DESCENDING, update=True)

tbl.msg_title = ""
l1 = ["NaMeS",    "LaStS",    "AgeS",  "DeparTmenT", "AWeB"]
l = sorted(l1, reverse=False)
tbl.print_fancy_format(l)

result = pylo.sort_cols(data=l1, sort_type=pylo.Order.ASCENDING, update=False)
tbl.print_fancy_format(result)