import math
import numpy as np
# import custom_print as cp
import cp_designs as ds

#ds.print_msg1()

ds.rule_msg("Miguel Aguilar Cuesta Center!", "center", "-",  4)
ds.rule_msg("Miguel Aguilar Cuesta Left!!!", "left",   "@",  4)
ds.rule_msg("Miguel Aguilar Cuesta Right!!", "right",  "*",  4)
ds.rule_msg("Miguel Aguilar Cuesta Justify", "Justi",  "+",  4)


ds.rule_msg_box("Miguel Aguilar Cuesta Center!", "center", 4)
ds.rule_msg_box("Miguel Aguilar Cuesta Left!!!", "left",   4)
ds.rule_msg_box("Miguel Aguilar Cuesta Right!!", "right",  4)
ds.rule_msg_box("Miguel Aguilar Cuesta Justify", "Justi",  4)
#----------------------------------------------------------------------------------------------
def magnitude(vector):
    return math.sqrt(sum(pow(element,2) for element in vector))

# u = np.array([-3,7])
# v = np.array([-4, 2, 4])

# print(f"Magnitude U = {magnitude(u)}");        print(f"Magnitude V = {magnitude(v)}")
# print(f"Magnitude U = {np.linalg.norm(u)}");   print(f"Magnitude V = {np.linalg.norm(v)}")


# num = ["Numbers",1,2,3,74,5]
# ds.tbl1.print_fancy_format(num)
