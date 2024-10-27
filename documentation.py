import sys
import fancyprint as fp
lst = fp.FancyFormat()
#----------------------------------------------------------------------------------------------------------------------------------------------
# Difining all the clases
blue_msg  = fp.FancyMessage()  # for titles

green_msg = fp.FancyMessage()  # for subtitles
green_msg.bg_body = 2;  green_msg.fg_body = 0; green_msg.bold_body = True

dark_green_msg = fp.FancyMessage()
dark_green_msg.bg_body = 22; dark_green_msg.bold_body = True

purple_msg = fp.FancyMessage()
purple_msg.bg_body = 90; purple_msg.fg_body = 231

white_msg = fp.FancyMessage()
white_msg.bg_body = 231; white_msg.fg_body = 21
white_msg.bold_note = True; white_msg.bold_body = True

msg = fp.FancyMessage()   # Note
msg.right_indent = 5

simple_msg = fp.FancyFormat()
simple_msg.adj_top_margin = 1;    simple_msg.align_title = fp.Align.JUSTIFY
simple_msg.bg_title = 231;        simple_msg.fg_title = 0
simple_msg.bold_title = True

crs = fp.Cursor()

fst = fp.FontStyle() 
fst.bold = True; 
fst.fg = 0
fst.bg = 231
fst.indent = 2
fst.next_line = False

pen = fp.Pen()
pen.bg_draw_line = 229
pen.fg_draw_line = 128
pen.bold_draw_line = True


#----------------------------------------------------------------------------------------------------------------------------------------------
def adj_screen(y, x):
   if (fp.OS_Linux == True and fp.OS_Windows == False):   fp.resize(rows=y, cols=x) #fp.resize(44, 90)
   elif (fp.OS_Linux == False and fp.OS_Windows == True): fp.resize(rows=y, cols=x) #fp.resize(44, 90)
   else:                                                  pass

# Variables
ncols, nrows = fp.dimensions()
myrows = 92; mycols = 100
adj_screen(myrows, mycols)



screen_funs        = [[" Screen_Functions "],["clean"],["clear"],["erase"],["dimensions"], ["resize"]]

internal_functions = [[" Internal_Functions "],["ins_chr"],["ins_newline"], ["ansi_colors"], ["terminal_bell"]]

help_classes       = [[" Help_Classes "],["Move"],["Align"],["Layout"],["Length"],["Unicode"],["Line_Style"]]

classes_methods_fancyprint = [["Cursor",  "FontStyle",    "FancyMessage",          "FancyFormat"        ,  "Pen"],
                              ["jumpTo",  "start_style",  "print_fancy_message",   "print_fancy_format",   "draw_line"],
                              ["jumpxy",  "stop_style",   "print_fancy_note",      "reset_fancy_format",   "draw_box"],
                              ["moveTo",  "print_style",  "----             ",      "----             ",   "----"],
                              ["movexy",  "reset_style",  "----             ",      "----             ",   "----"]]

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
   blue_msg.bold_body = True
   blue_msg.italic_body = True
   blue_msg.print_fancy_message(welcome_msg)
   fp.ins_newline()

   lst.bg_all_cell_header = False
   lst.bold_header = True
   lst.bg_header = 90; lst.fg_header = 231

   # lst.bg_header = 231; lst.fg_header = 90
   lst.italic_header = True
   
   lst.print_fancy_format(screen_funs)
   

   lst.adj_indent = 34
   crs.jumpTo(qty=8,direction=fp.Move.UP)
   lst.print_fancy_format(internal_functions)

   # lst.bg_header = 90; lst.fg_header = 231
   
   lst.adj_indent = 68
   crs.jumpTo(qty=7,direction=fp.Move.UP)
   lst.print_fancy_format(help_classes)


   lst.adj_indent = 2
   #print(f"{crs.moveTo(qty=45, direction=fp.Move.RIGHT)}{fp.set_font(True,-1,230)} {fp.Unicode.FACE} {fp.reset_font()}")
   
   
   fp.ins_newline(3)


   blue_msg.length = fp.Length_bg.ONLY_WORD
   blue_msg.print_fancy_message("  Classes and Methods in fancyprint Module ")
   lst.msg_title = " Clasess ";         lst.bg_title = 90; lst.fg_title = 231
   lst.bold_title = True;               lst.align_title = fp.Align.LEFT
   lst.msg_footnote = "Methods";        lst.align_footnote = fp.Align.RIGHT
   lst.fg_footnote = 11;  lst.fg_data = 11
   lst.bg_all_cell_header = True

   lst.horizontal_separator_line_on = True
   lst.print_fancy_format(classes_methods_fancyprint,fp.Line_Style.SINGLE)
   fp.ins_newline(2)

   print("  To display help for specific function or method, just pass the name as a parameter\n    when running this script.")
   fp.ins_newline(1)
   fst.print_style(" Example 1:")
   print(" python documentation.py clean\n")   
   fp.ins_newline(1)

   note=" Note: "
#                  20                  40                  60                  80   85   90
   message_note = '''
It is possible to display help for more than one function or method at the same    
time, it just need to be specified. If it's preferred, it can display all the      
methods for a specific class or a combination of them.'''
   blue_msg.length = fp.Length_bg.ALL_ROW
   blue_msg.bold_body = False
   blue_msg.msg_note = note
   blue_msg.position_note = 2
   blue_msg.bold_note = True
   blue_msg.print_fancy_note(message_note)

   fp.ins_newline(1); fst.print_style(" Example 2: "); print(" python documentation.py clean terminal_bell get_style Cursor")
      
   fp.ins_newline(2); fst.print_style(" Example 3: "); print(" python documentation.py help_functions")
   
   fp.ins_newline(2)
   message = '''     
     In example 2, notice that we are calling a mix of functions, methods and a class.
  For the class, it will call all the methods that this class contains as shown in the
  tables above. Cursor Class contains four methos, jump, move, gotoxy, and moveTo and
  so on for the rest of the following classes.
 
  In example 3, we are calling help for all the functions that this class contains.

  It's possible to display the complete documentation by passing \"all\" as parameter.
'''
   blue_msg.left_indent = 2
   blue_msg.print_fancy_message(message)
   fp.ins_newline(2)
   blue_msg.length = fp.Length_bg.ONLY_WORD; 
   blue_msg.left_indent = li
   message = "  python documentation.py all  "
   blue_msg.print_fancy_message(message)
   
   blue_msg.length = fp.Length_bg.ALL_ROW   
   blue_msg.left_indent = 2
   lst.msg_title = "";        lst.msg_footnote = ""
   lst.fg_data = -1;          lst.adj_indent = 30
   lst.adj_top_margin = 2;    lst.adj_bottom_margin = 2
   # lst.print_fancy_format("Report Bugs \u2192 acma82@yahoo.com", fp.Line_Style.DOUBLE)
   lst.print_fancy_format("Bugs \u2192 acma.mex@gmail.com", fp.Line_Style.DOUBLE)


#---------------------------------------------------------------------------------------------------
#  Screen_Functions in fancyprint Module                                                           -
#---------------------------------------------------------------------------------------------------
def Screen_Functions():
   blue_msg.bold_body = True
   blue_msg.italic_body = True
   blue_msg.print_fancy_message("Screen Functions")
   Clean_Function()
   Clear_Function()
   Erase_Function()
   Dimensions_Function()
   Resize_Function()
   fp.ins_newline(3)
   message = "\u25CF Reference \u2192  00_screen_functions.py"
   dark_green_msg.print_fancy_message(message)


def Clean_Function():
   #------------------------------------------------------------------------------------------------
   # clean                                                                                         -
   #------------------------------------------------------------------------------------------------
   message = '''
      It cleans the terminal and return the cursor to home.
      It uses ansi code.
   '''
   green_msg.print_fancy_message(screen_funs[1][0])
   print(message)
   print(f"{fp.ins_chr(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_chr(18)}fp.clear()\n")

