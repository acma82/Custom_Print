'''
Demo 2 for fancyprint module...!
'''

import os
import custom_print as cp

list1 = cp.FancyFormat()
csr   = cp.Cursor()
draw  = cp.Pen()
msg   = cp.FancyMessage()


ncols, nrows = cp.dimensions()
os.system("resize -s 44 95")

# setting for the format
# general use

list1.adj_indent = 3
list1.horizontal_line_under_header_on = False
#list1.update_list = 1
list1.dim_header = True

print()

high = 0
sp_list = []
while high < 19:
    sp_list.append([cp.ins_chr(85)])
    high += 1

# Double Line Square
list1.bold_title  = True
list1.bg_title    = 22
list1.fg_title    = 15
list1.align_title = "left"
list1.msg_title   = f"{cp.ins_chr(34)}Nice Double Line Frame{cp.ins_chr(35)}"

# Corner Section
list1.top_left_corner_chr     = '\u2554'         # 13
list1.top_right_corner_chr    = '\u2557'         # 14
list1.bottom_right_corner_chr = '\u255d'         # 15
list1.bottom_left_corner_chr  = '\u255a'         # 16

# Vertical Line Selection
list1.left_vertical_line_chr  = "\u2551"         # 11
list1.right_vertical_line_chr = "\u2551"         # 12
# Horizontal Line
list1.top_horizontal_line_chr    = '\u2550'      # 9
list1.bottom_horizontal_line_chr = '\u2550'      # 10
# Header Section
list1.left_vertical_header_line_chr  = "\u2551"  # 22
list1.right_vertical_header_line_chr = "\u2551"  # 23


list1.print_fancy_format(sp_list)




# title
list1.bg_title = 11
list1.fg_title = 21
list1.bold_title  = 1
list1.align_title = "l"

# footnote
list1.align_footnote = "r"
list1.fg_footnote    = 226
list1.bg_footnote    = 6
list1.bold_footnote  = 1

# header
list1.middle_vertical_header_line_chr = '\u2022'  # matrix list only
list1.horizontal_line_under_header_on = 1         # horizontal line between headers and the firs data row. 1 shows it and 0 hides it
list1.horizontal_line_under_header_chr = "-"      # chr to be printed for theheader line
list1.bg_header = 55
list1.fg_data   = 1

list1.top_left_corner_chr     = "+"            # 13
list1.top_right_corner_chr    = "+"            # 14
list1.bottom_right_corner_chr = "+"            # 15
list1.bottom_left_corner_chr  = "+"            # 16

list1.left_vertical_line_chr  = "|"            # 11
list1.right_vertical_line_chr = "|"            # 12
list1.bottom_horizontal_line_chr = "-"         # 10

list1.left_vertical_header_line_chr   = "|"    # 22
list1.right_vertical_header_line_chr  = "|"    # 23
list1.top_horizontal_line_chr = "-"            #

# set vertical
print(csr.moveTo(qty=19,direction=cp.Move.UP), end="")
list1.msg_title    = " Set Data "
list1.msg_footnote = " Case 7 "
set_tags = {1,3,5,7,9}
list1.adj_indent = 70
new_set = cp.set2list(set_tags, "Header", cp.Layout.VERTICAL)
list1.print_fancy_format(new_set)


# Frozenset vertical
list1.msg_title    = " FrozenSet Data "
list1.msg_footnote = " Case 8 "
vowelsT = ("a", "e", "i", "o", "u")
frozenset_Tuple = frozenset(vowelsT)

print(csr.moveTo(qty=11,direction=cp.Move.UP), end="")
list1.adj_indent = 47
vowellist = cp.set2list(frozenset_Tuple,"header",cp.Layout.VERTICAL)
list1.print_fancy_format(vowellist)


# set horizontal
print(csr.moveTo(qty=11,direction=cp.Move.UP), end="")
list1.adj_indent   = 6
list1.msg_title    = " Set Data "
list1.msg_footnote = " Case 7 "
list1.print_fancy_format(set_tags)


# Frozenset horizontal
list1.inverse_title = True
list1.msg_title     = " FrozenSet Data "
list1.msg_footnote  = " Case 8 "
list1.print_fancy_format(frozenset_Tuple)

vowellist = cp.set2list(frozenset_Tuple)
list1.print_fancy_format(vowellist)
cp.ins_newline(4)

mensaje = f"{cp.ins_chr(44)}THE END"
msg.print_fancy_message(mensaje)

input("Enter to Continue: ")
os.system(f"resize -s {nrows} {ncols}")
