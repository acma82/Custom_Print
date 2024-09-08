import sys
import fancyprint as fp
lst = fp.FancyFormat()
blue_msg  = fp.FancyMessage()  # for titles

green_msg = fp.FancyMessage()  # for subtitles
green_msg.bg = 2;  green_msg.fg = 0; green_msg.bold = True

darkg_msg = fp.FancyMessage()  # for script examples
darkg_msg.bg = 22; darkg_msg.bold = True

red_msg   = fp.FancyMessage()   # Note
red_msg.bg = 124; red_msg.bold = True

simple_msg= fp.FancyMessage()
simple_msg.bg =-1

crs = fp.Cursor()

ncols, nrows = fp.dimensions()
myrows = 90; mycols = 95
if (fp.OS_Linux == True and fp.OS_Windows == False):   fp.resize(rows=myrows, cols=mycols) #fp.resize(44, 90)
elif (fp.OS_Linux == False and fp.OS_Windows == True): fp.resize(rows=myrows, cols=mycols) #fp.resize(44, 90)
else:                                                  pass


screen_funs = [[" Screen_Functions "],["clean"],["clear"],["erase"],["dimensions"],
               ["resize"]]
miscellaneous_functions = [[" Help_Functions "],["ins_space"],["ins_newline"],["terminal_bell"],
                          ["bg_ansi_colors"],["fg_ansi_colors"],["set_font"],["reset_font"]]

help_classes = [[" Help_Classes "],["Align"],["Layout"],["Move"],["Length"],["Square"]]
classes_methods_fancyprint = [["Cursor", "FontStyle",   "FancyMessage",    "FancyFormat"        ,"Draw"],
                              ["jump",   "get_style",   "print_fancy_msg", "print_fancy_format", "line"],
                              ["move",   "reset_style", "----",            "----",               "square"],
                              ["gotoxy", "print_style", "----",      "----",               "----"],
                              ["moveTo", "----",        "----",            "----",               "----"]]

# classes_methods_fancyprint = [["Cursor", "FontStyle",   "FancyMessage",    "FancyFormat",       ],
#                               ["jump",   "get_style",   "print_fancy_msg", "print_fancy_format" ],
#                               ["move",   "reset_style", "----",            "----",              ],
#                               ["gotoxy", "print_style", "----",            "----",              ],
#                               ["moveTo", "----",        "----",            "----",              ]]




