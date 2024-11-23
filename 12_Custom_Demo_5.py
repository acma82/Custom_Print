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
list1.msg_title = " My Title List "          # 6
list1.bold_title = 1
list1.bg_title = 6
list1.fg_title = 0
list1.align_title = "c"


# Footnote Section, all its variable available
list1.msg_footnote =" Footnote "             # 7
list1.bold_footnote = 1
list1.bg_footnote = 55
list1.fg_footnote = 7
list1.align_footnote = "r"


# Data                                        # 8
list1.bold_data = 1
list1.bg_data = 7
list1.fg_data = 4
list1.align_data = "center"


# Horizontal Line Section, all its variable available
list1.top_horizontal_line_chr    = "."           # 9
list1.top_horizontal_line_on     = 1                          # By default is 1
list1.middle_horizontal_line_on  = 1
list1.bottom_horizontal_line_chr = "="        # 10        # u'\u2550'
list1.bottom_horizontal_line_on  = 1                       # By default is 1
list1.middle_horizontal_line_chr = "-"                           # u'\u2500'
# when using UniCode as u"\u2500" bold is not recpected unles is a normal character
list1.bold_horizontal_line = 1
list1.bg_horizontal_line   = 21
list1.fg_horizontal_line   = 11


# Vertical Line Selection
list1.left_vertical_line_chr   = "l"          # 11 u"\u2551"
list1.middle_vertical_line_chr = "m"          # 18 u"\u2551"
list1.right_vertical_line_chr  = "r"          # 12 u"\u2551"
list1.bold_vertical_line = 1
list1.bg_vertical_line   = 40
list1.fg_vertical_line   = 55

# Corner Section
list1.top_left_corner_chr     = "A"           # 13
list1.top_right_corner_chr    = "B"           # 14
list1.bottom_right_corner_chr = "C"           # 15
list1.bottom_left_corner_chr  = "D"           # 16
list1.bg_corner_chr   = 1
list1.fg_corner_chr   = 7
list1.bold_corner_chr = 1


# Middle Corner Section
list1.middle_top_corner_chr    = "!"          # 17
list1.middle_bottom_corner_chr = "?"          # 19
list1.middle_inner_corner_chr  = "@"          # 31
list1.left_lateral_corner_chr  = "*"          # 27
list1.right_lateral_corner_chr = "+"          # 28
list1.bold_inner_corner_chr = 1
list1.bg_inner_corner_chr   = 52
list1.fg_inner_corner_chr   = 79


# Header Section
list1.bold_header  = 1
list1.bg_header    = 206
list1.fg_header    = 0
list1.align_header = "j"
list1.left_vertical_header_line_chr   = "L"    # 22
list1.middle_vertical_header_line_chr = "M"    # 29
list1.right_vertical_header_line_chr  = "R"    # 23
list1.bold_vertical_header_line_chr   = 1
list1.bg_vertical_header_line_chr     = 21
list1.fg_vertical_header_line_chr     = 11


# Under Line Header Section
list1.horizontal_line_under_header_on  = 1
list1.horizontal_line_under_header_chr = '\u2022'# 21, bullet should be u'\u256C'
list1.bold_under_line_header = 1
list1.bg_under_line_header   = 22
list1.fg_under_line_header   = 7

list1.left_corner_line_under_header_chr   = "0"  # 24
list1.middle_corner_line_under_header_chr = "1"  # 30
list1.right_corner_line_under_header_chr  = "2"  # 25
list1.bold_corner_under_line_header = 1
list1.bg_corner_under_line_header   = 55
list1.fg_corner_under_line_header   = 7


print("Before: \n",my_list)
list1.print_fancy_format(my_list)
print("After: \n",my_list)
