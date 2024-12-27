import custom_print as cp
pylo = cp.PyLO()
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def str_to_num(data:list, fill_value=0, update:bool=False)->list:

    '''  Converts elements of a list type to number type  '''

    def _get_number(x):
        try:
            numb = int(x)
            return numb                 # the number is integer or a string integer
        except:
            try:
                numb = float(x)
                return numb             # the number is float or a string float
            except:
                try:
                    numb = complex(x)    # the number is complex or a string complex
                    return numb
                except:
                    return "no_number_type"

    def _conver2number(n):
        numb = _get_number(n)
        if numb != "no_number_type":
            pass
        else:
            numb = _get_number(fill_value)
            if numb != "no_number_type":
                pass
            else:
                numb = 0

        return numb


    tempo = []; num_list = []
    list_type = cp._get_list_type(data)

    if list_type == "incorrect_variable_type":  pass

    elif list_type == "empty_list":             pass

    elif list_type == "one_item_no_row": # Done  ["dato"]
        num_list.append(_conver2number(data[0]))
        if update == True:
            data.clear()
            data.append(num_list[0])

    elif list_type == "one_item_one_row": # Done [["dato"]]
        num_list.append([_conver2number(data[0][0])])
        if update == True:
            data.clear()
            data.append([num_list[0][0]])

    elif list_type == "multiple_items_no_row": # Done ["Hello","bye","good"]
        [num_list.append(_conver2number(n)) for n in data]
        if update == True:
            data.clear()
            [data.append(n) for n in num_list]

    elif list_type == "multiple_items_one_row": # Done [["Hello","bye","good"]]
        tempo = []
        [tempo.append(_conver2number(data[0][n])) for n in range(len(data[0]))]
        num_list.append(tempo)
        if update == True:
            data.clear()
            [data.append(n) for n in num_list]

    # Done [["Hello"],["bye"],["good"]] or [["Hello","mio"],["bye"],["good","hh"]]
    elif list_type == "multiple_items_multiple_rows":
        n_rows = len(data)
        n_cols = 0
        # getting the longest number of columns in the list
        for n in data:
            if len(n) > n_cols:
                n_cols = len(n)

        # filling the empty spots
        for row in range(n_rows):
            for col in range(n_cols):
                try:
                    tempo.append(_conver2number(data[row][col]))
                except:
                    tempo.append(_conver2number(fill_value))
            num_list.append(tempo)
            tempo = []

        if update == True:
            data.clear()
            [data.append(n) for n in num_list]
        else: pass

    else:
        for n in data:
            num_list.append(_conver2number(n))

        if update == True:
            data.clear()
            [data.append(n) for n in num_list]

    return num_list

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
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
result = str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
lst = [];      print("original: ", lst)
result = str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
lst = ["5"];      print("original: ", lst)
result = str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
print()
lst = ["5.7"];    print("original: ", lst)
result = str_to_num(data=lst, fill_value="0.1", update=True)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
lst = [["1"]];      print("original: ", lst)
result = str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
print()
lst = [["-1.1"],["(6+3j)"]];    print("original: ", lst)
result = str_to_num(data=lst, fill_value="0.1", update=True)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 5  {cp.reset_font()}")
lst = ["-1.5",2,"3","4.5","5",6,"(5+5j)"];      print("original: ", lst)
result = str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
print(f"Addition:  (1+2j)+result[6] {(1+2j)+result[6]}")


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 6  {cp.reset_font()}")
lst = [["1",2],["3.3",4],["-5",6],["-7.7",8]];      print("original: ", lst)
result = str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
print()
lst = [["t",2],["-4",3],["-5.5","6.0",5]];      print("original: ", lst)
result = str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 7  {cp.reset_font()}")
lst = ["-10.5","-40",["50"],[250],["H"],"10"];      print("original: ", lst)
result = str_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)











print(msg)
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 1  {cp.reset_font()}")
lst = "hello";      print("original: ", lst)
result = pylo.data_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
lst = [];      print("original: ", lst)
result = pylo.data_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
lst = ["5"];      print("original: ", lst)
result = pylo.data_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
print()
lst = ["5.7"];    print("original: ", lst)
result = pylo.data_to_num(data=lst, fill_value="0.1", update=True)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
lst = [["1"]];      print("original: ", lst)
result = pylo.data_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
print()
lst = [["-1.1"],["(6+3j)"]];    print("original: ", lst)
result = pylo.data_to_num(data=lst, fill_value="0.1", update=True)
print("result  : ",result)
print("Original:",lst)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 5  {cp.reset_font()}")
lst = ["-1.5",2,"3","4.5","5",6,"(5+5j)"];      print("original: ", lst)
result = pylo.data_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
print(f"Addition:  (1+2j)+result[6] = {(1+2j)+result[6]}")


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,90,231)}  Case 6  {cp.reset_font()}")
lst = [["1",2],["3.3",4],["-5",6],["-7.7",8]];      print("original: ", lst)
result = pylo.data_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)
print()
lst = [["t",2],["-4",3],["-5.5","6.0",5]];      print("original: ", lst)
result = pylo.data_to_num(data=lst, fill_value="0.1", update=False)
print("result  : ",result)


#-------------------------------------------------------------------------------------------
print(f"{cp.ins_chr(n=80, unicode="-")}")

print(f"{cp.set_font(1,90,231)}  Case 7  fill_value = 10 {cp.reset_font()}")
lst = ["-10.5","-40",["50"],[250],["a","H"],"10"]
print("original: ", lst)
result = pylo.data_to_num(data=lst, fill_value=10, update=False)
print("result  : ",result)
print("original: ", lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print(f"{cp.set_font(1,90,231)}  fill_value = \'A\' {cp.reset_font()}")
print("original: ", lst)
result = pylo.data_to_num(data=lst, fill_value='A', update=True)
print("result  : ",result)
print("original: ", lst)

print(f"{cp.Bg.BLOOD_RED} When NOT possible the conversion, it will set to 0 {cp.Bg.OFF}")