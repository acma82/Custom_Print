'''
Demo 5 for fancyprint module...!
'''

import custom_print as cp

list1 = cp.FancyFormat()

my_list = [["Header 1","Header 2","Header 3","Header 4"],
           ["Data 1","Data 2","Data 3","Data 4"],
           ["Data 5","Data 6","Data 7","Data 8"],
           ["Data 9","Data A","Data B"]]

# General Use, all its variable available
list1.adj_top_margin = 2                     # 1
list1.adj_top_space = 1                      # 2
list1.adj_indent = 6                         # 3
list1.adj_space = 4                          # 4
list1.adj_bottom_space = 1                   # 5
list1.set_fill_chr = "None"                  # 32
list1.update_list = 1                        # Only list type


# Title Section, all its variable available
list1.title_msg = " My Title List "          # 6
list1.title_bold = 1
list1.title_bg = 6
list1.title_fg = 0
list1.title_align = "c"


# Footnote Section, all its variable available
list1.footnote_msg =" Footnote "             # 7
list1.footnote_bold = 1
list1.footnote_bg = 55
list1.footnote_fg = 7
list1.footnote_align = "r"


# Data                                        # 8
list1.data_bold = 1
list1.data_bg = 7
list1.data_fg = 4
list1.data_align = "center"


# Horizontal Line Section, all its variable available
list1.top_horizontal_line_chr    = "."           # 9
list1.top_horizontal_line_on     = 1                          # By default is 1
list1.middle_horizontal_line_on  = 1
list1.bottom_horizontal_line_chr = "="        # 10        # u'\u2550'
list1.bottom_horizontal_line_on  = 1                       # By default is 1
list1.middle_horizontal_line_chr = "-"                           # u'\u2500'
# when using UniCode as u"\u2500" bold is not recpected unles is a normal character
list1.horizontal_line_bold = 1
list1.horizontal_line_bg   = 21
list1.horizontal_line_fg   = 11


# Vertical Line Selection
list1.left_vertical_line_chr   = "l"          # 11 u"\u2551"
list1.middle_vertical_line_chr = "m"          # 18 u"\u2551"
list1.right_vertical_line_chr  = "r"          # 12 u"\u2551"
list1.vertical_line_bold = 1
list1.vertical_line_bg   = 40
list1.vertical_line_fg   = 55

# Corner Section
list1.top_left_corner_chr     = "A"           # 13
list1.top_right_corner_chr    = "B"           # 14
list1.bottom_right_corner_chr = "C"           # 15
list1.bottom_left_corner_chr  = "D"           # 16
list1.bg_corner_chr   = 1
list1.fg_corner_chr   = 7
list1.all_corner_bold_chr = 1


# Middle Corner Section
list1.middle_top_corner_chr    = "!"          # 17
list1.middle_bottom_corner_chr = "?"          # 19
list1.middle_inner_corner_chr  = "@"          # 31
list1.left_lateral_corner_chr  = "*"          # 27
list1.right_lateral_corner_chr = "+"          # 28
list1.inner_corner_bold_chr = 1
list1.inner_corner_bg_chr   = 52
list1.inner_corner_fg_chr   = 79


# Header Section
list1.header_bold  = 1
list1.header_bg    = 206
list1.header_fg    = 0
list1.header_align = "j"
list1.header_left_vertical_line_chr   = "L"    # 22
list1.header_middle_vertical_line_chr = "M"    # 29
list1.header_right_vertical_line_chr  = "R"    # 23
list1.header_vertical_line_bold_chr   = 1
list1.header_vertical_line_bg_chr     = 21
list1.header_vertical_line_fg_chr     = 11


# Under Line Header Section
list1.header_horizontal_line_on  = 1
list1.header_horizontal_line_chr = '\u2022'# 21, bullet should be u'\u256C'
list1.header_horizontal_line_bold = 1
list1.header_horizontal_line_bg   = 22
list1.header_horizontal_line_fg   = 7

list1.header_left_corner_chr   = "0"  # 24
list1.header_middle_corner_chr = "1"  # 30
list1.header_right_corner_chr  = "2"  # 25
list1.header_corner_bold = 1
list1.header_corner_bg   = 55
list1.header_corner_fg   = 7


print("Before: \n",my_list)
list1.print_fancy_format(my_list)
print("After: \n",my_list)


tbl = cp.FancyFormat()
tbl.header_bg = 90
tbl.header_fg = 231
tbl.print_fancy_format(my_list)

tbl.header_all_cell_bg = False
tbl.middle_vertical_line_on = False
tbl.print_fancy_format(my_list)