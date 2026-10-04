import custom_print as cp
pylo = cp.PyLO()

tbl  = cp.FancyFormat()
tbl.title_bg  = 90
tbl.title_bold = True
tbl.title_italic = True
tbl.title_align = cp.Align.CENTER

#         0           1          2            3         4
l1 = [["NaMeS",    "LaStS",    "AgeS",  "DeparTmenT", "AWeB"    ],
      ["MigueL",   "AC",       40,         "EE",      "One"     ],
      ["TyleR",    "HiG",      35,         "ECE",     "Two"     ],
      ["AleX",     "CalL",     38,         "EE",      "Thre"    ],
      ["MatT",     "ArmacI",   40,         "CS",      "Fourth"  ]]

tbl.title_msg = " Original"
tbl.print_fancy_format(l1)

tbl.title_msg = " Header=upper, Data=Lower, col_index=4, Update=False"
result = pylo.update_case_col(data=l1, header_case="upper", data_case="LOWER", col_index=-40, update=False)
tbl.print_fancy_format(result)

cp.ins_newline(2)



# l1 = "asdf"
# l1 = []
# l1= [1,2,5,"hello"]
# l1 = [[1,2,5,"hello"]]
# l1 = [1,2,[5,9],"hello"]
l1 = [["HE"],[2],[5],["hello"]]
result = pylo.update_case_col(data=l1, header_case=pylo.Case.LOWER, data_case=pylo.Case.UPPER, col_index=4, update=True)
tbl.title_msg = " Header=Lower, Data=Upper, col_index=4, Update=True"
tbl.print_fancy_format(result)






