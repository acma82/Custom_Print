import custom_print as cp
paragraph = '''
 This is the Module Docstrings
 Trailing WhiteSpace refers to any whitespace characters 
 at the end of a line of code or string. 
 missing-final-newline refers to set
 the last empty line at the end of the code
 pyloint practis.py
'''
fst = cp.FontStyle()
fst.bg = 231
fst.fg = 0
fst.bold = True
fst.bg_top_lines = 1
fst.bg_bottom_lines = 1
fst.align = cp.Align.CENTER

pylo = cp.PyLO()
#-------------------------------------------------------------------------------------------------------------------------------
#cp.ins_newline(2)
fst.print_style("  Working With Bool Type  ")
variable = True
result = pylo.bool_to_list(data=variable, convert_to_str=False)
print(result)
result = pylo.bool_to_list(data=variable, convert_to_str=True)
print(result)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
fst.print_style("  Working With Integer Type  ")
variable = 10
result = pylo.int_to_list(data=variable, convert_to_str=False)
print(result)
result = pylo.int_to_list(data=variable, convert_to_str=True)
print(result)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
fst.print_style("  Working With Float Type  ")
variable = 5.5
result = pylo.float_to_list(data=variable, convert_to_str=False)
print(result)
result = pylo.float_to_list(data=variable, convert_to_str=True)
print(result)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
fst.print_style("  Working With Complex Type  ")
variable = 5+5j
result = pylo.complex_to_list(variable, False)
print(result)
result = pylo.complex_to_list(variable, True)
print(result)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
fst.print_style("  Working With String Type  ")
print(f"{cp.set_font(1,90,231)}  WORD_BY_WORD  {cp.reset_font()}")
result = pylo.str_to_list(data=paragraph, option=pylo.Str_List_Option.WORD_BY_WORD, counter=False)
print(result)
cp.ins_newline(2)
print(f"{cp.set_font(1,90,231)}  counter WORD_BY_WORD  {cp.reset_font()}")
result = pylo.str_to_list(paragraph, pylo.Str_List_Option.WORD_BY_WORD, counter=True)
print(result)
cp.ins_newline(2)
print(f"{cp.set_font(1,90,231)}  LINE_BY_LINE  {cp.reset_font()}")
result = pylo.str_to_list(paragraph, pylo.Str_List_Option.LINE_BY_LINE, counter=False)
print(result)
cp.ins_newline(2)
print(f"{cp.set_font(1,90,231)}  counter LINE_BY_LINE  {cp.reset_font()}")
result = pylo.str_to_list(paragraph, pylo.Str_List_Option.LINE_BY_LINE, counter=True)
print(result)
cp.ins_newline(2)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
mydict = {"Name":"Jose Alfredo","Last":"Jimenez","Country":"Mexico","Age":82, "Lista":[1,2,3]}
fst.print_style("  Working With Dictionary Type  ")
print(f"{cp.set_font(1,90,231)}  Case 1  {cp.reset_font()}")
result = pylo.dict_to_list(data=mydict, convert_to_str=False)
for dato in result:
   print(dato)
cp.ins_newline(2)

print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
result = pylo.dict_to_list(data=mydict, key_title="My Keys", value_title="My Values",convert_to_str=False)
for dato in result:
   print(dato)
cp.ins_newline(2)

print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
result = pylo.dict_to_list(data=mydict, key_title="none", value_title=None,convert_to_str=False)
for dato in result:
   print(dato)
cp.ins_newline(2)
# Note: with one of then that is "none" or None, it won't set the key_title neither the value_title

print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
result = pylo.dict_to_list(data=mydict, key_title="My Keys", value_title="My Values",convert_to_str=True)
for dato in result:
   print(dato)
print()
# Note: Check that the 42 number on Age is converted to String.

print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
fst.print_style("  Working With Range Type  ")
# Note:
# values for Range: convert_to_str = True/False,         -> layout="vertical"/"horizontal" or "h"/"v"
#                   header_title = ""                    -> this will put Range Value(s) for header_title
#                   header_title = None/"none"           -> It won't set any header_title
#                   header_title = "Any Title Header"
r = range(0,15,3)
print(r)
print(f"{cp.set_font(1,90,231)}  Case 1  {cp.reset_font()}")
l = pylo.range_to_list(data=r, layout=cp.Layout.VERTICAL, convert_to_str=False)
for n in l:
   print(n)
cp.ins_newline(2)

print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
l = pylo.range_to_list(data=r, header_title="none", layout=cp.Layout.VERTICAL, convert_to_str=False)
for n in l:
   print(n)
cp.ins_newline(2)

