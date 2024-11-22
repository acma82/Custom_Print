import custom_print as cp
print()
#-------------------------------------------------------------------------
print(f"{cp.set_font(1,22,231)}  Bool to List  {cp.reset_font()}")
print(f"{cp.set_font(1,-1,99)}Bool:{cp.reset_font()}")
b = False
print(b)
print(f"{cp.set_font(1,-1,11)}List:{cp.reset_font()}")
l = cp.bool2list(b)
print(l)
print("-----------------------------------------------------------------------------------")
print()


#-------------------------------------------------------------------------
print(f"{cp.set_font(1,22,231)}  Integer to List  {cp.reset_font()}")
print(f"{cp.set_font(1,-1,99)}Integer:{cp.reset_font()}")
i = 12; print(i)
print(f"{cp.set_font(1,-1,11)}List:{cp.reset_font()}")
l = cp.int2list(i)
print(l)
print("-----------------------------------------------------------------------------------")
print()


#-------------------------------------------------------------------------
print(f"{cp.set_font(1,22,231)}  Float to List  {cp.reset_font()}")
print(f"{cp.set_font(1,-1,99)}Float:{cp.reset_font()}")
f = 3.2; print(f)
print(f"{cp.set_font(1,-1,11)}List:{cp.reset_font()}")
l = cp.float2list(f)
print(l)
print("-----------------------------------------------------------------------------------")
print()


#-------------------------------------------------------------------------
print(f"{cp.set_font(1,22,231)}  Complex to List  {cp.reset_font()}")
print(f"{cp.set_font(1,-1,99)}Complex:{cp.reset_font()}")
c = 5+6j; print(c)
print(f"{cp.set_font(1,-1,11)}List:{cp.reset_font()}")
l = cp.complex2list(c)
print(l)
print("-----------------------------------------------------------------------------------")
print()


#-------------------------------------------------------------------------
print(f"{cp.set_font(1,22,231)}  String to List  {cp.reset_font()}")
print(f"{cp.set_font(1,-1,99)}String:{cp.reset_font()}")
s = "Hello there!"; print(s)
print(f"{cp.set_font(1,-1,11)}List:{cp.reset_font()}")
l = cp.str2list(s)
print(l)
print("-----------------------------------------------------------------------------------")
print()


print()
print(f"{cp.set_font(1,22,231)}  Dictionary to List  {cp.reset_font()}")
print(f"{cp.set_font(1,-1,99)}Dictionary:{cp.reset_font()}")
dict_tags = {"name":"miguel", "last1":"aguilar", "last2":"cuesta"}
print(dict_tags)
print(f"{cp.set_font(True,-1,22)}List:{cp.reset_font()}")

list_tags = cp.dict2list(dict_tags, "My Key Title", "My Value Title")
print(list_tags)
print("-----------------------------------------------------------------------------------")
print()


#-------------------------------------------------------------------------
print(f"{cp.set_font(1,22,231)}  Set to List  {cp.reset_font()}")
print(f"{cp.set_font(True,-1,99)}Set:{cp.reset_font()}")
set_tags = {1,3,5,7,9}
print(set_tags)
print(f"{cp.set_font(1,-1,11)}List:{cp.reset_font()}")

list_tags = cp.set2list(set_tags, "My Set Title")
print(list_tags)
print("-----------------------------------------------------------------------------------")
print()


#-------------------------------------------------------------------------
print(f"{cp.set_font(1,22,231)}  Frozenset to List  {cp.reset_font()}")
print(f"{cp.set_font(True,-1,99)}FrozenSet_Tuple:{cp.reset_font()}")

vowelsT = ("a", "e", "i", "o", "u"); frozenset_Tuple = frozenset(vowelsT); print(frozenset_Tuple)

print(f"{cp.set_font(True,-1,22)}List:{cp.reset_font()}")
list_frozenset_T = cp.set2list(frozenset_Tuple); print(list_frozenset_T)

vowelsL = ["a", "e", "i", "o", "u"]
frozenset_List = frozenset(vowelsL)
print(f"{cp.set_font(True,-1,99)}FrozenSet_List:{cp.reset_font()}")
print(frozenset_List)

print(f"{cp.set_font(True,-1,1)}List:{cp.reset_font()}")
list_frozenset_L = cp.set2list(frozenset_List,"My Frozenset Title","horizontal")
print(list_frozenset_L)
print("-----------------------------------------------------------------------------------")
print()



#-------------------------------------------------------------------------
print(f"{cp.set_font(1,22,231)}  Range to List  {cp.reset_font()}")
print(f"{cp.set_font(1,-1,99)}Range:{cp.reset_font()}")
r = range(0,15,3)
print(r)
print(f"{cp.set_font(1,-1,11)}List:{cp.reset_font()}")
l = cp.range2list(r,"none","horizontal")
print(l)
l = cp.range2list(r,"Range Title","vertical")
print(l)
print("-----------------------------------------------------------------------------------")


#-------------------------------------------------------------------------
print(f"{cp.set_font(1,22,231)}  Tuple to List  {cp.reset_font()}")
print(f"{cp.set_font(1,-1,99)}Tutle Case 1:{cp.reset_font()}")
tupleData1 = (("Apple"));    print(tupleData1)       # this is a string                     Case 0
tupleData2 = ("",);          print(tupleData2)       # this is a tuple                      Case 1
tupleData3 = ("Apple",);     print(tupleData3)       # this is a simple tuple               Case 2
tupleData4 = (("Apple",));   print(tupleData4)       # this is a tuple inside tuple         Case 3

tupleData5 = (("hello",),("hell",),("hi",),([1,2],)) # this is a simple tuple w/ tuples     Case 4
tupleData6 = (("hello","hello"),("hell",),("hi","bye","good"),([1,2],)) #                   Case 4
print(tupleData5); print(tupleData6)

tupleData7 = ("hello","hell","hi",[1,2])             # this is a simple tuple w/ string     Case 5
tupleData8 = (("hello"),("hell"),("hi"),([1,2]))     # this is a simple tuples w/ string    Case 5
print(tupleData7); print(tupleData8)

# this is a tuple w/ combination other type of variables Case 6
tupleData9 = (("hello","hello"),("hell",),("hi","bye","good"),[1,2], "hello")
print(tupleData9)


print(f"{cp.set_font(1,-1,11)}List:{cp.reset_font()}")
listData1 = cp.tuple2list(tupleData1);   print(listData1)
listData2 = cp.tuple2list(tupleData2);   print(listData2)
listData3 = cp.tuple2list(tupleData3);   print(listData3)
listData4 = cp.tuple2list(tupleData4);   print(listData4)
listData5 = cp.tuple2list(tupleData5);   print(listData5)
listData6 = cp.tuple2list(tupleData6);   print(listData6)
listData7 = cp.tuple2list(tupleData7);   print(listData7)
listData8 = cp.tuple2list(tupleData8);   print(listData8)
listData9 = cp.tuple2list(tupleData9);   print(listData9)

print("-----------------------------------------------------------------------------------")
print()
t1 = (("hello","hell","hi"),)

print(t1);   print(len(t1));   print(t1[0])

l1 = cp.tuple2list(t1);   print(len(l1));   print(l1);   print(l1[0])
print()
