import custom_print as cp
pylo = cp.PyLO()

lst = [[9,8,7],[4],[5,6]]

print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")

print("Original:",lst)
result = pylo.autofill_data(lst)
print("Using default values")
print("Result  :",result)
print("Original:",lst)


print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")


print("Original:",lst)
result = pylo.autofill_data(lst, fill_value=9.8, update=False)
print("mylist=lst, fill_value=9.8, update=False")
print("Result  :",result)
print("Original:",lst)


print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")


print("Original:",lst)
result = pylo.autofill_data(data=lst, fill_value=99, update=True)
print("mylist=lst, fill_value=99, type= \"string\", update=True")
print("Result  :",result)
print("Original:",lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")

lst=[[1,2],[3,4],[5,6]]
print("Original:",lst)
result = pylo.autofill_data(data=lst, fill_value=99, update=True)
print("mylist=lst, fill_value=99, type= \"string\", update=True")
print("Result  :",result)
print("Original:",lst)
