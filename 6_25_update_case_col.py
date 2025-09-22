import custom_print as cp
pylo = cp.PyLO()

tbl  = cp.FancyFormat()
tbl.title_bg  = 90
tbl.title_bold = True
tbl.title_italic = True
tbl.title_align = cp.Align.CENTER

#         0           1          2            3         4
l1 = [["NaMeS",    "LaStS",    "AgeS",  "DeparTmenT", "AWeB"    ],
      ["MigueL",   "AC",       40,         "EE",      "UnO"     ],
      ["TyleR",    "HiG",      35,         "ECE",     "DoS"     ],
      ["AleX",     "CalL",     38,         "EE",      "TreS"    ],
      ["MatT",     "ArmacI",   40,         "CS",      "CuatrO"  ]]

tbl.title_msg = " Original"
tbl.print_fancy_format(l1)

result = pylo.update_case_col(data=l1, header_case="capitalize", data_case="LOWER", col_ref=4, update=False)
tbl.title_msg = " Header=Capitalize, Data=Lower, col_ref=4, Update=False"
tbl.print_fancy_format(result)

cp.ins_newline(2)

result = pylo.update_case_col(data=l1, header_case=pylo.Case.LOWER, data_case=pylo.Case.UPPER, col_ref=4, update=True)
tbl.title_msg = " Header=Lower, Data=Upper, col_ref=4, Update=True"
tbl.print_fancy_format(result)
tbl.title_msg = " Original"
tbl.print_fancy_format(l1)





