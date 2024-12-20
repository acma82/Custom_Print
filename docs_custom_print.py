#!/usr/bin/python3.12
'''
Documentation for fancyprint module...!
python3.12 cp_documentation.py
'''

import sys
import source.source.custom_print as cp

lst = cp.FancyFormat()

# Difining all the clases
blue_msg  = cp.FancyMessage()  # for titles

green_msg = cp.FancyMessage()  # for subtitles
green_msg.bg_body = 2
green_msg.fg_body = 0
green_msg.bold_body = True


purple_msg = cp.FancyMessage() # Messages
purple_msg.bg_body = 90
purple_msg.fg_body = 231


white_msg = cp.FancyMessage()  # Notes
white_msg.bg_body = 231
white_msg.fg_body = 21
white_msg.bold_note = True
white_msg.bold_body = True

msg = cp.FancyMessage()       # Note
msg.right_indent = 5

simple_msg = cp.FancyFormat() # Tables, default values
simple_msg.adj_top_margin = 1
simple_msg.align_title    = cp.Align.JUSTIFY
simple_msg.bg_title   = 231
simple_msg.fg_title   = 0
simple_msg.bold_title = True

red_msg = cp.FancyMessage()   # For wrong parameters
red_msg.bg_body = 1
red_msg.fg_body = 231
red_msg.bg_note = 1
red_msg.fg_note = 157
red_msg.italic_note = True
red_msg.bold_body = True
red_msg.bold_note = True

# Cursor Object
crs = cp.Cursor()


# FontStyle Object
fst = cp.FontStyle()
fst.bold = True
fst.fg   = 0
fst.bg   = 231
fst.indent = 2
fst.next_line = False


# Pen Object
pen = cp.Pen()
pen.bg_draw_line = 229
pen.fg_draw_line = 128
pen.bold_draw_line = True


#---------------------------------------------------------------------------------------------------
# Variables
ncols, nrows = cp.dimensions()

if (cp.OS_Linux == True and cp.OS_Windows == False):   myrows = 92;  mycols = 100
elif (cp.OS_Linux == False and cp.OS_Windows == True): myrows = 920; mycols = 100
else:                                                  pass


cp.resize(myrows, mycols)




screen_funs        = [[" Screen_Functions "], ["clean"], ["clear"], ["erase"], ["dimensions"], ["resize"]]

internal_functions = [[" Internal_Functions "],["ins_chr"], ["ins_newline"], ["ansi_colors"], ["terminal_bell"]]

help_classes       = [[" Help_Classes "],["Move"],["Align"],["Layout"],["Length"],["Unicode"],["Line_Style"]]

classes_methods_fancyprint = [["Cursor",  "FontStyle",    "FancyMessage",          "FancyFormat"        ,  "Pen"],
                              ["jumpTo",  "start_style",  "print_fancy_message",   "print_fancy_format",   "draw_line"],
                              ["jumpxy",  "stop_style",   "print_fancy_note",      "reset_fancy_format",   "draw_rectangle"],
                              ["moveTo",  "print_style",  "----             ",      "----             ",   "----"],
                              ["movexy",  "reset_style",  "----             ",      "----             ",   "----"]]

#----------------------------------------------------------------------------------------------------------------------------------------------
# W elcome Message Function for fancyprint Module                                                                                              -
#-- --------------------------------------------------------------------------------------------------------------------------------------------
def  Welcome_Message():
    welcome_msg = "Documentation For fancyprint Module....!"
    li = int(((mycols)-(len(welcome_msg)))/2)
    blue_msg.left_indent = li
    blue_msg.bold_body   = True
    blue_msg.italic_body = True
    blue_msg.print_fancy_message(welcome_msg)
    cp.ins_newline()

    lst.bg_all_cell_header = False
    lst.bold_header = True
    lst.bg_header   = 90; lst.fg_header = 231
    lst.italic_header = True

    lst.print_fancy_format(screen_funs)

    lst.adj_indent = 34
    crs.jumpTo(qty=8,direction=cp.Move.UP)
    lst.print_fancy_format(internal_functions)

    lst.adj_indent = 68
    crs.jumpTo(qty=7,direction=cp.Move.UP)
    lst.print_fancy_format(help_classes)
    lst.adj_indent = 2


    cp.ins_newline(3)


    blue_msg.length = cp.Length_bg.ONLY_WORD
    blue_msg.print_fancy_message("  Classes and Methods in fancyprint Module ")
    lst.msg_title      = " Clasess "
    lst.bg_title       = 90
    lst.fg_title       = 231
    lst.bold_title     = True
    lst.align_title    = cp.Align.LEFT
    lst.msg_footnote   = "Methods"
    lst.align_footnote = cp.Align.RIGHT
    lst.fg_footnote    = 11
    lst.fg_data        = 11
    lst.bg_all_cell_header = True
    lst.middle_horizontal_line_on = True

    lst.print_fancy_format(classes_methods_fancyprint,cp.Line_Style.SINGLE)
    cp.ins_newline(2)

    print("  To display help for a specific function or method, just pass the name as a parameter\n    when running this script.")
    cp.ins_newline(1)
    fst.print_style(" Example 1:")
    print(" python cp_documentation.py clean\n")   
    cp.ins_newline(1)

    note=" Note: "
    #                  20                  40                  60                  80   85   90
    message_note = '''
    It is possible to display help for more than one function or method at the same    
    time, it just needs to be specified. If it's preferred, it can display all the      
    methods for a specific class or a combination of them.

    '''
    blue_msg.length    = cp.Length_bg.ALL_ROW
    blue_msg.bold_body = False
    blue_msg.msg_note  = note
    blue_msg.position_note = 2
    blue_msg.bold_note     = True
    blue_msg.print_fancy_note(message_note)

    cp.ins_newline(1)
    fst.print_style(" Example 2: ")
    print(" python cp_documentation.py clean terminal_bell get_style Cursor")    
    cp.ins_newline(2)
    fst.print_style(" Example 3: ")
    print(" python cp_documentation.py help_classes")
    cp.ins_newline(2)

    message = '''     
    In example 2, notice that we are calling a mix of functions, methods and a class.
    For the class, it will call all the methods that this class contains as shown in the
    tables above. Cursor Class contains four methods: jump, move, gotoxy, and moveTo, and
    so on for the rest of the following classes.
 
    In example 3, we are calling help for all the functions that this class contains.
 
    It's possible to display the complete documentation by passing \"all\" as the parameter.
    '''
    blue_msg.left_indent = 2
    blue_msg.print_fancy_message(message)
    cp.ins_newline(2)
    blue_msg.length = cp.Length_bg.ONLY_WORD; 
    blue_msg.left_indent = li
    message = "  python cp_documentation.py all  "
    blue_msg.print_fancy_message(message)
 
    blue_msg.length       = cp.Length_bg.ALL_ROW   
    blue_msg.left_indent  = 2
    lst.msg_title         = ""
    lst.msg_footnote      = ""
    lst.fg_data           = -1
    lst.adj_indent        = 30
    lst.adj_top_margin    = 2
    lst.adj_bottom_margin = 2

    cp.ins_newline(2)
    message = '''
    fancyprint module has been tested on RedHat 9, Centos Stream 9, AlmaLinux 9, and Windows 10.

    fancymodule requires python3.12 or greater.

    https://github.com/acma82/Fancy_Print/

    '''

    blue_msg.bg_body   = 231
    blue_msg.fg_body   = 0
    blue_msg.bold_body = True
    blue_msg.print_fancy_message(message)
    lst.print_fancy_format("Bugs \u2192 acma.mex@hotmail.com", cp.Line_Style.DOUBLE)
 
 
#-- -------------------------------------------------------------------------------------------------
#   Screen_Functions in fancyprint Module                                                           -
#-- -------------------------------------------------------------------------------------------------
def Screen_Functions():   
    blue_msg.bold_body = True
    blue_msg.italic_body = True
    blue_msg.print_fancy_message("Screen Functions")
    Clean_Function()
    Clear_Function()
    Erase_Function()
    Dimensions_Function()
    Resize_Function()


def Clean_Function():
   #------------------------------------------------------------------------------------------------
   # clean, It uses ansi code                                                                      -
   #------------------------------------------------------------------------------------------------   
    message = '''
      It cleans the terminal and returns the cursor to home.
    '''
    green_msg.print_fancy_message(screen_funs[1][0]+"()")
    print(message)
    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp")
    print(f"{cp.ins_chr(18)}cp.clean()\n")


def Clear_Function():
   #------------------------------------------------------------------------------------------------
   # clear,       It uses the system command                                                       -
   #------------------------------------------------------------------------------------------------
    message = '''
      It clears the terminal and returns the cursor to home.
    '''
    green_msg.print_fancy_message(screen_funs[2][0]+"()")
    print(message)
    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp")
    print(f"{cp.ins_chr(18)}cp.clear()\n")


def Erase_Function():
   #------------------------------------------------------------------------------------------------
   # erase,       It uses ansi code                                                                -
   #------------------------------------------------------------------------------------------------
    menssage = '''
      It erases the terminal and leaves the cursor in the current position.
    '''
    green_msg.print_fancy_message(screen_funs[3][0]+"()")
    print(menssage)
    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp")
    print(f"{cp.ins_chr(18)}cp.erase()\n")

