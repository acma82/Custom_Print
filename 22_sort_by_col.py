#-----------------------------------------------------------------------------------------------------------
import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()
tbl.msg_title = "Original"
lst  = [["ID","Names",  "Last",    "Age","Department"],
        [1,   "Juan",   "Alegria",   30,  "EE"       ],
        [17,  "Manuel", "Alvarez",   25,  "EC"       ],
        [9,   "Luis",   "Naguse",    21,  "AD"       ],
        [3,   "Pancho", "Marlo",     41,  "BE"       ],
        [2,   "Felipe", "Cautizo",   15              ]] 
tbl.print_fancy_format(lst)

result = pylo.sort_by_col(data=lst, ref_col=0, sort_type="number", reverse_order=False, update=False)
tbl.msg_title = "Sort_by Col 0. Number"
tbl.print_fancy_format(result)

tbl.msg_title = "Sort_by Col 0. String"
result = pylo.sort_by_col(data=lst, ref_col=0, sort_type="string", reverse_order=False, update=False)
tbl.print_fancy_format(result)

tbl.msg_title = "Sort_by Col 0. Number, rever_order=True, update=True"
result = pylo.sort_by_col(data=lst, ref_col=0, sort_type="number", reverse_order=True, update=True)
tbl.print_fancy_format(result)

tbl.msg_title = "New Original"
tbl.print_fancy_format(lst)


tbl.msg_title = ""
lst_2 = [10,1,5,3]
result2 = pylo.sort_by_col(data=lst_2, ref_col=0, sort_type=pylo.Sort_By.STRING, reverse_order=False)
tbl.print_fancy_format(lst_2)
tbl.print_fancy_format(result2)

result2 = pylo.sort_by_col(data=lst_2, ref_col=0, sort_type=pylo.Sort_By.NUMBER, reverse_order=True)
tbl.print_fancy_format(lst_2)
tbl.print_fancy_format(result2)
