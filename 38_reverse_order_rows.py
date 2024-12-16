import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()
tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True
tbl.align_title = cp.Align.CENTER


methods = [\
    ["Header 0","Header 1"   ,    "Header 2"           ,    "Header 3",],
    ["Cursor",  "FontStyle"  ,    "FancyMessage"       ,    "FancyFormat"        ],
    ["jumpTo",  "start_style",    "print_fancy_message",    "print_fancy_format" ],
    ["jumpxy",  "stop_style" ,    "print_fancy_note"   ,    "reset_fancy_format" ],
    ["moveTo",  "print_style"],
    ["movexy"]]

result = pylo.reverse_order_ROWS(methods, False)
tbl.msg_title = " Rever_Order_ROWS "
tbl.print_fancy_format(result)

tbl.msg_title = " Original Values "
tbl.print_fancy_format(methods)
