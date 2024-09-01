def insp(n_space=0):
   space = ""
   while n_space > 0:
     space +=" "
     n_space -= 1
   return space

def print_hort_chr(start_chr,end_chr,x):
   print(start_chr,end="")
   for n in range(x):
      print(end_chr,end="")


print()
#----------------------------------------------------------------------------------------------------------------------------------------------------
print("\033[1;48;5;231;38;5;21m  DASH_LINE  \033[0m")
print("+---------------+---------+------------+")
print("|  Terminology  |  Hello  |  Good Bye  |")
print("+---------------+---------+------------+")
print("|  Terminology  |  Hello  |  Good Bye  |")
print("+---------------+---------+------------+")
print("\n")


#----------------------------------------------------------------------------------------------------------------------------------------------------
print(insp(4) + "\u25A3 Double Line and Single Line Square...! ")
print(insp(10) + u"\u2554"+u"\u2550"+u"\u2550"+u"\u2550"+u"\u2550"+u"\u2557"+ insp(12) + "\u250c\u2500\u2500\u2500\u2500\u2510")
print(insp(10) + u'\u2551'+"\033[1;38;5;99m HI \033[0m"+u'\u2551' +           insp(12) + "\u2502 AC \u2502" )
print(insp(10) + u"\u255a"+u"\u2550"+u"\u2550"+u"\u2550"+u"\u2550"+u"\u255d"+ insp(12) + "\u2514\u2500\u2500\u2500\u2500\u2518")


#----------------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
print("\033[1;48;5;231;38;5;21m  SINGLE_LINE  \033[0m")
print_hort_chr(u"\u250c",u"\u2500",15) # left top corner and horizontal line
print_hort_chr(u'\u252C',u"\u2500",9)  # T down and horizontal line
print_hort_chr(u'\u252C',u"\u2500",12) # T down and horizontal line
print_hort_chr(u'\u2510',u"\u2500",0)  # right top corner and horizontal line
print()
print(u'\u2502'+"  Terminology  "+u'\u2502'+"  Hello  "+u'\u2502'+"  Good Bye  "+u'\u2502') # vertical line

print_hort_chr(u'\u251C',u'\u2500',15) # left middle line
print_hort_chr(u'\u253C',u'\u2500',9)  # middle middle line
print_hort_chr(u'\u253C',u'\u2500',12) # middle middle line
print_hort_chr(u'\u2524',u'\u2500',0)  # right middle line
print()

print(u'\u2502'+"  Terminology  "+u'\u2502'+"  Hello  "+u'\u2502'+"  Good Bye  "+u'\u2502') # vertical line
print_hort_chr(u"\u2514",u"\u2500",15) # left bottom corner and horizontal line
print_hort_chr(u'\u2534',u"\u2500",9)  # T up and horizontal line
print_hort_chr(u'\u2534',u"\u2500",12) # T up and horizontal line
print_hort_chr(u'\u2518',u"\u2500",0)  # right bottom corner and horizontal line


#----------------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
print("\033[1;48;5;231;38;5;21m  DOUBLE_LINE  \033[0m")
print_hort_chr(u"\u2554",u"\u2550",15) # left top corner and horizontal top
print_hort_chr(u'\u2566',u"\u2550",9)  # T down and horizontal line
print_hort_chr(u'\u2566',u"\u2550",12) # T down and horizontal line
print_hort_chr(u'\u2557',u"\u2550",0)  # right top corner and horizontal top
print()
print(u'\u2551'+"  Terminology  "+u'\u2551'+"  Hello  "+u'\u2551'+"  Good Bye  "+u'\u2551') # vertical line

print_hort_chr(u'\u2560',u'\u2550',15) # left middle line
print_hort_chr(u'\u256C',u'\u2550',9)  # middle middle line
print_hort_chr(u'\u256C',u'\u2550',12) # middle middle line
print_hort_chr(u'\u2563',u'\u2550',0)  # right middle line
print()

