import custom_print as cp
pylo = cp.PyLO()

list_0 = [["A"],["B"]]
result = pylo.make_to_vector(list_0)
print(result)

list_1 = [5,6,[1,2,3],[1,0,3]]
result = pylo.make_to_vector(list_1)
print(result)

list_2 = [[5,6,9],[1,2,3],[1,0,3]]
result = pylo.make_to_vector(list_2)
print(result)

list_2 = [[1,2],["Hello",99],[[3,[5],[95,3],[5]],3],3,[5,6,7,8]]
result = pylo.make_to_vector(list_2)
print(result)

list_2 = [10,"MiGueL", "HellO",7]
result = pylo.make_to_vector(list_2)
print(result)