def Clear_Function():
   #------------------------------------------------------------------------------------------------
   # clear                                                                                         -
   #------------------------------------------------------------------------------------------------
   message = '''
      It cleans the terminal and return the cursor  to home.
      It uses the system command.
   '''
   green_msg.print_fancy_message(screen_funs[2][0])
   print(message)
   print(f"{fp.ins_chr(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_chr(18)}fp.clear()\n")

def Erase_Function():
   #------------------------------------------------------------------------------------------------
   # erase                                                                                         -
   #------------------------------------------------------------------------------------------------
   menssage = '''
      It cleans the terminal and the cursor remain in the same position.
      It uses ansi code.
   '''
   green_msg.print_fancy_message(screen_funs[3][0])
   print(menssage)
   print(f"{fp.ins_chr(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_chr(18)}fp.erase()\n")

def Dimensions_Function():
   #------------------------------------------------------------------------------------------------
   # dimensions                                                                                    -
   #------------------------------------------------------------------------------------------------
   menssage ='''
      It returns the size of the actual terminal: cols, rows.
      '''
   green_msg.print_fancy_message(screen_funs[4][0])
   print(menssage)
   print(f"{fp.ins_chr(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_chr(18)}ncols, nrows = fp.dimensions()\n")

def Resize_Function():
   #------------------------------------------------------------------------------------------------
   # resize                                                                                        -
   #------------------------------------------------------------------------------------------------
   message = '''
      It resizes the terminal
         '''
   green_msg.print_fancy_message(screen_funs[5][0])
   print(message)
   print(f"{fp.ins_chr(6)}{fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp")
   print(f"{fp.ins_chr(18)}fp.resize(rows = n_rows, cols = n_cols)\n")

#---------------------------------------------------------------------------------------------------
#  internal_functions in fancyprint Module                                                           -
#---------------------------------------------------------------------------------------------------
def Internal_Functions():   
   blue_msg.print_fancy_message("Internal Functions")
   ins_chr_Function()
   Ins_Newline_Function()
   Ansi_Color_Function()   
   Terminal_Bell_Function()
   message = "\u25CF Reference \u2192  01_ansi_colors.py"
   dark_green_msg.print_fancy_message(message)
   

def ins_chr_Function():
   #------------------------------------------------------------------------------------------------
   # ins_chr                                                                                     -
   #------------------------------------------------------------------------------------------------
   green_msg.print_fancy_message(internal_functions[1][0])
   message = f'''
      This function inserts x number of spaces between words.

               fancy_print.ins_chr(x)

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp      
                  print("Hello"+fp.ins_chr(20)+"There")

      {fp.set_font(1,231,90)} \u25CF Output {fp.reset_font()}  Hello                    There

      Note: By default is set to space if character is not specified.
      '''
   
   print(message)
   # print(f"{fp.ins_chr(6)}{fp.set_font(1,231,90)} \u25CF Reference \u2192 ins_chr.py {fp.reset_font()}\n")

def Ins_Newline_Function():
   #------------------------------------------------------------------------------------------------
   # ins_newline                                                                                   -
   #------------------------------------------------------------------------------------------------
   green_msg.print_fancy_message(internal_functions[2][0])
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
   green_msg.print_fancy_message(internal_functions[3][0]+": fancy_print contains 4 functions that make use of ansi code.")
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

   purple_msg.print_fancy_message("bg_ansi_colors(bool, int, int)")
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

   purple_msg.print_fancy_message("fg_ansi_colors(bool, int, int)")
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

   purple_msg.print_fancy_message("set_font() and reset_font()")

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

blinking might not work in all the OS. We use Red Hat Family.
'''   
   white_msg.print_fancy_note(message)
   #fp.ins_newline(2)


def Terminal_Bell_Function():
   #------------------------------------------------------------------------------------------------
   # terminal_bell                                                                                 -
   #------------------------------------------------------------------------------------------------
   message = f'''
      This function makes sound of the terminal bell.               

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
                  fp.terminal_bell()
      '''
   green_msg.print_fancy_message(internal_functions[4][0])
   print(message)
   fp.terminal_bell()

#---------------------------------------------------------------------------------------------------
# Help_Fucntions                                                                                   -
#---------------------------------------------------------------------------------------------------
def Help_Classes():
   blue_msg.print_fancy_message("Help Classes")
   Move_Class()
   Align_Class()
   Layout_Class()
   Length_Class()
   Unicode_Class()
   Style_Line_Class()



def Move_Class():
   #------------------------------------------------------------------------------------------------
   # Move                                                                                          -
   #------------------------------------------------------------------------------------------------
   green_msg.print_fancy_message(help_classes[1][0])
   message = f'''
      This class is used with the Cursor Class and it contains 4 options.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp

      {fp.ins_chr(10)}  fp.Move.RIGHT
      {fp.ins_chr(10)}  fp.Move.LEFT
      {fp.ins_chr(10)}  fp.Move.UP
      {fp.ins_chr(10)}  fp.Move.DOWN
   
      Note: These options can be replaced for the original value as display below:

      {fp.ins_chr(10)}  fp.Move.RIGHT  \u2192  \"right\"
      {fp.ins_chr(10)}  fp.Move.LEFT   \u2192  \"left\"
      {fp.ins_chr(10)}  fp.Move.UP     \u2192  \"up\"
      {fp.ins_chr(10)}  fp.Move.DOWN   \u2192  \"down\"        

'''
   print(message)

def Align_Class():
   #------------------------------------------------------------------------------------------------
   # Align                                                                                         -
   #------------------------------------------------------------------------------------------------
   # Works with FancyFormat (print_fancy_format)
   # works with FancyMessage (print_fancy_note, print_fancy_header)
   green_msg.print_fancy_message(help_classes[2][0])
   message = f'''
      Aligns Class is used with the FancyFormat Class and FancyMessage Class.
      It contains 4 options.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp

      {fp.ins_chr(10)}  fp.Align.RIGHT
      {fp.ins_chr(10)}  fp.Align.LEFT
      {fp.ins_chr(10)}  fp.Align.CENTER
      {fp.ins_chr(10)}  fp.Align.JUSTIFY
      
      Note: These options can be replaced for the original value as display below:

      {fp.ins_chr(10)}  fp.Move.RIGHT    \u2192  \"right\"    \u2192  \"r\"
      {fp.ins_chr(10)}  fp.Move.LEFT     \u2192  \"left\"     \u2192  \"l"
      {fp.ins_chr(10)}  fp.Move.CENTER   \u2192  \"center\"   \u2192  \"c\"
      {fp.ins_chr(10)}  fp.Move.JUSTIFY  \u2192  \"justify\"  \u2192  \"j\"
'''   
   print(message)


def Layout_Class():
   #------------------------------------------------------------------------------------------------
   # Layout                                                                                        -
   #------------------------------------------------------------------------------------------------
   # works with FancyFormat, range, set, setfrozen obj.set_layout = fp.Layout.VERTICAL
   # works with Draw (line, arrow)
   green_msg.print_fancy_message(help_classes[3][0])
   message = f'''     
      Layout Class is used on FancyFormat only for the range, set, frozenset type of variables.
      Layout also is uded with Draw Class. It contains 2 options.
      
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp

      {fp.ins_chr(10)}  fp.Layout.HORIZONTAL
      {fp.ins_chr(10)}  fp.Layout.VERTICAL
      
      Note: These options can be replaced for the original value as display below:

      {fp.ins_chr(10)}  fp.Layout.HORIZONTAL   \u2192  \"horizontal\"
      {fp.ins_chr(10)}  fp.Layout.VERTICAL     \u2192  \"vertical\"