print(u'\u2551'+"  Terminology  "+u'\u2551'+"  Hello  "+u'\u2551'+"  Good Bye  "+u'\u2551') # vertical line
print_hort_chr(u"\u255A",u"\u2550",15) # left bottom corner and horizontal line
print_hort_chr(u'\u2569',u"\u2550",9)  # T up and horizontal line
print_hort_chr(u'\u2569',u"\u2550",12) # T up and horizontal line
print_hort_chr(u'\u255D',u"\u2550",0)  # right bottom corner and horizontal line


#----------------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
print("\033[1m")
print('+', '+', '+', '+', '+', '+', '+', '+', '+', '-', '|')
print()
print(u'\u250c',u'\u252C',u'\u2510',u'\u251C',u'\u253C',u'\u2524',u'\u2514',u'\u2534',u'\u2518',u'\u2500',u'\u2502')
print()
print(u'\u2554',u'\u2566',u'\u2557',u'\u2560',u'\u256C',u'\u2563',u'\u255a',u'\u2569',u'\u255d',u'\u2550',u'\u2551')
print("\033[0m")


#----------------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
print("\033[1;48;5;22;38;5;231m")
print(f"Symbol Description  \u2192   Normal    Heavy            Type_Line  \033[0m")
print(f"Left  Top Corner    \u2192    \u250C   {insp(4)}  \u250F  {insp(10)} Single Line \u21B5")
print(f"Middle Down Corner  \u2192    \u252C   {insp(4)}  \u2533  {insp(10)} Single Line \u21B5")
print(f"Right Top Corner    \u2192    \u2510   {insp(4)}  \u2513  {insp(10)} Single Line \u21B5")
print()
print(f"Middle Left Corner  \u2192    \u251C   {insp(4)}  \u2523  {insp(10)} Single Line \u21B5")
print(f"Middle Middle Corner\u2192      \u253C {insp(4)}    \u254B{insp(10)} Single Line \u21B5")
print(f"Middle Right Corner \u2192    \u2524   {insp(4)}  \u252B  {insp(10)} Single Line \u21B5")
print()
print(f"Left Bottom Corner  \u2192    \u2514   {insp(4)}  \u2517  {insp(10)} Single Line \u21B5")
print(f"Middle Up Corner    \u2192    \u2534   {insp(4)}  \u253B  {insp(10)} Single Line \u21B5")
print(f"Right Bottom Corner \u2192    \u2518   {insp(4)}  \u251B  {insp(10)} Single Line \u21B5")
print()
print(f"Horizontal Line     \u2192    \u2500   {insp(4)}  \u2501  {insp(10)} Single Line \u21B5")
print(f"Vertical Line       \u2192    \u2502   {insp(4)}  \u2503  {insp(10)} Single Line \u21B5")


#----------------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
print("\033[1;48;5;22;38;5;231m")
print( "Description         \u2192  Symbol_Unicode            Type_Line  \033[0m")
print(f"Left  Top Corner    \u2192     \u2554    {insp(10)} Double Line \u21B5")
print(f"Middle Down Corner  \u2192        \u2566 {insp(10)} Double Line \u21B5")
print(f"Right Top Corner    \u2192     \u2557    {insp(10)} Double Line \u21B5")
print(f"Middle Left Corner  \u2192        \u2560 {insp(10)} Double Line \u21B5")
print(f"Middle Middle Corner\u2192     \u256C    {insp(10)} Double Line \u21B5")
print(f"Middle Right Corner \u2192       \u2563  {insp(10)} Double Line \u21B5")
print(f"Left Bottom Corner  \u2192     \u255A    {insp(10)} Double Line \u21B5")
print(f"Middle Up Corner    \u2192        \u2569 {insp(10)} Double Line \u21B5")
print(f"Right Bottom Corner \u2192     \u255D    {insp(10)} Double Line \u21B5")
print(f"Horizontal Line     \u2192        \u2550 {insp(10)} Double Line \u21B5")
print(f"Vertical Line       \u2192     \u2551    {insp(10)} Double Line \u21B5")



#----------------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
print("\033[1;48;5;231;38;5;21m  RECTANGLE_LINE  \033[0m")
print_hort_chr(u"\u2586",u"\u2586",15) # left top corner and horizontal top
print_hort_chr(u'\u2586',u"\u2586",9)  # T down and horizontal line
print_hort_chr(u'\u2586',u"\u2586",12) # T down and horizontal line
print_hort_chr(u'\u2586',u"\u2586",0)  # right top corner and horizontal top
print()
print(u'\u2588'+"  Terminology  "+u'\u2588'+"  Hello  "+u'\u2588'+"  Good Bye  "+u'\u2588') # vertical line

