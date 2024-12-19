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

#----------------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
print("\033[1;48;5;22;38;5;231m")
print(f"Symbol Description         \u2192   Symbol      Code",end="");print(f"{insp(7)}Heavy    Code     \033[0m")

print(f"9  Top Horizontal Line            \u2192    \u2500         \\u2500        \u2501     \\u2501  \u21B5\n")
print(f"10 Bottom Horizontal Line         \u2192    \u2500         \\u2500        \u2501     \\u2501  \u21B5\n")
print(f"11 Left  Vertical Line            \u2192    \u2502         \\u2502        \u2503     \\u2503  \u21B5\n")
print(f"12 Right Vertical Line            \u2192    \u2502         \\u2502        \u2503     \\u2503  \u21B5\n")

print(f"13 Top Left  Corner               \u2192    \u250C         \\u250C        \u250F     \\u250F  \u21B5\n")
print(f"14 Top Right Corner               \u2192    \u2510         \\u2510        \u2513     \\u2513  \u21B5\n")
print(f"15 Bottom Right Corner            \u2192    \u2518         \\u2518        \u251B     \\u251B  \u21B5\n")
print(f"16 Bottom Left Corner             \u2192    \u2514         \\u2514        \u2517     \\u2517  \u21B5\n")

print(f"17 Middle Top Corner              \u2192    \u252C         \\u252C        \u2533     \\u2533  \u21B5\n")
print(f"18 Middle Vertical Line           \u2192    \u2502         \\u2502        \u2503     \\u2503  \u21B5\n")
print(f"19 Middle Bottom Corner           \u2192    \u2534         \\u2534        \u253B     \\u253B  \u21B5\n")

print(f"21 Horizontal Line Under Header   \u2192    \u2500         \\u2500        \u2501     \\u2501  \u21B5\n")
print(f"22 Left Vertical Header Line      \u2192    \u2502         \\u2502        \u2503     \\u2503  \u21B5\n")
print(f"23 Right Vertical Header Line     \u2192    \u2502         \\u2502        \u2503     \\u2503  \u21B5\n")

print(f"24 Left Corner Under Line Header  \u2192    \u250C         \\u250C        \u250F     \\u250F  \u21B5\n")
print(f"25 Right Corner Under Line Header \u2192    \u2510         \\u2510        \u2513     \\u2513  \u21B5\n")

print(f"26 Horizontal Line                \u2192    \u2500         \\u2500        \u2501     \\u2501  \u21B5\n")


print(f"27 Left Lateral Corner            \u2192    \u251C         \\u251C        \u2523     \\u2523  \u21B5\n")
print(f"28 Right Lateral Corner           \u2192    \u2524         \\u2524        \u252B     \\u252B  \u21B5\n")

print(f"29 Middle Vertical Header Line    \u2192    \u2502         \\u2502        \u2503     \\u2503  \u21B5\n")
print(f"30 Middle Corner Under Line Header\u2192    \u253C         \\u253C        \u254B   \\u254B  \u21B5\n")
print(f"31 Middle Inner Corner            \u2192    \u253C         \\u253C        \u254B   \\u254B  \u21B5\n")


print(f"29 Bottom Right Corner            \u2192    \u2518         \\u2518        \u251B     \\u251B  \u21B5\n")
print(f"27 Bottom Left Corner             \u2192    \u2514         \\u2514        \u2517     \\u2517  \u21B5\n")

#----------------------------------------------------------------------------------------------------------------------------------------------------
print("\n")
print("\033[1;48;5;22;38;5;231m")
print(f"Description         \u2192      Symbol    {insp(4)} Code            Type_Line  \033[0m")
print(f"Top Left  Corner    \u2192     \u2554     {insp(8)} \\u2554  {insp(10)} Double Line \u21B5")
print(f"Middle Down Corner  \u2192        \u2566  {insp(8)} \\u2566  {insp(10)} Double Line \u21B5")
print(f"Right Top Corner    \u2192     \u2557     {insp(8)} \\u2557  {insp(10)} Double Line \u21B5")
print(f"Middle Left Corner  \u2192        \u2560  {insp(8)} \\u2560  {insp(10)} Double Line \u21B5")
print(f"Middle Middle Corner\u2192     \u256C     {insp(8)} \\u256C  {insp(10)} Double Line \u21B5")
print(f"Middle Right Corner \u2192       \u2563   {insp(8)} \\u2563  {insp(10)} Double Line \u21B5")
print(f"Left Bottom Corner  \u2192     \u255A     {insp(8)} \\u255A  {insp(10)} Double Line \u21B5")
print(f"Middle Up Corner    \u2192        \u2569  {insp(8)} \\u2569  {insp(10)} Double Line \u21B5")
print(f"Right Bottom Corner \u2192     \u255D     {insp(8)} \\u255D  {insp(10)} Double Line \u21B5")
print(f"Horizontal Line     \u2192        \u2550  {insp(8)} \\u2550  {insp(10)} Double Line \u21B5")
print(f"Vertical Line       \u2192     \u2551     {insp(8)} \\u2551  {insp(10)} Double Line \u21B5")



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


print("\033[1m")
print(" \u23A1               \u23A7  ")
print(" \u23A2               \u23AA  ")
print(" \u23A2               \u23A8  ")
print(" \u23A2               \u23AA  ")
print(" \u23A3               \u23A9  ")
print()



