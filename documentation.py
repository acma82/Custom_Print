import sys
import fancyprint as fp
lst = fp.FancyFormat()
#----------------------------------------------------------------------------------------------------------------------------------------------
# Difining all the clases
blue_msg  = fp.FancyMessage()  # for titles

green_msg = fp.FancyMessage()  # for subtitles
green_msg.bg = 2;  green_msg.fg = 0; green_msg.bold = True

dark_green_msg = fp.FancyMessage()
dark_green_msg.bg = 22; dark_green_msg.bold = True

purple_msg = fp.FancyMessage()
purple_msg.bg = 90; purple_msg.fg = 231


msg = fp.FancyMessage()   # Note
msg.right_indent = 5

simple_msg= fp.FancyMessage()
simple_msg.bg =-1; simple_msg.fg = -1
simple_msg.right_indent = 5


crs = fp.Cursor()

fst = fp.FontStyle() 
fst.bold = True; 
fst.fg = 0
fst.bg = 231
fst.indent = 2
fst.next_line = False

#----------------------------------------------------------------------------------------------------------------------------------------------
# Variables
ncols, nrows = fp.dimensions()
myrows = 90; mycols = 100
if (fp.OS_Linux == True and fp.OS_Windows == False):   fp.resize(rows=myrows, cols=mycols) #fp.resize(44, 90)
elif (fp.OS_Linux == False and fp.OS_Windows == True): fp.resize(rows=myrows, cols=mycols) #fp.resize(44, 90)
else:                                                  pass


screen_funs = [[" Screen_Functions "],["clean"],["clear"],["erase"],["dimensions"],
               ["resize"]]
miscellaneous_functions = [[" Miscellaneous_Functions "],["ins_space"],["ins_newline"],["terminal_bell"],
                          ["bg_ansi_colors"],["fg_ansi_colors"],["set_font"],["reset_font"]]

help_classes = [[" Help_Classes "],["Move"],["Align"],["Layout"],["Length"],["Style_Line"]]
classes_methods_fancyprint = [["Cursor", "FontStyle",   "FancyMessage",    "FancyFormat"        ,"Draw"],
                              ["jump",   "get_style",   "print_fancy_msg", "print_fancy_format", "line"],
                              ["move",   "reset_style", "print_fancy_note",            "----",   "Arrow"],
                              ["gotoxy", "print_style", "print_fancy_header",      "----",       "square"],
                              ["moveTo", "----",        "----",            "----",               "Brakets"]]

# classes_methods_fancyprint = [["Cursor", "FontStyle",   "FancyMessage",    "FancyFormat",       ],
#                               ["jump",   "get_style",   "print_fancy_msg", "print_fancy_format" ],
#                               ["move",   "reset_style", "----",            "----",              ],
#                               ["gotoxy", "print_style", "----",            "----",              ],
#                               ["moveTo", "----",        "----",            "----",              ]]
#----------------------------------------------------------------------------------------------------------------------------------------------
# Welcome Message Function for fancyprint Module                                                                                              -
#----------------------------------------------------------------------------------------------------------------------------------------------
def Welcome_Message():
   welcome_msg = "Documentation For fancyprint Module....!"
   li = int(((mycols)-(len(welcome_msg)))/2)
   blue_msg.left_indent = li
   blue_msg.bold = True
   blue_msg.italic = True
   blue_msg.print_fancy_msg(welcome_msg)
   fp.ins_newline()

   lst.bg_all_cell_header = False
   lst.bold_header = True
   lst.bg_header = 90; lst.fg_header = 231

   # lst.bg_header = 231; lst.fg_header = 90
   lst.italic_header = True
   
   lst.print_fancy_format(screen_funs)
   

   lst.adj_indent = 34
   crs.jump(qty=9,direction=fp.Move.UP)
   lst.print_fancy_format(miscellaneous_functions)

   # lst.bg_header = 90; lst.fg_header = 231
   
   lst.adj_indent = 72
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

   lst.horizontal_separator_line_on = True
   lst.print_fancy_format(classes_methods_fancyprint,fp.Line_Style.SINGLE)
   fp.ins_newline(2)

   print("  To display help for specific function or method, just pass the name as a parameter\n    when running this script.")
   fp.ins_newline(1)
   fst.print_style(" Example 1: ")
   print(" python documentation.py clean")
   #print(f" {fp.set_font(1,231,0)} Example 1: {fp.reset_font()} python documentation.py clean")
   fp.ins_newline(1)

   note=" Note: "