'''
   print(message)
def Length_Class():
   #------------------------------------------------------------------------------------------------
   # Length                                                                                        -
   #------------------------------------------------------------------------------------------------
   # FancyMessage   
   green_msg.print_fancy_message(help_classes[4][0])
   message = f'''
      Length Class is used with FancyMessage Class and there 2 options.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp

      {fp.ins_chr(10)}  fp.Length.ALL_ROW
      {fp.ins_chr(10)}  fp.Length.ONLY_WORD
            
'''
   print(message)


def Unicode_Class():
   #------------------------------------------------------------------------------------------------
   # Unicode chrs                                                                                  -
   #------------------------------------------------------------------------------------------------     
   green_msg.print_fancy_message(help_classes[5][0])
   message = f'''
      Unicode Class is used with the Pen Class.
      It contains a few chr code to use Unicode.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp

      {fp.ins_chr(10)}  fp.Unicode.BLACK_DIAMOND
      {fp.ins_chr(10)}  fp.Unicode.WHITE_DIAMOND

      {fp.ins_chr(10)}  fp.Unicode.BLACK_CIRCLE 
      {fp.ins_chr(10)}  fp.Unicode.WHITE_CIRCLE 
      
      This class helps to set some unicode characters when using the Pen Class.

      For more reference {fp.Unicode.EM_DASH}{fp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE} https://www.unicode.org/charts/nameslist/
'''   
   print(message)


def Style_Line_Class():
   #------------------------------------------------------------------------------------------------
   # Style_Line                                                                                    -
   #------------------------------------------------------------------------------------------------
   # FancyFormat   
   green_msg.print_fancy_message(help_classes[6][0])
   message = f'''
      Style_Line Class is used with FancyFormat Class and Draw Class. There are 7 options.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp

      {fp.ins_chr(10)}  fp.Style_Line.CUSTOMIZED
      {fp.ins_chr(10)}  fp.Style_Line.SINGLE
      {fp.ins_chr(10)}  fp.Style_Line.SINGLE_BOLD
      {fp.ins_chr(10)}  fp.Style_Line.SINGLE_HEAVY
      {fp.ins_chr(10)}  fp.Style_Line.DOUBLE
      {fp.ins_chr(10)}  fp.Style_Line.DASH
      {fp.ins_chr(10)}  fp.Style_Line.SQR_BRACKETS
      {fp.ins_chr(10)}  fp.Style_Line.NONE

      Note: These options can be replaced for the original value as display below:

      {fp.ins_chr(10)}  fp.Style_Line.CUSTOMIZED     \u2192  \"customized\"  
      {fp.ins_chr(10)}  fp.Style_Line.SINGLE         \u2192  \"single\"   
      {fp.ins_chr(10)}  fp.Style_Line.SINGLE_BOLD    \u2192  \"single_bold\" 
      {fp.ins_chr(10)}  fp.Style_Line.SINGLE_HEAVY   \u2192  \"single_heavy\"
      {fp.ins_chr(10)}  fp.Style_Line.DOUBLE         \u2192  \"double\"
      {fp.ins_chr(10)}  fp.Style_Line.DASH           \u2192  \"dash\"      
      {fp.ins_chr(10)}  fp.Style_Line.SQR_BRACKETS   \u2192  \"sq_brackets\"
      {fp.ins_chr(10)}  fp.Style_Line.NONE           \u2192  \"none\"
   '''
   print(message)


#---------------------------------------------------------------------------------------------------
# Cursor Class                                                                                     -
#---------------------------------------------------------------------------------------------------
def Cursor_Class():
   blue_msg.print_fancy_message("Cursor Class")
   JumpTo_Method()
   Jumpxy_Method()
   MoveTo_Method()
   Movexy_Method()  
   message = "This methods only works with the actual size of the terminal, if you try to go beyond  \
the size of the terminal, it may not work properly."
   white_msg.print_fancy_note(message)

   message = "\u25CF Reference \u2192  02_Cursor_Move_Class.py"
   dark_green_msg.print_fancy_message(message)
   
def JumpTo_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[1][0])
   message = f'''
   
      jumpTo method is used to jump rows or columns for the cursor in the terminal.
      The difference between move and jump is that move return the code, while jump
      execute the code.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  crs = fp.Cursor()
      {fp.ins_chr(10)}  crs.jumpTo(qty=2,  direction = fp.Move.DOWN);        print("I am down")
      {fp.ins_chr(10)}  crs.jumpTo(qty=20, direction = "right");             print("I am right")
      {fp.ins_chr(10)}  crs.jumpTo(1, fp.Move.UP);                           print("I am up")
      {fp.ins_chr(10)}  crs.jumpTo(5, "down");                               print("GoodBye...!")

   '''
   print(message)


def Jumpxy_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[2][0])
   message = f'''
   
      jumpxy method is used to jump to especific coordinate on the terminal.
      The difference between jumpxy and movexy is that jumpxy execute the code
      while the movexy returns the code.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  crs = fp.Cursor()
      {fp.ins_chr(10)}  crs.jumpToxy(0,0);     print("*** Start Here ***")
      {fp.ins_chr(10)}  crs.jumpToxy(20, 5);   print("GoodBye...!")      

   '''
   print(message)


def MoveTo_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[3][0])
   message = f'''
   
      moveTo method is used to move rows or columns for the cursor in the terminal.
      The difference between move and jump is that move return the code, while jump
      execute the code.

      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  crs = fp.Cursor()
      '''
   
   message2 = '''                  print(f"{crs.moveTo(15,"right")} First One",  end="")

                  print(f"{crs.moveTo(15,"right")} Second One", end="")
            
                  print(f"{crs.moveTo(qty=20,direction="left")} Hello")
   
   '''
   print(message)
   print(message2)

def Movexy_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[4][0])
   message = f'''
   
      movexy method is used to move to especific coordinate on the terminal.
      The difference between jumpxy and movexy is that jumpxy execute the code
      while the movexy returns the code.


      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  crs = fp.Cursor()
   '''
   message2 = '''                  print(f"{crs.movexy(15,40)}hello again")

      '''
   print(message)
   print(message2)



#---------------------------------------------------------------------------------------------------
# FontStyle Class                                                                                  -
#---------------------------------------------------------------------------------------------------
def FontStyle_Class():
   blue_msg.print_fancy_message("FontStyle Class")
   font_style_options = [["bold","bg","fg","italic"],
                        ["dim","underline","blinking","inverse"],
                        ["hidden","strike","indent","next_line"]]
   lst.msg_title = "FontStyle Class Variables"
   lst.bg_header = -1; lst.fg_header = -1
   lst.print_fancy_format(font_style_options,fp.Line_Style.NONE)

   Start_Stop_Style_Method()
   Print_Style_Method()
   Reset_Style_Method()

   message = "\u25CF Reference \u2192  03_FontStyle_Class.py"
   dark_green_msg.print_fancy_message(message)

def Start_Stop_Style_Method():
   message = classes_methods_fancyprint[1][1] + " and "+ classes_methods_fancyprint[2][1]
   green_msg.print_fancy_message(message)
   message = f'''
   
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  fs = fp.FontStyle
      {fp.ins_chr(10)}  fs.bg = 14
      {fp.ins_chr(10)}  print(fs.start_style() + " FontStyle Class " + fs.stop_style())

   '''
   print(message)

def Print_Style_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[3][1])

   message = f'''
   
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  fs = fp.FontStyle
      {fp.ins_chr(10)}  fs.bg = 14
      {fp.ins_chr(10)}  fs.print_style(" FontStyle Class ")
      {fp.ins_chr(10)}  print("  Normal Font...!")

   '''
   print(message)

def Reset_Style_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[4][1])
   message = f'''
   
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  fs = fp.FontStyle
      {fp.ins_chr(10)}  fs.bg = 14
      {fp.ins_chr(10)}  fs.print("  FontStyle Class ")
      {fp.ins_chr(10)}  fs.reset_style()
      {fp.ins_chr(10)}  fs.print("  Default Values ")

   '''
   print(message)



#---------------------------------------------------------------------------------------------------
# FancyMessage Class                                                                               -
#---------------------------------------------------------------------------------------------------
def _display_body_args():
   # Body Default Values
   simple_msg.msg_title = " Body Default Values "
   default_values = [["bg_body     = 4",       "italic_body = False",        "blinking_body  = False"],
                     ["fg_body     = 231",     "strike_body = False",        "underline_body = False"],
                     ["dim_body    = False",   "hidden_body = False",        "inverse_body   = False"],                     
                     ["bold_body   = False",   "msg_body    = \"Body Msg\"", "help_lines     = False"]]
   simple_msg.print_fancy_format(default_values,fp.Line_Style.NONE)


def FancyMessage_Class():
   blue_msg.print_fancy_message("FancyMessage Class")



   print(f"\n     {fp.set_font(True,231,0)} Diagram Description {fp.reset_font()}\n")
   ex_msg = fp.FancyMessage()
   ex_msg.bg_body = 229;           ex_msg.bg_title = 229;            ex_msg.bg_footnote = 229
   ex_msg.fg_body=0;               ex_msg.fg_title = 21;             ex_msg.fg_footnote = 21
   ex_msg.italic_body = True;      ex_msg.italic_footnote = True;    ex_msg.italic_title = True
   ex_msg.bold_body = True;        ex_msg.bold_footnote = 1;         ex_msg.bold_title = True
   ex_msg.left_indent = 15;        ex_msg.right_indent = 15;         ex_msg.align_title = fp.Align.CENTER
   ex_msg.top_lines = 3;           ex_msg.bottom_lines = 3;          ex_msg.align_footnote = fp.Align.CENTER
   ex_msg.lines_title_body = 3;    ex_msg.lines_body_footnote=3      
   ex_msg.msg_title ="TITLE";      ex_msg.msg_footnote = "FOOTNOTE"; ex_msg.help_lines = True


   ex_fst = fp.FontStyle()
   #ex_fst.bold = True; 
   ex_fst.fg = 128;       ex_fst.bg = 229;      ex_fst.bold = True
   ex_fst.indent = 0
   ex_fst.next_line = False

   message = '''
