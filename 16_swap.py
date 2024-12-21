import custom_print as cp
pylo = cp.PyLO()

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
print(f"{cp.set_font(1,23,231)}    Swap Items in a List    {cp.reset_font()}")
lst = [[1,2],[3,4],[5,6],[7,8]]
print("original: ", lst,end=""); print("   update=False,  posi_1=0, posi_2=2")
newlist = pylo.swap(data=lst, update= False, posi_1= 0, posi_2=2)
print("swaped_l: ",newlist)
print("original: ", lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original: ", lst,end=""); print(f"   {cp.set_font(1,1,231)} update=True, {cp.reset_font()} posi_1=3, posi_2=0")
newlist = pylo.swap(data=lst, update=True, posi_1=3, posi_2=10)
print("swaped_l: ",newlist)
print("original: ", lst)

cp.ins_newline(2)
print(f"{cp.ins_chr(n=80, unicode="-")}")
newlist = pylo.swap(data=lst, update=True, posi_1=0, posi_2=0)
print("swaped_l: ",newlist)
print("original: ", lst)


'''
        This function swap two elements in a list.

        update is used to save the actual list with the swap elements.
        
        if update is set to False, then we keep the original list and save
        the new list into another variable.

        posi_1 -> position 1 to be swap with position 2
        posi_2 -> position 2 to be swap with position 1

        Note: If one of the position provided is out of range, the function
                will return the list as original and it will print a message
                out of range.    
'''