#------------------------------------------------------------------------------------------------
# Welcome Message Function for fancyprint Module                                                -
#------------------------------------------------------------------------------------------------
def welcome_message():
   welcome_msg = "Documentation For fancyprint Module....!"
   li = int(((mycols)-(len(welcome_msg)))/2)
   blue_msg.left_indent = li
   blue_msg.bold = True
   blue_msg.italic = True
   blue_msg.print_fancy_msg(welcome_msg)
   fp.ins_newline()

   lst.bg_all_cell_header = False
   lst.bold_header = True
   lst.bg_header = 90
   lst.fg_header = 231
   lst.italic_header = True
   # lst.underline_header = True
   
   lst.print_fancy_format(screen_funs)
   

   lst.adj_indent = 34
   crs.jump(qty=9,direction=fp.Move.UP)
   lst.print_fancy_format(miscellaneous_functions)

   lst.adj_indent = 64
   crs.jump(qty=11,direction=fp.Move.UP)
   lst.print_fancy_format(help_classes)


   lst.adj_indent = 2
   fp.ins_newline(3)


   blue_msg.length = fp.Length_bg.ONLY_WORD
   blue_msg.print_fancy_msg("  Classes and Methods in fancyprint Module ")
   lst.msg_title = " Clasess ";         lst.bg_title = 90; lst.fg_title = 231
   lst.bold_title = True;               lst.align_title = fp.Align.LEFT
   lst.msg_footnote = "Methods";        lst.fg_footnote = 11; 
   lst.align_footnote = fp.Align.RIGHT; lst.fg_data = 11 
   lst.bg_all_cell_header = True

   lst.print_fancy_format(classes_methods_fancyprint)
   fp.ins_newline(2)

   print("  To display help for specific function or method, just pass the name as a parameter\n    when running this script.")
   fp.ins_newline(1)
   print("  Example: python documentation.py clean")
   fp.ins_newline(1)

   
   message = "Note: "
   red_msg.bottom_lines = 0
   red_msg.print_fancy_msg(message)
   red_msg.bold = False
   message = '''     It is possible to display help for more than one function or method at the same time,
     it just need to be specified. If it's preferred, it can display all the methods for a     specific class or a combination of them.'''
     
   red_msg.fg = 15
   red_msg.top_lines = 0; red_msg.bottom_lines = 1
   red_msg.print_fancy_msg(message)

   print("\n  Example:")
   print("         python documentation.py clean terminal_bell get_style Cursor")
   fp.ins_newline(1)
   simple_msg.bg = -1

   menssage = "It's possible to display the complete documentation by passing \"all\" as parameter."
   simple_msg.print_fancy_msg(menssage)
   simple_msg.top_lines = 0
   
   message = "  python documentation.py all  "
   blue_msg.print_fancy_msg(message)
   fp.ins_newline(1)

   red_msg.bold = True
   red_msg.top_lines = 1
   message = "Note:"
   red_msg.bottom_lines = 0
   red_msg.print_fancy_msg(message)
   red_msg.bold = False
   red_msg.top_lines = 0
   red_msg.bottom_lines = 1   
   message = '''     The names for the functions, classes, and methods are not case sensitive.

     For example: python documentation.py screen_functions '''
   red_msg.print_fancy_msg(message)
   
#------------------------------------------------------------------------------------------------
#  All Screen Functions in fancyprint Module                                                    -
#------------------------------------------------------------------------------------------------
def clean_function():
   #------------------------------------------------------------------------------------------------
   # clean                                                                                         -
   #------------------------------------------------------------------------------------------------
   message = '''
      It cleans the terminal and return the cursor to home.
      It uses ansi code.
   '''
   green_msg.print_fancy_msg(screen_funs[1][0])
   print(message)
   print(f"{fp.ins_space(6)}{fp.set_font(1,90,231)} Example: {fp.reset_font()}")
   print(f"{fp.ins_space(16)}import fancyprint as fp")
   print(f"{fp.ins_space(16)}fp.clear()\n")

def clear_function():
   #------------------------------------------------------------------------------------------------
   # clear                                                                                         -
   #------------------------------------------------------------------------------------------------
   message = '''
      It cleans the terminal and return the cursor  to home.
      It uses the system command.
   '''
   green_msg.print_fancy_msg(screen_funs[2][0])
   print(message)
   print(f"{fp.ins_space(6)}{fp.set_font(1,90,231)} Example: {fp.reset_font()}")
   print(f"{fp.ins_space(16)}import fancyprint as fp")
   print(f"{fp.ins_space(16)}fp.clear()\n")

def erase_function():
   #------------------------------------------------------------------------------------------------
   # erase                                                                                         -
   #------------------------------------------------------------------------------------------------
   menssage = '''
      It cleans the terminal and the cursor remain in the same position.
      It uses ansi code.
   '''
   green_msg.print_fancy_msg(screen_funs[3][0])
   print(menssage)
   print(f"{fp.ins_space(6)}{fp.set_font(1,90,231)} Example: {fp.reset_font()}")
   print(f"{fp.ins_space(16)}import fancyprint as fp")
   print(f"{fp.ins_space(16)}fp.erase()\n")

def dimensions_function():
   #------------------------------------------------------------------------------------------------
   # dimensions                                                                                    -
   #------------------------------------------------------------------------------------------------
   menssage ='''
      It returns the size of the actual terminal: cols, rows.
      '''
   green_msg.print_fancy_msg(screen_funs[4][0])
   print(menssage)
   print(f"{fp.ins_space(6)}{fp.set_font(1,90,231)} Example: {fp.reset_font()}")
   print(f"{fp.ins_space(16)}import fancyprint as fp")
   print(f"{fp.ins_space(16)}ncols, nrows = fp.dimensions()\n")

