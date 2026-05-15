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

#l1 = [["NaMeS",    "LaStS",    "AgeS",  "DeparTmenT", "AWeB"]]

result = pylo.update_case(l1, pylo.Case.UPPER, pylo.Case.LOWER, False)
tbl.title_msg = " Headers Upper, Data Lower "; tbl.print_fancy_format(result)
tbl.title_msg = " Original List ";             tbl.print_fancy_format(l1)

result = pylo.update_case(data=l1, header_case=pylo.Case.CAPITALIZE, data_case=pylo.Case.LOWER, update=False)
tbl.title_msg = " Headers Capitalize, Data Lower "; tbl.print_fancy_format(result)
tbl.title_msg = " Original List ";                  tbl.print_fancy_format(l1)

result = pylo.update_case(data=l1, header_case=pylo.Case.LOWER, data_case=pylo.Case.UPPER, update=True)
tbl.title_msg = " Headers Lower, Data Upper. update=True "; tbl.print_fancy_format(result)
tbl.title_msg = " Original List ";             tbl.print_fancy_format(l1)


lista_lowcase = ["a","b","c","&","A",">","6","q","ñ"]
result = pylo.update_case(data=lista_lowcase, header_case=pylo.Case.LOWER, data_case=pylo.Case.UPPER, update=False )
tbl.print_fancy_format(result)

lista_lowcase = ["A","B","C","&","A",">","6","Q","Ñ"]
result = pylo.update_case(data=lista_lowcase, header_case=pylo.Case.LOWER, data_case=pylo.Case.LOWER, update=False )
tbl.print_fancy_format(result)


Doh_ñ = []
Doh_ñ.append("ñ")

Doh_Ñ = []
Doh_Ñ.append("Ñ")

print("\u00F1")  # ñ
print("\u00D1")  # Ñ
print(cp.Unicode.UPPERCASE_N_TILDE) # ñ
print(cp.Unicode.LOWERCASE_N_TILDE) # Ñ


a = "\u00F1"
if a == "ñ":
    print("success....!")
    my_l = eval(f"Doh_{a}")
    print(my_l)
    print(my_l[0])      




a = cp.Unicode.UPPERCASE_N_TILDE
if a == "Ñ":
    print("success....!")
    my_l = eval(f"Doh_{a}")
    print(my_l)
    print(my_l[0])      
