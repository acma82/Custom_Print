def print_hort_chr(start_chr,end_chr,x):
  print(start_chr,end="")
  for n in range(x):
      print(end_chr,end="")




print("SQUARE All Type")
print("\033[1;38;5;11m",end="")
print_hort_chr(u"\u25A0",u"\u25A0",15) # left top corner and horizontal top
print_hort_chr(u'\u25A0',u"\u25A0",9)  # T down and horizontal line
print_hort_chr(u'\u25A0',u"\u25A0",12) # T down and horizontal line
print_hort_chr(u'\u25A0',u"\u25A0",0)  # right top corner and horizontal top
print()
print(u'\u2588'+"  Terminology  "+u'\u25A2'+"  Hello  "+u'\u25A3'+"  Good Bye  "+u'\u25A4') # vertical line

print_hort_chr(u'\u25A5',u'\u25A5',15) # left middle line
print_hort_chr(u'\u25A5',u'\u25A5',9)  # middle middle line
print_hort_chr(u'\u25A5',u'\u25A5',12) # middle middle line
print_hort_chr(u'\u25A5',u'\u25A5',0)  # right middle line
print()

print(u'\u2588'+"  Terminology  "+u'\u25A7'+"  Hello  "+u'\u25A8'+"  Good Bye  "+u'\u25A9') # vertical line
print_hort_chr(u"\u25AA",u"\u25A1",15) # left bottom corner and horizontal line
print_hort_chr(u'\u25AA',u"\u25A6",9)  # T up and horizontal line
print_hort_chr(u'\u25AA',u"\u25AB",12) # T up and horizontal line
print_hort_chr(u'\u25AA',u"\u25AB",0)  # right bottom corner and horizontal line
print("\n")
print("\033[0m",end="")





print("RECTANGLE")
#print("\033[1;38;5;11m",end="")
print_hort_chr(u"\u2587",u"\u2587",15) # left top corner and horizontal top
print_hort_chr(u'\u2587',u"\u2587",9)  # T down and horizontal line
print_hort_chr(u'\u2587',u"\u2587",12) # T down and horizontal line
print_hort_chr(u'\u2587',u"\u2587",0)  # right top corner and horizontal top
print()
print(u'\u2588'+"  Terminology  "+u'\u2588'+"  Hello  "+u'\u2588'+"  Good Bye  "+u'\u2588') # vertical line

print_hort_chr(u'\u2588',u'\u2587',15) # left middle line
print_hort_chr(u'\u2588',u'\u2587',9)  # middle middle line
print_hort_chr(u'\u2588',u'\u2587',12) # middle middle line
print_hort_chr(u'\u2588',u'\u2587',0)  # right middle line
print()

print(u'\u2588'+"  Terminology  "+u'\u2588'+"  Hello  "+u'\u2588'+"  Good Bye  "+u'\u2588') # vertical line
print_hort_chr(u"\u2588",u"\u2587",15) # left bottom corner and horizontal line
print_hort_chr(u'\u2588',u"\u2587",9)  # T up and horizontal line
print_hort_chr(u'\u2588',u"\u2587",12) # T up and horizontal line
print_hort_chr(u'\u2588',u"\u2587",0)  # right bottom corner and horizontal line
print("\n")




print("CIRCLE All Type")
print_hort_chr(u"\u25C9",u"\u25CB",15) # left top corner and horizontal top
print_hort_chr(u'\u25C9',u"\u25CB",9)  # T down and horizontal line
print_hort_chr(u'\u25C9',u"\u25CB",12) # T down and horizontal line
print_hort_chr(u'\u25C9',u"\u25CB",0)  # right top corner and horizontal top
print()
print(u'\u25CC'+"  Terminology  "+u'\u25CD'+"  Hello  "+u'\u25CE'+"  Good Bye  "+u'\u25CF') # vertical line

print_hort_chr(u'\u25D0',u'\u25D1',15) # left middle line
print_hort_chr(u'\u25D0',u'\u25D1',9)  # middle middle line
print_hort_chr(u'\u25D0',u'\u25D1',12) # middle middle line
print_hort_chr(u'\u25D0',u'\u25D1',0)  # right middle line
print()

print(u'\u25D2'+"  Terminology  "+u'\u25D3'+"  Hello  "+u'\u25C6'+"  Good Bye  "+u'\u25C7') # vertical line
print_hort_chr(u"\u2587",u"\u2587",15) # left bottom corner and horizontal line
print_hort_chr(u'\u2587',u"\u2587",9)  # T up and horizontal line
print_hort_chr(u'\u2587',u"\u2587",12) # T up and horizontal line
print_hort_chr(u'\u2587',u"\u2587",0)  # right bottom corner and horizontal line
print("\n")