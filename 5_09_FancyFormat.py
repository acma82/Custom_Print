import custom_print as cp

tbl = cp.FancyFormat()

lst = [[" Header 0 ",    " Header 1 ",    " Header 2 ",    " Header 3 "],
       [" Col 0 Row 1 ", " Col 1 Row 1 ", " Col 2 Row 1 ", " Col 3 Row 1 "],
       [" Col 0 Row 2 ", " Col 1 Row 2 ", " Col 2 Row 2 ", " Col 3 Row 2 "],
       [" Col 0 Row 3 ", " Col 1 Row 3 ", " Col 2 Row 3 ", " Col 3 Row 3 "]]

# Default Options for the Lines
# +--------------------------------------------------+
# |               Horizontal Lines                   |
# +--------------------------------------------------+
#    tbl.top_horizontal_line_on           = True
#    tbl.header_horizontal_line_on  = False
#    tbl.middle_horizontal_line_on        = False
#    tbl.bottom_horizontal_line_on        = True

# +--------------------------------------------------+
# |               Vertical Lines                     |
# +--------------------------------------------------+
#    tbl.right_vertical_line_on  = True
#    tbl.left_vertical_line_on   = True
#    tbl.middle_vertical_line_on = True



tbl.header_bold = True
tbl.header_bg = cp.No.INDIGO
tbl.header_horizontal_line_on = True


# Colors are NOT accepted on these designs. The only 4 options for these
# designs are the 4 following:
# tbl.header_align = cp.Align.LEFT
# tbl.data_align   = cp.Align.RIGHT
# tbl.header_all_cell_bg = False
# tbl.data_all_cell_bg   = False
tbl.header_align = cp.Align.CENTER
# Using with Single empty space
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.WHITE_PURPLE)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.WHITE_BLACK_PURPLE)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.RED_WHITE)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.PURPLE_WHITE)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.BLUE_WHITE)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.TURQUOISE_WHITE)




# Note we can create our designs or use those template. There are others template in the
# READEME.md File.