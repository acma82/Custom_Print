'''
Demo 3 for fancyprint module...!
'''

import custom_print as cp

list1 = cp.FancyFormat()
csr   = cp.Cursor()
draw  = cp.Pen()


ncols, nrows = cp.dimensions()
cp.resize(45, 120)


# setting for the format
# general use
list1.bg_all_cell_header = False
list1.adj_indent = 6
list1.horizontal_line_under_header_on = False
#list1.update_list = 1
list1.bold_header = True
# list1.inverse_header = True

print()

high = 0
sp_list = []
while high < 20:
    sp_list.append([cp.ins_chr(95)])
    high += 1

# single line square
mymsg = f"{cp.ins_chr(35)}Nice Single Line Frame.{cp.ins_chr(35)}"


list1.bold_title  = True
list1.bg_title    = 22
list1.fg_title    = 15
list1.align_title = "left"
list1.msg_title   = f"{cp.ins_chr(39)}Tuple Style Is on \N{FIRE}{cp.ins_chr(40)}" # {"\U0001F525"} fire number
list1.print_fancy_format(mymsg,cp.Line_Style.SINGLE)

# Corner Section
list1.top_left_corner_chr     = '\u250C'          # 13
list1.top_right_corner_chr    = '\u2510'          # 14
list1.bottom_right_corner_chr = '\u2518'          # 15
list1.bottom_left_corner_chr  = '\u2514'          # 16

# Horizontal Line
list1.top_horizontal_line_chr    = '\u2500'       # 9
list1.bottom_horizontal_line_chr = '\u2500'       # 10

# Vertical Line Selection
list1.left_vertical_line_chr  = "\u2502"          # 11
list1.right_vertical_line_chr = "\u2502"          # 12

# Header Section
list1.left_vertical_header_line_chr   = "\u2502"  # 22
list1.right_vertical_header_line_chr  = "\u2502"  # 23


#list1.print_fancy_format(sp_list)
print("\n")
#------------------------------------------------------------------------------------------------
# The end of the single line square                                                             -
#------------------------------------------------------------------------------------------------
# title
list1.bg_title    = 11
list1.fg_title    = 0
list1.bold_title  = 1
list1.align_title = "l"

# footnote
list1.align_footnote = "r"
list1.fg_footnote    = 226
list1.bg_footnote    = 6
list1.bold_footnote  = 1

# header
list1.middle_vertical_header_line_chr  = '\u2022' # matrix list only
list1.horizontal_line_under_header_on  = 1        # horizontal line between headers and the firs data row. 1 shows it and 0 hides it
list1.horizontal_line_under_header_chr = "-"      # chr to be printed for theheader line
list1.bg_header = 55
list1.fg_data   = 1 

list1.top_left_corner_chr     = "+"            # 13
list1.top_right_corner_chr    = "+"            # 14
list1.bottom_right_corner_chr = "+"            # 15
list1.bottom_left_corner_chr  = "+"            # 16

list1.top_horizontal_line_chr = "-"            # 9
list1.bottom_horizontal_line_chr = "-"         # 10
list1.left_vertical_line_chr  = "|"            # 11
list1.right_vertical_line_chr = "|"            # 12

list1.left_vertical_header_line_chr   = "|"    # 22
list1.right_vertical_header_line_chr  = "|"    # 23


# Tuples all the cases
       # Case 1, 2, 3
tupleData1 = ("",)
tupleData2 = ("Apple",)
tupleData3 = (("Apple",))

tupleData4 = (("Header",),("hell",),("hi",),([1,2],)) # this is a simple tuple w/ tuples       Case 4
tupleData5 = (("Header 0","Header 1"),("hell",),("hi","bye","good"),([1,2],)) #                Case 4
tupleData6 = ("Header 0","hell","hi",[1,2])             # this is a simple tuple w/ string     Case 5
tupleData7 = (("Header 0"),("hell"),("hi"),([1,2]))     # this is a simple tuples w/ string    Case 5


list1.adj_indent   = 8
list1.msg_title    = " Case 1 "
list1.msg_footnote = "('',)"
list1.print_fancy_format(tupleData1)

csr.jumpTo(5, "up" )
list1.adj_indent   = 20
list1.msg_title    = " Case 2 "
list1.msg_footnote = "('apple',)"
list1.print_fancy_format(tupleData2)

csr.jumpTo(5, "up" )
list1.adj_indent   = 36
list1.msg_title    = " Case 3 "
list1.msg_footnote = "(('apple',))"
list1.print_fancy_format(tupleData2)


csr.jumpTo(5, "up" )
list1.adj_indent   = 52
list1.msg_title    = " Case 4 "
list1.msg_footnote = " One Col "
list1.print_fancy_format(tupleData4)


csr.jumpTo(9, "up" )
list1.adj_indent   = 69
list1.msg_title    = " Case 4 "
list1.msg_footnote = " Tuple Table Type"
list1.print_fancy_format(tupleData5)

print()
list1.adj_indent   = 8
list1.msg_title    = " Case 5 "
list1.msg_footnote = " One Row"
list1.print_fancy_format(tupleData6)

csr.jumpTo(5, "up" )
list1.adj_indent   = 52
list1.msg_title    = " Case 5 "
list1.msg_footnote = " Tuple Table Type"
list1.print_fancy_format(tupleData5)
print()

# this is a tuple w/ combination other type of variables Case 6
list1.adj_indent = 52
list1.msg_title  = " Case 6 "
tupleData9 = (("hello","hello"),("hell",),("hi","bye","good"),[1,2], "hello")
list1.msg_footnote = " Vars Combination in a Tuple "
list1.print_fancy_format(tupleData9)

msg = f"{cp.ins_chr(44)}THE END.....!{cp.ins_chr(44)}"


input("Enter to Continue: ")
cp.resize(nrows, ncols)
