import custom_print as cp
pylo = cp.PyLO()
'''
The Header of the list are not sort. 
It was intended to use it with square list and lineal list
Number list does not do the reverse order = True.
'''
print(f"{cp.ins_chr(n=80, unicode="-")}")

lst = [[4,2,1,5,'8',-1,10,5]]
print("Original: ", lst)
result = pylo.sort_by_col(data=lst, fill_type=pylo.Fill_Type.NUMBER)  #"number")
print("Result  :",result)
result = pylo.sort_by_col(data=lst, fill_type=pylo.Fill_Type.NUMBER, reverse_order=False)
print("Result  :",result)

print(f"{cp.ins_chr(n=80, unicode="-")}")

classes_methods_fancyprint = [["Header 1","Header 2",     "Header 3",              "Header 4"        ,     "Header 5"],
                              ["Cursor",  "FontStyle",    "FancyMessage",          "FancyFormat"        ,  "Pen"],
                              ["jumpTo",  "start_style",  "print_fancy_message",   "print_fancy_format",   "draw_line"],
                              ["jumpxy",  "stop_style",   "print_fancy_note",      "reset_fancy_format",   "draw_rectangle"],
                              ["moveTo",  "print_style",  "----             ",      "----             ",   "----"],
                              ["movexy",  "reset_style",  "----             ",      "----             "   ]]

tbl = cp.FancyFormat()
tbl.print_fancy_format(classes_methods_fancyprint)
result = pylo.sort_by_col(data=classes_methods_fancyprint,ref_col=0, fill_type=pylo.Fill_Type.STRING, reverse_order=False)
tbl.print_fancy_format(result)

result = pylo.sort_by_col(data=classes_methods_fancyprint,ref_col=0, fill_type=pylo.Fill_Type.STRING, reverse_order=True)
tbl.print_fancy_format(result)


lst = [["Names","last","Ages"],[5,5,4],[1,2,3],[9,9,9],[0,1,1]]
tbl.print_fancy_format(lst)
result = pylo.sort_by_col(data=lst,ref_col=1, fill_type=pylo.Fill_Type.NUMBER, reverse_order=True)
tbl.print_fancy_format(result)

result = pylo.sort_by_col(data=lst,ref_col=1, fill_type=pylo.Fill_Type.NUMBER, reverse_order=False)
tbl.print_fancy_format(result)