def Dimensions_Function():
   #------------------------------------------------------------------------------------------------
   # dimensions                                                                                    -
   #------------------------------------------------------------------------------------------------
    menssage ='''
      It returns the dimensions of the terminal, cols and rows.
     '''
    green_msg.print_fancy_message(screen_funs[4][0]+"()")
    print(menssage)
    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp")
    print(f"{cp.ins_chr(18)}ncols, nrows = cp.dimensions()\n")

def Resize_Function():
   #------------------------------------------------------------------------------------------------
   # resize                                                                                        -
   #------------------------------------------------------------------------------------------------
    message = '''
      It resizes the terminal size.
         '''
    green_msg.print_fancy_message(screen_funs[5][0]+"(rows=25, cols=80)")
    print(message)
    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp")
    print(f"{cp.ins_chr(18)}cp.resize(rows=20, cols=120)")
    cp.ins_newline(2)

#---------------------------------------------------------------------------------------------------
#  internal_functions in fancyprint Module                                                           -
#---------------------------------------------------------------------------------------------------
def Internal_Functions():   
    blue_msg.print_fancy_message("Internal Functions")
    Ins_Chr_Function()
    Ins_Newline_Function()
    Ansi_Color_Function()   
    Terminal_Bell_Function()
   

def Ins_Chr_Function():
   #------------------------------------------------------------------------------------------------
   # ins_chr                                                                                     -
   #------------------------------------------------------------------------------------------------
    green_msg.print_fancy_message("ins_chr(n=1, unicode=\" \")")
    message = f'''
      This function inserts n times the unicode provided, by default it is set to space.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp      
                  print("Hello"+cp.ins_chr(20)+"There")

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  Hello                    There

      '''
   
    print(message)


def Ins_Newline_Function():
   #------------------------------------------------------------------------------------------------
   # ins_newline                                                                                   -
   #------------------------------------------------------------------------------------------------
    green_msg.print_fancy_message(internal_functions[2][0]+"(n=1)")
    message = f'''
      This function inserts n new lines.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
                  print("Python 3.12")
                  cp.ins_newline(2)
                  print("is amazing...!")
              
      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  Python 3.12

               
                  is amazing...!
      '''
    print(message)
   

def Ansi_Color_Function():
   #------------------------------------------------------------------------------------------------
   # ansi_colors                                                                                -
    #------------------------------------------------------------------------------------------------
    green_msg.print_fancy_message(internal_functions[3][0]+": fancy_print contains functions that make use of ansi code.")
    print("\n  bg colors available in the ansi code \n")
 
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
        print (u"\u001b[0m")
    
    cp.ins_newline(2)
    print("  fg colors available in the ansi code \n")
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        print (u"\u001b[0m")
    
    print()
 
    purple_msg.print_fancy_message("bg_ansi_colors(bool=False, int=-1, int=0)")
    message = f''' 
       This function displays all background colors available with ansi code. 
       The following options are for a better visualization.
	    
       1.- The bold option for the font (True / False)
       2.- The fg option to visualize the background colors with a specific foreground color.
       3.- The n_line option to insert lines between the colors.
 
       
       {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
                   cp.bg_ansi_colors(bold=True, fg=22, n_line=1)
    '''
    print(message)
 
    purple_msg.print_fancy_message("fg_ansi_colors(bool=False, int=-1, int=0)")
    message = f'''
       This function displays all foreground colors available with ansi code. 
       The following options are for a better visualization.
 
       1.- The bold option for the font (True / False)
       2.- The bg option to visualize the background colors with a specific foreground color.
       3.- The n_line option to insert lines between the colors.
 
       
       {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
                   cp.fg_ansi_colors(bold=True, bg=22, n_line=1)
    '''
    print(message)
 
    purple_msg.print_fancy_message("set_font() and reset_font()")
 
    message =f'''
       reset_font() → This function resets the font attributes when we use the set_font() function.
 
       set_font()   → function changes the attributes of the font.
       
       
       Parameters with their default values:
       
       1) bold=False      4) italic=False         7) blinking=False      10) inverse=False
       2) bg=-1           5) underline=False      8) dim=False
       3) fg=-1           6) strike=False         9) hidden=False
       
      This function passes many attributes for the font. If passing all these arguments is a little
      annoying to you, you can use the FontStyle Class for simplicity.
 
      The best way to use this function is to pass only the first 3 parameters like the example.
 
       {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
                   print(cp.set_font(1,11,21) + " Python is " + cp.set_font(0,1) +
                         " Wonderful." + cp.reset_font())
 
''' 
    print(message)
    print(f"      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  {cp.set_font(1,11,21)} Python is {cp.set_font(0,1)} Wonderful. {cp.reset_font()}")
    print()
    message = '''Colors range goes from -1 to 256.
To  set the default color from the system use -1 or 256, for both bg and fg.
 
bli nking might not work in all the OS. We use Red Hat Family.
 
Not e: These functions are being used by the FancyFormat Class. Feel free to ignore them      if not useful to you.
'''   
    white_msg.print_fancy_note(message)
 


def Terminal_Bell_Function():
    #------------------------------------------------------------------------------------------------
   # terminal_bell                                                                                 -
   #------------------------------------------------------------------------------------------------
    message = f'''
      This function makes the sound of the terminal bell.               

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
                  cp.terminal_bell()
      '''
    green_msg.print_fancy_message(internal_functions[4][0]+"()")
    print(message)
    cp.terminal_bell()

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
    Line_Style_Class()


def Move_Class():
   #------------------------------------------------------------------------------------------------
   # Move                                                                                          -
   #------------------------------------------------------------------------------------------------
    green_msg.print_fancy_message(help_classes[1][0])
    message = f'''
      This class is used with the Cursor class and it contains 4 options.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp

      {cp.ins_chr(10)}  cp.Move.RIGHT
      {cp.ins_chr(10)}  cp.Move.LEFT
      {cp.ins_chr(10)}  cp.Move.UP
      {cp.ins_chr(10)}  cp.Move.DOWN
   
      Note: These options can be replaced for the original values as display below:

      {cp.ins_chr(10)}  cp.Move.RIGHT  \u2192  \"right\"  \u2192  \"r\"
      {cp.ins_chr(10)}  cp.Move.LEFT   \u2192  \"left\"   \u2192  \"l\"
      {cp.ins_chr(10)}  cp.Move.UP     \u2192  \"up\"     \u2192  \"u\"
      {cp.ins_chr(10)}  cp.Move.DOWN   \u2192  \"down\"   \u2192  \"d\"

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
      This class is used with the FancyFormat class and FancyMessage class. It contains 4 options.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp

      {cp.ins_chr(10)}  cp.Align.RIGHT
      {cp.ins_chr(10)}  cp.Align.LEFT
      {cp.ins_chr(10)}  cp.Align.CENTER
      {cp.ins_chr(10)}  cp.Align.JUSTIFY
      
      Note: These options can be replaced for the original values as display below:

      {cp.ins_chr(10)}  cp.Move.RIGHT    \u2192  \"right\"    \u2192  \"r\"
      {cp.ins_chr(10)}  cp.Move.LEFT     \u2192  \"left\"     \u2192  \"l"
      {cp.ins_chr(10)}  cp.Move.CENTER   \u2192  \"center\"   \u2192  \"c\"
      {cp.ins_chr(10)}  cp.Move.JUSTIFY  \u2192  \"justify\"  \u2192  \"j\"

'''   
    print(message)


def Layout_Class():
   #------------------------------------------------------------------------------------------------
   # Layout                                                                                        -
   #------------------------------------------------------------------------------------------------
   # works with FancyFormat, range, set, setfrozen obj.set_layout = cp.Layout.VERTICAL
   # works with Draw (line, arrow)
    green_msg.print_fancy_message(help_classes[3][0])
    message = f'''     
      This class is used with FancyFormat class and Pen class. It contains 2 options.
            
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp

      {cp.ins_chr(10)}  cp.Layout.HORIZONTAL
      {cp.ins_chr(10)}  cp.Layout.VERTICAL
      
      Note: These options can be replaced for the original values as display below:

      {cp.ins_chr(10)}  cp.Layout.HORIZONTAL   \u2192  \"horizontal\"
      {cp.ins_chr(10)}  cp.Layout.VERTICAL     \u2192  \"vertical\"

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

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp

      {cp.ins_chr(10)}  cp.Length.ALL_ROW
      {cp.ins_chr(10)}  cp.Length.ONLY_WORD
            
'''
    print(message)


def Unicode_Class():
   #------------------------------------------------------------------------------------------------
   # Unicode chrs                                                                                  -
   #------------------------------------------------------------------------------------------------     
    green_msg.print_fancy_message(help_classes[5][0])
    message = f'''
      This class is to insert some unicode characters.
      Unicode Class is used with the Pen Class.      

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp

      {cp.ins_chr(10)}  cp.Unicode.BLACK_DIAMOND
      {cp.ins_chr(10)}  cp.Unicode.WHITE_DIAMOND

      {cp.ins_chr(10)}  cp.Unicode.BLACK_CIRCLE 
      {cp.ins_chr(10)}  cp.Unicode.WHITE_CIRCLE 
      
      This class helps to set some unicode characters when using the Pen Class.

      For more reference {cp.Unicode.EM_DASH}{cp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE} https://www.unicode.org/charts/nameslist/

'''   
    print(message)