Guido van Rossum, a Dutch programmer, created Python in the late 1980s
as a hobby project. He started working on it in December 1989 at Cent-
rum Wiskunde & Informatica (CWI) in the Netherlands.

Python was first released on February 20, 1991. Python was named after
the 1970s BBC comedy sketch series Monty Python's Flying Circus.
'''
# Paragraph Description
   ex_msg.print_fancy_message(message)
   
   crs.jumpTo(qty=15, direction=fp.Move.UP)
   pen.draw_line(size=3, tail=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT, body=" left indent  ",\
                 head=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
   pen.draw_line(size=3, tail="\u2500", body=f"{fp.ins_chr(30,"\u2500")} msg_body {fp.ins_chr(27,"\u2500")}",\
                 head=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
   pen.draw_line(size=3, tail=" ", body="right indent ",\
                 head=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT)
   print()
   pen.adj_indent = 45
   crs.jumpTo(qty=7, direction=fp.Move.UP)
   crs.jumpTo(qty=45, direction=fp.Move.LEFT)
   
   pen.draw_line(size=4, layout=fp.Layout.VERTICAL, tail=fp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                 body=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
   pen.draw_line(size=3, layout=fp.Layout.VERTICAL, tail=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL,\
                 body=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=fp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL)
   
   print()
   crs.jumpTo(qty=6, direction=fp.Move.UP)
   pen.adj_indent = 29
   pen.draw_line(size=3, layout=fp.Layout.VERTICAL, tail="       top lines", body= " ", head="lines_title_body")


   crs.jumpTo(qty=8, direction=fp.Move.DOWN)
   pen.adj_indent = 55
   pen.draw_line(size=4, layout=fp.Layout.VERTICAL, tail=fp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                 body=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
   pen.draw_line(size=3, layout=fp.Layout.VERTICAL, tail=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL,\
                 body=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=fp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL)
   
   pen.adj_indent = 56
   crs.jumpTo(qty=6, direction=fp.Move.UP)
   pen.draw_line(size=3, layout=fp.Layout.VERTICAL, tail="lines_body_footnote", body= "\n\n", head="bottom lines") 
  
   crs.jumpTo(qty=2, direction=fp.Move.DOWN)
   pen.adj_indent = 0
   fp.ins_newline(3)
   
   # Note Description
   message = '''
Guido van Rossum, a Dutch programmer, created Python in the late 1980s
as a hobby project. He started working on it in December 1989 at Cent-
rum Wiskunde & Informatica (CWI) in the Netherlands.
Python was first released on February 20, 1991. Python was named after
the 1970s BBC comedy sketch series Monty Python's Flying Circus.
'''

   ex_msg.bold_note = True;    ex_msg.fg_note = 231
   ex_msg.position_note = 5;   ex_msg.bg_note = 90
   ex_msg.left_space_note = 5; ex_msg.right_space_note = 4
   ex_msg.right_indent = 10;   ex_msg.msg_note = " Python "
   #ex_msg.adj_bg_lines_to_right_indent = True;  ex_msg.adj_bg_msg_to_space_available = False;  ex_msg.length = fp.Length_bg.ONLY_WORD

   ex_msg.print_fancy_note(message)

   crs.jumpTo(qty=10, direction=fp.Move.UP)

   pen.draw_line(size=3, tail=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT, body=" A ",\
                 head=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
   pen.draw_line(size=3, tail="", body="msg_note",\
                 head=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
   pen.draw_line(size=3, tail=" ", body="B ",\
                 head=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   

   pen.draw_line(size=3, tail="\u2500", body=f"{fp.ins_chr(30,"\u2500")} msg_body {fp.ins_chr(27,"\u2500")}",\
                 head=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
   pen.draw_line(size=3, tail="", body="right indent",\
                 head=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT)
   
   print()
   crs.jumpTo(qty=3, direction=fp.Move.UP)
   pen.adj_indent = 35
   pen.draw_line(size=3, layout=fp.Layout.VERTICAL, tail=fp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                 body=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=fp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL)
   crs.jumpTo(qty=2, direction=fp.Move.UP)
   print(f"{crs.moveTo(22,fp.Move.RIGHT)}top_lines --{fp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE}")
   crs.jumpTo(6,fp.Move.DOWN)


   pen.draw_line(size=3, layout=fp.Layout.VERTICAL, tail=fp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                 body=fp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=fp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL)
   crs.jumpTo(qty=2, direction=fp.Move.UP)
   print(f"{crs.moveTo(19,fp.Move.RIGHT)}bottom_lines --{fp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE}")
   

   crs.jumpTo(qty=1, direction=fp.Move.UP)
   crs.jumpTo(qty=40, direction=fp.Move.RIGHT)

   print(f"A --{fp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE} left_space_note",end=",  ")
   print(f"B --{fp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE} right_space_note")

   crs.jumpTo(qty=3, direction=fp.Move.DOWN)

   # Indentation and Lines Default Values
   simple_msg.msg_title = " Default Indent and Line Values "
   default_values = [["top_lines    = 1", "length = Length_bg.ALL_ROW"],
                     ["bottom_lines = 1", "adj_bg_lines_to_right_indent  = False "],
                     ["right_indent = 2", "adj_bg_msg_to_space_available = False"]] 
   

   simple_msg.print_fancy_format(default_values,fp.Line_Style.NONE)
    
   _display_body_args()


   message = '''All the above variables are being used by both methods, print_fancy_message and
