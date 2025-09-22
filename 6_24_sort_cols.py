import custom_print as cp
pylo = cp.PyLO()

tbl  = cp.FancyFormat()
tbl.title_bg  = 90
tbl.title_bold = True
tbl.title_italic = True
tbl.title_align = cp.Align.CENTER

#         0           1          2            3         4
l1 = [["Names",    "Lasts",    "Ages",  "Department", "AWeb"    ],
      ["Miguel",   "AC",       40,         "EE",      "uno"     ],
      ["Tyler",    "Hig",      35,         "ECE",     "dos"     ],
      ["Alex",     "Call",     38,         "EE",      "tres"    ],
      ["Matt",     "Armaci",   40,         "CS",      "cuatro"  ]]



new_list = pylo.sort_cols(l1, "ascending", False)
tbl.title_msg = " Ascending Order ";    tbl.print_fancy_format(new_list)
tbl.title_msg = " Original List ";      tbl.print_fancy_format(l1)


new_list = pylo.sort_cols(l1, "descending", False)
tbl.title_msg = " Descending Order ";     tbl.print_fancy_format(new_list)
tbl.title_msg = " Original List ";        tbl.print_fancy_format(l1)

new_list = pylo.sort_cols(data=l1, sort_type=[4,0,1,3,2], update=True)
tbl.title_msg = " Order by List Reference [4,0,1,3,2] update=True "
tbl.print_fancy_format(new_list)
tbl.title_msg = " Original List "
tbl.print_fancy_format(l1)


new_list = pylo.sort_cols(data=l1, sort_type=pylo.Order.ASCENDING, update=False)
new_list = pylo.sort_cols(data=l1, sort_type=pylo.Order.DESCENDING, update=True)

tbl.title_msg = ""
l1 = ["NaMeS",    "LaStS",    "AgeS",  "DeparTmenT", "AWeB"]
l = sorted(l1, reverse=False)
tbl.print_fancy_format(l)

new_list = pylo.sort_cols(data=l1, sort_type=pylo.Order.ASCENDING, update=False)
tbl.print_fancy_format(new_list)