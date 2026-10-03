import custom_print as cp

pylo = cp.PyLO()
tbl  = cp.FancyFormat()

methods = [\
    ["Cursor",  "FontStyle"  ,  "Pen"           ],
    ["jumpTo",  "start_style",  "draw_line"     ],
    ["jumpxy",  "stop_style" ,  "draw_rectangle"],
    ["moveTo",  "print_style",  "----"          ],
    ["movexy",  "reset_style",  "----"          ]]

tbl.title_align = cp.Align.CENTER
tbl.title_bg = 90
tbl.title_fg = 231
tbl.title_msg = " Original List "
tbl.print_fancy_format(methods, cp.Line_Style.WHITE_BLACK_2)

new_methods = pylo.add_col_id(data=methods, start_number=1, id_label="No.", renumber=False, update=False)

tbl.title_msg = " New List With col_id Added "
tbl.print_fancy_format(new_methods,cp.Line_Style.WHITE_BLACK_2)



print(methods)

print("\n")


print(new_methods)