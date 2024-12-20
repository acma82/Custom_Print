'''  Demo 2  '''

import os
import source.custom_print as cp

list1 = cp.FancyFormat()
csr   = cp.Cursor()
draw  = cp.Pen()
msg   = cp.FancyMessage()


ncols, nrows = cp.dimensions()
cp.resize(44, 95)

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

list1.print_fancy_format(sp_list,cp.Line_Style.DOUBLE)

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
# horizontal line between headers and the firs data row. 1 shows it and 0 hides it
list1.horizontal_line_under_header_on = 1
list1.bg_header = 55
list1.fg_data   = 1

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
cp.resize(nrows, ncols)
