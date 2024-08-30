
print("# double lines")
print(u"\u2554"+u"\u2550"+u"\u2550"+u"\u2550"+u"\u2550"+u"\u2557")
print(u'\u2551'+"\033[1;38;5;99m HI \033[0m"+u'\u2551')
print(u"\u255a"+u"\u2550"+u"\u2550"+u"\u2550"+u"\u2550"+u"\u255d")

print(u"\u2551"+"  "+u"\u2551")
print(u"\u2551"+"  "+u"\u2551")

print("# single lines")
print(u"\u250c"+u"\u2500"+u"\u2500"+u"\u2510")
print(u"\u2502"+"  "+u"\u2502")
print(u"\u2514"+u"\u2500"+u"\u2500"+u"\u2518")

print("+---------------+---------+------------+")
print("|  Terminology  |  Hello  |  Good Bye  |")
print("+---------------+---------+------------+")
print("|  Terminology  |  Hello  |  Good Bye  |")
print("+---------------+---------+------------+")
print("\n")
print("+--------------------------------------+")
print("|  Terminology  |  Hello  |  Good Bye  |")
print("|--------------------------------------|")
print("|  Terminology  |  Hello  |  Good Bye  |")
print("+--------------------------------------+")


def print_hort_chr(start_chr,end_chr,x):
  print(start_chr,end="")
  for n in range(x):
      print(end_chr,end="")
  
print("\n")
print_hort_chr(u"\u250c",u"\u2500",15) # top open corner and line
print_hort_chr(u'\u252C',u"\u2500",9)  # T down and line
print_hort_chr(u'\u252C',u"\u2500",12) # T down and line
print_hort_chr(u'\u2510',u"\u2500",0)  # top close corner and line
print()
print(u'\u2502'+"  Terminology  "+u'\u2502'+"  Hello  "+u'\u2502'+"  Good Bye  "+u'\u2502') # vertical line
print_hort_chr(u"\u2514",u"\u2500",15) # bottom open corner and line
print_hort_chr(u'\u2534',u"\u2500",9)  # T up and line
print_hort_chr(u'\u2534',u"\u2500",12) # T up and line
print_hort_chr(u'\u2518',u"\u2500",0)  # bottom close corner and line
print()
print('+', '+', '+', '+', '+', '+', '+', '+', '+', '-', '|')
print(u'\u250c',u'\u252C',u'\u2510',u'\u251C',u'\u253C',u'\u2524',u'\u2514',u'\u2534',u'\u2518',u'\u2500',u'\u2502')
print()
print(u'\u2554',u'\u2566',u'\u2557',u'\u2560',u'\u256C',u'\u2563',u'\u255a',u'\u2569',u'\u255d',u'\u2550',u'\u2551')
print()
print("\033[1m")
print('+', '+', '+', '+', '+', '+', '+', '+', '+', '-', '|')
print(u'\u250c',u'\u252C',u'\u2510',u'\u251C',u'\u253C',u'\u2524',u'\u2514',u'\u2534',u'\u2518',u'\u2500',u'\u2502')
print()
print(u'\u2554',u'\u2566',u'\u2557',u'\u2560',u'\u256C',u'\u2563',u'\u255a',u'\u2569',u'\u255d',u'\u2550',u'\u2551')
print("\033[0m")
print("\n")


print_hort_chr(u"\u250c",u"\u2500",15) # top open corner and line
print_hort_chr(u'\u252C',u"\u2500",9)  # T down and line
print_hort_chr(u'\u252C',u"\u2500",12) # T down and line
print_hort_chr(u'\u2510',u"\u2500",0)  # top close corner and line
print()
print(u'\u2502'+"  Terminology  "+u'\u2502'+"  Hello  "+u'\u2502'+"  Good Bye  "+u'\u2502') # vertical line
print_hort_chr(u'\u251C',u"\u2500",15)
print_hort_chr(u'\u253C',u"\u2500",9)
print_hort_chr(u'\u253C',u"\u2500",12)
print_hort_chr(u'\u2524',u"\u2500",0)
print()
print(u'\u2502'+"  Terminology  "+u'\u2502'+"  Hello  "+u'\u2502'+"  Good Bye  "+u'\u2502') # vertical line
print_hort_chr(u"\u2514",u"\u2500",15) # bottom open corner and line
print_hort_chr(u'\u2534',u"\u2500",9)  # T up and line
print_hort_chr(u'\u2534',u"\u2500",12) # T up and line
print_hort_chr(u'\u2518',u"\u2500",0)  # bottom close corner and line
print()


print_hort_chr(u"\u250c",u"\u2500",15) # top open corner and line
print_hort_chr(u'\u252C',u"\u2500",9)  # T down and line
print_hort_chr(u'\u252C',u"\u2500",12) # T down and line
print_hort_chr(u'\u2510',u"\u2500",0)  # top close corner and line
print()
print(u'\u2502'+"  Terminology  "+u'\u2502'+"  Hello  "+u'\u2502'+"  Good Bye  "+u'\u2502') # vertical line

print(u'\u2502'+"  Terminology  "+u'\u2502'+"  Hello  "+u'\u2502'+"  Good Bye  "+u'\u2502') # vertical line
print_hort_chr(u"\u2514",u"\u2500",15) # bottom open corner and line
print_hort_chr(u'\u2534',u"\u2500",9)  # T up and line
print_hort_chr(u'\u2534',u"\u2500",12) # T up and line
print_hort_chr(u'\u2518',u"\u2500",0)  # bottom close corner and line

print()