import fancyprint as fp
fun = fp.FancyFormat()

import enum

set11 = {1,2,3,4,5}
print(set11)

newlist = fp.set2list(set11,'hola',fp.Layout.HORIZONTAL)
print(newlist)


# new = fp.set2list(set11, "none", layout="HORIZONTAL")
# print(new)

x = range(0,16,2); l = fp.range2list(x,"hello",fp.Layout.HORIZONTAL)
print(l)

# lista = 4.5+8.3j
# print(type(lista))
# fun.print_fancy_data(lista)
# fun.update_list = True

# #lista = [["uno","dos"],["hello"]]
# lista = [[1]]
# print(lista)
# fun.print_fancy_list(lista)
# print(lista)
# tags_status_dict = {"name":["miguel","dos"], "last1":"aguilar", "last2":"cuesta"}
# fun.print_fancy_data(tags_status_dict)

# tags_status_dict = {"name":"miguel"}
# fun.print_fancy_data(tags_status_dict)

# fd.moveTo(4, 30)
# print("hello again")
# fd.ins_newline(8)

# tupleData = ("",)          # this is a tuple     Case 1
# tupleData = (("Apple"))  # this is a string
# tupleData = ("Apple",)   # this is a tuple     Case 1
# tupleData = (("Apple",)) # this is a tuple     Case 2

#tupleData1 = (("hello",),("hell",),("hi",))
# tupleData1 = ("hello","hell","hi",[1,2])
# print(type(tupleData1))
# print(type(tupleData1[0]))
# print(len(tupleData1))
# print(len(tupleData1[0]), end="   "); print(tupleData1[0])
# #print(len(tupleData1[0]), end="   "); print(tupleData1[0][0])
# for n in tupleData1:
#    print(n, end="    ")

# print()
# print("------------------------------------------------------------")
# print()

# tupleData2 = (("hello","hello"),("hell",),("hi","bye","good"),([1,2],))
# for col in tupleData2:
#    for i in col:
#       print(i, end="   ")

# print()
# print("------------------------------------------------------------")
# print()


# print(type(tupleData2))
# print(type(tupleData2[0]))
# print(len(tupleData2))
# print(len(tupleData2[0]),end="   "); print(tupleData2[0][0])

# print()
# print("------------------------------------------------------------")
# print()

# tupleData3 = (("hello","hello"),("hell",),("hi","bye","good"),[1,2], "hello")
# for col in tupleData3:
#    for i in col:
#       print(i, end="   ")

# # print(type(tupleData))
# fun.print_fancy_format(tupleData1)
# fun.print_fancy_format(tupleData2)
# fun.print_fancy_format(tupleData3)

# lista = (("apple","manzana"),("miguel","name"),("bye","adios")) # this is a tuple
# #lista =("apple",)
# fun.print_fancy_list(lista)

# type_type = ["tuple","tuple","tuple","other","other"]
# tempo_list = []
# lengths = [2,1,3,1,1]
# l = len(tupleData3)

# for n in range(l):
#    if (lengths[n]) > 1:
#       tempo = []

#       for i in range(lengths[n]):
#          tempo.append(tupleData3[n][i])
#       tempo_list.append(tempo)

#    else:
#       if (type_type[n] == "other"):
#          tempo_list.append([tupleData3[n]])
#       else:
#          tempo_list.append([tupleData3[n][0]])

# print(tempo_list)


# #lista = [['hello', 'hello'], ['hell'], ['hi', 'bye', 'good'], [[1, 2]], ['hello']]
# fun.print_fancy_format(tupleData3)



print(f"{fp.set_font(bold=True, bg=-1, fg=22)} hello {fp.reset_font()}")
print(f"{fp.set_font(bold=False, bg=-1, fg=22)} hello {fp.reset_font()}")