def Line_Style_Class():
   #------------------------------------------------------------------------------------------------
   # Style_Line                                                                                    -
   #------------------------------------------------------------------------------------------------
   # FancyFormat   
    green_msg.print_fancy_message(help_classes[6][0])
    message = f'''
      Style_Line Class is used with FancyFormat Class and Pen Class. There are 8 options.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp

      {cp.ins_chr(10)}  cp.Line_Style.CUSTOMIZED
      {cp.ins_chr(10)}  cp.Line_Style.SINGLE
      {cp.ins_chr(10)}  cp.Line_Style.SINGLE_BOLD
      {cp.ins_chr(10)}  cp.Line_Style.SINGLE_HEAVY
      {cp.ins_chr(10)}  cp.Line_Style.DOUBLE
      {cp.ins_chr(10)}  cp.Line_Style.DASH
      {cp.ins_chr(10)}  cp.Line_Style.SQR_BRACKETS
      {cp.ins_chr(10)}  cp.Line_Style.DOUBLE_SPACE
      {cp.ins_chr(10)}  cp.Line_Style.NONE_SPACE
      {cp.ins_chr(10)}  cp.Line_Style.NONE

      Note: These options can be replaced for the original values as display below:

      {cp.ins_chr(10)}  cp.Style_Line.CUSTOMIZED     \u2192  \"customized\"  
      {cp.ins_chr(10)}  cp.Style_Line.SINGLE         \u2192  \"single\"   
      {cp.ins_chr(10)}  cp.Style_Line.SINGLE_BOLD    \u2192  \"single_bold\" 
      {cp.ins_chr(10)}  cp.Style_Line.SINGLE_HEAVY   \u2192  \"single_heavy\"
      {cp.ins_chr(10)}  cp.Style_Line.DOUBLE         \u2192  \"double\"
      {cp.ins_chr(10)}  cp.Style_Line.DASH           \u2192  \"dash\"      
      {cp.ins_chr(10)}  cp.Style_Line.SQR_BRACKETS   \u2192  \"sq_brackets\"
      {cp.ins_chr(10)}  cp.Line_Style.DOUBLE_SPACE   \u2192  \"double_space\"
      {cp.ins_chr(10)}  cp.Line_Style.NONE_SPACE     \u2192  \"none_space\"
      {cp.ins_chr(10)}  cp.Line_Style.NONE           \u2192  \"none\"

      {cp.set_font(True,231,0)}   Note:  {cp.reset_font()}  Options{cp.set_font(True,-1,14)} DOUBLE_SPACE, NONE_SPACE, {cp.reset_font()} and {cp.set_font(True,-1,14)} NONE, {cp.reset_font()} use colors to visualize
                  the difference between them as shown in the example below.

      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  tbl = cp.FancyFormat()

      {cp.ins_chr(10)}  tbl.bg_header   = 23;              tbl.bg_data   = 231
      {cp.ins_chr(10)}  tbl.fg_header   = 231;             tbl.fg_data   = 21
      {cp.ins_chr(10)}  tbl.bold_header = True;            tbl.bold_data = True
    
      {cp.ins_chr(10)}  tbl.bg_horizontal_line  = 1;       tbl.bg_corner_under_line_header = 1
      {cp.ins_chr(10)}  tbl.bg_vertical_line    = 1;       tbl.bg_under_line_header        = 1
      {cp.ins_chr(10)}  tbl.bg_inner_corner_chr = 1;       tbl.bg_vertical_header_line_chr = 1
      {cp.ins_chr(10)}  tbl.bg_corner_chr       = 1;

      {cp.ins_chr(10)}  lst = [["Header 1", "Header 2", "Header 3", "Header 4"],
      {cp.ins_chr(10)}         ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
      {cp.ins_chr(10)}         ["Data 5",   "Data 6",   "Data 7",   "Data 8"  ]]

      {cp.ins_chr(10)}  tbl.print_fancy_format(data=lst, style=cp.Line_Style.NONE)
      {cp.ins_chr(10)}  tbl.print_fancy_format(data=lst, style=cp.Line_Style.DOUBLE_SPACE)
      {cp.ins_chr(10)}  tbl.print_fancy_format(data=lst, style=cp.Line_Style.NONE_SPACE)
           
   '''
    print(message)
    print()


#---------------------------------------------------------------------------------------------------
# Cursor Class                                                                                     -
#---------------------------------------------------------------------------------------------------
def Cursor_Class():
    blue_msg.print_fancy_message("Cursor Class")
    message = '''
      This class contains 4 methods. The difference between jump and move is that jump executes 
      the code while move returns the code.

      This methods only works with the actual size of the terminal, if you try to go beyond the
      size of the terminal, it may not work properly.
   '''
    print(message)
   
    JumpTo_Method()
    Jumpxy_Method()
    MoveTo_Method()
    Movexy_Method()  

   
def JumpTo_Method():
    green_msg.print_fancy_message(classes_methods_fancyprint[1][0]+"(qty=0, direction=cp.Move.DOWN)")
    message = f'''
   
      This method jumps rows or columns for the cursor in the terminal.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  crs = cp.Cursor()
      {cp.ins_chr(10)}  crs.jumpTo(qty=2,  direction = cp.Move.DOWN);        print("I am down")
      {cp.ins_chr(10)}  crs.jumpTo(qty=20, direction = "right");             print("I am right")
      {cp.ins_chr(10)}  crs.jumpTo(1, cp.Move.UP);                           print("I am up")
      {cp.ins_chr(10)}  crs.jumpTo(5, "down");                               print("GoodBye...!")

   '''
    print(message)

   

def Jumpxy_Method():
    green_msg.print_fancy_message(classes_methods_fancyprint[2][0]+"(x=0, y=0)")
    message = f'''
   
      This method jumps the cursor to specific coordinates in the terminal.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  crs = cp.Cursor()
      {cp.ins_chr(10)}  crs.jumpToxy(0,0);     print("*** Start Here ***")
      {cp.ins_chr(10)}  crs.jumpToxy(20, 5);   print("GoodBye...!")      

   '''
    print(message)


def MoveTo_Method():
    green_msg.print_fancy_message(classes_methods_fancyprint[3][0]+"(qty=0, direction=cp.Move.DOWN)")
    message = f'''
   
      This method moves rows or columns for the cursor in the terminal.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  crs = cp.Cursor()
      '''
   
    message2 = '''                  print(f"{crs.moveTo(15,"right")} First One",  end="")

                  print(f"{crs.moveTo(15,"right")} Second One", end="")
            
                  print(f"{crs.moveTo(qty=20,direction="left")} Hello")
   
   '''
    print(message)
    print(message2)



def Movexy_Method():
    green_msg.print_fancy_message(classes_methods_fancyprint[4][0]+"(x=0, y=0)")
    message = f'''
   
      This method moves the cursor to specific coordinates in the terminal.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  crs = cp.Cursor()
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
    message = '''
     This class contains 4 methods and the attributes and their default values are displays below.
'''
    print(message)

    default_values = [["bg     = 4",       "italic = False",        "blinking   = False"],
                     ["fg     = 231",     "strike = False",        "underline  = False"],
                     ["dim    = False",   "hidden = False",        "inverse    = False"],                     
                     ["bold   = False",   "indent = False",        "next_lines = True"]]
   
    lst.bg_header = -1; lst.fg_header = -1
    lst.print_fancy_format(default_values,cp.Line_Style.NONE)
    message = '''
      indent    → this defines how far we want to start to print the message from the left.
      next_line → this defines where we want to jump the line or not when printing the message.

'''
    print(message)
    Start_Stop_Style_Method()
    Print_Style_Method()
    Reset_Style_Method()
   


def Start_Stop_Style_Method():
    message = classes_methods_fancyprint[1][1] + "() and "+ classes_methods_fancyprint[2][1]+"()"
    green_msg.print_fancy_message(message)
    message = f'''
      These methods are used if we will be continuing using the style in many rows.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp'''
    print(message)
    print(cp.ins_chr(18)+"fs = cp.FontStyle()")
    print(cp.ins_chr(18)+"fs.bg = 21")
    print(cp.ins_chr(18)+"fs.fg = 231")
    print(cp.ins_chr(18)+"print(f\"{fs.start_style()} Font Style Line 1")
    print(cp.ins_chr(18)+"print(f\" Font Style Line 2")
    print(cp.ins_chr(18)+"print(f\" Font Style Line 3 {fs.stop_style()}")
    print(cp.ins_chr(18)+"fs.reset_style()")
    print(cp.ins_chr(18)+"f\"{fs.start_style()} Default Style {fs.stop_style()}")
    cp.ins_newline(2)


def Print_Style_Method():
    green_msg.print_fancy_message(classes_methods_fancyprint[3][1]+"(msg)")

    message = f'''
   
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  fs = cp.FontStyle
      {cp.ins_chr(10)}  fs.bg = 14
      {cp.ins_chr(10)}  fs.print_style(msg = " FontStyle Class ")
      {cp.ins_chr(10)}  print("  Normal Font...!")

   '''
    print(message)



def Reset_Style_Method():
    green_msg.print_fancy_message(classes_methods_fancyprint[4][1]+"()")
    message = f'''
   
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  fs = cp.FontStyle
      {cp.ins_chr(10)}  fs.bg = 14
      {cp.ins_chr(10)}  fs.print("  FontStyle Class ")
      {cp.ins_chr(10)}  fs.reset_style()
      {cp.ins_chr(10)}  fs.print("  Default Values ")

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
   
    simple_msg.print_fancy_format(default_values,cp.Line_Style.NONE)



