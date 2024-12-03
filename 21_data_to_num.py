import custom_print as cp
pylo = cp.PyLO()

print(f"{cp.ins_chr(n=80, unicode="-")}")
msg = '''
Options                                       # Results                           Cases
lst = "hello"                                 # incorrect_variable_type             1
lst = []                                      # empty_list                          2

lst = ["5"]                                   # one_item_no_row                     3
lst = ["-5.7"]                                # one_item_no_row                     3

lst = [["1"]]                                 # one_item_one_row                    4
lst = [["-1.1"],["(6+3j)"]]                   # one_item_one_row                    4

lst = ["-1.5",2,"3","4.5","5",6,"(5+5j)"]     # multiple_items_no_row               5

lst = [["1",2],["3.3",4],["-5",6],["-7.7",8]] # multiple_items_multiple_rows        6
lst = [["t",2],["-4",3],["-5.5","6.0",5]]

lst = ["-10.5","-40",["50"],[250],["H"],"10"] # mix_items                           7
'''

print(msg)
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 1  {cp.reset_font()}")
lst = "hello";      print("original: ", lst)
result = pylo.str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
lst = [];      print("original: ", lst)
result = pylo.str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
lst = ["5"];      print("original: ", lst)
result = pylo.str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
print()
lst = ["5.7"];    print("original: ", lst)
result = pylo.str_to_num(data=lst, fill_value="0.1", update=True)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
lst = [["1"]];      print("original: ", lst)
result = pylo.str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
print()
lst = [["-1.1"],["(6+3j)"]];    print("original: ", lst)
result = pylo.str_to_num(data=lst, fill_value="0.1", update=True)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 5  {cp.reset_font()}")
lst = ["-1.5",2,"3","4.5","5",6,"(5+5j)"];      print("original: ", lst)
result = pylo.str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
print(f"Addition:  (1+2j)+result[6] {(1+2j)+result[6]}")


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 6  {cp.reset_font()}")
lst = [["1",2],["3.3",4],["-5",6],["-7.7",8]];      print("original: ", lst)
result = pylo.str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
print()
lst = [["t",2],["-4",3],["-5.5","6.0",5]];      print("original: ", lst)
result = pylo.str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 7  {cp.reset_font()}")
lst = ["-10.5","-40",["50"],[250],["H"],"10"];      print("original: ", lst)
result = pylo.str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