print_fancy_note.
'''
   white_msg.print_fancy_note(message)

   fp.ins_newline(1)

   message = f'''
     {fp.set_font(True,-1,14)}length{fp.set_font(False)}
         This is the width of the terminal and it has 2 options.

         ALL_ROW  :  It will do the background color to the complete row in the terminal
         ONLY_WORD:  It will do the background color to only the text ignoring the 
                        left_indent and right_indent
     
     {fp.set_font(True,-1,14)}adj_bg_lines_to_right_indent{fp.set_font(False)}
         This applies to the top_lines and bottom_lines

         True : This will do the background color to the space available (74)
         False: This will do the background color to the longest line in the msg_body

     {fp.set_font(True,-1,14)}adj_bg_msg_to_space_available{fp.set_font(False)}
         This applies to the lines of text in the msg_body

         True : This will do the background to the space available (74)
         False: This will do the background to the longest line in all the msg_body

'''
   print(message)

   message = '''adj_bg_lines_to_right_indent and adj_bg_msg_to_space_available only take action when

   length = Length_bg.ONLY_WORD
'''
   white_msg.print_fancy_note(message)

   Print_Fancy_Message_Method()
   Print_Fancy_Note_Method()



def Print_Fancy_Message_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[1][2])
   # Title Default Values
   simple_msg.msg_title = " Title Default Values "
   default_values = [["bg_title    = 4    ",     "italic_title  = False",      "blinking_title   = False"],
                     ["fg_title    = 231  ",     "strike_title  = False",      "underline_title  = False"],
                     ["dim_title   = False",     "hidden_title  = False",      "inverse_title    = False"],
                     ["bold_title  = False",     "                     ",      "                       "],
                     ["                   ",     "                     ",      "                       "],
                     ["msg_title   = \"\"",      "title_indent  = 2",          "align_title      = Align.LEFT"],
                     ["                 ",        "                ",          "lines_title_body = 1"]]

   simple_msg.print_fancy_format(default_values,fp.Line_Style.NONE)
   

   # Body Default Values
   _display_body_args()
   
   # Footnote Default Values
   simple_msg.msg_title = " Footnote Default Values "
   default_values = [["bg_footnote     = 4",       "italic_footnote = False",        "blinking_footnote  = False"],
                     ["fg_footnote     = 231",     "strike_footnote = False",        "underline_footnote = False"],
                     ["dim_footnote    = False",   "hidden_footnote = False",        "inverse_footnote   = False"],                     
                     ["bold_footnote   = False",   "msg_footnote    = \"\" ",         "                         "],
                     ["                       ",   "                       ",         "                         "],
                     ["footnote_indent = 2",       "lines_body_footnote = 1",         "align_footnote = Align.RIGHT"]]

   simple_msg.print_fancy_format(default_values,fp.Line_Style.NONE)
   
   message = f'''
   
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  fmsg = fp.FancyMessage()
      {fp.ins_chr(10)}  fmsg.title = \" Title \"
      {fp.ins_chr(10)}  fmsg.footnote = \" Footnote \"
      {fp.ins_chr(10)}  fmsg.help_lines = True      
      {fp.ins_chr(10)}  paragraph = " This is a short Paragraph.....!
      {fp.ins_chr(10)}  fmsg.print_fancy_mesage(paragraph)

   '''
   print(message)
   fmsg = fp.FancyMessage()
   fmsg.msg_title = " Title "
   fmsg.msg_footnote = "Footnote"
   #fmsg.align_footnote = fp.Align.CENTER
   paragraph = " This is a short paragraph.....!"
   fmsg.help_lines = True
   fmsg.print_fancy_message(paragraph)
   
   fp.ins_newline(2)
   message = '''footnote_indent works with align_footnote. When the align_footnote is set to
Align.Justify, then footnote_indent controls the position of the msg_footnote.

The same situation applies for title_indent and align_title.
'''
   white_msg.print_fancy_note(message)

   

def Print_Fancy_Note_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[2][2])
   # Note Default Values
   default_values = [["bg_note   = 231",            "italic_note   = False",    "blinking_note  = False"],
                     ["fg_note   = 0",              "strike_note   = False",    "underline_note = False"],
                     ["dim_note  = False",          "hidden_note   = False",    "inverse_note   = False"],
                     ["bold_note = False",           "                     ",    "                     "],
                     ["                 ",          "                     ",    "                      "],
                     ["msg_note  = \" Note: \"",    "position_note    = 1",     "                      "],
                     ["left_space_note = 2    ",    "right_space_note = 2",     "align_note = Align.JUSTIFY"]]
   simple_msg.msg_title = " Note Default Values "
   simple_msg.print_fancy_format(default_values,fp.Line_Style.NONE)
   
   # Body Default Values
   _display_body_args()
   
   message = f'''
  
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  fmsg = fp.FancyMessage()      
      {fp.ins_chr(10)}  fmsg.bold_note = True
      {fp.ins_chr(10)}  fmsg.bg_body = 90      
      {fp.ins_chr(10)}  message = \"There are variables that are being used by both methods.....\"
      {fp.ins_chr(10)}  fmsg.print_fancy_mesage(paragraph)

   '''   

   print(message)
   message = '''There are variables that are being used by both methods, print_fancy_message
