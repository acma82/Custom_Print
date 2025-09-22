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

cp.ins_newline(2)
tbl.adj_space = 4
tbl.adj_indent = 8

tbl.middle_horizontal_line_on = True
tbl.header_horizontal_line_on = True

tbl.data_bg   = cp.No.AQUAMARINE_GREEN
tbl.data_fg   = cp.No.BLACK

tbl.header_bg = cp.No.LIME
tbl.header_fg = cp.No.BLACK
tbl.header_bold = True

tbl.bg_line_colors = cp.No.INDIAN_RED # to colors all bg lines at once
tbl.fg_line_colors = cp.No.WHITE      # to colors all fg lines at once

tbl.print_fancy_format(data=lst, style=cp.Line_Style.DASH)


cp.ins_newline(2)
tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_4)


cp.ins_newline(2)
# Creating Design 4 Here
tbl.header_horizontal_line_bold = False
tbl.header_horizontal_line_fg = 21
tbl.header_horizontal_line_bg = 11
tbl.header_horizontal_line_chr = "-"

tbl.horizontal_line_bg          = tbl.header_bg
tbl.header_vertical_line_bg     = tbl.header_bg

tbl.header_corner_bg = tbl.header_bg

tbl.top_horizontal_line_on    = False
tbl.bottom_horizontal_line_on = False
tbl.right_vertical_line_on    = False
tbl.left_vertical_line_on     = False
tbl.middle_vertical_line_on   = False
tbl.middle_horizontal_line_on = False

tbl.print_fancy_format(data=lst, style=cp.Line_Style.CUSTOMIZED)







