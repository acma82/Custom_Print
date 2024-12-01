import custom_print as cp
msg = cp.FancyFormat()

pylo = cp.PyList()

msg = f'''
   Options                             Results                           Cases
   list_1 = "hello"                    incorrect_variable_type             1
   list_1 = []                         empty_list                          2
   list_1 = [5]                        one_item_no_row                     3
   list_1 = [[1]]                      one_item_one_row                    4
   list_1 = [1,2,3,4,5,6]              multiple_items_no_row               5
   list_1 = [[1,2],[3,4],[5,6]]        multiple_items_multiple_rows        6
   list_1 = [[1],[4],[5,6,7]]
   list_1 = [10,[50],[250],["H"],100]  mix_items                           7
   list_1 = [[1,2,3,4,5,6]]            multiple_items_one_row              8 
   '''
print(msg)

print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = "Hello"
lst_dimension = pylo.dimensions(data=list_1, length_col=pylo.Length_Col.MAX)
print(f"Case 1 \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = []
lst_dimension = pylo.dimensions(data=list_1, length_col=pylo.Length_Col.MAX)
print(f"Case 2 \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = [5]
lst_dimension = pylo.dimensions(data=list_1, length_col=pylo.Length_Col.MAX)
print(f"Case 3 \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = [[1]]
lst_dimension = pylo.dimensions(data=list_1, length_col=pylo.Length_Col.MAX)
print(f"Case 4 \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = [1,2,3,4,5,6]
lst_dimension = pylo.dimensions(data=list_1, length_col=pylo.Length_Col.MAX)
print(f"Case 5 \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = [[1,2],[3,4],[5,6,7]]
lst_dimension = pylo.dimensions(data=list_1, length_col=pylo.Length_Col.MAX)
print(f"Case 6 Max \u279C {lst_dimension}")


list_1 = [[1],[4],[5,6,7]]
lst_dimension = pylo.dimensions(data=list_1, length_col=pylo.Length_Col.MIN)
print(f"Case 6 Min \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = [10,[50],[250],["H"],100]
lst_dimension = pylo.dimensions(data=list_1, length_col=pylo.Length_Col.MAX)
print(f"Case 7 \u279C {lst_dimension}")

print(f"{cp.ins_chr(n=80, unicode="-")}")

print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = [[1,2,3,4,5,6]]
lst_dimension = pylo.dimensions(data=list_1, length_col=pylo.Length_Col.MAX)
print(f"Case 8 \u279C {lst_dimension}")
