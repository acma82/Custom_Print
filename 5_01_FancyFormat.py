'''  Demo 2  '''

import custom_print as cp

list1 = cp.FancyFormat()
csr   = cp.Cursor()
# draw  = cp.Pen()
msg   = cp.FancyMessage()


ncols, nrows = cp.dimensions()
cp.resize(44, 95)

# setting for the format
# general use

list1.adj_indent = 3
list1.header_horizontal_line_on = False
#list1.update_list = 1
list1.header_dim = True

print()

high = 0
sp_list = []
while high < 19:
    sp_list.append([cp.ins_chr(85)])
    high += 1

# Double Line Square
list1.title_bold  = True
list1.title_bg    = 22
list1.title_fg    = 15
list1.title_align = "left"
list1.title_msg   = f"{cp.ins_chr(34)}Nice Double Line Frame{cp.ins_chr(35)}"

list1.print_fancy_format(sp_list,cp.Line_Style.DOUBLE_LINE)




# title
list1.title_bg = 11
list1.title_fg = 21
list1.title_bold  = 1
list1.title_align = "l"

# footnote
list1.footnote_align = "r"
list1.footnote_fg    = 226
list1.footnote_bg    = 6
list1.footnote_bold  = 1

# header
# horizontal line between headers and the firs data row. 1 shows it and 0 hides it
list1.header_horizontal_line_on = 1
list1.header_bg = 55
list1.data_fg   = 1

list1.data_align = "c"#cp.Align.CENTER
list1.header_align = "c"


# set vertical
print(csr.moveTo(qty=19,direction=cp.Move.UP), end="")
list1.title_msg    = " Set Data "
list1.footnote_msg = " Case 7 "
set_tags = {1,3,5,7,9}
list1.adj_indent = 70
pylo = cp.PyLO()
new_set = pylo.set_to_list(set_tags, "Header", cp.Layout.VERTICAL)
list1.print_fancy_format(new_set)


# Frozenset vertical
list1.title_msg    = " FrozenSet Data "
list1.footnote_msg = " Case 8 "
vowelsT = ("a", "e", "i", "o", "u")
frozenset_Tuple = frozenset(vowelsT)

print(csr.moveTo(qty=11,direction=cp.Move.UP), end="")
list1.adj_indent = 47
vowellist = pylo.set_to_list(frozenset_Tuple,"header",cp.Layout.VERTICAL)
list1.print_fancy_format(vowellist)


# set horizontal
print(csr.moveTo(qty=11,direction=cp.Move.UP), end="")
list1.adj_indent   = 6
list1.title_msg    = " Set Data "
list1.footnote_msg = " Case 7 "
list1.print_fancy_format(set_tags)


# Frozenset horizontal
list1.title_inverse = True
list1.title_msg     = " FrozenSet Data "
list1.footnote_msg  = " Case 8 "
list1.print_fancy_format(frozenset_Tuple)

vowellist = pylo.set_to_list(data=frozenset_Tuple, layout=cp.Layout.HORIZONTAL, header_title=None)
list1.print_fancy_format(vowellist)
cp.ins_newline(4)





mensaje = f"{cp.ins_chr(44)}THE END"
msg.print_fancy_message(mensaje)

input("Enter to Continue: ")
cp.resize(nrows, ncols)