def FancyMessage_Class():
    blue_msg.print_fancy_message("FancyMessage Class")



    print(f"\n     {cp.set_font(True,231,0)} Diagram Description {cp.reset_font()}\n")
    ex_msg = cp.FancyMessage()
    ex_msg.bg_body = 229;             ex_msg.bg_title = 229;            ex_msg.bg_footnote = 229
    ex_msg.fg_body = 0;               ex_msg.fg_title = 21;             ex_msg.fg_footnote = 21
    ex_msg.italic_body = True;        ex_msg.italic_footnote = True;    ex_msg.italic_title = True
    ex_msg.bold_body   = True;        ex_msg.bold_footnote = 1;         ex_msg.bold_title = True
    ex_msg.left_indent = 15;          ex_msg.right_indent = 15;         ex_msg.align_title = cp.Align.CENTER
    ex_msg.top_lines   = 3;           ex_msg.bottom_lines = 3;          ex_msg.align_footnote = cp.Align.CENTER
    ex_msg.lines_title_body = 3;      ex_msg.lines_body_footnote=3      
    ex_msg.msg_title ="TITLE";        ex_msg.msg_footnote = "FOOTNOTE"; ex_msg.help_lines = True


    ex_fst = cp.FontStyle()
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
   
    crs.jumpTo(qty=15, direction=cp.Move.UP)
    pen.draw_line(size=3, tail=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT, body=" left indent  ",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
    pen.draw_line(size=3, tail="\u2500", body=f"{cp.ins_chr(30,"\u2500")} msg_body {cp.ins_chr(27,"\u2500")}",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
    pen.draw_line(size=3, tail=" ", body="right indent ",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT)
    print()
    pen.adj_indent = 45
    crs.jumpTo(qty=7, direction=cp.Move.UP)
    crs.jumpTo(qty=45, direction=cp.Move.LEFT)
   
    pen.draw_line(size=4, layout=cp.Layout.VERTICAL, tail=cp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                 body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
    pen.draw_line(size=3, layout=cp.Layout.VERTICAL, tail=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL,\
                 body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=cp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL)
   
    print()
    crs.jumpTo(qty=6, direction=cp.Move.UP)
    pen.adj_indent = 29
    pen.draw_line(size=3, layout=cp.Layout.VERTICAL, tail="       top lines", body= " ", head="lines_title_body")


    crs.jumpTo(qty=8, direction=cp.Move.DOWN)
    pen.adj_indent = 55
    pen.draw_line(size=4, layout=cp.Layout.VERTICAL, tail=cp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                 body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
    pen.draw_line(size=3, layout=cp.Layout.VERTICAL, tail=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL,\
                 body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=cp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL)
   
    pen.adj_indent = 56
    crs.jumpTo(qty=6, direction=cp.Move.UP)
    pen.draw_line(size=3, layout=cp.Layout.VERTICAL, tail="lines_body_footnote", body= "\n\n", head="bottom lines") 
  
    crs.jumpTo(qty=2, direction=cp.Move.DOWN)
    pen.adj_indent = 0
    cp.ins_newline(3)
   
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
   

    ex_msg.print_fancy_note(message)

    crs.jumpTo(qty=10, direction=cp.Move.UP)

    pen.draw_line(size=3, tail=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT, body=" A ",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
    pen.draw_line(size=3, tail="", body="msg_note",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
    pen.draw_line(size=3, tail=" ", body="B ",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   

    pen.draw_line(size=3, tail="\u2500", body=f"{cp.ins_chr(30,"\u2500")} msg_body {cp.ins_chr(27,"\u2500")}",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)
   
    pen.draw_line(size=3, tail="", body="right indent",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT)
   
    print()
    crs.jumpTo(qty=3, direction=cp.Move.UP)
    pen.adj_indent = 35
    pen.draw_line(size=3, layout=cp.Layout.VERTICAL, tail=cp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                 body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=cp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL)
    crs.jumpTo(qty=2, direction=cp.Move.UP)
    print(f"{crs.moveTo(22,cp.Move.RIGHT)}top_lines --{cp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE}")
    crs.jumpTo(6,cp.Move.DOWN)


    pen.draw_line(size=3, layout=cp.Layout.VERTICAL, tail=cp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                 body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=cp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL)
    crs.jumpTo(qty=2, direction=cp.Move.UP)
    print(f"{crs.moveTo(19,cp.Move.RIGHT)}bottom_lines --{cp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE}")
   

    crs.jumpTo(qty=1, direction=cp.Move.UP)
    crs.jumpTo(qty=40, direction=cp.Move.RIGHT)
   #cp.ins_newline(2)
    print(f"A --{cp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE} left_space_note",end=",  ")
    print(f"B --{cp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE} right_space_note")

    crs.jumpTo(qty=4, direction=cp.Move.DOWN)

   # Indentation and Lines Default Values
    simple_msg.msg_title = " Default Indent and Line Values "
    default_values = [["top_lines    = 1", "length = Length_bg.ALL_ROW"],
                     ["bottom_lines = 1", "adj_bg_lines_to_right_indent  = False "],
                     ["right_indent = 2", "adj_bg_msg_to_space_available = False"]] 
   

    simple_msg.print_fancy_format(default_values,cp.Line_Style.NONE)
    
    _display_body_args()


    message = '''All the above variables are being used by both methods, print_fancy_message and
print_fancy_note.
'''
    white_msg.print_fancy_note(message)

    cp.ins_newline(1)

    message = f'''
     {cp.set_font(True,-1,14)}length{cp.set_font(False)}
         This is the width of the terminal and it has 2 options.

         ALL_ROW  :  It will do the background color to the complete row in the terminal
         ONLY_WORD:  It will do the background color to only the text ignoring the 
                        left_indent and right_indent
     
     {cp.set_font(True,-1,14)}adj_bg_lines_to_right_indent{cp.set_font(False)}
         This applies to the top_lines and bottom_lines

         True : This will do the background color to the space available (74)
         False: This will do the background color to the longest line in the msg_body

     {cp.set_font(True,-1,14)}adj_bg_msg_to_space_available{cp.set_font(False)}
         This applies to the lines of text in the msg_body

         True : This will do the background to the space available (74)
         False: This will do the background to the longest line in all the msg_body

'''
    print(message)

    message = '''adj_bg_lines_to_right_indent and adj_bg_msg_to_space_available only take action when

   length = Length_bg.ONLY_WORD
'''
    white_msg.print_fancy_note(message)

    message = '''
      paragraph = Guido van Rossum, a Dutch programmer, created Python in the late 1980s
                  as a hobby project. He started working on it in December 1989 at Cent-
                  rum Wiskunde & Informatica (CWI) in the Netherlands.
                  Python was first released on February 20, 1991. Python was named after
                  the 1970s BBC comedy sketch series Monty Python's Flying Circus.

      import fancyprint as cp
      msg = cp.FancyMessage()
      
      msg.msg_title = "TITLE"
      msg.msg_footnote = "FOOTNOTE"
      
      msg.print_fancy_message(paragraph)
      cp.ins_newline(2)
      
      msg.msg_note = "Python"
      ex_msg.position_note = 5
      msg.print_fancy_note(paragraph)

'''
    print(message)
    Print_Fancy_Message_Method()
    Print_Fancy_Note_Method()



def Print_Fancy_Message_Method():
    green_msg.print_fancy_message(classes_methods_fancyprint[1][2]+"(msg_body=\"\")")
    # Title Default Values
    simple_msg.msg_title = " Title Default Values "
    default_values = [["bg_title    = 4    ",     "italic_title  = False",      "blinking_title   = False"],
                     ["fg_title    = 231  ",     "strike_title  = False",      "underline_title  = False"],
                     ["dim_title   = False",     "hidden_title  = False",      "inverse_title    = False"],
                     ["bold_title  = False",     "                     ",      "                       "],
                     ["                   ",     "                     ",      "                       "],
                     ["msg_title   = \"\"",      "title_indent  = 2",          "align_title      = Align.LEFT"],
                     ["                 ",        "                ",          "lines_title_body = 1"]]

    simple_msg.print_fancy_format(default_values,cp.Line_Style.NONE)
   

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

    simple_msg.print_fancy_format(default_values,cp.Line_Style.NONE)
   
    message = f'''
   
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  fmsg = cp.FancyMessage()
      {cp.ins_chr(10)}  fmsg.title = \" Title \"
      {cp.ins_chr(10)}  fmsg.footnote = \" Footnote \"
      {cp.ins_chr(10)}  fmsg.help_lines = True      
      {cp.ins_chr(10)}  paragraph = " This is a short Paragraph.....!
      {cp.ins_chr(10)}  fmsg.print_fancy_mesage(paragraph)

   '''
    print(message)
    fmsg = cp.FancyMessage()
    fmsg.msg_title = " Title "
    fmsg.msg_footnote = "Footnote"
    #fmsg.align_footnote = cp.Align.CENTER
    paragraph = " This is a short paragraph.....!"
    fmsg.help_lines = True
    fmsg.print_fancy_message(paragraph)
   
    cp.ins_newline(2)
    message = '''footnote_indent works with align_footnote. When the align_footnote is set to
Align.Justify, then footnote_indent controls the position of the msg_footnote.

The same situation applies for title_indent and align_title.
'''
    white_msg.print_fancy_note(message)

   

def Print_Fancy_Note_Method():
    green_msg.print_fancy_message(classes_methods_fancyprint[2][2]+"(msg_body=\"\")")
    # Note Default Values
    default_values = [["bg_note   = 231",            "italic_note   = False",    "blinking_note  = False"],
                     ["fg_note   = 0",              "strike_note   = False",    "underline_note = False"],
                     ["dim_note  = False",          "hidden_note   = False",    "inverse_note   = False"],
                     ["bold_note = False",           "                     ",    "                     "],
                     ["                 ",          "                     ",    "                      "],
                     ["msg_note  = \" Note: \"",    "position_note    = 1",     "                      "],
                     ["left_space_note = 2    ",    "right_space_note = 2",     "align_note = Align.JUSTIFY"]]
    simple_msg.msg_title = " Note Default Values "
    simple_msg.print_fancy_format(default_values,cp.Line_Style.NONE)
   
    # Body Default Values
    _display_body_args()
   
    message = f'''
  
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  fmsg = cp.FancyMessage()      
      {cp.ins_chr(10)}  fmsg.bold_note = True
      {cp.ins_chr(10)}  fmsg.bg_body = 90      
      {cp.ins_chr(10)}  message = \"There are variables that are being used by both methods.....\"
      {cp.ins_chr(10)}  fmsg.print_fancy_mesage(paragraph)

   '''   

    print(message)
    message = '''There are variables that are being used by both methods, print_fancy_message
and print_fancy_note.
'''
    fmsg = cp.FancyMessage()
    fmsg.bold_note = True
    fmsg.bg_body = 90

    fmsg.help_lines = True
    fmsg.print_fancy_note(message)
    cp.ins_newline(2)

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
      {cp.set_font(1,14,0)} Single Data/Figure 1 {cp.reset_font()}        
   '''
    print(message)
   
    d1_lst = cp.FancyFormat()
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
    d1_lst.bottom_horizontal_line_chr = "*"



    d1_lst.print_fancy_format(data)

    crs.jumpTo(qty=6, direction=cp.Move.UP)
    print("      \u2190 2")
    crs.jumpTo(qty=3, direction=cp.Move.DOWN)
    print("      \u2190 7")
    cp.ins_newline(1)
    print("      \u2190 9")

   
    crs.jumpTo(qty=8, direction=cp.Move.UP)
    d1_lst.adj_indent = 50
    data = "   Data Inside The Box   "
    d1_lst.msg_title    = "Title"
    d1_lst.msg_footnote = "Footnote"   
    d1_lst.print_fancy_format(data,cp.Line_Style.DASH)
   
    crs.jumpTo(qty=5, direction=cp.Move.UP)
    print(",,,")
    crs.jumpTo(qty=5, direction=cp.Move.DOWN)
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
    simple_msg.print_fancy_format(values,cp.Line_Style.NONE)


    message = f'''
  
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  f_data = cp.FancyFormat()
      {cp.ins_chr(10)}  f_data.msg_title        = \"Title\"
      {cp.ins_chr(10)}  f_data.msg_footnote     = \"footnote\"
      {cp.ins_chr(10)}  f_data.adj_top_space    = 1
      {cp.ins_chr(10)}  f_data.adj_bottom_space = 1
      {cp.ins_chr(10)}  f_data.adj_indent       = 3
      {cp.ins_chr(10)}  data = \"Data Inside The Box\"      
      {cp.ins_chr(10)}  f_data.print_fancy_format(data)

   '''      
    print(message)
   
    print(f"{cp.ins_chr(100,"=")}")
    print()
   
def Diagram2():
    d2_lst = cp.FancyFormat()
    values = [["Data 1","Data 2","Data 3"]]
    message = f'''
      {cp.set_font(1,14,0)} Multiple Horizontal Data/Figure 2 {cp.reset_font()}        
   '''
    print(message)
    d2_lst.middle_top_corner_chr = "!"
    d2_lst.middle_vertical_line_chr = "|"
    d2_lst.middle_bottom_corner_chr = "?"
    d2_lst.print_fancy_format(values)
   
    crs.jumpTo(qty=3, direction=cp.Move.UP)
    d2_lst.adj_indent = 50
    d2_lst.print_fancy_format(values,cp.Line_Style.DASH)

    simple_msg.msg_title = " Description "
    values = [["! \u2192 middle_top_corner_chr"],
             ["| \u2192 middle_vertical_line_chr"],
             ["? \u2192 middle_bottom_corner_chr"]]

    simple_msg.print_fancy_format(values,cp.Line_Style.NONE)

    message = f'''
  
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  f_data = cp.FancyFormat()
      {cp.ins_chr(10)}  data = [["Data 1","Data 2","Data 3"]]
      {cp.ins_chr(10)}  f_data.print_fancy_format(data)

   '''      
    print(message)
    print(f"{cp.ins_chr(100,"=")}")

    values = [["Header"],["Data 1"],["Data 2"],["Data 3"]]
    message = f'''
      {cp.set_font(1,14,0)} Multiple Vertical Data/Figure 3 {cp.reset_font()}        
   '''
    print(message)
    d2_lst.adj_indent = 2
    d2_lst.horizontal_line_under_header_on = True
    d2_lst.middle_horizontal_line_on = True

    d2_lst.horizontal_line_under_header_chr = "\u2022"
    d2_lst.middle_horizontal_line_chr = "="
   
    d2_lst.left_vertical_header_line_chr = "l"
    d2_lst.right_vertical_header_line_chr = "r"

    d2_lst.left_corner_line_under_header_chr = "A"
    d2_lst.right_corner_line_under_header_chr = "B"

    d2_lst.left_lateral_corner_chr = "C"
    d2_lst.right_lateral_corner_chr = "E"

    d2_lst.print_fancy_format(values)


    crs.jumpTo(qty=9, direction=cp.Move.UP)
    d2_lst.adj_indent = 50
    d2_lst.print_fancy_format(values,cp.Line_Style.DASH)

    simple_msg.msg_title = " Description "
    values = [["\u2022 \u2192 horizontal_line_under_header_chr"],
              ["= \u2192 middle_horizontal_line_chr"],
              ["l \u2192 left_vertical_header_line_chr"],
              ["r \u2192 right_vertical_header_line_chr"],
              ["A \u2192 left_corner_line_under_header_chr"],
              ["B \u2192 right_corner_line_under_header_chr"],
              ["C \u2192 left_lateral_corner_chr"],
              ["E \u2192 right_lateral_corner_chr"]]
    simple_msg.print_fancy_format(values,cp.Line_Style.NONE)

    message = f'''
  
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  f_data = cp.FancyFormat()
      {cp.ins_chr(10)}  f_data.horizontal_line_under_header_on = True
      {cp.ins_chr(10)}  f_data.middle_horizontal_line_on = True
      {cp.ins_chr(10)}  data = [["Header"],["Data 1"],["Data 2"],["Data 3"]]
      {cp.ins_chr(10)}  f_data.print_fancy_format(data)

   '''      
    print(message)

    print(f"{cp.ins_chr(100,"=")}")

    d3_lst = cp.FancyFormat()
    values = [["Header 1","Header 2","Header 3"],
             ["Data 1",  "Data 2",  "Data 3"  ],
             ["Data 4",  "Data 5",  "Data 6"  ],
             ["Data 7",  "Data 8"]]

    message = f'''
      {cp.set_font(1,14,0)} Matrix Data/Figure 4 {cp.reset_font()}
   '''
    print(message)

    d3_lst.horizontal_line_under_header_on = True
    d3_lst.middle_horizontal_line_on = True
   
    d3_lst.middle_vertical_header_line_chr = "M"
    d3_lst.middle_corner_line_under_header_chr = "m"
    d3_lst.middle_inner_corner_chr = "D"
    
    d3_lst.set_fill_chr = "////"
    
    d3_lst.print_fancy_format(values)

    crs.jumpTo(qty=9, direction=cp.Move.UP)
    d3_lst.adj_indent = 50
    d3_lst.print_fancy_format(values,cp.Line_Style.DASH)


    simple_msg.msg_title = " Description "
    values = [["M    \u2192 middle_vertical_header_line_chr"],
              ["m    \u2192 middle_corner_line_under_header_chr"],
              ["D    \u2192 middle_inner_corner_chr"],
              ["|    \u2192 middle_vertical_line_chr"],
              ["//// \u2192 set_fill_chr"]]

    simple_msg.print_fancy_format(values,cp.Line_Style.NONE)

   
    message = f'''
  
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  f_data = cp.FancyFormat()
      {cp.ins_chr(10)}  f_data.horizontal_line_under_header_on = True
      {cp.ins_chr(10)}  f_data.middle_horizontal_line_on = True
      {cp.ins_chr(10)}  values = [["Header 1","Header 2","Header 3"],
      {cp.ins_chr(10)}           ["Data 1",  "Data 2",  "Data 3"  ],
      {cp.ins_chr(10)}           ["Data 4",  "Data 5",  "Data 6"  ],
      {cp.ins_chr(10)}           ["Data 7",  "Data 8"]]
      {cp.ins_chr(10)}  f_data.print_fancy_format(data)

   '''      
    print(message)

    print(f"{cp.ins_chr(100,"=")}")   


def Diagram3():
    message = f'''
      {cp.set_font(1,14,0)} Full Matrix Data Diagram/Figure 5 {cp.reset_font()}
   '''
    print(message)

    print("$")
    print("      \u2190 0")

    dt_lst = cp.FancyFormat()
    dt_lst.adj_top_space = 1;              dt_lst.adj_bottom_space = 1
    dt_lst.adj_space     = 0;              dt_lst.adj_indent       = 3

    dt_lst.msg_title   = " Title \u2190 1 "; dt_lst.msg_footnote = " Footnote \u2190 8 "
    dt_lst.align_title = "center";         dt_lst.align_footnote = "right"
    dt_lst.bg_title    = 6;                dt_lst.bg_footnote    = 55
    dt_lst.fg_title    = 0;                dt_lst.fg_footnote    = 231
    dt_lst.bold_title  = True;             dt_lst.bold_footnote  = True
    dt_lst.set_fill_chr = "...//////..."
    dt_lst.middle_horizontal_line_on = True
    dt_lst.horizontal_line_under_header_on = True

    # Single Data   
    dt_lst.top_left_corner_chr = " 3 "      # corners
    dt_lst.top_right_corner_chr = " 4 "
    dt_lst.bottom_right_corner_chr = " 5 "
    dt_lst.bottom_left_corner_chr  = " 6 "
    dt_lst.left_vertical_line_chr  = " L "   # left and right lines
    dt_lst.right_vertical_line_chr = " R "
    #dt_lst.top_horizontal_line_chr ="."
    dt_lst.bottom_horizontal_line_chr = "*"

    # Multiple Horizontal Data
    dt_lst.middle_top_corner_chr = " ! "
    dt_lst.middle_vertical_line_chr = " | "
    dt_lst.middle_bottom_corner_chr = " ? "

    # Multiple Vertical Data
    dt_lst.horizontal_line_under_header_chr = "\u2022"
    dt_lst.middle_horizontal_line_chr = "="
    dt_lst.left_vertical_header_line_chr = " l "
    dt_lst.right_vertical_header_line_chr = " r "
    dt_lst.left_corner_line_under_header_chr = " A "
    dt_lst.right_corner_line_under_header_chr = " B "

    dt_lst.left_lateral_corner_chr = " C "
    dt_lst.right_lateral_corner_chr = " E "

    # Matrix Data
    dt_lst.middle_vertical_header_line_chr = " M "
    dt_lst.middle_corner_line_under_header_chr = " m "
    dt_lst.middle_inner_corner_chr = " D "

    # Some color to visualize a little better
    dt_lst.bg_horizontal_line = 21
 
    
    dt_lst.bg_corner_chr = 1
    dt_lst.fg_corner_chr = 231
    dt_lst.bold_corner_chr = True

    dt_lst.bg_inner_corner_chr = 52
    dt_lst.fg_inner_corner_chr = 231
    dt_lst.bold_inner_corner_chr = True


    dt_lst.bg_corner_under_line_header = 90
    dt_lst.fg_corner_under_line_header = 231
    dt_lst.bold_corner_under_line_header = True

    dt_lst.bg_under_line_header = 23
    dt_lst.fg_under_line_header = 231
    dt_lst.bold_under_line_header = True

    dt_lst.bg_vertical_header_line_chr = 15
    dt_lst.fg_vertical_header_line_chr = 0
    dt_lst.bold_vertical_header_line_chr = True

    dt_lst.bg_vertical_line = 191
    dt_lst.fg_vertical_line = 0
    dt_lst.bold_vertical_line = True
    
    dt_lst.bg_header = 206
    dt_lst.fg_header = 0
    dt_lst.bold_header = True

    dt_lst.bg_data = 7
    dt_lst.fg_data = 4
    dt_lst.bold_data = True



    values = [["...Head 1...",  "...Head 2...",  "...Head 3...",     "...Head 4..."  ],
              ["...Data 1...",  "...Data 2...",  "...Data 3...",     "...Data 4..."  ],
              ["...Data 5...",  "...Data 6...",  "...Data 7...",     "...Data 8..."  ],
              ["...Data 9...",  "...Data A..."]]
    dt_lst.print_fancy_format(values)


    crs.jumpTo(qty=12, direction=cp.Move.UP)
    print("      \u2190 2")
    print(",,,")
    crs.jumpTo(qty=8, direction=cp.Move.DOWN)
    print("      \u2190 7")
    cp.ins_newline(1)
    print("      \u2190 9")



    values=[["0 \u2192 adj_top_margin",         " "],
           ["1 \u2192 msg_title",""            " "],
           ["2 \u2192 adj_top_space",          "--- \u2192 top_horizontal_line_chr"],
           ["3 \u2192 top_left_corner_chr",    "... \u2192 adj_space"],
           ["4 \u2192 top_right_corner_chr",   "*   \u2192 bottom_horizontal_line_chr"],
           ["5 \u2192 bottom_right_corner_chr",",,, \u2192 adj_indent"],
           ["6 \u2192 bottom_left_corner_chr", "L   \u2192 left_vertical_line_chr"],
           ["7 \u2192 adj_bottom_space",       "R   \u2192 right_vertical_line_chr"          ],
           ["8 \u2192 msg_footnote",                         " "],
           ["9 \u2192 adj_bottom_margin",                    " "],
           ["                          ",                    " "],
           ["! \u2192 middle_top_corner_chr",                " "],
           ["| \u2192 middle_vertical_line_chr",             " "],
           ["? \u2192 middle_bottom_corner_chr",             " "],
           ["                                 ",             " "],
           ["\u2022 \u2192 horizontal_line_under_header_chr"," "],
           ["= \u2192 middle_horizontal_line_chr",           " "],
           ["                          ",                    " "],
           ["l \u2192 left_vertical_header_line_chr",        " "],
           ["r \u2192 right_vertical_header_line_chr",       " "],
           ["                          ",                    " "],
           ["A \u2192 left_corner_line_under_header_chr",    " "],
           ["B \u2192 right_corner_line_under_header_chr",   " "],
           ["                          ",                    " "],
           ["C \u2192 left_lateral_corner_chr",              " "],
           ["E \u2192 right_lateral_corner_chr",             " "],
           ["                                 ",             " "],
           ["M \u2192 middle_vertical_header_line_chr",      " "],
           ["m \u2192 middle_corner_line_under_header_chr",  " "],
           ["D \u2192 middle_inner_corner_chr",              " "],
           ["                          ",                    " "],
           ["//// \u2192 set_fill_chr",                      " "]
           ]


    simple_msg.msg_title = " Full Description "
    simple_msg.print_fancy_format(values,cp.Line_Style.NONE)

    message = f'''
     {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)} tlb = cp.FancyFormat()
      
      {cp.ins_chr(10)} lst = [["Header 1","Header 2","Header 3","Header 4"],
      {cp.ins_chr(10)} ["R2C1","R2C2","R2C3","R2C4"],
      {cp.ins_chr(10)} ["R3C1","R3C2","R3C3","R3C4"],
      {cp.ins_chr(10)} ["R4C1","R4C2"]]
      
      {cp.ins_chr(10)} tlb.msg_title	= " Title "
      {cp.ins_chr(10)} tlb.align_title	= cp.Align.CENTER
      {cp.ins_chr(10)} tlb.bold_title	= True
      {cp.ins_chr(10)} tlb.fg_title		= 21
      {cp.ins_chr(10)} tlb.bg_title	= 231
      
      {cp.ins_chr(10)} tlb.bg_header	= 90
      {cp.ins_chr(10)} tlb.fg_header	= 231
      {cp.ins_chr(10)} tlb.horizontal_line_under_header_on = True
      
      {cp.ins_chr(10)} tlb.align_data	= cp.Align.CENTER
      {cp.ins_chr(10)} tlb.fg_data		= 14
      
      {cp.ins_chr(10)} tlb.msg_footnote	= " Footnote "
      {cp.ins_chr(10)} tlb.align_footnote	= cp.Align.RIGHT
      {cp.ins_chr(10)} tlb.bold_footnote	= True
      {cp.ins_chr(10)} tlb.bg_footnote	= 231
      {cp.ins_chr(10)} tlb.fg_footnote	= 21
      
      {cp.ins_chr(10)} tlb.print_fancy_format(lst)
      {cp.ins_chr(10)} lst = [["Header"],["R2C1"],["R3C1"],["R4C1"]]
      {cp.ins_chr(10)} tlb.print_fancy_format(lst, cp.Line_Style.SINGLE)
'''
   
    print(message)
    print(f"       {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}")
    lst = [["Header 1","Header 2","Header 3","Header 4"],
          ["R2C1","R2C2","R2C3","R2C4"],
          ["R3C1","R3C2","R3C3","R3C4"],
          ["R4C1","R4C2"]]
    tlb = cp.FancyFormat()

    tlb.msg_title	= " Title "
    tlb.align_title	= cp.Align.CENTER
    tlb.bold_title	= True
    tlb.fg_title		= 21
    tlb.bg_title	= 231

    tlb.bg_header	= 90
    tlb.fg_header	= 231
    tlb.horizontal_line_under_header_on = True

    tlb.align_data	= cp.Align.CENTER
    tlb.fg_data		= 14

    tlb.msg_footnote	= " Footnote "
    tlb.align_footnote	= cp.Align.RIGHT
    tlb.bold_footnote	= True
    tlb.bg_footnote	= 231
    tlb.fg_footnote	= 21

    tlb.print_fancy_format(lst)

    lst = [["Header"],["R2C1"],["R3C1"],["R4C1"]]

    tlb.print_fancy_format(lst, cp.Line_Style.SINGLE)
    cp.ins_newline(2)




def Print_Fancy_Format_Method():
    green_msg.print_fancy_message(classes_methods_fancyprint[1][3])
    print("\n     print_fancy_format will print any type of variable into a fancy list style\n")

    # General Use Default Values
    simple_msg.msg_title = " General Use Default Values "
    default_values = [["adj_top_margin    = 0",     "set_fill_chr = \"----\""],
                     ["adj_bottom_margin = 0",     "set_layout   = Layout.HORIZONTAL"],
                     ["adj_top_space     = 0",     "update_list  = False"],
                     ["adj_bottom_space  = 0",     "                    "],
                     ["adj_indent        = 2",     "                    "],
                     ["adj_space         = 2",     "                    "]]
    simple_msg.print_fancy_format(default_values,cp.Line_Style.NONE)

    message = f'''
     {cp.set_font(False,-1,14)}adj_top_margin{cp.set_font()}
     lines to be add between the terminal and the title.

     {cp.set_font(False,-1,14)}adj_bottom_margin{cp.set_font()}
     lines to be add between the end of list or footnote and the terminal.
     
     {cp.set_font(False,-1,14)}adj_top_space{cp.set_font()}
     lines to be added between title and top list. This only work
     when title exist.
     
     {cp.set_font(False,-1,14)}adj_bottom_space{cp.set_font()}
     lines to be added between bottom list and footnote. This only work
     when a footnote exist.
     
     {cp.set_font(False,-1,14)}adj_indent{cp.set_font()}
     space from the terminal to the box.
     
     {cp.set_font(False,-1,14)}adj_space{cp.set_font()}
     space from vertical left line to the data and the space from the data to
     the vertical right line, inside the box.
     
     {cp.set_font(False,-1,14)}set_fill_chr{cp.set_font()}
     to fill the empty spots when the list is not complete. This only
     works when we are dealing with a table list.
     
     {cp.set_font(False,-1,14)}set_layout{cp.set_font()}
     This is only for Range, Set, and SetFrozen type data. It defines how
     to print the data, horizontal or vertical.
     
     {cp.set_font(False,-1,14)}update_list{cp.set_font()}
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
    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)




    # Footnote Default Values
    default_values = [["msg_footnote   = \"\"",     "align_footnote     = \"justify\"",    "blinking_footnote  = False"],
                     ["bold_footnote  = False",    "italic_footnote    = False",          "dim_footnote       = False"],
                     ["bg_footnote    = -1",       "underline_footnote = False",          "hidden_footnote    = False"],
                     ["fg_footnote    = -1",       "strike_footnote    = False",          "inverse_footnote   = False"]]

    simple_msg.msg_title = " Footnote Default Values "
    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)


    # Data Default Values
    default_values = [["bg_all_cell_data = True",     "align_data     = \"justify\"",    "blinking_data  = False"],
                     ["bold_data        = False",    "italic_data    = False",          "dim_data       = False"],
                     ["bg_data          = -1",       "underline_data = False",          "hidden_data    = False"],
                     ["fg_data          = -1",       "strike_data    = False",          "inverse_data   = False"]]

    simple_msg.msg_title = " Data Default Values "
    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)

    message = f'''
     {cp.set_font(False,-1,14)}bg_all_cell_data{cp.set_font()}
     It defines how long will be the bg in the data (all the cell or only the data)
         
'''
    print(message)


    # Header Default Values
    simple_msg.msg_title = " Header Default Values "
    default_values = [["bg_all_cell_header = True",     "align_header     = \"justify\"",    "blinking_header  = False"],
                     ["bold_header        = False",    "italic_header    = False",          "dim_header       = False"],
                     ["bg_header          = -1",       "underline_header = False",          "hidden_header    = False"],
                     ["fg_header          = -1",       "strike_header    = False",          "inverse_header   = False"]]
    message = f'''
     {cp.set_font(False,-1,14)}bg_all_cell_header{cp.set_font()}
     It defines how long will be the bg in the header (all the cell or only the header)
         
'''
    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)
    print(message)


    # Horizontal Line Section
    simple_msg.msg_title = " Horizontal Line Default Values "   
    default_values = [["top_horizontal_line_chr    = \"-\"" ,  "top_horizontal_line_on = True"    ],
                     ["middle_horizontal_line_chr = \"-\"" ,  "middle_horizontal_line_on = False"],
                     ["bottom_horizontal_line_chr = \"-\"" ,  "bottom_horizontal_line_on = True" ],
                     ["                                  " ,  "                                " ],
                     ["bold_horizontal_line = False"       ,  "bg_horizontal_line = -1"          ],
                     ["fg_horizontal_line = -1"            ,  "                       "          ]]
   
   
    message = f'''
     {cp.set_font(False,-1,14)} top_horizontal_line_on {cp.set_font()}   controls \u2192  -
     {cp.set_font(False,-1,14)} middle_horizontal_line_on {cp.set_font()}controls \u2192  e
     {cp.set_font(False,-1,14)} bottom_horizontal_line_on {cp.set_font()}controls \u2192  *

     {cp.set_font(False,1,231)} Refer to Figure 5 {cp.set_font()}
'''
    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)
    print(message)
   
      
   
    # Vertical Line Section
    simple_msg.msg_title = " Vertical Line Default Values"
    default_values = [["left_vertical_line_chr   = \"|\" ",  "bold_vertical_line = False"],
                     ["middle_vertical_line_chr = \"|\" ",  "bg_vertical_line = -1"     ],
                     ["right_vertical_line_chr  = \"|\" ",  "fg_vertical_line = -1"     ]]
   
    message = f'''     {cp.set_font(False,1,231)} Refer to Figure 1 {cp.set_font()}
'''
   
    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)
    print(message)

    # Corner Section
    simple_msg.msg_title = " Corner Default Values "
    default_values = [["top_left_corner_chr     = \"+\"  ",  "bold_corner_chr = False"],
                     ["top_right_corner_chr    = \"+\"  ",  "bg_corner_chr = -1 "    ],
                     ["bottom_right_corner_chr = \"+\"  ",  "fg_corner_chr = -1 "    ],
                     ["bottom_left_corner_chr  = \"+\"  ",  "                   "    ]]
      
   
    message = f'''     {cp.set_font(False,1,231)} Refer to Figure 1 {cp.set_font()}
'''
    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)
    print(message)

    # Middle Corner Section
    simple_msg.msg_title = " Middle Corner Default Values "
    default_values = [["middle_top_corner_chr    = \"+\" ",  "bold_inner_corner_chr = False"],
                     ["middle_inner_corner_chr  = \"+\" ",  "bg_inner_corner_chr   = -1"   ],
                     ["middle_bottom_corner_chr = \"+\" ",  "fg_inner_corner_chr   = -1"   ],
                     ["left_lateral_corner_chr  = \"+\" ",  "   "                          ],
                     ["right_lateral_corner_chr = \"+\" ",  "   "                          ]]
   
    message = f'''     {cp.set_font(False,1,231)} Refer to Figure 5 {cp.set_font()}
'''
   
    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)
    print(message)


    # Header Vertical Lines for the Header Section
    simple_msg.msg_title = " Vertical Header Lines Default Values "
    # Data Default Values
    default_values =[["left_vertical_header_line_chr   = \"|\"", "bold_vertical_header_line_chr = False"],
                    ["middle_vertical_header_line_chr = \"|\"", "bg_vertical_header_line_chr   = -1"   ],
                    ["right_vertical_header_line_chr  = \"|\"", "fg_vertical_header_line_chr   = -1"   ]]
   
    message = f'''     {cp.set_font(False,1,231)} Refer to Figure 5 {cp.set_font()}
'''
    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)
    print(message)


    # Under Line Header and Attributes for the Under Line Header Section
    simple_msg.msg_title = " Horizontal Under Header Line Default Values "
    default_values = [["horizontal_line_under_header_on  = False", "bold_under_line_header = False"],
                     ["horizontal_line_under_header_chr = \"-\"", "bg_under_line_header   = -1"],
                     ["                                        ", "fg_under_line_header   = -1"]]
   
    message = f'''
     {cp.set_font(False,-1,14)} horizontal_line_under_header_on {cp.set_font()}controls \u2192  d

     {cp.set_font(False,1,231)} Refer to Figure 5 {cp.set_font()}
'''

    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)
    print(message)


    # Header Under line Corners for the Header Section
    simple_msg.msg_title = " Horizontal Corner Under Header Line Default Values "
    default_values = [["left_corner_line_under_header_chr   = \"+\"", "bold_corner_under_line_header = False"],
                     ["middle_corner_line_under_header_chr = \"-\"", "bg_corner_under_line_header   = -1"],
                     ["right_corner_line_under_header_chr  = \"+\"", "fg_corner_under_line_header   = -1"]]
    message = f'''     {cp.set_font(False,1,231)} Refer to Figure 5 {cp.set_font()}
'''
    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)
    print(message)



    message = f'''
     {cp.set_font(True,231,0)} Note: {cp.reset_font()}
     {cp.set_font(False,-1,11)} bg {cp.set_font(bg=-1,fg=14)}and {cp.set_font(False,-1,11)}fg {cp.set_font(bg=-1,fg=14)}accepts int values from -1 to 256. {cp.set_font()}
     {cp.set_font(False,-1,14)} where -1 and 256 are the default value from the system {cp.set_font()}
   
     {cp.set_font(False,1,231)} Refer to set_font() internal function or FontStyle class. {cp.set_font()}    
'''

    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)
    print(message)
    cp.ins_newline(2)




