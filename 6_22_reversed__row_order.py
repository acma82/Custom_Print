import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()
tbl.title_bg  = 90
tbl.title_bold = True
tbl.title_italic = True
tbl.title_align = cp.Align.CENTER
tbl.adj_space = 1


methods = [\
    ["Header 0",    "Header 1"   ,    "Header 2"           ,    "Header 3"           ],
    ["Cursor",      "FontStyle"  ,    "FancyMessage"       ,    "FancyFormat"        ],
    ["jumpTo",      "start_style",    "print_fancy_message",    "print_fancy_format" ],
    ["jumpxy",      "stop_style" ,    "print_fancy_note"   ,    "reset_fancy_format" ],
    ["moveTo",      "print_style"                                                    ],
    ["movexy"                                                                        ]]


tbl.title_msg = " Original List "
tbl.print_fancy_format(methods)


result = pylo.reversed_row_order(data=methods, keep_header=True, update=False)
tbl.title_msg = " Reversed_ROW_Order, Keep_header=True, update=False "
tbl.print_fancy_format(result)


result = pylo.reversed_row_order(data=methods, keep_header=False, update=False)
tbl.title_msg = " Reversed_ROW_Order, Keep_header=False, update=False "
tbl.print_fancy_format(result)



# tbl.title_msg = " Reversed_ROW_Order "
# tmp = []
# reversed_list = []
# for row in reversed(methods):
#     reversed_list.append(row)
# tbl.print_fancy_format(reversed_list)