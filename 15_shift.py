import custom_print as cp

lst = cp.PyList()
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
list_1 = [[1],[4],[5,6]]
# Right Shift List
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,23,231)}    Shift Item in a List    {cp.reset_font()}")
print(f"{cp.ins_chr(n=80, unicode="-")}")
cp.ins_newline(2)
#---------------------------------------------------------------------------
print("original_list:  ", list_1, end=""); print("   right_shift 2, update=False")
newlist = lst.shift(list_1, "r", 2, False)
print("shifted _list:  ",newlist)
print("original_list:  ", list_1)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original_list:  ", list_1,end=""); print("   right_shift 2, update=True")
newlist = lst.shift(data=list_1, direction=cp.Move.RIGHT, qty= 2, update= True)
print("shifted _list:  ",newlist)
print("original_list:  ", list_1)

cp.ins_newline(2)


# Left Shift List
list_1 = [[1,2,3,4,5,6]]
#---------------------------------------------------------------------------
print("original_list:  ", list_1, end=""); print("   left_shift 2, update=False")
newlist = lst.shift(list_1, "l", 2, False)
print("shifted _list:  ",newlist)
print("original_list:  ", list_1)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original_list:  ", list_1,end=""); print("   left_shift 2, update=True")
newlist = lst.shift(data=list_1, direction=cp.Move.LEFT, qty= 2, update= True)
print("shifted _list:  ",newlist)
print("original_list:  ", list_1)

'''
----------------------------------------------------------------------------
   This function shift the elements in a list to the left or right.

   update is used to save the actual list with the shift elements.
   If we set update to False, then we keep the original list and save
   the new list into another variable.
      
Options                             Results                   Cases
list_1 = "hello"                    incorrect_variable_type        1
list_1 = []                         empty_list                     2
list_1 = [5]                        one_item_no_row                3
list_1 = [[1]]                      one_item_one_row               4
list_1 = [1,2,3,4,5,6]              multiple_items_no_row          5
list_1 = [[1,2],[3,4],[5,6]]        multiple_items_multiple_rows   6
list_1 = [[1],[4],[5,6]]
list_1 = [10,[50],[250],["H"],100]  mix_items                      7
list_1 = [[1,2,3,4,5,6]]            multiple_items_one_row         8 
'''