def Reset_Fancy_Format_Method():
    green_msg.print_fancy_message(classes_methods_fancyprint[2][3])

    print("\n It will set all the variables in print_fancy_format method to their default values")
    message = f'''
  
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  fmsg = cp.FancyFormat()      
      {cp.ins_chr(10)}  message = \"Data Text Here.....\"      
      {cp.ins_chr(10)}  fmsg.bg_data = 90
      {cp.ins_chr(10)}  fmsg.print_fancy_format(message)
      {cp.ins_chr(10)}  fmsg.reset_fancy_format()
      {cp.ins_chr(10)}  fmsg.print_fancy_mesage(message)

   '''      
    print(message)

    fmsg = cp.FancyFormat()
    message  = "Data Text Here......"
    fmsg.bg_data = 90
    fmsg.print_fancy_format(message)
    fmsg.reset_fancy_format()
    print("\n")
    fmsg.print_fancy_format(message)
    cp.ins_newline(2)


#---------------------------------------------------------------------------------------------------
# Pen Class                                                                                        -
#---------------------------------------------------------------------------------------------------
def Pen_Class():
    blue_msg.print_fancy_message(classes_methods_fancyprint[0][4] + " Class")
    message = '''
      This class contains two methods:

	   draw_line(size=0, layout=Layout.HORIZONTAL, tail="\N{BLACK DIAMOND}", body="-", head="\N{BLACK DIAMOND}")

	   draw_rectangle(length=3, width=3, style=Line_Style.DASH)
'''
    print(message)

    simple_msg.msg_title = " General Use Default Values "
    default_values = [["adj_indent      = 0",     "bold_draw_line = False"],
                     ["refill_bg_color = False", "bg_draw_line   = -1"],
                     ["                       ", "fg_draw_line   = -1"]]
   
    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)
   
    simple_msg.msg_title = " Rectangle Default Values "
    default_values = [["\033[1;38;5;14mHorizontal Lines\033[0m",                    "  "],
                     ["top_horizontal_line_chr = \"-\"       ",   "bottom_horizontal_line_chr = \"-\""],
                     ["                                      ",   "                                  "],
                     ["\033[1;38;5;14mVertical Lines\033[0m  ",   "                                  "],
                     ["right_vertical_line_chr = \"|\"       ",   "left_vertical_line_chr = \"|\"    "],
                     ["                                      ",   "                                  "],
                     ["\033[1;38;5;14mCorner Lines\033[0m    ",   "                                  "],
                     ["top_left_corner_chr     = \"+\"       ",   "top_right_corner_chr   = \"+\"    "],
                     ["bottom_right_corner_chr = \"+\"       ",   "bottom_left_corner_chr = \"+\"    "]]
   
    simple_msg.print_fancy_format(default_values, cp.Line_Style.NONE)
   #message = f'''     {cp.set_font(False,1,231)} Refer to Figure 5 {cp.set_font()}