def resize_function():
   #------------------------------------------------------------------------------------------------
   # resize                                                                                        -
   #------------------------------------------------------------------------------------------------
   message = '''
         It resizes the terminal
         '''
   green_msg.print_fancy_msg(screen_funs[5][0])
   print(message)
   print(f"{fp.ins_space(6)}{fp.set_font(1,90,231)} Example: {fp.reset_font()}")
   print(f"{fp.ins_space(16)}import fancyprint as fp")
   print(f"{fp.ins_space(16)}fp.resize(rows = n_rows, cols = n_cols)\n")

def screen_functions():
   clean_function()
   clear_function()
   erase_function()
   dimensions_function()
   resize_function()
   message = "For further reference check script:"   
   darkg_msg.print_fancy_msg(message)
   simple_msg.left_indent = 16
   simple_msg.print_fancy_msg("00_screen_funcs.py")
   simple_msg.left_indent = 2


#------------------------------------------------------------------------------------------------
# Start the Documentation for fancyprint Module                                                 -
#------------------------------------------------------------------------------------------------

fp.clear()
cmdl_argv = []
for argv in sys.argv:
   cmdl_argv.append(argv.lower())

print(cmdl_argv)
print(len(cmdl_argv))
flag_control = 0

if (len(cmdl_argv) == 1):
   welcome_message()
else:
   if ("screen_functions" in cmdl_argv):
      screen_functions()
      flag_control = 1
   elif ("clean" in cmdl_argv and flag_control == 0):
      clean_function()
   elif ("clear" in cmdl_argv and flag_control == 0):
      clear_function()
   elif ("erase" in cmdl_argv and flag_control == 0):
      erase_function()
   elif ("dimensions" in cmdl_argv and flag_control == 0):
      dimensions_function()
   elif ("resize" in cmdl_argv and flag_control == 0):
      resize_function()
   else:
      pass

   # if 


exit()


#------------------------------------------------------------------------------------------------
# All Functions and Classes in fancyprint Module                                                -
#------------------------------------------------------------------------------------------------
title = ''' All Functions, Classes and Methods in fancyprint Module  '''       
use_module = " import fancyprint as fp"
blue_msg.bold = True
blue_msg.print_fancy_msg(title)

blue_msg.italic = True
blue_msg.fg = 226
blue_msg.print_fancy_msg(use_module)
blue_msg.fg = 231


#
# ---+if ("Screen" in cmdl_argv):




print(cmdl_argv)


exit()


#------------------------------------------------------------------------------------------------
# reference for clean, clear, erase, dimensions and resize                                      -
#------------------------------------------------------------------------------------------------
def note_ref(bg, file_name):
   darkg_msg.bg = bg; darkg_msg.bold = True
   message = "Note:"
   darkg_msg.print_fancy_msg(message)
   darkg_msg.bold = False; darkg_msg.italic = True
   crs.jump(1,direction=fp.Move.UP)
   message = f'''
   For more reference, check {file_name} file.
             ''' 
   darkg_msg.print_fancy_msg(message)
   darkg_msg.italic = False
   print()
fp.resize(ncols, nrows)
note_ref(bg=22, file_name="00_screen_funs.py")

#------------------------------------------------------------------------------------------------
font_funs = [[" Font Functions "],["fp.bg_ansi_colors(bold=False, fg=-1)"],["fp.fg_ansi_colors(bold=False, bg=-1)"],
             ["set_font(bold=True,bg=22,fg=231)"],["reset_font()"],["ins_space(sp)"],["isn_newline(nl)"]]
lst.print_fancy_format(font_funs)
fp.ins_newline(2)

