import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()
tbl.title_bg  = 90
tbl.title_bold = True
tbl.title_italic = True
tbl.title_align = cp.Align.CENTER

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



people = [\
      ["Names",  "Lasts",   "Age"],
      ["Pancho", "Melti",    50  ],
      ["Javier", "Nangy",    32  ],
      ["Melony", "Archi",    40  ],
      ["Jose",   "Valvimar", 18  ]]

tbl.title_msg = " Original People List "
tbl.print_fancy_format(people)
print(f"{cp.set_font(1,23,231)} Delete age item on header with case_sensitive=False, update=True. {cp.reset_font()}")



new_people = pylo.delete_value(data=people, value="age", case_sensitive=False, update=True)  # case 6
print(new_people)
tbl.title_msg = " Age Deleted "
tbl.print_fancy_format(people)






print(f"{cp.set_font(1,23,231)} Original {cp.reset_font()}")


cp.ins_newline(2)


print(f"{cp.set_font(1,23,231)} Delete 3 case_sensitive=False, update=False. {cp.reset_font()}")
numbers = [[11,[10,3],12,3],[14,15,3],[12,3,3]] # case 7
# numbers = [0,1,2,8,3,9,7,3]                     # case 5
# numbers = [[1,3,5,6,9,3]]                       # case 8
# numbers = [[3]]                                 # case 4
# numbers = [3]                                   # case 3
# numbers = []                                      # case 2
# numbers = 3                                     # case 1

new_numbers = pylo.delete_value(numbers, 3, False, False)
print("3 is gone: ",new_numbers)
print("Original : ",numbers)