#'''
   #print(message)


    Draw_Line_Method()
    Draw_Rectangle_Method()

def Draw_Line_Method():
    green_msg.print_fancy_message(classes_methods_fancyprint[1][4]+"()")
    message = f'''
  
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  pen = cp.Pen()      
      {cp.ins_chr(10)}  pen.adj_indent = 8
      {cp.ins_chr(10)}  pen.draw_line(size=20, layout=cp.Layout.HORIZONTAL,
                                tail=cp.Unicode.BLACK_LEFT_POINTING_TRIANGLE,
                                body=cp.Unicode.EM_DASH, head=cp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE)

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}

      '''
    print(message)

    pen = cp.Pen()
    pen.adj_indent = 8
    pen.draw_line(size=20, layout=cp.Layout.HORIZONTAL, tail=cp.Unicode.BLACK_LEFT_POINTING_TRIANGLE,
                                      body=cp.Unicode.EM_DASH, head=cp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE)
   
    cp.ins_newline(2)    
   

def Draw_Rectangle_Method():
    green_msg.print_fancy_message(classes_methods_fancyprint[2][4]+"()")
    message = f'''
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  pen = cp.Pen()
      {cp.ins_chr(10)}  pen.adj_indent    = 8
      {cp.ins_chr(10)}  pen.bg_draw_lines = 90
      {cp.ins_chr(10)}  pen.fg_draw_lines = 231
      {cp.ins_chr(10)}  pen.refill_bg_color = True
      {cp.ins_chr(10)}  pen.draw_rectangle(length=8, width=4, style=cp.Line_Style.DOUBLE)

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}

      '''
    print(message)
    pen = cp.Pen()
    pen.adj_indent = 8
    pen.bg_draw_line = 90
    pen.fg_draw_line = 231
    pen.refill_bg_color = True
    pen.draw_rectangle(length=8, width=4, style=cp.Line_Style.DOUBLE)

