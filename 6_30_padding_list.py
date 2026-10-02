import custom_print as cp
pylo = cp.PyLO()

# lst = [["1454545454"],["Migue"], ["acma"], ["Miguelito"]]       # multiple_items_multiple_rows  -> works
# lst = [["Migue","44545454", "acma", "Miguelito"]]         # multiple_items_one_row  -> works

# lst = [["Python",  "th",  "on"],       # 0.  Letters
#         [True,  True,  True ],         # 1.  Bold
#         [152,   115,   202  ],         # 2.  bg
#         [16,    177,    23  ],         # 3.  Fg
#         [22,     33,    10  ],         # 11. left_space
#         [21,     33,    11  ],         # 12. middle_space
#         [24,     33,     1  ]]         # 13. right_space

lst = ["acma2",4787878,"Migue", "acma", "Miguelito"]         # multiple_items_no_row   ->  works

# resultl = pylo.find_longest_item(lst)
# # resultl = pylo.find_shortest_item(lst)
# print(resultl)                         

# # print(cp.get_list_type(lst))


padding_list = pylo.padding_list(data=lst, align="j", padding_size=1, left_pad=4, right_pad=1)
print(padding_list)


# explanation.
# this method padd a list. the align is specified and the size of the padding is taking 
# from the padding_size parameter. If the padding_size parameter is shorter than the
# longest element in the list then it will be take the longest len of the list as
# the padding_size. 
# for the left_pad and right_pad are used only when the align is set to "j" or "justify"
# otherwise it is ignored.
# The justify alignment will pad the list as left using the reference of padding_size or 
# the longest item in the list and then it will add the spaces specify
# for the left_pad and the right_pad

# mylist = pylo.to_string_list(lst)
# longest = pylo.find_longest_item(mylist)
# print(longest[1][1])

# # A matrix with unaligned text 
# matrix = [ ["apple", "to"], ["banana", "strawberry"] ]
# # Pad each string to a width of 10 spaces on the right 
# padded_matrix = [[cell.ljust(longest[1][1]) for cell in row] for row in mylist]
# # Print the result cleanly 
# print(padded_matrix)
# # for row in padded_matrix: print(row)