print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
l = pylo.range_to_list(data=r, header_title="Header Title", layout=cp.Layout.VERTICAL, convert_to_str=False)
for n in l:
   print(n)
cp.ins_newline(2)

print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
l = pylo.range_to_list(data=r, header_title="Header Title", layout="h", convert_to_str=True)
print(l)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
fst.print_style("  Working With Set Type  ")
# Note:
# values for Set:   convert_to_str = True/False,         -> layout="vertical"/"horizontal" or "h"/"v"
#                   header_title = ""                    -> this will put Set Value(s) for header_title
#                   header_title = None/"none"           -> It won't set any header_title
#                   header_title = "Any Title Header"
set_1 = {1,3,5,7,9}
print(f"{cp.set_font(1,90,231)}  Case 1  {cp.reset_font()}")
result = pylo.set_to_list(data=set_1, header_title="None", layout=cp.Layout.VERTICAL, convert_to_str=False)
print(result)
print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
result = pylo.set_to_list(data=set_1, header_title="", layout="vertical", convert_to_str=False)
print(result)
print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
result = pylo.set_to_list(data=set_1, layout="v", convert_to_str=False)
print(result)
print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
result = pylo.set_to_list(data=set_1, header_title="Hello_SET", layout="h", convert_to_str=True)
print(result)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


fst.print_style("  Working With FrozenSet Type  ")
# Note:
# values for Set:   convert_to_str = True/False,         -> layout="vertical"/"horizontal" or "h"/"v"
#                   header_title = ""                    -> this will put Frozenset Value(s) for header_title
#                   header_title = None/"none"           -> It won't set any header_title
#                   header_title = "Any Title Header"
set_1 = {1,3,5,7,9}
frozenset_1 = frozenset(set_1)
print(f"{cp.set_font(1,90,231)}  Case 1  {cp.reset_font()}")
result = pylo.set_to_list(data=frozenset_1, header_title="None", layout=cp.Layout.VERTICAL, convert_to_str=False)
print(result)
print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
result = pylo.set_to_list(data=frozenset_1, header_title="", layout="vertical", convert_to_str=False)
print(result)
print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
result = pylo.set_to_list(data=frozenset_1, layout="v", convert_to_str=False)
print(result)
print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
result = pylo.set_to_list(data=frozenset_1, header_title="Hello_SET", layout="h", convert_to_str=True)
print(result)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)

#-------------------------------------------------------------------------------------------------------------------------------
fst.print_style("  Working With Tuple  ")
tupleData1 = (("Apple"));    print("case 0:",tupleData1)       # this is a string                     Case 0
tupleData2 = ("",);          print("case 1:",tupleData2)       # this is a tuple                      Case 1
tupleData3 = ("Apple",);     print("case 2:",tupleData3)       # this is a simple tuple               Case 2
tupleData4 = (("Apple",));   print("case 3:",tupleData4)       # this is a tuple inside tuple         Case 3
print()
tupleData5 = (("hello",),("hell",),("hi",),([1,2],)) # this is a simple tuple w/ tuples     Case 4
tupleData6 = (("hello","hello"),("hell",),("hi","bye","good"),([1,2],)) #                   Case 4

print("Case 4:",tupleData5); print("Case 4:",tupleData6)
print()

tupleData7 = ("hello","hell","hi",[1,2])             # this is a simple tuple w/ string     Case 5
tupleData8 = (("hello"),("hell"),("hi"),([1,2]))     # this is a simple tuples w/ string    Case 5
print("Case 5:",tupleData7); print("Case 5:",tupleData8)
print()

# this is a tuple w/ combination other type of variables Case 6
tupleData9 = (("hello","hello"),("hell",),("hi","bye","good"),[1,2], "hello")
print("Case 6:",tupleData9)
print()

listData1 = pylo.tuple_to_list(tupleData1);   print("Case 0:",listData1)
listData2 = pylo.tuple_to_list(tupleData2);   print("Case 1:",listData2)
listData3 = pylo.tuple_to_list(tupleData3);   print("Case 2:",listData3)
listData4 = pylo.tuple_to_list(tupleData4);   print("Case 3:",listData4)
listData5 = pylo.tuple_to_list(tupleData5);   print("Case 4:",listData5)
listData6 = pylo.tuple_to_list(tupleData6);   print("Case 4:",listData6)
listData7 = pylo.tuple_to_list(tupleData7);   print("Case 5:",listData7)
listData8 = pylo.tuple_to_list(tupleData8);   print("Case 5:",listData8)
listData9 = pylo.tuple_to_list(tupleData9);   print("Case 6:",listData9)
print(f"{cp.ins_chr(n=100, unicode="-")}")
print()


