import custom_print as cp
tbl = cp.FancyFormat()
lst = [["Header 0","Header 1","Header 2","Header 3"],
       ["Col 0 Row 1", "Col 1 Row 1", "Col 2 Row 1", "Col 3 Row 1"],
       ["Col 0 Row 2", "Col 1 Row 2", "Col 2 Row 2", "Col 3 Row 2"],
       ["Col 0 Row 3", "Col 1 Row 3", "Col 2 Row 3", "Col 3 Row 3"]]

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
tbl.middle_horizontal_line_on = True
tbl.header_horizontal_line_on = True

tbl.header_bg = cp.No.INDIGO
tbl.header_fg = cp.No.WHITE
tbl.header_bold = True

tbl.data_bg   = cp.No.EARLY_NIGHT_BLUE
tbl.data_fg   = cp.No.WHITE

# bg_line_colors and fg_line_colors, works with Designs 1,2,3,4
tbl.design_color = cp.No.WHITE

cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_1)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_2)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_3)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_4)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_5)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_6)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_7)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_8)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_9)
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_10)


# Only DESIGN_1 is affected by these two options
tbl.middle_horizontal_line_on = False
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_1)
tbl.header_horizontal_line_on = False
cp.ins_newline(2); tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_1)


