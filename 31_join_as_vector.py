import source.custom_print as cp
pylo = cp.PyLO()


list_1 = [[0,1],[2,3,4],5,[6,7,8]]
list_2 = [99,98,97]




print("List_1: ",list_1)
print("List_2: ",list_2)
print("\n")

for n in range(len(list_1)):
    join_list = pylo.join_as_vector(data=list_1, list_to_join=list_2, col_posi=n)
    print(f"Result:{n} {join_list}")


join_list = pylo.join_as_vector(data=list_1, list_to_join=list_2, col_posi=9)
print(f"Result:9 {join_list}")
