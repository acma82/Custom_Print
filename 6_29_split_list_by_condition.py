import custom_print as cp
tbl = cp.FancyFormat()
pylo = cp.PyLO()
tbl.title_bg = 90
tbl.title_fg = 231



matrix = [["Id",    "Name",         "Status",    "Grade"], 
          [1,       "Student 1",    "pass",       95    ],
          [2,       "Student 2",    "fail",       50    ],
          [3,       "Student 3",    "Pass",       100   ],
          [4,       "Student 4",    "Pass",       70.1  ],
          [5,       "Student 5",    "Fail",       60    ]]

# matrix = [["Name"],["Student 1"], ["Student 2"],["Professor"],[90]]
 # explain this that is the columns if the column is greater it does not cause error just add the col data in the false_condition_list
# matrix = [["Grade"],[9.7],[9.9],[9.5],[9.0]]
# matrix = [["Name","Javier", "Miguel","Miguelito",98]]
# matrix = ["Name","Javier", "Miguel","Miguelito",98]
# print(matrix)
# new_matrix = pylo.transpose(matrix)
# print(new_matrix)
# matrix = pylo.transpose(new_matrix)
# print(matrix)
# matrix = []
true_condition_list,  false_condition_list = pylo.split_list_by_condition(data=matrix, col_index=3, condition=70, sensitive_case=True,
                                                                operator=pylo.Operator.GREATER_THAN, start_row=1)

print("\n")

tbl.title_msg = " Original List, col_index=3, condition > 70 "
tbl.print_fancy_format(matrix)

tbl.title_msg = " True Condition List, Grade > 70 "
tbl.print_fancy_format(true_condition_list)

tbl.title_msg = " False Conditon List, Grade > 70 "
tbl.print_fancy_format(false_condition_list)

