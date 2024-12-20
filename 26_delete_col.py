'''
Eliminate a column in a list, it has to be a list with rows and cols as a table.
Otherwise, it will be ignored.
'''
import source.source.custom_print as cp
pylo = cp.PyLO()
tbl = cp.FancyFormat()
#tbl.set_fill_chr = " "

msg = f'''
   Options                             Results                           Cases
   list_1 = "hello"                    incorrect_variable_type             1
   list_1 = []                         empty_list                          2
   list_1 = [5]                        one_item_no_row                     3
   list_1 = [[1]]                      one_item_one_row                    4
   list_1 = [1,2,3,4,5,6]              multiple_items_no_row               5
   list_1 = [[1,2],[3,4],[5,6]]        multiple_items_multiple_rows        6
   list_1 = [[1],[4],[5,6]]
   list_1 = [10,[50],[250],["H"],100]  mix_items                           7
   list_1 = [[1,2,3,4,5,6]]            multiple_items_one_row              8 
   '''
print(msg)

print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,23,231)} Case 1. index = 0, update=False {cp.reset_font()}")
lst_1 = "hello"
print("Original str: ",lst_1)
result = pylo.delete_col(lst_1,0, update=False)
print("Result      : ",result)
print("New Original: ",lst_1)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print(f"{cp.set_font(1,23,231)} Case 2. index = 0, update=True {cp.reset_font()}")
lst_2 = []
print("Original    : ",lst_2)
result = pylo.delete_col(lst_2,0, update=True)
print("Result      : ",result)
print("New Original: ",lst_2)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print(f"{cp.set_font(1,23,231)} Case 3. index = 0, update=False {cp.reset_font()}")
lst_3 = ["hello"]
print("Original    : ",lst_3)
result = pylo.delete_col(lst_3,0, update=False)
print("Result      : ",result)
print("New Original: ",lst_3)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print(f"{cp.set_font(1,23,231)} Case 4. index = 0, update=True {cp.reset_font()}")
lst_4 = [["hello"]]
print("Original    : ",lst_4)
result = pylo.delete_col(lst_4,0, update=True)
print("Result      : ",result)
print("New Original: ",lst_4)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print(f"{cp.set_font(1,23,231)} Case 5. index = 0, update=True {cp.reset_font()}")
lst_5 = [1,2,3,4,5,6]
print("Original    : ",lst_5)
result = pylo.delete_col(lst_5, 0, update=True)
print("Result      : ",result)
print("New Original: ",lst_5)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print(f"{cp.set_font(1,23,231)} Case 6. index = 0, update=False  {cp.reset_font()}")
lst_6 = [[1,2],[3,4],[5,6]]
print("Original    : ",lst_6)
result = pylo.delete_col(lst_6, 0, update=False)
print("Result      : ",result)
print("New Original: ",lst_6)

print(f"{cp.ins_chr(n=80, unicode="-")}")

lst_6 = [[1],[3],[5,6]]
print("Original    : ",lst_6)
result = pylo.delete_col(lst_6,0, update=False)
print("Result      : ",result)
print("New Original: ",lst_6)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print(f"{cp.set_font(1,23,231)} Case 7. index = 2, update=True  {cp.reset_font()}")
lst_7 =  [10,[50],[250],["H"],100] 
print("Original    : ",lst_7)
result = pylo.delete_col(lst_7,2, update=True)
print("Result      : ",result)
print("New Original: ",lst_7)


print(f"{cp.ins_chr(n=80, unicode="-")}")

print(f"{cp.set_font(1,23,231)} Case 8. index = 1, update=False {cp.reset_font()}")
lst_8 = [[1,2,3,4,5,6]]
print("Original    : ",lst_8)
result = pylo.delete_col(lst_8, 1, update=False)
print("Result      : ",result)
print("New Original: ",lst_8)

print(f"{cp.ins_chr(n=80, unicode="-")}")

methods = [\
    ["Cursor",  "FontStyle"  ,  "FancyMessage"       ,  "FancyFormat"       ,  "Pen"           ],
    ["jumpTo",  "start_style",  "print_fancy_message",  "print_fancy_format",  "draw_line"     ],
    ["jumpxy",  "stop_style" ,  "print_fancy_note"   ,  "reset_fancy_format",  "draw_rectangle"],
    ["moveTo",  "print_style",  "----"               ,  "----"              ,  "----"          ],
    ["movexy",  "reset_style",  "----"               ,  "----"              ,  "----"          ]]

tbl.bg_title = 90; tbl.align_title = cp.Align.CENTER
tbl.msg_title = " index = 2, update=False "
tbl.print_fancy_format(methods)
tbl.msg_title = " Result After Deleting col 2 "
new_list = pylo.delete_col(methods, 2)
tbl.print_fancy_format(new_list)

tbl.msg_title = " Adding Numbers, update=True "
pylo.number(methods, start_number=1, id_txt="No.", renumber=False, update=True)
tbl.print_fancy_format(methods)