and print_fancy_note.
'''
   fmsg = fp.FancyMessage()
   fmsg.bold_note = True
   fmsg.bg_body = 90

   fmsg.help_lines = True
   fmsg.print_fancy_note(message)

#---------------------------------------------------------------------------------------------------
# FancyFormat Class                                                                                -
#---------------------------------------------------------------------------------------------------
def FancyFormat_Class():
   blue_msg.print_fancy_message(classes_methods_fancyprint[0][3] + " Class")
   Diagram1()
   Diagram2()
   Diagram3()
   Print_Fancy_Format_Method()
   Reset_Fancy_Format_Method()


def Diagram1():
   message = f'''
      {fp.set_font(1,14,0)} Single Data {fp.reset_font()}        
   '''
   print(message)
   
   d1_lst = fp.FancyFormat()
   print("$")
   print("      \u2190 0")

   d1_lst.adj_top_space = 1; d1_lst.adj_bottom_space = 1

   d1_lst.adj_space = 0; d1_lst.adj_indent = 3

   data = "...Data Inside The Box \u2190 data..."
   d1_lst.msg_title = "Title \u2190 1";       d1_lst.align_title = "center"
   
   d1_lst.msg_footnote = "Footnote \u2190 8"; d1_lst.align_footnote = "right"

   #corners
   d1_lst.top_left_corner_chr = "3"
   d1_lst.top_right_corner_chr = "4"
   d1_lst.bottom_right_corner_chr = "5"
   d1_lst.bottom_left_corner_chr = "6"

   # left and right lines
   d1_lst.left_vertical_line_chr = "L"
   d1_lst.right_vertical_line_chr = "R"
   #d1_lst.top_horizontal_line_chr = "-"
   d1_lst.bottom_horizontal_line_chr = "*"



   d1_lst.print_fancy_format(data)

   crs.jumpTo(qty=6, direction=fp.Move.UP)
   print("      \u2190 2")
   crs.jumpTo(qty=3, direction=fp.Move.DOWN)
   print("      \u2190 7")
   fp.ins_newline(1)
   print("      \u2190 9")

   
   crs.jumpTo(qty=8, direction=fp.Move.UP)
   d1_lst.adj_indent = 50
   data = "   Data Inside The Box   "
   d1_lst.msg_title = "Title"; d1_lst.msg_footnote = "Footnote"   
   d1_lst.print_fancy_format(data,fp.Line_Style.DASH)
   
   crs.jumpTo(qty=5, direction=fp.Move.UP)
   print(",,,")
   crs.jumpTo(qty=5, direction=fp.Move.DOWN)
   print("")
  

   values=[["0 \u2192 adj_top_margin",         " "],
           ["1 \u2192 msg_title",""            " "],
           ["2 \u2192 adj_top_space",          "-   \u2192 top_horizontal_line_chr"],
           ["3 \u2192 top_left_corner_chr",    "... \u2192 adj_space"],
           ["4 \u2192 top_right_corner_chr",   "*   \u2192 bottom_horizontal_line_chr"],
           ["5 \u2192 bottom_right_corner_chr",",,, \u2192 adj_indent"],
           ["6 \u2192 bottom_left_corner_chr", "L   \u2192 left_vertical_line_chr"],
           ["7 \u2192 adj_bottom_space",       "R   \u2192 right_vertical_line_chr"          ],
           ["8 \u2192 msg_footnote",           " "          ],
           ["9 \u2192 adj_bottom_margin",      " "          ]
          ]
   simple_msg.msg_title = " Description "
   simple_msg.print_fancy_format(values,fp.Line_Style.NONE)


   message = f'''
  
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  f_data = fp.FancyFormat()
      {fp.ins_chr(10)}  f_data.msg_title        = \"Title\"
      {fp.ins_chr(10)}  f_data.msg_footnote     = \"footnote\"
      {fp.ins_chr(10)}  f_data.adj_top_space    = 1
      {fp.ins_chr(10)}  f_data.adj_bottom_space = 1
      {fp.ins_chr(10)}  f_data.adj_indent       = 3
      {fp.ins_chr(10)}  data = \"Data Inside The Box\"      
      {fp.ins_chr(10)}  f_data.print_fancy_format(data)

   '''      
   print(message)
   
   print(f"{fp.ins_chr(100,"=")}")
   
   print()
   
def Diagram2():
   d2_lst = fp.FancyFormat()
   values = [["Data 1","Data 2","Data 3"]]
   message = f'''
      {fp.set_font(1,14,0)} Multiple Horizontal Data {fp.reset_font()}        
   '''
   print(message)
   d2_lst.middle_top_corner_chr = "a"
   d2_lst.middle_vertical_line_chr = "b"
   d2_lst.middle_bottom_corner_chr = "c"
   d2_lst.print_fancy_format(values)
   
   crs.jumpTo(qty=3, direction=fp.Move.UP)
   d2_lst.adj_indent = 50
   d2_lst.print_fancy_format(values,fp.Line_Style.DASH)

   simple_msg.msg_title = " Description "
   values = [["a \u2192 middle_top_corner_chr"],
             ["b \u2192 middle_vertical_line_chr"],
             ["c \u2192 middle_bottom_corner_chr"]]

   simple_msg.print_fancy_format(values,fp.Line_Style.NONE)

   message = f'''
  
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  f_data = fp.FancyFormat()
      {fp.ins_chr(10)}  data = [["Data 1","Data 2","Data 3"]]
      {fp.ins_chr(10)}  f_data.print_fancy_format(data)

   '''      
   print(message)
   print(f"{fp.ins_chr(100,"=")}")

   values = [["Header"],["Data 1"],["Data 2"],["Data 3"]]
   message = f'''
      {fp.set_font(1,14,0)} Multiple Vertical Data {fp.reset_font()}        
   '''
   print(message)
   d2_lst.adj_indent = 2
   d2_lst.horizontal_line_under_header_on = True
   d2_lst.horizontal_separator_line_on = True

   d2_lst.horizontal_line_under_header_chr = "d"
   d2_lst.horizontal_line_chr = "e"
   
   d2_lst.left_vertical_header_line_chr = "f"
   d2_lst.right_vertical_header_line_chr = "g"

   d2_lst.left_corner_under_line_header_chr = "h"
   d2_lst.right_corner_under_line_header_chr = "i"

   d2_lst.left_lateral_corner_chr = "j"
   d2_lst.right_lateral_corner_chr = "k"

   d2_lst.print_fancy_format(values)


   crs.jumpTo(qty=9, direction=fp.Move.UP)
   d2_lst.adj_indent = 50
   d2_lst.print_fancy_format(values,fp.Line_Style.DASH)

   simple_msg.msg_title = " Description "
   values = [["d \u2192 horizontal_line_under_header_chr"],
             ["e \u2192 horizontal_line_chr"],
             ["f \u2192 left_vertical_header_line_chr"],
             ["g \u2192 right_vertical_header_line_chr"],
             ["h \u2192 left_corner_under_line_header_chr"],
             ["i \u2192 right_corner_under_line_header_chr"],
             ["j \u2192 left_lateral_corner_chr"],
             ["k \u2192 right_lateral_corner_chr"]]
   simple_msg.print_fancy_format(values,fp.Line_Style.NONE)

   message = f'''
  
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  f_data = fp.FancyFormat()
      {fp.ins_chr(10)}  f_data.horizontal_line_under_header_on = True
      {fp.ins_chr(10)}  f_data.horizontal_separator_line_on = True
      {fp.ins_chr(10)}  data = [["Header"],["Data 1"],["Data 2"],["Data 3"]]
      {fp.ins_chr(10)}  f_data.print_fancy_format(data)

   '''      
   print(message)

   print(f"{fp.ins_chr(100,"=")}")

   d3_lst = fp.FancyFormat()
   values = [["Header 1","Header 2","Header 3"],
             ["Data 1",  "Data 2",  "Data 3"  ],
             ["Data 4",  "Data 5",  "Data 6"  ],
             ["Data 7",  "Data 8"]]

   message = f'''
      {fp.set_font(1,14,0)} Matrix Data {fp.reset_font()}
   '''
   print(message)

   d3_lst.horizontal_line_under_header_on = True
   d3_lst.horizontal_separator_line_on = True
   
   d3_lst.middle_vertical_header_line_chr = "l"
   d3_lst.middle_corner_under_line_header_chr = "m"
   d3_lst.middle_inner_corner_chr = "n"

   d3_lst.print_fancy_format(values)

   crs.jumpTo(qty=9, direction=fp.Move.UP)
   d3_lst.adj_indent = 50
   d3_lst.print_fancy_format(values,fp.Line_Style.DASH)


   simple_msg.msg_title = " Description "
   values = [["l    \u2192 horizontal_line_under_header_chr"],
             ["m    \u2192 horizontal_line_chr"],
             ["n    \u2192 left_vertical_header_line_chr"],
             ["---- \u2192 set_fill_chr"]]

   simple_msg.print_fancy_format(values,fp.Line_Style.NONE)

   
   message = f'''
  
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  f_data = fp.FancyFormat()
      {fp.ins_chr(10)}  f_data.horizontal_line_under_header_on = True
      {fp.ins_chr(10)}  f_data.horizontal_separator_line_on = True
      {fp.ins_chr(10)}  values = [["Header 1","Header 2","Header 3"],
      {fp.ins_chr(10)}           ["Data 1",  "Data 2",  "Data 3"  ],
      {fp.ins_chr(10)}           ["Data 4",  "Data 5",  "Data 6"  ],
      {fp.ins_chr(10)}           ["Data 7",  "Data 8"]]
      {fp.ins_chr(10)}  f_data.print_fancy_format(data)

   '''      
   print(message)

   print(f"{fp.ins_chr(100,"=")}")   


def Diagram3():
   message = f'''
      {fp.set_font(1,14,0)} Matrix Data Diagram {fp.reset_font()}
   '''
   print(message)

   print("$")
   print("      \u2190 0")

   dt_lst = fp.FancyFormat()
   dt_lst.adj_top_space = 1; dt_lst.adj_bottom_space = 1
   dt_lst.adj_space = 0; dt_lst.adj_indent = 3
   dt_lst.msg_title = "Title \u2190 1"; dt_lst.msg_footnote = "Footnote \u2190 8"
   dt_lst.align_title = "center"; dt_lst.align_footnote = "right"
   dt_lst.set_fill_chr = "...------..."
   dt_lst.horizontal_separator_line_on = True
   dt_lst.horizontal_line_under_header_on = True
   
   # Single Data   
   dt_lst.top_left_corner_chr = "3"      # corners
   dt_lst.top_right_corner_chr = "4"
   dt_lst.bottom_right_corner_chr = "5"
   dt_lst.bottom_left_corner_chr = "6"
   dt_lst.left_vertical_line_chr = "L"   # left and right lines
   dt_lst.right_vertical_line_chr = "R"
   #d1_lst.top_horizontal_line_chr = "-"
   dt_lst.bottom_horizontal_line_chr = "*"
   
   # Multiple Horizontal Data
   dt_lst.middle_top_corner_chr = "a"
   dt_lst.middle_vertical_line_chr = "b"
   dt_lst.middle_bottom_corner_chr = "c"

   # Multiple Vertical Data
   dt_lst.horizontal_line_under_header_chr = "d"
   dt_lst.horizontal_line_chr = "e"
   dt_lst.left_vertical_header_line_chr = "f"
   dt_lst.right_vertical_header_line_chr = "g"
   dt_lst.left_corner_under_line_header_chr = "h"
   dt_lst.right_corner_under_line_header_chr = "i"
   dt_lst.left_lateral_corner_chr = "j"
   dt_lst.right_lateral_corner_chr = "k"

   # Matrix Data
   dt_lst.middle_vertical_header_line_chr = "l"
   dt_lst.middle_corner_under_line_header_chr = "m"
   dt_lst.middle_inner_corner_chr = "n"

   # Some color to visualize a little better
   dt_lst.bg_horizontal_line = 14
   dt_lst.bg_corner_chr = 21
   dt_lst.bg_inner_corner_chr = 90
   
   dt_lst.bg_corner_under_line_header = 3
   dt_lst.fg_corner_under_line_header = 231
   
   dt_lst.bg_under_line_header = 191
   dt_lst.fg_under_line_header = 0
 
   dt_lst.bg_vertical_header_line_chr = 15
   dt_lst.fg_vertical_header_line_chr = 0

   dt_lst.bg_vertical_line = 85
   dt_lst.fg_vertical_line = 0

   dt_lst.bg_data = 1
   dt_lst.fg_data = 231

   values = [["...Head 1...",  "...Head 2...",  "...Head 3..."],
             ["...Data 1...",  "...Data 2...",  "...Data 3..."  ],
             ["...Data 4...",  "...Data 5...",  "...Data 6..."  ],
             ["...Data 7...",  "...Data 8..."]]
   dt_lst.print_fancy_format(values)


   crs.jumpTo(qty=12, direction=fp.Move.UP)
   print("      \u2190 2")
   print(",,,")
   crs.jumpTo(qty=8, direction=fp.Move.DOWN)
   print("      \u2190 7")
   fp.ins_newline(1)
   print("      \u2190 9")



   values=[["0 \u2192 adj_top_margin",         " "],
           ["1 \u2192 msg_title",""            " "],
           ["2 \u2192 adj_top_space",          "-   \u2192 top_horizontal_line_chr"],
           ["3 \u2192 top_left_corner_chr",    "... \u2192 adj_space"],
           ["4 \u2192 top_right_corner_chr",   "*   \u2192 bottom_horizontal_line_chr"],
           ["5 \u2192 bottom_right_corner_chr",",,, \u2192 adj_indent"],
           ["6 \u2192 bottom_left_corner_chr", "L   \u2192 left_vertical_line_chr"],
           ["7 \u2192 adj_bottom_space",       "R   \u2192 right_vertical_line_chr"          ],
           ["8 \u2192 msg_footnote",           " "            ],
           ["9 \u2192 adj_bottom_margin",      " "            ],
           ["                          ",      " "            ],
           ["a \u2192 middle_top_corner_chr",  " "            ],
           ["b \u2192 middle_vertical_line_chr",  " "         ],
           ["c \u2192 middle_bottom_corner_chr",  " "         ],
           ["                                 ",  " "         ],
           ["d \u2192 horizontal_line_under_header_chr",   " "],
           ["e \u2192 horizontal_line_chr",                " "],
           ["f \u2192 left_vertical_header_line_chr",      " "],
           ["g \u2192 right_vertical_header_line_chr",     " "],
           ["h \u2192 left_corner_under_line_header_chr",  " "],
           ["i \u2192 right_corner_under_line_header_chr", " "],
           ["j \u2192 left_lateral_corner_chr",            " "],
           ["k \u2192 right_lateral_corner_chr",           " "],
           ["                                 ",           " "],
           ["l    \u2192 horizontal_line_under_header_chr"," "],
           ["m    \u2192 horizontal_line_chr",             " "],
           ["n    \u2192 left_vertical_header_line_chr",   " "],
           ["---- \u2192 set_fill_chr",                    " "]
           ]


   simple_msg.msg_title = " Full Description "
   simple_msg.print_fancy_format(values,fp.Line_Style.NONE)



def Print_Fancy_Format_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[1][3])
   print("\n print_fancy_format will print any type of variable into a fancy list style\n")

   # General Use Default Values
   simple_msg.msg_title = " General Use Default Values "
   default_values = [["adj_top_margin    = 0",     "set_fill_chr = \"----\""],
                     ["adj_bottom_margin = 0",     "set_layout   = Layout.HORIZONTAL"],
                     ["adj_top_space     = 0",     "update_list  = False"],
                     ["adj_bottom_space  = 0",     "                    "],
                     ["adj_indent        = 2",     "                    "],
                     ["adj_space         = 2",     "                    "]]
   simple_msg.print_fancy_format(default_values,fp.Line_Style.NONE)

   message = f'''
     {fp.set_font(True,-1,14)}adj_top_margin{fp.set_font(False)}
     lines to be add between the terminal and the title.

     {fp.set_font(True,-1,14)}adj_bottom_margin{fp.set_font(False)}
     lines to be add between the end of list or footnote and the terminal.
     
     {fp.set_font(True,-1,14)}adj_top_space{fp.set_font(False)}
     lines to be added between title and top list. This only work
     when title exist.
     
     {fp.set_font(True,-1,14)}adj_bottom_space{fp.set_font(False)}
     lines to be added between bottom list and footnote. This only work
     when a footnote exist.
     
     {fp.set_font(True,-1,14)}adj_indent{fp.set_font(False)}
     space from the terminal to the box.
     
     {fp.set_font(True,-1,14)}adj_space{fp.set_font(False)}
     space from vertical left line to the data and the space from the data to
     the vertical right line, inside the box.
     
     {fp.set_font(True,-1,14)}set_fill_chr{fp.set_font(False)}
     to fill the empty spots when the list is not complete. This only
     works when we are dealing with a table list.
     
     {fp.set_font(True,-1,14)}set_layout{fp.set_font(False)}
     This is only for Range, Set, and SetFrozen type data. It defines how
     to print the data, horizontal or vertical.
     
     {fp.set_font(True,-1,14)}update_list{fp.set_font(False)}
     if we want to save the data as it's presented, but in string type for 
     each element in list. This only work when the variable is a list type.
         
