
import custom_print as cp
pylo = cp.PyLO()

def num_to_str(data:list, fill_value="----", update:bool=False)->list:
   tempo = []; str_list = []
   list_type = cp._get_list_type(data)

   if list_type == "incorrect_variable_type":  pass

   elif list_type == "empty_list":             pass

   elif list_type == "one_item_no_row": # Done  ["dato"]
      str_list.append(str(data[0]))
      if update == True:
            data.clear()
            data.append(str_list[0])

   elif list_type == "one_item_one_row": # Done [["dato"]]
      str_list.append([str(data[0][0])])
      if update == True:
            data.clear()
            data.append([str_list[0][0]])

   elif list_type == "multiple_items_no_row": # Done ["Hello","bye","good"]
      [str_list.append(str(n)) for n in data]
      if update == True:
            data.clear()
            [data.append(n) for n in str_list]

   elif list_type == "multiple_items_one_row": # Done [["Hello","bye","good"]]
      tempo = []
      [tempo.append(str(data[0][n])) for n in range(len(data[0]))]
      str_list.append(tempo)
      if update == True:
            data.clear()
            [data.append(n) for n in str_list]

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
                  tempo.append(str(data[row][col]))
               except:
                  tempo.append(str(fill_value))
            str_list.append(tempo)
            tempo = []

      if update == True:
            data.clear()
            [data.append(n) for n in str_list]
      else: pass

   else:   # list_type == "mix_items"
      for n in data:
            str_list.append(str(n))

      if update == True:
            data.clear()
            [data.append(n) for n in str_list]

   return str_list    






msg = f'''
            Inputs                     Outputs                                       Cases
   list_1 = "hello"                    []                                              1
   list_1 = []                         []                                              2
   list_1 = [5]                        [[5]]                                           3
   list_1 = [[1]]                      [1]                                             4
   list_1 = [1,2,3,4,5,6]              [[1],[2],[3],[4],[5],[6]]                       5
   list_1 = [[1,2],[3,4],[5,6]]        [[1,3,5],[2,4,6]           ]                    6
   list_1 = [[1],[4],[5,6]]            [[1,4,5],[fill_value,fill_value,6]]
                                       [[1,4,5]] -> autofill = False
                                       [[1,4,5]] -> autofill = False, type=\'string\'
   list_1 = [10,[50],[250],["H"],100]  [[10],[[50]],[[250]],[["H"]],[100]]             7

   list_1 = [[1,2,3,4,5,6]]            [1, 2, 3, 4, 5, 6]                              8 
   list_1 = [1, 2, 3, 4, 5, 6]         [[1], [2], [3], [4], [5], [6]]
   list_1 = [[1],[2],[3],[4],[5],[6]]  [[1,2,3,4,5,6]]
   '''

print(f"{cp.ins_chr(n=80, unicode="-")}")
print(msg)


print(f"{cp.set_font(1,90,231)}  Case 1  {cp.reset_font()}")
lst = "hello";  print("Original:",lst)
result = num_to_str(data=lst, fill_value=None, update=False)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
lst = [];   print("Original:",lst)
result = pylo.num_to_str(data=lst)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
lst = [5];   print("Original:",lst)
result = pylo.num_to_str(data=lst)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
lst = [[1]];   print("Original:",lst)
result = pylo.num_to_str(data=lst)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 5  {cp.reset_font()}")
lst = [1,2,3,4,5,6];   print("Original:",lst)
result = pylo.num_to_str(data=lst)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 6  {cp.reset_font()}")
lst = [[1,2],[3,4],[5,6]];  print("Original:",lst)
result = pylo.num_to_str(data=lst)
print("Result  :",result)

lst = [[1],[4],[5,6]];  print("Original:",lst)
result = pylo.num_to_str(data=lst)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 7  {cp.reset_font()}")
lst = [10,[50],[250],["H"],100];  print("Original:",lst)
result = pylo.num_to_str(data=lst)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 8  {cp.reset_font()}")
lst = [[1,2,3,4,5,6]];  print("Original:",lst)
result = pylo.num_to_str(data=lst)
print("Result  :",result)

print(f"{cp.ins_chr(n=80, unicode="-")}")
lst = [1,2,3,4,5,6];  print("Original:",lst)
result = pylo.num_to_str(data=lst)
print("Result  :",result)

print(f"{cp.ins_chr(n=80, unicode="-")}")
lst = [[1],[2],[3],[4],[5],[6]];  print(f"Original: {lst}  {cp.set_font(1,1,231)} update = True {cp.reset_font()}")
result = num_to_str(data=lst, fill_value=None, update=True)
print("Result  :",result)
print("Original:",lst)