'''
Demo 1...!
'''


import custom_print as cp

list1 = cp.FancyFormat()
csr   = cp.Cursor()
draw  = cp.Pen()
msg   = cp.FancyMessage()


ncols, nrows = cp.dimensions()
cp.resize(40, 125)


lst = [["Header 1","Header 2","Header 3","Header 4"],
       ["R2C1","R2C2","R2C3","R2C4"],
       ["R3C1","R3C2","R3C3","R3C4"],
       ["R3C1","R3C2"]]

list1.print_fancy_format(lst)

#-------------------------------------------------------------------------------------
# int, bool, str, complex, float, range (horizontal and vertical), dictionary
# set (horizontal and vertical), and fronzenset (horizontal and vertical) variables.
#-------------------------------------------------------------------------------------
# SETTINGS FOR THE Fancy_Format Class:

# general use
list1.adj_indent = 6
list1.inverse_data = True
#list1.update_list = 1

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
list1.middle_vertical_header_line_chr = '\u2022'   # matrix list only
list1.horizontal_line_under_header_on = 1          # horizontal line between headers and the firs data row.
                                                   # 1 shows it and 0 hides it
list1.horizontal_line_under_header_chr = "-"       # chr to be printed for theheader line
list1.bg_header   = 55
list1.fg_data     = 1
list1.bold_header = 1
list1.bg_all_cell_header = False

print()
#------------------------------------------------------------------------------------------------------
# Printing from right to left  <--                                                                    -
# bool type                                                                                           -
#------------------------------------------------------------------------------------------------------
list1.adj_indent   = 20
list1.msg_title    = " bool "
list1.msg_footnote = " Case 0 "
my_list0 = True
list1.print_fancy_format(my_list0)

# int type
print(csr.moveTo(6,"up"))
list1.adj_indent   = 2
list1.msg_title    = " int "
list1.msg_footnote = " Case 1 "
my_list0 = 2547
list1.print_fancy_format(my_list0)
cp.ins_newline(2)


#------------------------------------------------------------------------------------------------------
# Printing from left to right -->                                                                     -
# str type                                                                                            -
#------------------------------------------------------------------------------------------------------
list1.msg_title    = " str "
list1.msg_footnote = " Case 4 "
my_list0 = "Hello There"
list1.print_fancy_format(my_list0)

# float type
print(csr.moveTo(5,"up"),end="")
list1.adj_indent = 48
list1.msg_title  = " float "
list1.msg_footnote = " Case 2 "
my_list0 = 25.987
list1.print_fancy_format(my_list0)


# complex type
print(csr.moveTo(5,"up"),end="")
list1.adj_indent  = 25
list1.msg_title    = " complex "
list1.msg_footnote = " Case 3 "
my_list0 = 45.8+698j
list1.print_fancy_format(my_list0)
cp.ins_newline(2)

compl = 45.9+25j
newl = cp.complex2list(compl)
list1.print_fancy_format(newl)


# square
list1.adj_indent = 2
sp_list = []; n = 0
while n < 16:
    sp_list.append([cp.ins_chr(85)])
    n += 1


list1.bg_header    = -1
list1.fg_data      = -1
list1.msg_title    = ""
list1.msg_footnote = ""
list1.horizontal_line_under_header_on = False
list1.print_fancy_format(sp_list)
list1.horizontal_line_under_header_on = True

list1.adj_indent = 8
list1.bg_header  = 55
list1.fg_data    = 1

list1.blinking_header    = True
list1.bg_all_cell_header = True

# range type
   # vertical
print(csr.moveTo(16,"up"),end="")
list1.adj_indent = 65
x = range(0,16,2)
l = cp.range2list(x,"Header","vertical")
list1.msg_title      = " Range Data"; list1.msg_footnote =" Case 5 "
list1.print_fancy_format(l)


   # horizontal
print(csr.moveTo(14,"up"),end="")
list1.adj_indent = 8
x = range(0,16,2)
list1.msg_title    = " Range Data"
list1.msg_footnote = " Case 5 "
list1.print_fancy_format(x)


# dictionary type
list1.msg_title    = " Dictionary "
list1.msg_footnote =" Case 6 "
dict_tags = {"NAME":"name", "LAST_1":"last_1", "LAST_2":"last_2"}
cp.terminal_bell()
list1.print_fancy_format(dict_tags)
cp.ins_newline(2)

mensaje = f"{cp.ins_chr(44)}THE END"
msg.print_fancy_message(mensaje)

input("Enter to Continue: ")
cp.resize(nrows, ncols)
