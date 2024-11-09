'''
Demo 4 for fancyprint module...!
'''
import fancyprint

list1 = fancyprint.FancyFormat()

# title
list1.bg_title    = 11
list1.fg_title    = 0
list1.bold_title  = 1
list1.align_title = "r"
list1.msg_title   = " Title List "

# footnote
list1.align_footnote = "l"
list1.msg_footnote   = " Footnote "
list1.fg_footnote    = 226
list1.bg_footnote    = 6
list1.bold_footnote  = 1

list1.top_left_corner_chr        = "\u250c"
list1.middle_horizontal_line_chr = "\u2500"
list1.top_right_corner_chr       = "\u2510"
list1.bottom_left_corner_chr     = "\u2514"
list1.bottom_right_corner_chr    = "\u2518"
list1.left_vertical_line_chr     = "\u2502"
list1.right_vertical_line_chr    = "\u2502"
list1.middle_inner_corner_chr    = "\u2502"
list1.middle_top_corner_chr      = "\u252c"
list1.middle_bottom_corner_chr   = "\u2534"
list1.middle_inner_corner_chr    = '\u253C'
list1.middle_vertical_line_chr   = '\u2502'

list1.middle_corner_under_line_header_chr = '\u253C'
list1.left_corner_under_line_header_chr   = '\u251C'
list1.right_corner_under_line_header_chr  = '\u2524'

list1.left_lateral_corner_chr  = '\u251C'
list1.right_lateral_corner_chr = '\u2524'
list1.left_vertical_line_chr   = '\u2502'
list1.right_vertical_line_chr  = '\u2502'

list1.middle_vertical_header_line_chr = '\u2502'
list1.left_vertical_header_line_chr   = '\u2502'
list1.right_vertical_header_line_chr  = '\u2502'

list1.top_horizontal_line_chr    = '\u2500'
list1.bottom_horizontal_line_chr = '\u2500'

list1.horizontal_line_under_header_chr = '\u2500'

list1.horizontal_line_under_header_on = 1
list1.middle_horizontal_line_on = 1
list1.bg_header = 6
list1.fg_header = 0
list1.bold_header = 1
list1.align_data = "left"
list1.bg_data = 55
list1.fg_data = 256

list1.adj_top_margin = 2

my_list = [["Header 1","Header 2","Header 3","Header 4"],["R2C1","R2C2","R2C3","R2C4"],
           ["R3C1","R3C2","R3C3","R3C4"],["R4C1","R4C2","R4C3","R4C4"]]

# list1.top_horizontal_line_on = 0
# list1.bottom_horizontal_line_on = 0
list1.print_fancy_format(my_list)

list1.top_horizontal_line_on = 0
list1.horizontal_line_under_header_on = 0
list1.middle_horizontal_line_on = 0
list1.bottom_horizontal_line_on = 0
list1.print_fancy_format(my_list)

print('\n')
