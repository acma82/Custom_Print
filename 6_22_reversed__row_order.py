import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()
tbl.title_bg  = 90
tbl.title_bold = True
tbl.title_italic = True
tbl.title_align = cp.Align.CENTER


methods = [\
    ["Header 0","Header 1"   ,    "Header 2"           ,    "Header 3",],
    ["Cursor",  "FontStyle"  ,    "FancyMessage"       ,    "FancyFormat"        ],
    ["jumpTo",  "start_style",    "print_fancy_message",    "print_fancy_format" ],
    ["jumpxy",  "stop_style" ,    "print_fancy_note"   ,    "reset_fancy_format" ],
    ["moveTo",  "print_style"],
    ["movexy"]]

result = pylo.reversed_row_order(methods, False)
tbl.title_msg = " Reversed_ROW_Order "
tbl.print_fancy_format(result)

tbl.title_msg = " Original Values "
tbl.print_fancy_format(methods)

tbl.title_msg = " Reversed_ROW_Order "
tmp = []
reversed_list = []
for row in reversed(methods):
    reversed_list.append(row)
tbl.print_fancy_format(reversed_list)