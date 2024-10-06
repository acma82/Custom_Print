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

white_msg = fp.FancyMessage()
white_msg.bg = 231; white_msg.fg = 21; white_msg.bold = True

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
def adj_screen(y, x):
   if (fp.OS_Linux == True and fp.OS_Windows == False):   fp.resize(rows=y, cols=x) #fp.resize(44, 90)
   elif (fp.OS_Linux == False and fp.OS_Windows == True): fp.resize(rows=y, cols=x) #fp.resize(44, 90)
   else:                                                  pass

# Variables
ncols, nrows = fp.dimensions()
myrows = 90; mycols = 100
adj_screen(myrows, mycols)



screen_funs        = [[" Screen_Functions "],["clean"],["clear"],["erase"],["dimensions"], ["resize"]]

internal_functions = [[" Internal_Functions "],["ins_space"],["ins_newline"], ["ansi_colors"], ["terminal_bell"]]

help_classes       = [[" Help_Classes "],["Move"],["Align"],["Layout"],["Length"],["Style_Line"]]

classes_methods_fancyprint = [["Cursor", "FontStyle",   "FancyMessage",    "FancyFormat"        ,"Draw"],
                              ["jump",   "get_style",   "print_fancy_msg", "print_fancy_format", "line"],
                              ["move",   "reset_style", "print_fancy_note",            "----",   "arrow"],
                              ["gotoxy", "print_style", "print_fancy_header",      "----",       "box"],
                              ["moveTo", "----",        "----",            "----",               "brakets"]]

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
   crs.jump(qty=8,direction=fp.Move.UP)
   lst.print_fancy_format(internal_functions)

   # lst.bg_header = 90; lst.fg_header = 231
   
   lst.adj_indent = 68
   crs.jump(qty=7,direction=fp.Move.UP)
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

   fp.ins_newline(1); fst.print_style(" Example 2: "); print(" python documentation.py clean terminal_bell get_style Cursor")
      
   fp.ins_newline(2); fst.print_style(" Example 3: "); print(" python documentation.py help_functions")
   
   message = '''     
     In example 2, notice that we are calling a mix of functions, methods and a class.
  For the class, it will call all the methods that this class contains as shown in the
  tables above. Cursor Class contains four methos, jump, move, gotoxy, and moveTo and
  so on for the rest of the following classes.
 
  In example 3, we are calling help for all the functions that this class contains.

  It's possible to display the complete documentation by passing \"all\" as parameter.
'''
   fp.ins_newline(1); blue_msg.length = fp.Length_bg.ONLY_WORD; simple_msg.print_fancy_msg(message)

   message = "  python documentation.py all  "
   blue_msg.print_fancy_msg(message)
   
   blue_msg.length = fp.Length_bg.ALL_ROW   
   lst.msg_title = "";        lst.msg_footnote = ""
   lst.fg_data = -1;          lst.adj_indent = 30
   lst.adj_top_margin = 2;    lst.adj_bottom_margin = 2
   # lst.print_fancy_format("Report Bugs \u2192 acma82@yahoo.com", fp.Line_Style.DOUBLE)
   lst.print_fancy_format("Bugs \u2192 acma.mex@gmail.com", fp.Line_Style.DOUBLE)


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
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_space(18)}fp.clear()\n")

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
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_space(18)}fp.clear()\n")

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
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_space(18)}fp.erase()\n")

def Dimensions_Function():
   #------------------------------------------------------------------------------------------------
   # dimensions                                                                                    -
   #------------------------------------------------------------------------------------------------
   menssage ='''
      It returns the size of the actual terminal: cols, rows.
      '''
   green_msg.print_fancy_msg(screen_funs[4][0])
   print(menssage)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_space(18)}ncols, nrows = fp.dimensions()\n")

