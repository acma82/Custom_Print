'''
Demo 1...!
'''
import custom_print as cp

tbl  = cp.FancyFormat()
csr  = cp.Cursor()
pylo = cp.PyLO()
#-------------------------------------------------------------------------------------
# int, bool, str, complex, float, range (horizontal and vertical), dictionary
# set (horizontal and vertical), and fronzenset (horizontal and vertical) variables.
#-------------------------------------------------------------------------------------
# SETTINGS FOR THE Fancy_Format Class:

print()
# float type
tbl.title_msg  = " float "
tbl.footnote_msg = " Case 2 "
my_list0 = 25.987
tbl.adj_indent = 60
tbl.print_fancy_format(my_list0)


# int type
tbl.title_msg    = " int "
tbl.footnote_msg = " Case 1 "
my_integer = 2547
tbl.adj_indent = 35
print(csr.moveTo(5,"up"),end="")
tbl.print_fancy_format(my_integer)

# bool type                                                                                           -
tbl.title_msg    = " bool "
tbl.footnote_msg = " Case 0 "
my_bool = True
tbl.adj_indent = 12
print(csr.moveTo(5,"up"),end="")
tbl.print_fancy_format(my_bool)
cp.ins_newline(2)


# complex type
tbl.adj_indent  = 60
tbl.title_msg    = " complex "
tbl.footnote_msg = " Case 3 "
my_list0 = 45.8+698j
tbl.print_fancy_format(my_list0)


print(csr.moveTo(5,"up"),end="")
tbl.adj_indent  = 35
pylo = cp.PyLO()
compl = 45.9+25j
newl = pylo.complex_to_list(compl)
tbl.print_fancy_format(newl)

# string
print(csr.moveTo(5,"up"),end="")
tbl.adj_indent  = 12
tbl.title_msg    = " str "
tbl.footnote_msg = " Case 4 "
my_list0 = "Hello There"
tbl.print_fancy_format(my_list0)
cp.ins_newline(2)


# range type
   # vertical
tbl.adj_indent = 65
x = range(0,16,2)
tbl.set_layout = cp.Layout.VERTICAL
tbl.title_msg      = " Range Data"; tbl.footnote_msg =" Case 5 "
tbl.print_fancy_format(x)

   # horizontal
print(csr.moveTo(12,"up"),end="")
tbl.adj_indent = 8
# x = range(0,16,2)
tbl.title_msg    = " Range Data"
tbl.footnote_msg = " Case 5 "
tbl.set_layout = cp.Layout.HORIZONTAL
tbl.print_fancy_format(x)
cp.ins_newline(2)


# dictionary type
tbl.title_msg    = " Dictionary Vertical"
tbl.footnote_msg =" Case 6 "
dict_tags = {"NAME":"name", "LAST_1":"last_1", "LAST_2":"last_2"}
cp.terminal_bell()
tbl.set_layout = cp.Layout.VERTICAL
tbl.print_fancy_format(dict_tags)
cp.ins_newline(4)
tbl.title_msg    = " Dictionary Horizontal"
tbl.set_layout = cp.Layout.HORIZONTAL
tbl.print_fancy_format(dict_tags)
cp.ins_newline(2)



tbl.title_msg    = " Tuple "
tupleData9 = (("hello","hello"),("hell",),("hi","bye","good"),[1,2], "hello")
tbl.print_fancy_format(tupleData9)