'''
   print(message)

   # Title Default Values
   default_values = [["msg_title   = \"\"",     "align_title     = \"justify\"",    "blinking_title  = False"],
                     ["bold_title  = False",    "italic_title    = False",          "dim_title       = False"],
                     ["bg_title    = -1",       "underline_title = False",          "hidden_title    = False"],
                     ["fg_title    = -1",       "strike_title    = False",          "inverse_title   = False"]]

   simple_msg.msg_title = " Title Default Values "
   simple_msg.print_fancy_format(default_values, fp.Line_Style.NONE)




   # Footnote Default Values
   default_values = [["msg_footnote   = \"\"",     "align_footnote     = \"justify\"",    "blinking_footnote  = False"],
                     ["bold_footnote  = False",    "italic_footnote    = False",          "dim_footnote       = False"],
                     ["bg_footnote    = -1",       "underline_footnote = False",          "hidden_footnote    = False"],
                     ["fg_footnote    = -1",       "strike_footnote    = False",          "inverse_footnote   = False"]]

   simple_msg.msg_title = " Footnote Default Values "
   simple_msg.print_fancy_format(default_values, fp.Line_Style.NONE)


   # Data Default Values
   default_values = [["bg_all_cell_data = True",     "align_data     = \"justify\"",    "blinking_data  = False"],
                     ["bold_data        = False",    "italic_data    = False",          "dim_data       = False"],
                     ["bg_data          = -1",       "underline_data = False",          "hidden_data    = False"],
                     ["fg_data          = -1",       "strike_data    = False",          "inverse_data   = False"]]

   simple_msg.msg_title = " Data Default Values "
   simple_msg.print_fancy_format(default_values, fp.Line_Style.NONE)

   message = f'''
     {fp.set_font(True,-1,14)}bg_all_cell_data{fp.set_font(False)}
     It defines how long will be the bg in the data (all the cell or only the data)
         