def Resize_Function():
   #------------------------------------------------------------------------------------------------
   # resize                                                                                        -
   #------------------------------------------------------------------------------------------------
   message = '''
      It resizes the terminal
         '''
   green_msg.print_fancy_msg(screen_funs[5][0])
   print(message)
   print(f"{fp.ins_space(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_space(18)}fp.resize(rows = n_rows, cols = n_cols)\n")

#---------------------------------------------------------------------------------------------------
#  internal_functions in fancyprint Module                                                           -
#---------------------------------------------------------------------------------------------------
def Internal_Functions():   
   blue_msg.print_fancy_msg("Internal Functions")
   Ins_Space_Function()
   Ins_Newline_Function()
   Ansi_Color_Function()   
   Terminal_Bell_Function()
   message = "\u25CF Reference \u2192  01_ansi_colors.py"
   dark_green_msg.print_fancy_msg(message)
   

def Ins_Space_Function():
   #------------------------------------------------------------------------------------------------
   # ins_space                                                                                     -
   #------------------------------------------------------------------------------------------------
   green_msg.print_fancy_msg(internal_functions[1][0])
   message = f'''
      This function inserts x number of spaces between words.

               fancy_print.ins_space(x)

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp      
                  print("Hello"+fp.ins_space(20)+"There")

      {fp.set_font(1,231,90)} \u25CF Output {fp.reset_font()}  Hello                    There
      '''
   
   print(message)
   # print(f"{fp.ins_space(6)}{fp.set_font(1,231,90)} \u25CF Reference \u2192 ins_space.py {fp.reset_font()}\n")

def Ins_Newline_Function():
   #------------------------------------------------------------------------------------------------
   # ins_newline                                                                                   -
   #------------------------------------------------------------------------------------------------
   green_msg.print_fancy_msg(internal_functions[2][0])
   message = f'''
      This function inserts x number of lines.

               fancy_print.ins_newline(x)

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
                  print("Python 3.12")
                  fp.ins_newline(2)
                  print("is amazing...!")
              
      {fp.set_font(1,231,90)} \u25CF Output {fp.reset_font()}  Python 3.12

               
                  is amazing...!
      '''
   print(message)
   

def Ansi_Color_Function():
   #------------------------------------------------------------------------------------------------
   # ansi_colors                                                                                -
   #------------------------------------------------------------------------------------------------
   green_msg.print_fancy_msg(internal_functions[3][0]+": fancy_print contains 4 functions that make use of ansi code.")
   print("\n  bg colors available in the ansi code \n")

   for i in range(0, 16):
      for j in range(0, 16):
         code = str(i * 16 + j)
         sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
      print (u"\u001b[0m")
   
   fp.ins_newline(2)
   print("  fg colors available in the ansi code \n")
   for i in range(0, 16):
      for j in range(0, 16):
         code = str(i * 16 + j)
         sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
      print (u"\u001b[0m")
   
   print()

   purple_msg.print_fancy_msg("bg_ansi_colors(bool, int, int)")
   message = f''' 
      This function displays all background colors available in the fancyprint
      module. Three options for better visualization:
   
      1.- The option bold for the font (True/False).
      2.- The option fg to visualize the background colors with a specific foreground color.
      3.- The option n_line to insert lines between the colors.

      
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
                  fp.bg_ansi_colors(bold=1, fg=22, n_line=1)
   '''
   print(message)

   purple_msg.print_fancy_msg("fg_ansi_colors(bool, int, int)")
   message = f'''
      This function displays all foreground colors available in the fancyprint
      module. Two options for better visualization:
   
      1.- The option bold helps for font.
      2.- The option bg to visualize the foreground colors with a specific
          background color.
      3.- It insert lines to have space between them.

      
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
                  fp.fg_ansi_colors(bold=1, bg=22, n_line=1)
   '''
   print(message)

   purple_msg.print_fancy_msg("set_font() and reset_font()")

   message =f'''
      set_font() function changes the attributes of the font.
      reset_font() set font to its default attributes.
      
      Parameters with their default values:
      
      1) bold=False      4) italic=False         7) blinking=False      10) inverse=False
      2) bg=-1           5) underline=False      8) dim=False
      3) fg=-1           6) strike=False         9) hidden=False
      
      As you see there are many parameters to pass, if this is a littlle bit annoying, then use
      the FontStyle Class. Check the documentation for that class.

      The best way to use this function is only to pass the first 3 parameters as the example below.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
                  print(fp.set_font(1,11,21) + " Python is " + fp.set_font(0,1) +
                        " Wonderful." + fp.reset_font())

'''
   print(message)
   
   message = '''The range for colors goes from -1 to 256. 

to set the default color use -1 or 256 for bg and fg.

blinking might not work in all the OS. We use Red Hat Family.'''
   
   white_msg.print_fancy_note("Note:", message)

