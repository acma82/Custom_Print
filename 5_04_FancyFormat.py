'''  Demo  '''
import custom_print

list1 = custom_print.FancyFormat()

# title
list1.title_bg    = 11
list1.title_fg    = 0
list1.title_bold  = 1
list1.title_align = "r"
list1.title_msg   = " Title List "

# footnote
list1.footnote_align = "l"
list1.footnote_msg   = " Footnote "
list1.footnote_fg    = 226
list1.footnote_bg    = 6
list1.footnote_bold  = 1

list1.header_horizontal_line_on = 1
list1.middle_horizontal_line_on = 1
list1.header_bg = 6
list1.header_fg = 0
list1.header_bold = 1
list1.data_align = "left"
list1.data_bg = 55
list1.data_fg = 256

list1.adj_top_margin = 2

my_list = [["Header 1","Header 2","Header 3","Header 4"],["R2C1","R2C2","R2C3","R2C4"],
           ["R3C1","R3C2","R3C3","R3C4"],["R4C1","R4C2","R4C3","R4C4"]]

list1.print_fancy_format(my_list, custom_print.Line_Style.SINGLE_LINE)

list1.top_horizontal_line_on = 0
list1.header_horizontal_line_on = 0
list1.middle_horizontal_line_on = 0
list1.bottom_horizontal_line_on = 0
list1.print_fancy_format(my_list)

