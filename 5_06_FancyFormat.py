import custom_print as cp

tbl = cp.FancyFormat()

lst = [["Header 0","Header 1","Header 2","Header 3"],
       ["Col 0 Row 1", "Col 1 Row 1", "Col 2 Row 1", "Col 3 Row 1"],
       ["Col 0 Row 2", "Col 1 Row 2", "Col 2 Row 2", "Col 3 Row 2"],
       ["Col 0 Row 3", "Col 1 Row 3", "Col 2 Row 3", "Col 3 Row 3"]]

# Default Table Option
tbl.title_msg = f"Default {cp.Unicode.BLAKC_RIGHT_POINTING_TRIANGLE} Customized"
# tbl.print_fancy_format(data=lst, style=cp.Line_Style.CUSTOMIZED)
tbl.print_fancy_format(lst,cp.Line_Style.CUSTOMIZED)

cp.ins_newline(2)


# Style DASH -> DASh is the default one. It can be changed as you wish but dash is its own style.
tbl.title_msg = f"Option {cp.Unicode.BLAKC_RIGHT_POINTING_TRIANGLE} Line Style DASH"
tbl.print_fancy_format(data=lst, style=cp.Line_Style.DASH) # default one


cp.ins_newline(2)


# Modifying some attributes in the class.
tbl.title_msg = f"Default {cp.Unicode.BLAKC_RIGHT_POINTING_TRIANGLE} Customized with some changes"
tbl.middle_top_corner_chr ="@";           tbl.middle_bottom_corner_chr = "@"
tbl.bottom_left_corner_chr = "@";         tbl.bottom_right_corner_chr = "@"
tbl.top_left_corner_chr = "@";            tbl.top_right_corner_chr = "@"
tbl.print_fancy_format(lst,cp.Line_Style.CUSTOMIZED)


cp.ins_newline(2)

# Note: even the customize was modified the DASH style keep the same type of lines
tbl.title_msg = f"Option {cp.Unicode.BLAKC_RIGHT_POINTING_TRIANGLE} Line Style DASH"
tbl.print_fancy_format(lst,cp.Line_Style.DASH)