#------------------------------------------------------------------------------------------------
# reset_font()                                                                                  -
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
# ins_space()                                                                                   -
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
# ins_newline()                                                                                 -
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
# bg_ansi_colors                                                                                -
#------------------------------------------------------------------------------------------------
green_msg.print_fancy_msg(font_funs[1][0])
message = '''
   import fancyprint as fp
   
   fp.bg_ansi_colors(bool, int)
   
   This function displays all background colors available in the fancyprint
      module. Two options for better visualization:
   
   1.- The option bold for the font (True/False).
   2.- The option fg to visualize the background colors with a specific
         foreground color.


   Colors range from -1 to 256.
   To set the default color use -1 or 256.

   Example:
            fp.bg_ansi_colors(0,22)
            fp.bg_ansi_colors(fg=0, bold=1)
'''
print(message)
print(f"{fp.set_font(fg=118)}  For more reference check 01_bg_ansi_colosr.py file.\n")
#note_ref("01_bg_ansi_colors.py")

#------------------------------------------------------------------------------------------------
# fg_ansi_colors                                                                                -
#------------------------------------------------------------------------------------------------
green_msg.print_fancy_msg(font_funs[2][0])
message =    '''
   import fancyprint as fp

   fl.fg_ansi_colors(bool, int)
   
   This function displays all foreground colors available in the fancyprint
      module. Two options for better visualization:
   
   1.- The option bold helps for font.
   2.- The option bg to visualize the foreground colors with a specific
         background color.

   Colors range from -1 to 256.# lst = fp.FancyFormat()
   To set the default color use -1 or 256.

   Example:
            fl.fg_ansi_colors(0,22)
            fl.fg_ansi_colors(bg=32, bold=0)
'''
print(message)
#note_ref("02_fg_ansi_colors.py")
print(f"{fp.set_font(fg=118)}  For more reference check 02_fg_ansi_colosr.py file.\n")
#------------------------------------------------------------------------------------------------
# Explanation of the Functions                                                                  -
#------------------------------------------------------------------------------------------------
lst.bg_all_cell_header = True; lst.underline_header = False
classes_methods = [["Classes","Mehtods"],["FancyFormat","print_fa"]]# lst = fp.FancyFormat()
blue_msg  = fp.FancyMessage()  # for titles
green_msg = fp.FancyMessage()  # for subtitles
darkg_msg= fp.FancyMessage()   # for warning
crs = fp.Cursor()
lst.print_fancy_format(classes_methods)




#------------------------------------------------------------------------------------------------
# print("\033[2m")
input(f"{fp.bold_on()}{fp.reverse_on()}{fp.blink_on()} Enter to Continue: {fp.off_all()}")
fp.resize(nrows, ncols)

# print("\033[22m")
ncols, nrows = fp.dimensions()
if (fp.OS_Linux == True and fp.OS_Windows == False): fp.resize(nrows, ncols) #fp.resize(44, 90)
elif (fp.OS_Linux == False and fp.OS_Windows == True): pass
else:                                                  pass


import sys
# import fancyprint as fp

lst = fp.FancyFormat()
font = fp.FontCustomization()
font.set_bg = 22
font.set_fg = 231
font.set_bold = True
font.set_italic = True
title = ''' All Functions, Classes and Methods in fancyprint Module  '''  
blue_msg  = fp.FancyMessage(font)  # for titles
blue_msg.print_fancy_msg(title)
font.set_bg = 90

purple_msg  = fp.FancyMessage(font)  # for titles
purple_msg.print_fancy_msg(title)

blue_msg.fg = 0
blue_msg.bg = 231
blue_msg.print_fancy_msg(title)


print()
print(f"{fp.bg_on(22)} Miguelito {fp.fg_on(13)} I am here {fp.bold_on()} Hello Again. {fp.off_all()}")
print()
print(f"{fp.bold_on()}{fp.bg_on(90)} Miguelito  I am here {fp.fg_on(11)} Hello Again. {fp.reset_font()}")
print(f"{fp.reverse_on()}Miguel Angel{fp.reverse_off()}")

for i in range(0, 16):
   for j in range(0, 16):
      code = str(i * 16 + j)
      sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
   print (u"\u001b[0m")


for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
    print (u"\u001b[0m")