'''
   print(message)


   # Header Default Values
   default_values = [["bg_all_cell_header = True",     "align_header     = \"justify\"",    "blinking_header  = False"],
                     ["bold_header        = False",    "italic_header    = False",          "dim_header       = False"],
                     ["bg_header          = -1",       "underline_header = False",          "hidden_header    = False"],
                     ["fg_header          = -1",       "strike_header    = False",          "inverse_header   = False"]]

   simple_msg.msg_title = " Header Default Values "
   simple_msg.print_fancy_format(default_values, fp.Line_Style.NONE)

   message = f'''
     {fp.set_font(True,-1,14)}bg_all_cell_header{fp.set_font(False)}
     It defines how long will be the bg in the header (all the cell or only the header)
         
'''
   print(message)


# Horizontal Line Section
   default_values = ["  "]
   simple_msg.msg_title = " Horizontal Line Default Values "
   simple_msg.print_fancy_format(default_values, fp.Line_Style.NONE)

# Vertical Line Section
   simple_msg.msg_title = " Vertical Line Default Values "
   simple_msg.print_fancy_format(default_values, fp.Line_Style.NONE)

# Corner Section
   simple_msg.msg_title = " Corner Default Values "
   simple_msg.print_fancy_format(default_values, fp.Line_Style.NONE)

# Middle Corner Section
   simple_msg.msg_title = " Middle Corner Default Values "
   simple_msg.print_fancy_format(default_values, fp.Line_Style.NONE)

# Attributes for the header text
   simple_msg.msg_title = " Header Chr Default Values "
   simple_msg.print_fancy_format(default_values, fp.Line_Style.NONE)

# Under Line Header Section
   simple_msg.msg_title = " Under Line Header Default Values "
   simple_msg.print_fancy_format(default_values, fp.Line_Style.NONE)



def Reset_Fancy_Format_Method():
   green_msg.print_fancy_message(classes_methods_fancyprint[2][3])

   print("\n It will set all the variables in print_fancy_format method to their default values")
   message = f'''
  
      {fp.set_font(1,231,0)} Example: {fp.reset_font()}  import fancyprint as fp
      {fp.ins_chr(10)}  fmsg = fp.FancyFormat()      
      {fp.ins_chr(10)}  message = \"Data Text Here.....\"      
      {fp.ins_chr(10)}  fmsg.bg_data = 90
      {fp.ins_chr(10)}  fmsg.print_fancy_format(message)
      {fp.ins_chr(10)}  fmsg.reset_fancy_format()
      {fp.ins_chr(10)}  fmsg.print_fancy_mesage(message)

   '''      
   print(message)

   fmsg = fp.FancyFormat()
   message  = "Data Text Here......"
   fmsg.bg_data = 90
   fmsg.print_fancy_format(message)
   fmsg.reset_fancy_format()
   print("\n")
   fmsg.print_fancy_format(message)
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
flag_fancy_format = False;     flag_pen = False

if (len(cmdl_argv) == 1):
   Welcome_Message()

elif ("all" in cmdl_argv):  
   Screen_Functions()
   Internal_Functions()
   Help_Classes()
   Cursor_Class()
   FontStyle_Class()
   FancyMessage_Class()
   FancyFormat_Class()

   

else:
   blue_msg.bold_body = True
   blue_msg.italic_body = True
   for fun in cmdl_argv:
      if ("screen_functions" in fun):     Screen_Functions();    flag_screen_functions = True
      elif ("internal_functions" in fun): Internal_Functions();  flag_internal_functions = True
      elif ("help_classes" in fun):       Help_Classes();        flag_help_classes = True
      elif ("cursor" in fun):             Cursor_Class();        flag_cursor = True
      elif ("fontstyle" in fun):          FontStyle_Class();     flag_font_style = True
      elif ("fancymessage" in fun):       FancyMessage_Class();  flag_fancy_message = True
      elif ("fancyformat" in fun):        FancyFormat_Class();   flag_fancy_format = True

      elif ("clean" == fun and flag_screen_functions == False):           Clean_Function()
      elif ("clear" == fun and flag_screen_functions == False):           Clear_Function()
      elif ("erase" == fun and flag_screen_functions == False):           Erase_Function()
      elif ("dimensions" == fun and flag_screen_functions == False):      Dimensions_Function()
      elif ("resize" == fun and flag_screen_functions == False):          Resize_Function()
      

      elif ("ins_chr"     == fun and flag_internal_functions == False):  ins_chr_Function()
      elif ("ins_newline"   == fun and flag_internal_functions == False):  Ins_Newline_Function()
      elif ("terminal_bell" == fun and flag_internal_functions == False):  Terminal_Bell_Function()
      elif ("ansi_colors"   == fun and flag_internal_functions == False):  Ansi_Color_Function()


      elif ("move"       == fun and flag_help_classes == False):  Move_Class()
      elif ("align"      == fun and flag_help_classes == False):  Align_Class()
      elif ("layout"     == fun and flag_help_classes == False):  Layout_Class()
      elif ("length"     == fun and flag_help_classes == False):  Length_Class()
      elif ("unicode"    == fun and flag_help_classes == False):  Unicode_Class()
      elif ("style_line" == fun and flag_help_classes == False):  Style_Line_Class()

      
      elif ("jumpto" == fun and flag_cursor == False):                    JumpTo_Method()
      elif ("jumpxy" == fun and flag_cursor == False):                    Jumpxy_Method()
      elif ("moveto" == fun and flag_cursor == False):                    MoveTo_Method()
      elif ("movexy" == fun and flag_cursor == False):                    Movexy_Method()


      elif ("start_style" == fun and flag_font_style == False):           Start_Stop_Style_Method()
      elif ("stop_style"  == fun and flag_font_style == False):           Start_Stop_Style_Method()
      elif ("print_style" == fun and flag_font_style == False):           Print_Style_Method()
      elif ("reset_style" == fun and flag_font_style == False):           Reset_Style_Method()


      elif ("print_fancy_message" == fun  and flag_fancy_message == False):  Print_Fancy_Message_Method()
      elif ("print_fancy_note"    == fun  and flag_fancy_message == False):  Print_Fancy_Note_Method()

      
      elif ("print_fancy_format"  == fun  and flag_fancy_format  == False):  Print_Fancy_Format_Method()
      elif ("reset_fancy_format"  == fun  and flag_fancy_format  == False):  Reset_Fancy_Format_Method()


      else: pass
         

fp.ins_newline(3)
input("  Press Enter to Continue: ")
adj_screen(nrows, ncols)

# fp.clear()
# fp.clean()green_msg.print_fancy_message(screen_funs[5][0])