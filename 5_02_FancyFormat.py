import custom_print as cp

lst = [["Header 1 Miguelito", "Header 2", "Header 3", "Header 4"],
        ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
        ["Data 5",   "Data 6",   "Data 7",   "Data 8"  ]]

tbl = cp.FancyFormat()
tbl.header_align = cp.Align.CENTER
tbl.data_align   = cp.Align.CENTER

cp.ins_newline(2)
tbl.print_fancy_format(data=lst, style=cp.Line_Style.CUSTOMIZED) # This is the default one
cp.ins_newline(2)

tbl.print_fancy_format(data=lst, style=cp.Line_Style.DASH)

cp.ins_newline(2)
tbl.print_fancy_format(data=lst, style=cp.Line_Style.SINGLE_LINE)

cp.ins_newline(2)
tbl.print_fancy_format(data=lst, style=cp.Line_Style.SINGLE_BOLD)

cp.ins_newline(2)
tbl.print_fancy_format(data=lst, style=cp.Line_Style.SINGLE_HEAVY)

cp.ins_newline(2)
tbl.print_fancy_format(data=lst, style=cp.Line_Style.DOUBLE_LINE)