print_hort_chr(u'\u2588',u'\u2586',15) # left middle line
print_hort_chr(u'\u2588',u'\u2586',9)  # middle middle line
print_hort_chr(u'\u2588',u'\u2586',12) # middle middle line
print_hort_chr(u'\u2588',u'\u2586',0)  # right middle line
print()

print(u'\u2588'+"  Terminology  "+u'\u2588'+"  Hello  "+u'\u2588'+"  Good Bye  "+u'\u2588') # vertical line
print_hort_chr(u"\u2588",u"\u2586",15) # left bottom corner and horizontal line
print_hort_chr(u'\u2588',u"\u2586",9)  # T up and horizontal line
print_hort_chr(u'\u2588',u"\u2586",12) # T up and horizontal line
print_hort_chr(u'\u2588',u"\u2586",0)  # right bottom corner and horizontal line
print("\n")




#----------------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
print("\033[1;48;5;231;38;5;21m  TRIANGLE_LINE  \033[0m")
print_hort_chr(u"\u25B6",u"\u25B6",15) # left top corner and horizontal top
print_hort_chr(u'\u25B6',u"\u25B6",9)  # T down and horizontal line
print_hort_chr(u'\u25B6',u"\u25B6",12) # T down and horizontal line
print_hort_chr(u'\u25B6',u"\u25B6",0)  # right top corner and horizontal top
print()
print(u'\u25B2'+"  Terminology  "+u'\u2588'+"  Hello  "+u'\u2588'+"  Good Bye  "+u'\u25BC') # vertical line

print_hort_chr(u'\u25B2',u'\u25C8',15) # left middle line
print_hort_chr(u'\u25C6',u'\u25C8',9)  # middle middle line
print_hort_chr(u'\u25C6',u'\u25C8',12) # middle middle line
print_hort_chr(u'\u25BC',u'\u25C8',0)  # right middle line
print()

print(u'\u25B2'+"  Terminology  "+u'\u2588'+"  Hello  "+u'\u2588'+"  Good Bye  "+u'\u25BC') # vertical line
print_hort_chr(u"\u25C0",u"\u25C0",15) # left bottom corner and horizontal line
print_hort_chr(u'\u25C0',u"\u25C0",9)  # T up and horizontal line
print_hort_chr(u'\u25C0',u"\u25C0",12) # T up and horizontal line
print_hort_chr(u'\u25C0',u"\u25C0",0)  # right bottom corner and horizontal line
print("\n")




#----------------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
def square(ver,hor,cor):
   print("\033[1;48;5;231;38;5;21m  SQUARE_LINE  \033[0m")
   print_hort_chr(cor,hor,15) # left top corner and horizontal top
   print_hort_chr(cor,hor,9)  # T down and horizontal line
   print_hort_chr(cor,hor,12) # T down and horizontal line
   print_hort_chr(cor,hor,0)  # right top corner and horizontal top
   print()
   print(f"{ver}  Terminology  {ver}  Hello  {ver}  Good Bye  {ver}") # vertical line

   print_hort_chr(cor,hor,15) # left middle line
   print_hort_chr(cor,hor,9)  # middle middle line
   print_hort_chr(cor,hor,12) # middle middle line
   print_hort_chr(cor,hor,0)  # right middle line
   print()

   print(ver + "  Terminology  "+ver + "  Hello  " + ver + "  Good Bye  " + ver) # vertical line
   print_hort_chr(cor,hor,15) # left bottom corner and horizontal line
   print_hort_chr(cor,hor,9)  # T up and horizontal line
   print_hort_chr(cor,hor,12) # T up and horizontal line
   print_hort_chr(cor,hor,0)  # right bottom corner and horizontal line
   print("\n")




square("\u25AE","\u25AC","\u25AC")
square("\u25C9","\u25A3","\u25A3")
square("\u2758","\u2796","\u2724")
square("\u2B1B","\u2B1B","\u2B1B")