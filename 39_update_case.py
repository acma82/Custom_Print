import source.source.custom_print as cp
pylo = cp.PyLO()

tbl  = cp.FancyFormat()
tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True
tbl.align_title = cp.Align.CENTER

#         0           1          2            3         4
l1 = [["NaMeS",    "LaStS",    "AgeS",  "DeparTmenT", "AWeB"    ],
      ["MigueL",   "AC",       40,         "EE",      "UnO"     ],
      ["TyleR",    "HiG",      35,         "ECE",     "DoS"     ],
      ["AleX",     "CalL",     38,         "EE",      "TreS"    ],
      ["MatT",     "ArmacI",   40,         "CS",      "CuatrO"  ]]

l1 = [["NaMeS",    "LaStS",    "AgeS",  "DeparTmenT", "AWeB"]]

result = pylo.update_case(l1, pylo.Case.UPPER, pylo.Case.LOWER, False)
tbl.msg_title = " Headers Upper, Data Lower "; tbl.print_fancy_format(result)
tbl.msg_title = " Original List ";             tbl.print_fancy_format(l1)

result = pylo.update_case(data=l1, header_case=pylo.Case.CAPITALIZE, data_case=pylo.Case.LOWER, update=False)
tbl.msg_title = " Headers Capitalize, Data Lower "; tbl.print_fancy_format(result)
tbl.msg_title = " Original List ";                  tbl.print_fancy_format(l1)

result = pylo.update_case(data=l1, header_case=pylo.Case.LOWER, data_case=pylo.Case.UPPER, update=True)
tbl.msg_title = " Headers Lower, Data Upper. update=True "; tbl.print_fancy_format(result)
tbl.msg_title = " Original List ";             tbl.print_fancy_format(l1)


