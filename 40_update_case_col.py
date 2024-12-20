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

#l1 = ["NaMeS",    "LaStS",    "AgeS",  "DeparTmenT", "AWeB"]

result = pylo.update_case_col(data=l1, header_case="capitalize", data_case="lower", col_ref=4, update=False)
tbl.print_fancy_format(result)
#print(result)