#                  20                  40                  60                  80   85   90
   message_note = '''
It is possible to display help for more than one function or method at the same    
time, it just need to be specified. If it's preferred, it can display all the      
methods for a specific class or a combination of them.'''
   blue_msg.length = fp.Length_bg.ALL_ROW
   blue_msg.bold = False
   blue_msg.print_fancy_note(note_msg=note, body_msg=message_note)
   fp.ins_newline(1)
   fst.print_style(" Example 1: ")
   print(" python documentation.py clean terminal_bell get_style Cursor")
   #print(f" {fp.set_font(1,231,0)} Example 2: {fp.reset_font()} python documentation.py clean terminal_bell get_style Cursor")
   
   fp.ins_newline(2)
   
   fst.print_style(" Example 3: ")
   print(" python documentation.py help_functions")
   # print(f" {fp.set_font(1,231,0)} Example 3: {fp.reset_font()} python documentation.py help_functions")
   
   message = '''     
     In example 2, notice that we are calling a mix of functions, methods and a class.
  For the class, it will call all the methods that this contain as shown in the tables
  above. Cursor Class contains four methos, jump, move, gotoxy, and moveTo and
  so on for the rest of the following classes.
 
  In example 3, we are calling help for all the function that this table contains.

  It's possible to display the complete documentation by passing \"all\" as parameter.
'''
   blue_msg.length = fp.Length_bg.ONLY_WORD
   fp.ins_newline(1)
   simple_msg.print_fancy_msg(message)
   message = "  python documentation.py all  "
   blue_msg.print_fancy_msg(message)
   blue_msg.length = fp.Length_bg.ALL_ROW
   fp.ins_newline(1)

#---------------------------------------------------------------------------------------------------
#  Screen_Functions in fancyprint Module                                                           -
#---------------------------------------------------------------------------------------------------
def Screen_Functions():
   blue_msg.bold = True
   blue_msg.italic = True
   blue_msg.print_fancy_msg("Screen Functions")
   Clean_Function()
   Clear_Function()
   Erase_Function()
   Dimensions_Function()
   Resize_Function()
   fp.ins_newline(3)
   message = "\u25CF Reference \u2192  00_screen_functions.py"
   dark_green_msg.print_fancy_msg(message)
   # fp.ins_newline(2)

def Clean_Function():
   #------------------------------------------------------------------------------------------------
   # clean                                                                                         -
   #------------------------------------------------------------------------------------------------
   message = '''
      It cleans the terminal and return the cursor to home.
      It uses ansi code.
   '''
   green_msg.print_fancy_msg(screen_funs[1][0])
   print(message)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}")
   print(f"{fp.ins_space(16)}import fancyprint as fp")
   print(f"{fp.ins_space(16)}fp.clear()\n")

def Clear_Function():
   #------------------------------------------------------------------------------------------------
   # clear                                                                                         -
   #------------------------------------------------------------------------------------------------
   message = '''
      It cleans the terminal and return the cursor  to home.
      It uses the system command.
   '''
   green_msg.print_fancy_msg(screen_funs[2][0])
   print(message)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}")
   print(f"{fp.ins_space(16)}import fancyprint as fp")
   print(f"{fp.ins_space(16)}fp.clear()\n")

def Erase_Function():
   #------------------------------------------------------------------------------------------------
   # erase                                                                                         -
   #------------------------------------------------------------------------------------------------
   menssage = '''
      It cleans the terminal and the cursor remain in the same position.
      It uses ansi code.
   '''
   green_msg.print_fancy_msg(screen_funs[3][0])
   print(menssage)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}")
   print(f"{fp.ins_space(16)}import fancyprint as fp")
   print(f"{fp.ins_space(16)}fp.erase()\n")

def Dimensions_Function():
   #------------------------------------------------------------------------------------------------
   # dimensions                                                                                    -
   #------------------------------------------------------------------------------------------------
   menssage ='''
      It returns the size of the actual terminal: cols, rows.
      '''
   green_msg.print_fancy_msg(screen_funs[4][0])
   print(menssage)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}")
   print(f"{fp.ins_space(16)}import fancyprint as fp")
   print(f"{fp.ins_space(16)}ncols, nrows = fp.dimensions()\n")

def Resize_Function():
   #------------------------------------------------------------------------------------------------
   # resize                                                                                        -
   #------------------------------------------------------------------------------------------------
   message = '''
      It resizes the terminal
         '''
   green_msg.print_fancy_msg(screen_funs[5][0])
   print(message)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}")
   print(f"{fp.ins_space(16)}import fancyprint as fp")
   print(f"{fp.ins_space(16)}fp.resize(rows = n_rows, cols = n_cols)\n")

#---------------------------------------------------------------------------------------------------
#  Miscellaneous_Functions in fancyprint Module                                                           -
#---------------------------------------------------------------------------------------------------
def Miscellaneous_Functions():   
   blue_msg.print_fancy_msg("Miscellaneous Functions")
   Ins_Space_Function()
   Ins_Newline_Function()
   Terminal_Bell_Function()
   BG_Ansi_Colors_Function()

