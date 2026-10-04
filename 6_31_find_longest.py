import custom_print as cp

pylo = cp.PyLO()
nl   = cp.NestedList()
print()
# #         0               1                 2
l1 = [["Header 1",    "Header 2",  "I am the longest one"],
        ["Data 1",      "Data 2",    "Data 4"  ],
        ["Data 5",      "Data 6",    "Data 1"  ]]
nl.adj_left_space = 4
nl.adj_right_space = 4
nl.adj_middle_space = 4
nl.print_nested_list(l1)



print("\n")



result = pylo.find_longest_item(l1)
new_result = pylo.to_string_list(result)



# new_result = [["value","length", "row", "col"],
#               ["I am the longest one", "20", "0", "2"]]



# # nl.adj_middle_space = 0
# # nl.adj_left_space = 0
# nl.adj_right_space = 0
# new_result = pylo.to_string_list(result)
# nl.id_on = False

nl.print_nested_list(new_result)


# cp.ins_newline(2)

# l1 = [["Header 1",    "I am the longest one"],
        # ["Data 1",    "Data 4"  ],
        # ["Data 5",    "Data 1"  ]]
# nl.print_nested_list(l1)