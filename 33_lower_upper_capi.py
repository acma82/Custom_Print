import source.source.custom_print as cp
pylo = cp.PyLO()


list_1 = [["HeadeR 1", "HeadeR 2", "HeadeR 3",0],
          ["DatitO 1", "DatitO 2", "DatitO 3",1],
          ["DatitO 4", "DatitO 5", "DatitO 6",0],
          ["DatitO 1", "DatitO 2", "DatitO 1",3]]

list_2 = ["miGUEL", "heLLO",[7,8,"bBBB"]]


mylower = pylo.lower_case(list_1)
print(mylower)

myupper = pylo.upper_case(list_1)
print(myupper)

mycapitalize = pylo.capitalize_case(list_1)
print(mycapitalize)

mycapitalize = pylo.capitalize_case(list_2)
print(mycapitalize)

