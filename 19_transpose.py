import source.source.custom_print as cp
pylo = cp.PyLO()

# cp.PyLO()
# cp.PyLO()
# cp.PyLo()

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
a = 6+2j
print(a)
lst1 = "hello"
lst2 = []
lst3 = [5]
lst4 = [[1]]
lst5 = [1,2,3,4,5,6]
lst61 = [[1,2],[3,4],[5,6]]
lst62 = [[1],[4],[5,6]]
lst7  = [10,[50],[250],["H"],100]
lst81 = [[1,2,3,4,5,6]]
lst82 = [1, 2, 3, 4, 5, 6]
lst83 = [[1],[2],[3],[4],[5],[6]]


print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")


print("original :", lst1)
trans_lst = pylo.transpose(data=lst1, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)


print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst2)
trans_lst = pylo.transpose(data=lst2, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst3)
trans_lst = pylo.transpose(data=lst3, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst4)
trans_lst = pylo.transpose(data=lst4, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst5)
trans_lst = pylo.transpose(data=lst5, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst61)
trans_lst = pylo.transpose(data=lst61, autofill=True, fill_value=15, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst62)
trans_lst = pylo.transpose(data=lst62, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst7)
trans_lst = pylo.transpose(data=lst7, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst81)
trans_lst = pylo.transpose(data=lst81, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst82)
trans_lst = pylo.transpose(data=lst82, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst83)
trans_lst = pylo.transpose(data=lst83, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)
