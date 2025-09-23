import custom_print as cp
'''
    It create a divider through the terminal screen.
'''
cp.ins_newline(1)

div = cp.Divider()


# +--------------------------------------------------------------------------------------------+
# | Divider Settings                                                                           |
# +--------------------------------------------------------------------------------------------+
my_color = cp.No.EARLY_NIGHT_BLUE         # cp.No.INDIGO

div.all_corner_bg = my_color
div.top_horizontal_line_bg    = my_color
div.bottom_horizontal_line_bg = my_color

div.left_vertical_line_bg  = cp.No.WHITE
div.right_vertical_line_bg = cp.No.WHITE

div.all_fill_bg  = cp.No.WHITE

div.msg_align = cp.Align.JUSTIFY
div.adj_indent = 20
div.msg_bold = True


# +--------------------------------------------------------------------------------------------+
# | Printing the Divider                                                                       |
# +--------------------------------------------------------------------------------------------+
div.print_fancy_divider(message=" SQ BRACKET OPTION ", style=cp.Divider_Style.SQ_BRACKETS)
# div.print_fancy_divider()

cp.ins_newline(2)
div.msg_bg = 231
div.msg_fg = 234

div.print_fancy_divider(message=" SQ BRACKET OPTION ", style=cp.Divider_Style.SQ_BRACKETS)

