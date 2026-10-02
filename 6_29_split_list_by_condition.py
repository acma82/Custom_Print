import custom_print as cp
tbl = cp.FancyFormat()
pylo = cp.PyLO()



matrix = [["Id",    "Name",         "Status",    "Grade"], 
          [1,       "Student 1",    "pass",       95    ],
          [2,       "Student 2",    "fail",       50    ],
          [3,       "Student 3",    "Pass",       100   ],
          [4,       "Student 4",    "Pass",       70.1  ],
          [5,       "Student 5",    "Fail",       60    ]]

# matrix = [["Name"],["Javier"], ["Miguel"],["Miguelito"],[90]]
 # explain this that is the columns if the column is greater it does not cause error just add the col data in the false_condition_list
# matrix = [["Grade"],[9.7],[9.9],[9.5],[9.0]]
# matrix = [["Name","Javier", "Miguel","Miguelito",98]]
# print(matrix)
# new_matrix = pylo.transpose(matrix)
# print(new_matrix)
# matrix = pylo.transpose(new_matrix)
# print(matrix)
# matrix = []
true_condition_list,  false_condition_list = pylo.split_list_by_condition(data=matrix, col_idx=3, condition=70, sensitive_case=True,
                                                                operator=pylo.Operator.GREATER_THAN, start_row=1)

print("\n")

# nl = cp.NestedList()
# nl.print_nested_list(true_condition_list)
# print("\n")
# nl.print_nested_list(false_condition_list)


tbl.title_msg = "True Condition List"
tbl.print_fancy_format(true_condition_list)

tbl.title_msg = "False Conditon List"
tbl.print_fancy_format(false_condition_list)

tbl.title_msg = "Original List"
tbl.print_fancy_format(matrix)

# print("\n")
# print(true_condition_list)
# print("\n")
# print(false_condition_list)

# Explanation
# When the sensitive_case = False, the operator is working regarless if the condition is a string comparison or a numeric comparison.
# However, when the condition_sensitive_case = True, the operator condition is dead and the condition only works for string comparison
# applying the sensitive_case to the condition.
# Note: that this method only work for a list in the form of table or matrix. Also the first row is the header row and it is not compared.
# however if you change the start_row to 0, then the header does not exist any longer. all row are treating as data, by default it is set to 1.
# in other words if the start_row is set to a number different than 1, everythig will be used as data. only on start_row = 1 the first row
# is treatted as header. 

# data(list[row][col]) operator condition 
#            95           >        70       True_Condition_list           
#            80           >        70       True_Condition_list
#            100          >        70       True_Condition_list           
#            70           >        70       Fasle_Condition_list
#            60           >        70       False_Condition_list

#  Operator                      Meaning
#  EQUAL_TO                    = "=="
#  NOT_EQUAL_TO                = "!="
#  GREATER_THAN                = ">"
#  LESS_THAN                   = "<"
#  GREATER_THAN_OR_EQUAL_TO    = ">="
#  LESS_THAN_OR_EQUAL_TO       = "<="




    # #-------------------------------------------------------------------------------------------------------------------------------------------------
    # # split list by col condition                                                                                                                    -
    # #-------------------------------------------------------------------------------------------------------------------------------------------------
    # def split_list_by_condition(self, data:list=[["Empthy"]], col_idx:int=0, condition:int|str="Fail", sensitive_case=False, operator:str="=="):
    #     # headers = data.pop(0)
    #     list_true_condition  = [];       list_true_condition.append(data[0])
    #     list_false_condition = [];      list_false_condition.append(data[0])
    #     # data.insert(0, headers)
    #     type_of_list = get_list_type(data)
    #     print(operator)
        
    #     length = len(data)
    #     if type_of_list == "multiple_items_multiple_rows":
    #         # print("The list is not a table or a matrix style")
    #         if length <= 1:
    #             print("No enough Data in the list")
    #             list_true_condition = []; list_false_condition = []
    #         else:
    #             if col_idx < 0 or col_idx > (len(data[0])-1):
    #                 print("The col_idx is out of range")
    #             else:
    #                 # print("we can work now.")
    #                 for row in range(1, length):
    #                     if sensitive_case == False:
    #                         try: # String type
    #                             if data[row][col_idx].lower() == condition.lower():
    #                                 list_true_condition.append(data[row])
    #                             else:
    #                                 list_false_condition.append(data[row])
    #                         except: # Number type
    #                             if isinstance(data[row][col_idx], str):
    #                                 list_false_condition.append(data[row])
    #                             else:
    #                                 if operator == "==":
    #                                     if data[row][col_idx] == condition:
    #                                         list_true_condition.append(data[row])
    #                                     else:
    #                                         list_false_condition.append(data[row])

    #                                 elif operator == "<=":
    #                                     if data[row][col_idx] <= condition:
    #                                         list_true_condition.append(data[row])
    #                                     else:
    #                                         list_false_condition.append(data[row])

    #                                 elif operator == "<":
    #                                     if data[row][col_idx] < condition:
    #                                         list_true_condition.append(data[row])
    #                                     else:
    #                                         list_false_condition.append(data[row])

    #                                 elif operator == ">=":
    #                                     if data[row][col_idx] >= condition:
    #                                         list_true_condition.append(data[row])
    #                                     else:
    #                                         list_false_condition.append(data[row])

    #                                 elif operator == ">":
    #                                     if data[row][col_idx] > condition:
    #                                         list_true_condition.append(data[row])
    #                                     else:
    #                                         list_false_condition.append(data[row])

    #                                 elif operator == "!=":
    #                                     if data[row][col_idx] != condition:
    #                                         list_true_condition.append(data[row])
    #                                     else:
    #                                         list_false_condition.append(data[row])

    #                                 else:
    #                                     pass
    #                     else:
    #                         if data[row][col_idx] == condition:
    #                             list_true_condition.append(data[row])
    #                         else:
    #                             list_false_condition.append(data[row])


    #     else:
    #         pass

    #     if (len(list_true_condition)) == 1:
    #         list_true_condition = []

    #     if (len(list_false_condition)) == 1:
    #         list_false_condition = []

    #     return list_true_condition, list_false_condition