#----------------------------------------------------------------------------------------------------------------------------------------------
# Start the Documentation for fancyprint Module                                                                                               -
#----------------------------------------------------------------------------------------------------------------------------------------------
cp.clear()
ctrl = 0
cmdl_argv = []
for argv in sys.argv:
    cmdl_argv.append(argv.lower())

flag_pen    = False
flag_cursor = False

flag_font_style    = False    
flag_help_classes  = False
flag_fancy_format  = False
flag_fancy_message = False

flag_screen_functions   = False
flag_internal_functions = False


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
    Pen_Class()



else:
    blue_msg.bold_body = True
    blue_msg.italic_body = True
    for fun in cmdl_argv:
        if ("screen_functions" in fun):     Screen_Functions();    flag_screen_functions   = True;      
        elif ("internal_functions" in fun): Internal_Functions();  flag_internal_functions = True;    
        elif ("help_classes" in fun):       Help_Classes();        flag_help_classes       = True;          
        elif ("cursor" in fun):             Cursor_Class();        flag_cursor             = True;                
        elif ("fontstyle" in fun):          FontStyle_Class();     flag_font_style         = True;            
        elif ("fancymessage" in fun):       FancyMessage_Class();  flag_fancy_message      = True;         
        elif ("fancyformat" in fun):        FancyFormat_Class();   flag_fancy_format       = True;          
        elif ("pen" in fun):                Pen_Class();           flag_pen                = True;                   


        elif ("clean" == fun and flag_screen_functions == False):              Clean_Function()
        elif ("clear" == fun and flag_screen_functions == False):              Clear_Function()
        elif ("erase" == fun and flag_screen_functions == False):              Erase_Function()
        elif ("dimensions" == fun and flag_screen_functions == False):         Dimensions_Function()
        elif ("resize" == fun and flag_screen_functions == False):             Resize_Function()


        elif ("ins_chr"       == fun and flag_internal_functions == False):    Ins_Chr_Function()
        elif ("ins_newline"   == fun and flag_internal_functions == False):    Ins_Newline_Function()
        elif ("terminal_bell" == fun and flag_internal_functions == False):    Terminal_Bell_Function()
        elif ("ansi_colors"   == fun and flag_internal_functions == False):    Ansi_Color_Function()


        elif ("move"       == fun and flag_help_classes == False):             Move_Class()
        elif ("align"      == fun and flag_help_classes == False):             Align_Class()
        elif ("layout"     == fun and flag_help_classes == False):             Layout_Class()
        elif ("length"     == fun and flag_help_classes == False):             Length_Class()
        elif ("unicode"    == fun and flag_help_classes == False):             Unicode_Class()
        elif ("line_style" == fun and flag_help_classes == False):             Line_Style_Class()


        elif ("jumpto" == fun and flag_cursor == False):                       JumpTo_Method()
        elif ("jumpxy" == fun and flag_cursor == False):                       Jumpxy_Method()
        elif ("moveto" == fun and flag_cursor == False):                       MoveTo_Method()
        elif ("movexy" == fun and flag_cursor == False):                       Movexy_Method()


        elif ("start_style" == fun and flag_font_style == False):              Start_Stop_Style_Method()
        elif ("stop_style"  == fun and flag_font_style == False):              Start_Stop_Style_Method()
        elif ("print_style" == fun and flag_font_style == False):              Print_Style_Method()
        elif ("reset_style" == fun and flag_font_style == False):              Reset_Style_Method()
 

        elif ("print_fancy_message" == fun  and flag_fancy_message == False):  Print_Fancy_Message_Method()
        elif ("print_fancy_note"    == fun  and flag_fancy_message == False):  Print_Fancy_Note_Method()
 

        elif ("print_fancy_format"  == fun  and flag_fancy_format  == False):  Print_Fancy_Format_Method()
        elif ("reset_fancy_format"  == fun  and flag_fancy_format  == False):  Reset_Fancy_Format_Method()


        elif ("draw_line" == fun and flag_pen == False):                       Draw_Line_Method()
        elif ("draw_rectangle" == fun and flag_pen == False):                  Draw_Rectangle_Method()


        else:
            if (fun != cmdl_argv[0]):
                red_msg.msg_note = fun
                red_msg.msg_body = "is NOT a parameter available in cp_docs.py...!"
                red_msg.print_fancy_note()
                cp.ins_newline(2)
                



          
 
cp.ins_newline(3)
input("  Press Enter to Continue: ")
cp.resize(nrows, ncols)
