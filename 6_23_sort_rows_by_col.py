#-----------------------------------------------------------------------------------------------------------
import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

lst  = [["ID","Names",  "Last",    "Age",    "Department"],
        [  1, "Juan",   "Alegria",   30,     "EE"       ],
        [ 17, "Manuel", "Alvarez",   25,     "EC"       ],
        [  9, "Luis",   "Nanguse",   21,     "AD"       ],
        [  3, "Pancho", "Marlo",     41+8j,  "BE"       ],
        [  2, "Felipe", "Cautizo",   15.5              ]] 

tbl.title_bg = 90
tbl.title_fg = 231
tbl.title_msg = " Original List "
tbl.title_align = cp.Align.LEFT
tbl.print_fancy_format(lst)





tbl.title_msg = " Sort_by Col 0, reversed_order=False "
result = pylo.sort_rows_by_col(data=lst, col_index=0, reversed_order=False, keep_header=True, update=False)
tbl.print_fancy_format(result)

tbl.title_msg = " Sort_by Col 0. reverse_order=True "
result = pylo.sort_rows_by_col(data=lst, col_index=0, reversed_order=True, keep_header=True, update=False)
tbl.print_fancy_format(result)


tbl.title_msg = " Sort_by Col 1. reverse_order=False, keep_header=False "
result = pylo.sort_rows_by_col(data=lst, col_index=1, reversed_order=False, keep_header=False, update=False)
tbl.print_fancy_format(result)



tbl.title_msg = " Sort_by Col 1. reverse_order=True, keep_header=False "
result = pylo.sort_rows_by_col(data=lst, col_index=10, reversed_order=True, keep_header=False, update=False)
tbl.print_fancy_format(result)

# tbl.title_msg = " New Original "
# tbl.print_fancy_format(lst)

# tbl.title_msg = ""
# lst_2 = [5,1,9,5]
# result2 = pylo.sort_rows_by_col(data=lst_2, col_index=10, reversed_order=False, update=False)
# print("\n\nResult  : reverse_order=False, update=False")
# tbl.print_fancy_format(result2)
# print("Original:");  tbl.print_fancy_format(lst_2)

# result2 = pylo.sort_rows_by_col(data=lst_2, col_index=0, reversed_order=True, update=True)
# print("Result  : reverse_order=True, update=True ")
# tbl.print_fancy_format(result2)
# print("Original:");  tbl.print_fancy_format(lst_2)

