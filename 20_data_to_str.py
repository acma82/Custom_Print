
import source.source.custom_print as cp
pylo = cp.PyLO()

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
result = pylo.data_to_str(data=lst, update=False)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
lst = [];   print("Original:",lst)
result = pylo.data_to_str(data=lst)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
lst = [5];   print("Original:",lst)
result = pylo.data_to_str(data=lst)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
lst = [[1]];   print("Original:",lst)
result = pylo.data_to_str(data=lst)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 5  {cp.reset_font()}")
lst = [1,2,3,4,5,6];   print("Original:",lst)
result = pylo.data_to_str(data=lst)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 6  {cp.reset_font()}")
lst = [[1,2],[3,4],[5,6]];  print("Original:",lst)
result = pylo.data_to_str(data=lst)
print("Result  :",result)

lst = [[1],[4],[5,6]];  print("Original:",lst)
result = pylo.data_to_str(data=lst)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 7  {cp.reset_font()}")
lst = [10,[50],[250],["H"],100];  print("Original:",lst)
result = pylo.data_to_str(data=lst)
print("Result  :",result)


print(f"{cp.set_font(1,90,231)}  Case 8  {cp.reset_font()}")
lst = [[1,2,3,4,5,6]];  print("Original:",lst)
result = pylo.data_to_str(data=lst)
print("Result  :",result)

print(f"{cp.ins_chr(n=80, unicode="-")}")
lst = [1,2,3,4,5,6]
print(f"Original: {lst}  {cp.set_font(1,21,231)} update = False {cp.reset_font()}")
result = pylo.data_to_str(data=lst)
print("Result  :",result)
print("Original:", lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")
lst = [[1],[2],[3],[4],[5],[6]]
print(f"Original: {lst}  {cp.set_font(1,1,231)} update = True {cp.reset_font()}")
result = pylo.data_to_str(data=lst, update=True)
print("Result  :",result)
print("Original:",lst)