import custom_print as cp
'''
    It create a divider through the terminal screen.
'''
cp.ins_newline(1)

div = cp.Divider()
div.msg_bold = True

# +--------------------------------------------------------------------------------------------+
# | Printing the Divider                                                                       |
# +--------------------------------------------------------------------------------------------+
cp.ins_newline(2)
div.print_fancy_divider(style=cp.Divider_Style.SINGLE_LINE)

cp.ins_newline(2)
div.print_fancy_divider(style=cp.Divider_Style.SINGLE_BOLD)

cp.ins_newline(2)
div.print_fancy_divider(style=cp.Divider_Style.SINGLE_HEAVY)

cp.ins_newline(2)
div.print_fancy_divider(style=cp.Divider_Style.DOUBLE_LINE)

cp.ins_newline(2)
div.print_fancy_divider(style=cp.Divider_Style.DASH_1)

cp.ins_newline(2)
div.print_fancy_divider(style=cp.Divider_Style.DASH_2)

cp.ins_newline(2)
div.print_fancy_divider(style=cp.Divider_Style.BLUE_WHITE_1)

cp.ins_newline(2)
div.print_fancy_divider(style=cp.Divider_Style.BLUE_WHITE_2)