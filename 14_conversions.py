import custom_print as cp
paragraph = '''
 This is the Module Docstrings
 Trailing WhiteSpace refers to any whitespace characters 
 at the end of a line of code or string. 
 missing-final-newline refers to set
 the last empty line at the end of the code
 pylint practis.py
'''
fst = cp.FontStyle()
fst.bg = 231
fst.fg = 0
fst.bold = True
fst.bg_top_lines = 1
fst.bg_bottom_lines = 1
fst.align = cp.Align.CENTER

lst = cp.PyList()
#-------------------------------------------------------------------------------------------------------------------------------
#cp.ins_newline(2)
fst.print_style("  Working With Bool Type  ")
variable = True
result = lst.bool_to_list(data=variable, convert_to_str=False)
print(result)
result = lst.bool_to_list(data=variable, convert_to_str=True)
print(result)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
fst.print_style("  Working With Integer Type  ")
variable = 10
result = lst.int_to_list(data=variable, convert_to_str=False)
print(result)
result = lst.int_to_list(data=variable, convert_to_str=True)
print(result)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
fst.print_style("  Working With Float Type  ")
variable = 5.5
result = lst.float_to_list(data=variable, convert_to_str=False)
print(result)
result = lst.float_to_list(data=variable, convert_to_str=True)
print(result)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
fst.print_style("  Working With Complex Type  ")
variable = 5+5j
result = lst.complex_to_list(variable, False)
print(result)
result = lst.complex_to_list(variable, True)
print(result)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
fst.print_style("  Working With String Type  ")
print(f"{cp.set_font(1,90,231)}  WORD_BY_WORD  {cp.reset_font()}")
result = lst.str_to_list(data=paragraph, option=lst.Str_List_Option.WORD_BY_WORD)
print(result)
cp.ins_newline(2)
print(f"{cp.set_font(1,90,231)}  COUNTER_WORD  {cp.reset_font()}")
result = lst.str_to_list(paragraph, lst.Str_List_Option.COUNTER_WORD)
print(result)
cp.ins_newline(2)
print(f"{cp.set_font(1,90,231)}  LINE_BY_LINE  {cp.reset_font()}")
result = lst.str_to_list(paragraph, lst.Str_List_Option.LINE_BY_LINE)
print(result)
cp.ins_newline(2)
print(f"{cp.set_font(1,90,231)}  COUNTER_LINE  {cp.reset_font()}")
result = lst.str_to_list(paragraph, lst.Str_List_Option.COUNTER_LINE)
print(result)
cp.ins_newline(2)
print(f"{cp.ins_chr(n=100, unicode="-")}")
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
mydict = {"Name":"Miguel Angel","Last":"Aguilar Cuesta","Country":"Mexico","Age":42, "Lista":[1,2,3]}
fst.print_style("  Working With Dictionary Type  ")
print(f"{cp.set_font(1,90,231)}  Case 1  {cp.reset_font()}")
result = lst.dict_to_list(data=mydict, convert_to_str=False)
for dato in result:
   print(dato)
cp.ins_newline(2)

print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
result = lst.dict_to_list(data=mydict, key_title="My Keys", value_title="My Values",convert_to_str=False)
for dato in result:
   print(dato)
cp.ins_newline(2)

print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
result = lst.dict_to_list(data=mydict, key_title="none", value_title=None,convert_to_str=False)
for dato in result:
   print(dato)
cp.ins_newline(2)
# Note: with one of then that is "none" or None, it won't set the key_title neither the value_title

print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
result = lst.dict_to_list(data=mydict, key_title="My Keys", value_title="My Values",convert_to_str=True)
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
l = lst.range_to_list(data=r, layout=cp.Layout.VERTICAL, convert_to_str=False)
for n in l:
   print(n)
cp.ins_newline(2)

print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
l = lst.range_to_list(data=r, header_title="none", layout=cp.Layout.VERTICAL, convert_to_str=False)
for n in l:
   print(n)
cp.ins_newline(2)

print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
l = lst.range_to_list(data=r, header_title="Header Title", layout=cp.Layout.VERTICAL, convert_to_str=False)
for n in l:
   print(n)
cp.ins_newline(2)

print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
l = lst.range_to_list(data=r, header_title="Header Title", layout="h", convert_to_str=True)
print(l)
cp.ins_newline(2)


#-------------------------------------------------------------------------------------------------------------------------------
fst.print_style("  Working With Set Type  ")