#-----------------------------------------------------------------------------------------------------------
import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

lst  = [["ID","Names",  "Last",    "Age","Department"],
        [  1, "Juan",   "Alegria",   30,  "EE"       ],
        [ 17, "Manuel", "Alvarez",   25,  "EC"       ],
        [  9, "Luis",   "Nanguse",   21,  "AD"       ],
        [  3, "Pancho", "Marlo",     41,  "BE"       ],
        [  2, "Felipe", "Cautizo",   15              ]] 

result = pylo.sort_by_col(data=lst, ref_col=0, reverse_order=False, update=False)
tbl.msg_title = "Sort_by Col 0"
tbl.print_fancy_format(result)

tbl.msg_title = "Original"
tbl.print_fancy_format(lst)

tbl.msg_title = "Sort_by Col 4"
result = pylo.sort_by_col(data=lst, ref_col=4, reverse_order=False, update=False)
tbl.print_fancy_format(result)

tbl.msg_title = "Sort_by Col 0. reverse_order=True, update=True"
result = pylo.sort_by_col(data=lst, ref_col=0, reverse_order=True, update=True)
tbl.print_fancy_format(result)

tbl.msg_title = "New Original"
tbl.print_fancy_format(lst)

tbl.msg_title = ""
lst_2 = [5,1,9,5]
result2 = pylo.sort_by_col(data=lst_2, ref_col=10, reverse_order=False, update=False)
print("\n\nResult  : reverse_order=False, update=False")
tbl.print_fancy_format(result2)
print("Original:");  tbl.print_fancy_format(lst_2)

result2 = pylo.sort_by_col(data=lst_2, ref_col=0, reverse_order=True, update=True)
print("Result  : reverse_order=True, update=True ")
tbl.print_fancy_format(result2)
print("Original:");  tbl.print_fancy_format(lst_2)