def Terminal_Bell_Function():
   #------------------------------------------------------------------------------------------------
   # terminal_bell                                                                                 -
   #------------------------------------------------------------------------------------------------
   message = f'''
      This function makes sound of the terminal bell.               

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
                  fp.terminal_bell()
      '''
   green_msg.print_fancy_msg(internal_functions[4][0])
   print(message)
   fp.terminal_bell()

#---------------------------------------------------------------------------------------------------
# Help_Fucntions                                                                                   -
#---------------------------------------------------------------------------------------------------
def Help_Classes():
   blue_msg.print_fancy_msg("Help Classes")


def Move_Class():
   #------------------------------------------------------------------------------------------------
   # Move                                                                                          -
   #------------------------------------------------------------------------------------------------
   green_msg.print_fancy_msg(help_classes[1][0])
   # UP    = "up"
   # RIGHT = "right"
   # DOWN  = "down"
   # LEFT  = "left"

#----------------------------------------------------------------------------------------------------------------------------------------------
# Start the Documentation for fancyprint Module                                                                                               -
#----------------------------------------------------------------------------------------------------------------------------------------------
fp.clear()
ctrl = 0
cmdl_argv = []
for argv in sys.argv:
   cmdl_argv.append(argv.lower())

flag_screen_functions = False; flag_internal_functions=False; flag_help_classes = False
flag_cursor = False;           flag_font_style = False;   flag_fancy_message = False
flag_fancy_format = False;     flag_draw = False

if (len(cmdl_argv) == 1):
   Welcome_Message()

elif ("all" in cmdl_argv):
   Screen_Functions()
   Internal_Functions()
   fp.terminal_bell()
   

else:
   for fun in cmdl_argv:
      if ("screen_functions" in fun):     Screen_Functions();    flag_screen_functions = True
      elif ("internal_functions" in fun): Internal_Functions();  flag_internal_functions = True
      elif ("help_classes" in fun):       Help_Classes();        flag_help_classes = True
      

      elif ("clean" == fun and flag_screen_functions == False):           Clean_Function()
      elif ("clear" == fun and flag_screen_functions == False):           Clear_Function()
      elif ("erase" == fun and flag_screen_functions == False):           Erase_Function()
      elif ("dimensions" == fun and flag_screen_functions == False):      Dimensions_Function()
      elif ("resize" == fun and flag_screen_functions == False):          Resize_Function()
      

      elif ("ins_space" == fun and flag_internal_functions == False):     Ins_Space_Function()
      elif ("ins_newline" == fun and flag_internal_functions == False):   Ins_Newline_Function()
      elif ("terminal_bell" == fun and flag_internal_functions == False): Terminal_Bell_Function()
      elif ("ansi_colors" == fun and flag_internal_functions == False):   Ansi_Color_Function()


      elif ("move" == fun and flag_help_classes == False):                Move_Class()



      else: pass
         

fp.ins_newline(3)
input("  Press Enter to Continue: ")
adj_screen(nrows, ncols)

# fp.clear()
# fp.clean()green_msg.print_fancy_msg(screen_funs[5][0])