def Ins_Space_Function():
   #------------------------------------------------------------------------------------------------
   # ins_space                                                                                     -
   #------------------------------------------------------------------------------------------------

   message = f'''
      This function inserts x number of spaces between words.

               import fancyprint as fp
               fp.ins_space(x)

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}
               print("Hello"+fp.ins_space(40)+"There")

      '''
   
   green_msg.print_fancy_msg(miscellaneous_functions[1][0])
   print(message)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,90)} \u25CF Reference \u2192 ins_space.py {fp.reset_font()}\n")

def Ins_Newline_Function():
   #------------------------------------------------------------------------------------------------
   # ins_newline                                                                                   -
   #------------------------------------------------------------------------------------------------
   message = f'''
      This function inserts x number of lines.

               import fancyprint as fp
               fp.ins_newline(x)

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}
               print("Python 3.12")
               fp.ins_newline(3)
               print("is amazing...!")
      '''
   green_msg.print_fancy_msg(miscellaneous_functions[2][0])
   print(message)
   
def Terminal_Bell_Function():
   #------------------------------------------------------------------------------------------------
   # terminal_bell                                                                                 -
   #------------------------------------------------------------------------------------------------
   message = f'''
      This function makes sound of the terminal bell.

               import fancyprint as fp

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}
               fp.terminal_bell()
      '''
   green_msg.print_fancy_msg(miscellaneous_functions[3][0])
   print(message)

def BG_Ansi_Colors_Function():
   #------------------------------------------------------------------------------------------------
   # bg_ansi_colors                                                                                -
   #------------------------------------------------------------------------------------------------
   message =f'''
      This function displays all background colors available in the fancyprint
         module. Two options for better visualization:
   
      1.- The option bold for the font (True/False).
      2.- The option fg to visualize the background colors with a specific
          foreground color.
      
               import fancyprint as fp
   
               fp.bg_ansi_colors(bool, int)
   

               Colors range from -1 to 256.
               To set the default color use -1 or 256.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}
              fp.bg_ansi_colors(0,22)
              fp.bg_ansi_colors(fg=0, bold=1)
'''
   green_msg.print_fancy_msg(miscellaneous_functions[4][0])
   print(message)

   for i in range(0, 16):
      for j in range(0, 16):
         code = str(i * 16 + j)
         sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
      print (u"\u001b[0m")

def FG_Ansi_Colors_Function():
   for i in range(0, 16):
      for j in range(0, 16):
         code = str(i * 16 + j)
         sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
      print (u"\u001b[0m")

   #------------------------------------------------------------------------------------------------
   # fg_ansi_colors                                                                                -
   #------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------
# Help_Fucntions                                                                                   -
#---------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------
# Start the Documentation for fancyprint Module                                                                                               -
#----------------------------------------------------------------------------------------------------------------------------------------------
fp.clear()
cmdl_argv = []
for argv in sys.argv:
   cmdl_argv.append(argv.lower())

flag_screen_functions = False; flag_miscellaneous_functions=False; flag_help_classes = False
flag_cursor = False;           flag_font_style = False;   flag_fancy_message = False
flag_fancy_format = False;     flag_draw = False

if (len(cmdl_argv) == 1):
   Welcome_Message()

elif ("all" in cmdl_argv):
   Screen_Functions()
   Miscellaneous_Functions()
   fp.terminal_bell()
   

else:
   for fun in cmdl_argv:
      if ("screen_functions" in fun):          Screen_Functions();        flag_screen_functions = True
      elif ("miscellaneous_functions" in fun): Miscellaneous_Functions(); flag_miscellaneous_functions = True
      

      elif ("clean" == fun and flag_screen_functions == False):      Clean_Function()
      elif ("clear" == fun and flag_screen_functions == False):      Clear_Function()
      elif ("erase" == fun and flag_screen_functions == False):      Erase_Function()
      elif ("dimensions" == fun and flag_screen_functions == False): Dimensions_Function()
      elif ("resize" == fun and flag_screen_functions == False):     Resize_Function()
      

      elif ("ins_space" == fun and flag_miscellaneous_functions == False):      Ins_Space_Function()
      elif ("ins_newline" == fun and flag_miscellaneous_functions == False):    Ins_Newline_Function()
      elif ("terminal_bell" == fun and flag_miscellaneous_functions == False):  Terminal_Bell_Function()
      elif ("bg_ansi_colors" == fun and flag_miscellaneous_functions == False): BG_Ansi_Colors_Function()
      else:
         pass

lst.msg_title = ""
lst.msg_footnote = ""
lst.fg_data = -1
lst.adj_indent = 30
lst.adj_top_margin = 4
lst.adj_bottom_margin = 4
lst.print_fancy_format("Report Bugs \u2192 acma82@yahoo.com", fp.Line_Style.DOUBLE)