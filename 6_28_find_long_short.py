import custom_print as cp

pylo = cp.PyLO()
nl   = cp.NestedList()
print()
# #         0               1                 2
l1 = [["Header 1",    "Header 2",  "I am the longest one"],
        ["Data 1",      "Data 2",    "D"                 ],
        ["Data 5",      "Data 6",    "Data 1"            ]]
nl.print_nested_list(l1)



print("\n")

# l1 = [["Header 1",    "Header",  "I am the longest one"]]
# l1 = [["Header 1"],    ["Header"],  ["I am the longest one"]]

resultL = pylo.find_longest_item(l1)
resultS = pylo.find_shortest_item(l1)


nl.adj_middle_space = 2
nl.adj_left_space = 4
nl.adj_right_space = 4
# nl.id_on = False

nl.print_nested_list(resultL)
cp.ins_newline(3)
nl.print_nested_list(resultS)

