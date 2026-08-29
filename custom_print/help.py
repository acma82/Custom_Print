#!/usr/bin/python3.12
'''
Documentation for custom_print module...!
python3.12 cp_documentation.py
'''

import sys
import custom_print as cp

# standar size on the terminal is -> 24 by 80
# resize -s 50 80

#-- -------------------------------------------------------------------------------------------------
#   Variables in common for all the functions and classes                                           -
#-- -------------------------------------------------------------------------------------------------
green_div = cp.Divider()  # Message for function titles
green_div.msg_bg = 10;                  green_div.msg_fg = 0;                          green_div.msg_bold = True
green_div.adj_indent = 2;               green_div.msg_align = cp.Align.CENTER;         green_div.left_right_fill_bg = 10
green_div.all_corner_bg = 10;           green_div.top_horizontal_line_bg = 10;         green_div.bottom_horizontal_line_bg = 10
green_div.left_vertical_line_bg = 10;   green_div.right_vertical_line_bg = 10

blue_div = cp.Divider()
blue_div.msg_bg = 10;                  blue_div.msg_fg = 0;                          blue_div.msg_bold = True
blue_div.adj_indent = 2;               blue_div.msg_align = cp.Align.CENTER;         blue_div.left_right_fill_bg = 10
blue_div.all_corner_bg = 10;           blue_div.top_horizontal_line_bg = 4;          blue_div.bottom_horizontal_line_bg = 4
blue_div.left_vertical_line_bg = 10;   blue_div.right_vertical_line_bg = 10

tbl = cp.FancyFormat()
tbl.header_align = cp.Align.CENTER
tbl.data_align   = cp.Align.CENTER
tbl.header_bold  = True


def about_custom_print():

    '''  Description of custom_print project  '''

    lst = [["Module Name",         "custom_print"                                   ],
           ["Version",             "1.1.5"                                          ],
           ["Author",              "Miguel Angel Aguilar Cuesta"                    ],
           ["Author Email",        "acma.mex@gmail.com"                             ],
           ["Description",         "Customized Print"                               ],
           ["Requirement",         "Python 3.12 or greater"                         ],
           ["Long Description",    "README.md"                                      ],
           ["Content Type",        "MarkDown"                                       ],
           ["Find README.md at",   "https://github.com/acma82/Custom_Print"         ],
           ["Help on Terminal",    "custom_print help"                              ],
           ["Dependencies",        "None"                                           ],
           ["License",             "Everyone Can Use It At Their Own Risk"          ]]



    FACE = " (" + "0" + chr(0x25E1) + "0" + ") "
    tbl.title_msg = FACE + "  Project Description "
    tbl.title_align = "center"
    tbl.title_bg = 231
    tbl.title_fg = 234
    tbl.title_bold = True


    tbl.footnote_msg = "Released on Friday, December 27, 2024"
    tbl.adj_top_space = 1
    tbl.adj_bottom_space = 1


    tbl.header_bg = 54;             tbl.data_bg = 231
    tbl.header_fg = 231;            tbl.data_fg = 234
    tbl.header_bold = True;         tbl.data_bold = True
    tbl.adj_top_margin = 2;         tbl.adj_indent = 4

    tbl.print_fancy_format(lst, "design_10")
    cp.ins_newline(1)
    tbl.reset_fancy_format()






all_topics = [
    "Screen_Functions",  "clean", "clear","dimensions", "erase", "resize",                                                                                               # 0, 1, 2, 3, 4, 5,

    "Internal_Functions", "ansi_colors", "ins_chr", "ins_newline", "set_reset_font", "terminal_bell",                                                                    # 6, 7, 8, 9, 10, 11

    "Help_Classes",  "Align", "Length_Bg", "Ascii_Letter", "Line_Style", "Bg", "Logo", "Move", "Divider_Style", "No", "Fg", "Style", "Layout", "Unicode",                # 12 - 25,

    "Cursor",  "jumpto", "jumpxy", "moveto", "movexy",                                                                                                                   # 26, 27, 28, 23, 30,

    "Fontstyle",  "start_style", "stop_style", "print_style", "reset_style",                                                                                             # 31, 32, 33, 34, 35,

    "FancyMessage",  "print_fancy_message", "print_fancy_note",                                                                                                          # 36, 37, 38,

    "Pen",  "draw_line", "draw_rectangle",                                                                                                                               # 39, 40, 41,

    "Divider",  "print_fancy_divider",                                                                                                                                   # 42, 43,

    "FancyFormat",  "fancyformat", "print_fancy_format", "reset_fancy_format",                                                                                           # 44, 45, 46, 47,

     "AsciiArt", "print_ascii_art", "print_multi_ascii_art", "print_ascii_logo_art", "print_reversed_ascii_logo_art"]                                                    # 48, 49, 50, 51, 52.

def  help_documentation():
    # pylo = cp.PyLO()
    # result = pylo.sort_rows_by_col(data=help_classes, ref_col=0, reversed_order=False, update=False)

    blue_msg  = cp.FancyMessage()   # for titles in the help menu and for class names
    blue_msg.body_bold   = True
    blue_msg.title_bold  = True
    blue_msg.body_italic = True

    cols, rows = cp.dimensions()

    crs = cp.Cursor()               # Cursor Object
    fst = cp.FontStyle()            # FontStyle Object
    tbl = cp.FancyFormat()          # for lists

    fst.bold = True
    fst.fg   = 0
    fst.bg   = 231
    fst.indent = 3



    # classes and methods for custom_print module
    screen_funs        = [[" Screen_Functions "], ["clean"], ["clear"], ["dimensions"], ["erase"], ["resize"]]

    internal_functions = [[" Internal_Functions "], ["ansi_colors"], ["ins_chr"], ["ins_newline"], ["set_reset_font"], ["terminal_bell"]]

    help_classes       = [["Align", "Line_Style"], ["Ascii_Letter", "Logo"],["Bg", "Move"], ["Divider_Style", "No"],["Fg", "Style"],["Layout", "Unicode"],["Length_Bg", "----"]]

    cmcpp1 = [["Cursor",  "FontStyle"   ,  "FancyMessage"       ,  "Pen"           ],
              ["jumpTo",  "start_style" ,  "print_fancy_message",  "draw_line"     ],
              ["jumpxy",  "stop_style"  ,  "print_fancy_note"   ,  "draw_rectangle"],
              ["moveTo",  "print_style" ,  "----"               ,  "----"          ],
              ["movexy",  "reset_style" ,  "----"               ,  "----"          ]]

    cmcpp2 = [["Divider",              "FancyFormat"       ],
              ["print_fancy_divider",  "print_fancy_format"],
              ["----",                 "reset_fancy_format"],
              ["----",                 "----"              ],
              ["----",                 "----"              ]]


    cmcpp3 = [["AsciiArt"],
              ["print_ascii_art"],
              ["print_multi_ascii_art"],
              ["print_ascii_logo_art"],
              ["print_reversed_ascii_logo_art"]]

    cp.ins_newline(1)
    mensaje = "Documentation For custom_print Module....!"
    blue_msg.left_indent = int(((cols)-(len(mensaje)))/2)
    blue_msg.print_fancy_message(mensaje)
    print(f"\n  Release Version: 1.1.5\n")

    mensaje = "Functions in custom_print Module"
    blue_msg.print_fancy_message(mensaje)
    tbl.header_all_cell_bg = False
    tbl.header_bold = True
    tbl.header_bg   = 90; tbl.header_fg = 231
    tbl.header_italic = True
    tbl.title_align = cp.Align.CENTER
    tbl.header_horizontal_line_on = True
    tbl.print_fancy_format(screen_funs)

    tbl.adj_indent = 32
    crs.jumpTo(qty=9,direction=cp.Move.UP)
    tbl.print_fancy_format(internal_functions)
    tbl.adj_indent = 2
    cp.ins_newline(n=1)
    mensaje = "Classes and Methods in custom_print Module"
    blue_msg.left_indent = int(((cols)-(len(mensaje)))/2)
    blue_msg.print_fancy_message(mensaje)
    cp.ins_newline(n=1)


    tbl.header_horizontal_line_on = False;               tbl.header_italic = False
    tbl.header_bg    = -1;      tbl.header_fg = -1;      tbl.header_align = cp.Align.JUSTIFY
    tbl.header_bold  = False;

    tbl.title_align = cp.Align.CENTER;                  tbl.title_italic = True
    tbl.title_bg    = 90;      tbl.title_fg = 231;      tbl.title_bold   = True
    tbl.title_msg   = " Help_Classes "
    tbl.print_fancy_format(help_classes)

    cp.ins_newline(n=2)

    crs.jumpTo(qty=10, direction=cp.Move.UP)
    tbl.adj_indent = 38;
    tbl.header_all_cell_bg = True
    tbl.header_align = cp.Align.CENTER

    tbl.title_msg = ""; tbl.header_horizontal_line_on = True
    tbl.header_italic = True; tbl.header_bold = True
    tbl.header_bg = 90; tbl.header_fg = 231
    tbl.print_fancy_format(cmcpp3)
    cp.ins_newline(n=2)


    tbl.adj_indent = 2
    tbl.print_fancy_format(data=cmcpp1)
    cp.ins_newline(n=2)
    tbl.adj_indent = 13
    tbl.print_fancy_format(data=cmcpp2)


    cp.ins_newline(1)
    mensaje = "How to use the documentation in custom_print Module"
    blue_msg.left_indent = int(((cols)-(len(mensaje)))/2)
    blue_msg.print_fancy_message(mensaje)
    cp.ins_newline(n=1)


    print("   To display help for a specific function or method just pass the name of the\n parameter as shown above.")
    cp.ins_newline(1)
    print(f"{fst.style_on()} Example 1: {fst.style_off()}  custom_print clean")

    note=" Note: "
    #                   20                   40                   60                   80   85   90
    message_note = '''
       It is possible to display the documentation for more
    than one function or method at the same time.
    It just needs to be specified when passing the parameters.
    If it is preferred, it can be displayed all the methods for
    a specific group of function, a class or a combination of them.
        '''
    cp.ins_newline(1)


    blue_msg.length    = cp.Length_Bg.ALL_ROW
    blue_msg.body_bold = False
    blue_msg.note_msg  = note
    blue_msg.note_bold = True
    blue_msg.body_bg   = 90
    blue_msg.note_position = 2
    blue_msg.print_fancy_note(message_note)
    cp.ins_newline(1)
    print(f"{fst.style_on()} Example 2: {fst.style_off()}  custom_print screen_functions art ins_chr movexy" )

# ----------------------------------------------------
    message = f'''     Notice that on\033[1m example 2\033[0m, is being called a function group, a class,
       a function and a method. For the group, it will be displayed all the
       documentation for all functions that belong to that group.

       {fst.style_on()} screen_functions: clean, clear, dimensions, erase, resize. {fst.style_off()}

       I will display the documentation for all the methods that belong to that
       class. The above tables show all the classes with their methods.

       It will display the documentation for the function \033[1;48;5;1m ins_chr \033[0m as well.

       Documentation for the method \033[1;48;5;22;1m movexy \033[0m will be called as well.

       It's possible to display the complete documentation help by passing
       \"all\" or \"documentation\" as a parameter.

    '''


    cp.ins_newline(1)

    print(message)

    print(f"{fst.style_on()} example 3: {fst.style_off()}  custom_print all")
    print(f"{cp.ins_chr(16, ' ')} custom_print documentation")

    cp.ins_newline(2)
    message = f'''
    \N{BULLET} custom_print module has been tested on RedHat 9, Centos Stream 9,
      AlmaLinux 9, and Windows 10.

    \N{BULLET} custom_print module requires python3.12 or greater.

    \N{BULLET} https://github.com/acma82/Custom_Print/tree/main/readme
    '''


    blue_msg.body_bg   = 90
    blue_msg.body_fg   = 231                                                                  # 15, 16, 17, 18, 19
    blue_msg.body_bold = False
    blue_msg.left_indent = 4
    blue_msg.print_fancy_message(message)

    cp.ins_newline(1)
    tbl.adj_indent = 24
    tbl.print_fancy_format("Bugs \u2192 acma.mex@hotmail.com", cp.Line_Style.DOUBLE_LINE)
    cp.ins_newline(1)





def all_documentation():
    purple_div = cp.Divider()
    purple_div.msg_bg = 231;                 purple_div.msg_fg = 16;                         purple_div.msg_bold = True
    purple_div.adj_indent = 2;               purple_div.msg_align = cp.Align.CENTER;         purple_div.left_right_fill_bg = 90
    purple_div.all_corner_bg = 90;           purple_div.top_horizontal_line_bg = 90;          purple_div.bottom_horizontal_line_bg = 90
    purple_div.left_vertical_line_bg = 90;   purple_div.right_vertical_line_bg = 90
    purple_div.print_fancy_divider("  Custom_Print Documentation  ")
    about_custom_print()
    help_documentation()
    screen_functions_info()
    internal_functions_info()
    help_classes_info()
    cursor_info()
    fontstyle_info()
    fancymessage_info()
    divider_info()
    fancyformat_info()
    pen_info()
    asciiart_info()
# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: SCREEN_FUNCTIONS                                                                  |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  Screen_Functions in custom_print Module                                                        |
# +-------------------------------------------------------------------------------------------------+
def screen_functions_info():
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[0])    # Screen Functions
    mensaje = '''
      It is used \"ansi code\" to manipulate the screen on the terminal.
    '''
    print(mensaje)
    clean_info()
    clear_info()
    dimensions_info()
    erase_info()
    resize_info()


def clean_info():
   #------------------------------------------------------------------------------------------------
   # clean, It uses ansi code                                                                      -
   #------------------------------------------------------------------------------------------------
    message = f'''
      It cleans the terminal and returns the cursor to home.

      Note: This function uses the ansi code.
    '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[1])
    print(message)

    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp")
    print(f"{cp.ins_chr(18)}cp.clean()\n")


def clear_info():
   #------------------------------------------------------------------------------------------------
   # clear,       It uses the system command                                                       -
   #------------------------------------------------------------------------------------------------
    message = '''
      It clears the terminal and returns the cursor to home.

      Note: This functions uses the OS command.
    '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[2])
    print(message)
    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp")
    print(f"{cp.ins_chr(18)}cp.clear()\n")


def dimensions_info():
   #------------------------------------------------------------------------------------------------
   # dimensions                                                                                    -
   #------------------------------------------------------------------------------------------------
    menssage ='''
      It returns the dimensions of the terminal, cols and rows.
    '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[3])
    print(menssage)
    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp")
    print(f"{cp.ins_chr(18)}ncols, nrows = cp.dimensions()")
    print("                  print(f\"(Number of Cols: {ncols})")
    print("                  print(f\"(Number of Rows: {nrows})\n")


#------------------------------------------------------------------------------------------------
# erase,       It uses ansi code                                                                -
#------------------------------------------------------------------------------------------------
def erase_info():
    menssage = '''
      It erases the terminal and leaves the cursor in the current position.
    '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[4])
    print(menssage)
    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example 1: {cp.reset_font()}  import custom_print as cp")
    print(f"{cp.ins_chr(20)}cp.erase()\n")


    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example 2: {cp.reset_font()}  import time")
    msg = f'''{cp.ins_chr(20)}from custom_print import erase
                    print("Hello custom_print",end=".", flush=True)
                    time.sleep(3)
                    erase()
                    print("Continuing from before")

    '''
    print(msg)

#------------------------------------------------------------------------------------------------
# resize                                                                                        -
#------------------------------------------------------------------------------------------------
def resize_info():
    message = '''
      It resizes the terminal size.
    '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[5]+"(rows=25, cols=80)")
    print(message)
    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp")
    print(f"{cp.ins_chr(18)}cp.resize(rows=20, cols=120)\n")
    print(f"\n{cp.ins_chr(6)}Note: This only works when we are using the gnome or Xfce terminal.")
    print(f"{cp.ins_chr(6)}      Using konsole or another type of termial it may not work.")






# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: INTERNAL_FUNCTIONS                                                                |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  Internal_Functions in custom_print Module                                                      |
# +-------------------------------------------------------------------------------------------------+
def internal_functions_info():
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[6]) #"Internal Functions")
    mensaje ='''
    All these functions are being used internally in the custom_print modules.
    It is available to the user if they find them usefull, otherwise, feel free
    to ignore them.
    '''
    print(mensaje)
    ansi_colors_info()
    ins_chr_info()
    ins_newline_info()
    set_reset_font_info()
    terminal_bell_info()


#------------------------------------------------------------------------------------------------
# ansi_colors                                                                                   -
#------------------------------------------------------------------------------------------------
def ansi_colors_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[7]) # Ansi Colors
    message = f'''
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  bg_ansi_colors(bold=False, fg=-1, n_line=0)  {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  bg colors available in the ansi code         {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}
    '''
    print(message)
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
        print (u"\u001b[0m")

    message = f'''
      This function displays all background colors available with ansi code.
      The following options are for a better visualization.

      1.- The bold option for the font (True / False)
      2.- The fg option to visualize the background colors with a specific
           foreground color.
      3.- The n_line option to insert lines between the colors.


      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  cp.bg_ansi_colors(bold=True, fg=22, n_line=1)
    '''
    print(message)

    cp.ins_newline(2)

    message = f'''
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  fg_ansi_colors(bold=False, bg=-1, n_line=0)  {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  fg colors available in the ansi code         {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}
    '''
    print(message)
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        print (u"\u001b[0m")


    message = f'''
      This function displays all foreground colors available with ansi code.
      The following options are for a better visualization.

      1.- The bold option for the font (True / False)
      2.- The bg option to visualize the background colors with a specific
         foreground color.
      3.- The n_line option to insert lines between the colors.


      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  cp.fg_ansi_colors(bold=True, bg=22, n_line=1)
    '''
    print(message)

    message = f'''
      {cp.set_font(1,196,231)} Note: {cp.reset_font()} These 2 functions will display the name and number of the colors.
              It will be handy when the user start using the Help_Classes.
              To set the default color for bg or fg, the user can use
              the value of -1 or 256.

    '''
    print(message)

#------------------------------------------------------------------------------------------------
# ins_chr                                                                                       -
#------------------------------------------------------------------------------------------------
def ins_chr_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[8]) # Ansi Colors
    message = f'''
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  ins_chr(n=1)                                 {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}

      This function inserts n times the unicode provided,
      by default it is set to space.

      {cp.set_font(1,231,0)} Example 1: {cp.reset_font()}  import custom_print as cp
                    print("Hello"+cp.ins_chr(20)+"There")

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}    Hello                    There

      '''
    print(message)

    message = f'''
      {cp.set_font(1,231,0)} Example 2: {cp.reset_font()}  import custom_print as cp
                    print("Hello"+cp.ins_chr(20,"@")+"There")

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}    Hello@@@@@@@@@@@@@@@@@@@@There


      '''
    print(message)

#------------------------------------------------------------------------------------------------
# ins_newline                                                                                   -
#------------------------------------------------------------------------------------------------
def ins_newline_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[9])
    message = f'''
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  ins_newline(n=1)                             {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}

      This function inserts n new lines.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  print("Python")
                  cp.ins_newline(2)
                  print("is amazing...!")

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  Python


                  is amazing...!

      '''
    print(message)

#------------------------------------------------------------------------------------------------
# set_font and reset_font                                                                       -
#------------------------------------------------------------------------------------------------
def set_reset_font_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[10])
    message = f'''
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  set_font(parameters)                         {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  reset_font()                                 {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}

      Colors range goes from -1 to 256.
      To set the default color from the system use -1 or 256,
      for both bg and fg.

      blinking might not work in all the OS. We use Red Hat Family.


       reset_font() → This function resets the font attributes to the default
                      values when we use the set_font() function.

       set_font()   → This function changes the font attributes, bg, fg,
                      bold, italic, and so on.


       Parameters with their default values:

       1)  bold    = False    4) italic    = False    7) blinking = False
       2)  bg      = -1       5) underline = False    8) dim      = False
       3)  fg      = -1       6) strike    = False    9) hidden   = False
       10) inverse = False

      This function passes many attributes for the font. If passing all these
      arguments is a little annoying to the user, the user can use the
      FontStyle Class for simplicity.

      The best way to use this function is to pass only the first 3 parameters
      like the example.

       {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                   print(cp.set_font(1,11,21) + " Python is " +
                   cp.set_font(0,1) + " Wonderful." + cp.reset_font()) +
                   " Default."

        {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  {cp.set_font(1,11,21)} Python is {cp.set_font(0,1)} Wonderful. {cp.reset_font()} Default.


      Note: These functions are being used by some classes.
            Feel free to ignore them if not useful to you.
    '''
    print(message)


#------------------------------------------------------------------------------------------------
# terminal_bell                                                                                 -
#------------------------------------------------------------------------------------------------
def terminal_bell_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[11])
    message = f'''
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  terminal_bell()                              {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}

      This function makes the bell sound in the terminal.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  cp.terminal_bell()

      '''
    print(message)
    cp.terminal_bell()





# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: HELP_CLASSES                                                                      |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  Help_Classes in custom_print Module                                                            |
# +-------------------------------------------------------------------------------------------------+
def help_classes_info():
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[12]) # Help Classes
    mensaje ='''
    All these classes are to help the user to do not mispell any instructions
    in all the other classes, methods, or functions. The user can still use
    the default value directly, however it is recomended to use these classes.
    '''
    print(mensaje)
    align_info()
    ascii_letter_info()
    bg_info()
    divider_style_info()
    fg_info()
    layout_info()
    length_bg_info()
    line_style_info()
    logo_info()
    move_info()
    no_info()
    style_info()
    unicode_info()






def align_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[13])
    message = f'''
      This class is used where alignment is needed. It contains 4 options.

      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Align.RIGHT      {cp.Unicode.BULLET} Align.CENTER            {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Align.LEFT       {cp.Unicode.BULLET} Align.JUSTIFY           {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                               {cp.reset_font()}

      This class makes the alignment for data.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  msg = cp.FancyMessage()
                  msg.title_align = cp.Align.CENTER
                  msg.footnote_align = "right"
                # msg.footnote_align = "r"  -> Same as above

      '''
    print(message)
    lista = [["Align.RIGHT","Align.LEFT", "Align.CENTER","Align.JUSTIFY"],
             ['\"right\"','\"left\"','\"center\"','\"justify\"'],
             ['\"r\"', '\"l\"', '\"c\"', '\"j\"']]
    tbl.print_fancy_format(data=lista, style=cp.Line_Style.TURQUOISE_BLACK)
    print("\n      Note: See the FancyMessage Class to visualize a complete example.\n\n")



def ascii_letter_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[15])
    message = f'''
      This class is used mainly with AsciiArt class. It contains 23 options.

      {cp.set_font(1,209,16,1)}                                           {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Alpha            {cp.Unicode.BULLET} Larry               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} ANSI_Shadow      {cp.Unicode.BULLET} Money_NE            {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Big              {cp.Unicode.BULLET} Money_NW            {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Blocks           {cp.Unicode.BULLET} Money_SE            {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Bulbhead         {cp.Unicode.BULLET} Money_SW            {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Classy           {cp.Unicode.BULLET} Mono                {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Colosal          {cp.Unicode.BULLET} Moon                {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Crazy            {cp.Unicode.BULLET} Moon2               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Doh              {cp.Unicode.BULLET} Roman               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Doom             {cp.Unicode.BULLET} Standard            {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Epic             {cp.Unicode.BULLET} Sweet               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Graceful                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                           {cp.reset_font()}

      This class select the type of letter to print.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  msg = cp.Art()
                  msg.ascii_type = cp.Ascii_Letter.Moon

      '''
    print(message)
    lista = [
    ["Ascii_Letters                 Value         " ],
    ["Alpha_Letter              = \"Alpha\"       " ],
    ["Ascii_Letter.ANSI_Shadow  = \"ANSI_Shadow\" " ],
    ["Ascii_Letter.Big          = \"Big\"         " ],
    ["Ascii_Letter.Blocks       = \"Blocks\"      " ],
    ["Ascii_Letter.Bulbhead     = \"Bulbhead\"    " ],
    ["Ascii_Letter.Classy       = \"Classy\"      " ],
    ["Ascii_Letter.Colossal     = \"Colossal\"    " ],
    ["Ascii_Letter.Crazy        = \"Crazy\"       " ],
    ["Ascii_Letter.Doh          = \"Doh\"         " ],
    ["Ascii_Letter.Doom         = \"Doom\"        " ],
    ["Ascii_Letter.Epic         = \"Epic\"        " ],
    ["Ascii_Letter.Graceful     = \"Graceful\"    " ],
    ["Ascii_Letter.Larry        = \"Larry\"       " ],
    ["Ascii_Letter.Money_NE     = \"Money_NE\"    " ],
    ["Ascii_Letter.Money_NW     = \"Money_NW\"    " ],
    ["Ascii_Letter.Money_SE     = \"Money_SE\"    " ],
    ["Ascii_Letter.Money_SW     = \"Money_SW\"    " ],
    ["Ascii_Letter.Mono         = \"Mono\"        " ],
    ["Ascii_Letter.Moon         = \"Moon\"        " ],
    ["Ascii_Letter.Moon2        = \"Moon2\"       " ],
    ["Ascii_Letter.Roman        = \"Roman\"       " ],
    ["Ascii_Letter.Standard     = \"Standard\"    " ],
    ["Ascii_Letter.Sweet        = \"Sweet\"       " ]]

    tbl.print_fancy_format(data=lista, style=cp.Line_Style.TURQUOISE_BLACK)
    print("\n      Note: See the AsciiArt Class to visualize a complete example.\n\n")


def bg_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[17])
    message = f'''
      This class is mainly used where background color is needed.

      {cp.set_font(1,209,16,1)}                                                            {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} See \"ansi_colors\" function to see all the bg color names {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                                            {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp  '''
    print(message)
    print("                  print(f\"{cp.Bg.SEA_BLUE} Hello There {cp.Bg.OFF} Bye \" )")

    message = f'''
      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  {cp.Bg.SEA_BLUE} Hello There {cp.Bg.OFF} Bye

    '''
    print(message)
    # cp.bg_ansi_colors(bold=True, fg=0, n_line=1)

def fg_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[22])
    message = f'''
      This class is mainly used where foreground color is needed.

      {cp.set_font(1,209,16,1)}                                                            {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} See ansi_colors function to see all the fg color names   {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                                            {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp  '''
    print(message)
    print("                  print(f\"{cp.Fg.SEA_BLUE} Hello There {cp.Fg.OFF} Bye \" )")

    message = f'''
      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  {cp.Fg.SEA_BLUE} Hello There {cp.Fg.OFF} Bye

    '''
    print(message)


def divider_style_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[20])
    message = f'''
      This class is with Divider class. It contains 10 options.

      {cp.set_font(1,209,16,1)}                                           {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} CUSTOMIZED   = \"customized\"            {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SINGLE_LINE  = \"single_line\"           {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SINGLE_BOLD  = \"single_bold\"           {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SINGLE_HEAVY = \"single_heavy\"          {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} DOUBLE_LINE  = \"double_line\"           {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} DASH_1       = \"dash_1\"                {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} DASH_2       = \"dash_2\"                {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SQ_BRACKETS  = \"sq_brackets\"           {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} BLUE_WHITE_1 = \"blue_white_1\"          {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} BLUE_WHITE_2 = \"blue_white_2\"          {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                           {cp.reset_font()}

      This class select the type of style for the divider to be used.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  div = cp.Divider()
                  div.print_fancy_divider(message = " Custom Print Divider",
                                          style   = cp.Divider_Style.DASH_2)

      '''
    print(message)
    print("\n      Note: See the Divider Class to visualize a complete example.\n\n")


def layout_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[24])

    message = f'''
      This class is used with FancyFormat class.

      {cp.set_font(1,209,16,1)}                                {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Layout.HORIZONTAL           {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Layout.VERTICAL             {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: Range type, vertical layout {cp.reset_font()}

                  import custom_print as cp
                  tbl  = cp.FancyFormat()
                  x    = range(0,16,2)

                  tbl.set_layout   = cp.Layout.VERTICAL
                  tbl.title_msg    = " Range Data"
                  tbl.footnote_msg = " Case 5 "
                  tbl.print_fancy_format(x)


      Note: These 2 options can be replaced by their original values.

      {cp.ins_chr(10)}  Layout.HORIZONTAL   \u2192  \"horizontal\"
      {cp.ins_chr(10)}  Layout.VERTICAL     \u2192  \"vertical\"

'''
    print(message)
    print("\n      Note: See the FancyFormat class to visualize a complete example.")
    print("            Layout works with Range, Set, Frozenset and Dictionary types.")


def length_bg_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[14])

    message = f'''
      This class is used with FancyMessage class.

      {cp.set_font(1,209,16,1)}                            {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} ALL_ROW   = 1           {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} ONLY_WORD = 2           {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                            {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: Range type, vertical layout {cp.reset_font()}

                  import custom_print as cp
                  msg = cp.FancyMessage()
                  paragraph1 = \" First paragraph,  Last  paragraph \"
                  msg.length = cp.Length_Bg.ONLY_WORD
                  msg.print_fancy_message(paragraph1)

      Note: These 2 options can be replaced by their original values.

      {cp.ins_chr(10)}  ALL_ROW   \u2192 1
      {cp.ins_chr(10)}  ONLY_WORD \u2192 2


      Note: See FancyFormat class to visualize a complete example.

      '''
    print(message)

def line_style_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[16])
    message = f'''
      Style_Line Class is used with FancyFormat Class. There are many options.

      {cp.set_font(1,209,16,1)}                                                          {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} CUSTOMIZED    {cp.Unicode.BULLET} DESIGN_1                              {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} DASH_LINE     {cp.Unicode.BULLET} DESIGN_2                              {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SINGLE_LINE   {cp.Unicode.BULLET} DESIGN_3      {cp.Unicode.BULLET} WHITE_BLACK_1         {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SINGLE_BOLD   {cp.Unicode.BULLET} DESIGN_4      {cp.Unicode.BULLET} WHITE_BLACK_2         {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SINGLE_HEAVY  {cp.Unicode.BULLET} DESIGN_5      {cp.Unicode.BULLET} WHITE_PURPLE          {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} DOUBLE_LINE   {cp.Unicode.BULLET} DESIGN_6      {cp.Unicode.BULLET} TURQUOISE_BLACK       {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SQ_BRACKETS   {cp.Unicode.BULLET} DESIGN_7      {cp.Unicode.BULLET} TURQUOISE_WHITE       {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} NONE          {cp.Unicode.BULLET} DESIGN_8      {cp.Unicode.BULLET} WHITE_BLACK_PURPLE    {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SPACE_0       {cp.Unicode.BULLET} DESIGN_9      {cp.Unicode.BULLET} GRAY_TEAL_WHITE       {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SPACE_1       {cp.Unicode.BULLET} DESIGN_10     {cp.Unicode.BULLET} BLUE_PURPLE_WHITE_1   {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SPACE_2       {cp.Unicode.BULLET} RED_WHITE     {cp.Unicode.BULLET} BLUE_PURPLE_WHITE_2   {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SPACE_3       {cp.Unicode.BULLET} BLUE_WHITE    {cp.Unicode.BULLET} GREEN_GREEN_BLACK     {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SPACE_4       {cp.Unicode.BULLET} TEAL_WHITE                            {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} SPACE_5       {cp.Unicode.BULLET} PURPLE_WHITE                          {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                                          {cp.reset_font()}

      Note: These options can be replaced for the original values.

      {cp.Unicode.BULLET} CUSTOMIZED   \u2192 \"customized\"        {cp.Unicode.BULLET} DESIGN_1     \u2192 \"design_1\"
      {cp.Unicode.BULLET} DASH_LINE    \u2192 \"dash_line\"         {cp.Unicode.BULLET} DESIGN_2     \u2192 \"design_2\"
      {cp.Unicode.BULLET} SINGLE_LINE  \u2192 \"single_line\"       {cp.Unicode.BULLET} DESIGN_3     \u2192 \"design_3\"
      {cp.Unicode.BULLET} SINGLE_BOLD  \u2192 \"single_bold\"       {cp.Unicode.BULLET} DESIGN_4     \u2192 \"design_4\"
      {cp.Unicode.BULLET} SINGLE_HEAVY \u2192 \"single_heavy\"      {cp.Unicode.BULLET} DESIGN_5     \u2192 \"design_5\"
      {cp.Unicode.BULLET} DOUBLE_LINE  \u2192 \"double_line\"       {cp.Unicode.BULLET} DESIGN_6     \u2192 \"design_6\"
      {cp.Unicode.BULLET} SQ_BRACKETS  \u2192 \"sq_brackets\"       {cp.Unicode.BULLET} DESIGN_7     \u2192 \"design_7\"
      {cp.Unicode.BULLET} NONE         \u2192 \"none\"              {cp.Unicode.BULLET} DESIGN_8     \u2192 \"design_8\"
      {cp.Unicode.BULLET} SPACE_0      \u2192 \"space_0\"           {cp.Unicode.BULLET} DESIGN_9     \u2192 \"design_9\"
      {cp.Unicode.BULLET} SPACE_1      \u2192 \"space_1\"           {cp.Unicode.BULLET} DESIGN_10    \u2192 \"design_10\"
      {cp.Unicode.BULLET} SPACE_2      \u2192 \"space_2\"           {cp.Unicode.BULLET} RED_WHITE    \u2192 \"red_white\"
      {cp.Unicode.BULLET} SPACE_3      \u2192 \"space_3\"           {cp.Unicode.BULLET} BLUE_WHITE   \u2192 \"blue_white\"
      {cp.Unicode.BULLET} SPACE_4      \u2192 \"space_4\"           {cp.Unicode.BULLET} TEAL_WHITE   \u2192 \"teal_white\"
      {cp.Unicode.BULLET} SPACE_5      \u2192 \"space_5\"           {cp.Unicode.BULLET} PURPLE_WHITE \u2192 \"purple_white\"

      {cp.Unicode.BULLET} WHITE_BLACK_1       \u2192 \"white_black_1\"
      {cp.Unicode.BULLET} WHITE_BLACK_2       \u2192 \"white_black_2\"
      {cp.Unicode.BULLET} WHITE_PURPLE        \u2192 \"white_purple\"
      {cp.Unicode.BULLET} TURQUOISE_BLACK     \u2192 \"turquoise_black\"
      {cp.Unicode.BULLET} TURQUOISE_WHITE     \u2192 \"turquoise_white\"
      {cp.Unicode.BULLET} WHITE_BLACK_PURPLE  \u2192 \"white_black_purple\"
      {cp.Unicode.BULLET} GRAY_TEAL_WHITE     \u2192 \"gray_teal_white\"
      {cp.Unicode.BULLET} BLUE_PURPLE_WHITE_1 \u2192 \"blue_purple_white_1\"
      {cp.Unicode.BULLET} BLUE_PURPLE_WHITE_2 \u2192 \"blue_purple_white_2\"
      {cp.Unicode.BULLET} GREEN_GREEN_BLACK   \u2192 \"green_green_black\"



      {cp.set_font(True,231,0)}   Note:  {cp.reset_font()}  Options {cp.set_font(True,-1,14)}SPACE_X,{cp.reset_font()} use colors to visualize the effect
                  on the tables while {cp.set_font(True,-1,14)}NONE{cp.reset_font()} will ignore all the colors
                  assigned to the table, See the example below.

      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import custom_print as cp
      {cp.ins_chr(10)}  tbli = cp.FancyFormat()
      {cp.ins_chr(10)}  tbli.header_bg   = 23;         tbli.data_bg        = 231
      {cp.ins_chr(10)}  tbli.header_fg   = 231;        tbli.data_fg        = 21
      {cp.ins_chr(10)}  tbli.header_bold = True;       tbli.data_bold      = True
      {cp.ins_chr(10)}  tbli.horizontal_line_bg = 1;   tbli.adj_top_margin = 1
      {cp.ins_chr(10)}  tbli.vertical_line_bg   = 1;   tbli.adj_top_space  = 1

      {cp.ins_chr(10)}  tbli.inner_corner_bg  = 1;
      {cp.ins_chr(10)}  tbli.outer_corner_bg  = 1;
      {cp.ins_chr(10)}  tbli.header_corner_bg = 1
      {cp.ins_chr(10)}  tbli.header_horizontal_line_on = True    # False
      {cp.ins_chr(10)}  tbli.bottom_horizontal_line_on = True    # False
      {cp.ins_chr(10)}  tbli.top_horizontal_line_on    = True    # False
      {cp.ins_chr(10)}  tbli.header_horizontal_line_bg = 1
      {cp.ins_chr(10)}  tbli.header_vertical_line_bg   = 1

      {cp.ins_chr(10)}  tbli.title_align = cp.Align.CENTER
      {cp.ins_chr(10)}  tbli.title_bg    = 231
      {cp.ins_chr(10)}  tbli.title_fg    = 16
      {cp.ins_chr(10)}  tbli.title_bold  = True


      {cp.ins_chr(10)}  lst = [["Header 1", "Header 2", "Header 3", "Header 4"],
      {cp.ins_chr(10)}         ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
      {cp.ins_chr(10)}         ["Data 5",   "Data 6",   "Data 7",   "Data 8"  ]]

      {cp.ins_chr(10)}  # tbli.print_fancy_format(data, style)

      {cp.ins_chr(10)}  tbli.header_horizontal_line_on = False
      {cp.ins_chr(10)}  tbli.print_fancy_format(data=lst, style=cp.Line_Style.NONE)
      {cp.ins_chr(10)}  tbli.title_msg = " SPACE_0"
      {cp.ins_chr(10)}  tbli.print_fancy_format(lst, cp.Line_Style.SPACE_0)
      {cp.ins_chr(10)}  tbli.print_fancy_format(data=lst, style=cp.Line_Style.NONE)
      {cp.ins_chr(10)}  tbli.title_msg = " SPACE_1"
      {cp.ins_chr(10)}  tbli.print_fancy_format(lst, cp.Line_Style.SPACE_1)
      {cp.ins_chr(10)}  tbli.title_msg = " SPACE_2"
      {cp.ins_chr(10)}  tbli.print_fancy_format(lst, cp.Line_Style.SPACE_2)
      {cp.ins_chr(10)}  tbli.title_msg = " SPACE_3 "
      {cp.ins_chr(10)}  tbli.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_3)
      {cp.ins_chr(10)}  tbli.title_msg = " SPACE_4 "
      {cp.ins_chr(10)}  tbli.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_4)
      {cp.ins_chr(10)}  tbli.title_msg = " SPACE_5 "
      {cp.ins_chr(10)}  tbli.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_5)

      {cp.set_font(1,231,90)} \u25CF Output: {cp.reset_font()}
   '''
    print(message)
    lst = [["Header 1", "Header 2", "Header 3", "Header 4"],
           ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
           ["Data 5",   "Data 6",   "Data 7",   "Data 8"  ]]
    tbli = cp.FancyFormat()
    tbli.header_bg   = 23;         tbli.data_bg   = 231
    tbli.header_fg   = 231;        tbli.data_fg   = 21
    tbli.header_bold = True;       tbli.data_bold = True
    tbli.horizontal_line_bg  = 1;  tbli.adj_top_margin = 1
    tbli.vertical_line_bg    = 1;  tbli.adj_top_space  = 1

    tbli.inner_corner_bg  = 1
    tbli.outer_corner_bg  = 1
    tbli.header_corner_bg = 1
    tbli.header_horizontal_line_on = True
    tbli.bottom_horizontal_line_on = True
    tbli.top_horizontal_line_on    = True
    tbli.header_horizontal_line_bg = 1
    tbli.header_vertical_line_bg   = 1

    tbli.title_bg    = 231;                tbli.title_fg  = 16;      tbli.title_bold = True
    tbli.title_align = cp.Align.CENTER;    tbli.title_msg = " NONE "

    tbli.header_horizontal_line_on = False
    tbli.print_fancy_format(data=lst, style=cp.Line_Style.NONE)
    tbli.title_msg = " SPACE_0"
    tbli.print_fancy_format(lst, cp.Line_Style.SPACE_0)
    tbli.title_msg = " SPACE_1"
    tbli.print_fancy_format(lst, cp.Line_Style.SPACE_1)
    tbli.title_msg = " SPACE_2"
    tbli.print_fancy_format(lst, cp.Line_Style.SPACE_2)
    tbli.title_msg = " SPACE_3 "
    tbli.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_3)
    tbli.title_msg = " SPACE_4 "
    tbli.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_4)
    tbli.title_msg = " SPACE_5 "
    tbli.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_5)

    print(f"\n{cp.ins_chr(10)}{cp.set_font(1,231,90)} \u25CF To see more examples regarding FancyFormat, check FancyFormat  {cp.reset_font()}\n"
           f"{cp.ins_chr(10)}{cp.set_font(1,231,90)}   class documentation.{cp.ins_chr(43)}{cp.reset_font()}")


def logo_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[18])
    message = f'''
      Logo Class has a few options.

      {cp.set_font(1,209,16,1)}                  {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Logo_Centos   {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Logo_Debian   {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Logo_Linux    {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Logo_RedHat   {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} Logo_Unix     {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                  {cp.reset_font()}



      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import custom_print as cp
      {cp.ins_chr(10)}  art_logo = cp.AsciiArt()
      {cp.ins_chr(10)}  art_logo.ascii_type = cp.Logo_Centos

      Note: See AsciiArt Class for more options.
    '''
    print(message)

def move_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[19])
    message = f'''
      Move Class has a few options.

      {cp.set_font(1,209,16,1)}             {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} DOWN     {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} LEFT     {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} RIGHT    {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} UP       {cp.reset_font()}
      {cp.set_font(1,209,16,1)}             {cp.reset_font()}

      Note: These options can be replaced for the original values.

      {cp.Unicode.BULLET} DOWN   \u2192  \"down\"
      {cp.Unicode.BULLET} LEFT   \u2192  \"left\"
      {cp.Unicode.BULLET} RIGHT  \u2192  \"right\"
      {cp.Unicode.BULLET} UP     \u2192  \"up\"


      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import custom_print as cp
      {cp.ins_chr(10)}  crs = cp.Cursor()
      {cp.ins_chr(10)}  crs.jumpTo(8, \"down\")
      {cp.ins_chr(10)}  crs.jumpTo(2, cp.Move.DOWN)

      Note: See Cursor Class for more examples.
    '''
    print(message)


def no_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[21])
    message = f'''
      {cp.set_font(1,209,16,1)}                                                                   {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} No Class has 256 options. To see them run the following code:  {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                                                   {cp.reset_font()}

      import custom_print as cp
      cp.bg_ansi_colors(bold=True, fg=0,  n_line=1)
      cp.fg_ansi_colors(bold=True, bg=-1, n_line=1)


      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import custom_print as cp
      {cp.ins_chr(10)}  blue_msg = cp.FancyMessage()
      {cp.ins_chr(10)}  blue_msg.body_bg   = cp.No.VERY_LIGHT_BLUE
      {cp.ins_chr(10)}  blue_msg.body_fg   = cp.No.GO_GREEN
      {cp.ins_chr(10)}  blue_msg.print_fancy_message(" This is a DEMO...! ")

      Note: These options can be replaced for the original values.

      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import custom_print as cp
      {cp.ins_chr(10)}  blue_msg = cp.FancyMessage()
      {cp.ins_chr(10)}  blue_msg.body_bg   = 14
      {cp.ins_chr(10)}  blue_msg.body_fg   = 35
      {cp.ins_chr(10)}  blue_msg.print_fancy_message(" This is a DEMO...! ")

      {cp.set_font(1,209,16,1)}                                                        {cp.reset_font()}
      {cp.set_font(1,209,16,1)} This class is used where a color needs to be assigned. {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                                        {cp.reset_font()}
'''
    print(message)


def style_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[23])
    message = f'''
      Style Class helps to customize the font style directly.
      The following are the options for the font to be used.

      {cp.set_font(1,209,16,1)}                                        {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} BOLD_ON           {cp.Unicode.BULLET}  BOLD_OFF       {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} DIM_ON            {cp.Unicode.BULLET}  DIM_OFF        {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} ITALIC_ON         {cp.Unicode.BULLET}  ITALIC_OFF     {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} UNDERLINE_ON      {cp.Unicode.BULLET}  UNDERLINE_OFF  {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} BLINKING_ON       {cp.Unicode.BULLET}  BLINKING_OFF   {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} INVERSE_ON        {cp.Unicode.BULLET}  INVERSE_OFF    {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} HIDDEN_ON         {cp.Unicode.BULLET}  HIDDEN_OFF     {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} STRIKE_ON         {cp.Unicode.BULLET}  STRIKE_OFF     {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} RESET_ALL         {cp.Unicode.BULLET}  OFF            {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                        {cp.reset_font()}

      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import custom_print as cp      
      '''
    
    print(message)
    print(cp.ins_chr(17),"print(f\"Normal {cp.Style.BOLD_ON}{cp.Style.ITALIC_ON}")
    print(cp.ins_chr(17),"{cp.Style.UNDERLINE_ON} I am Bold,Italic and Underline.")
    print(cp.ins_chr(17),"{cp.Style.OFF} Normal\")")  
    print()
    print(cp.ins_chr(17),"print(f\"{cp.Bg.SEA_BLUE}{cp.Style.BOLD_ON}{cp.Style.ITALIC_ON}")
    print(cp.ins_chr(17),"Hello There {cp.Style.OFF} Bye {cp.Bg.OFF}\")")
    print()
    print(cp.ins_chr(17),"print(f\"Normal {cp.Style.BOLD_ON}{cp.Style.ITALIC_ON}")
    print(cp.ins_chr(17),"{cp.Style.UNDERLINE_ON} Hello There {cp.Style.RESET_ALL} Bye")
    print()
    print(cp.ins_chr(17),"print(f\"{cp.Bg.SEA_BLUE}{cp.Fg.GREEN_YELLOW}{cp.Style.BOLD_ON}")
    print(cp.ins_chr(17),"{cp.Style.UNDERLINE_ON} Hello There {cp.reset_font()} Bye")

    message = f'''
      {cp.set_font(1,231,90)} \u25CF Output: {cp.reset_font()}
      {cp.ins_chr(11)} Normal {cp.Style.BOLD_ON}{cp.Style.ITALIC_ON}{cp.Style.UNDERLINE_ON} I am Bold,Italic and Underline. {cp.Style.OFF} Normal 

      {cp.ins_chr(11)} {cp.Bg.SEA_BLUE}{cp.Style.BOLD_ON}{cp.Style.ITALIC_ON} Hello There {cp.Style.OFF} Bye {cp.Bg.OFF}

      {cp.ins_chr(11)} {cp.Bg.SEA_BLUE}{cp.Fg.GREEN_YELLOW}{cp.Style.BOLD_ON}{cp.Style.UNDERLINE_ON} Hello There {cp.Style.RESET_ALL} Bye

      {cp.ins_chr(11)} {cp.Bg.SEA_BLUE}{cp.Fg.GREEN_YELLOW}{cp.Style.BOLD_ON}{cp.Style.UNDERLINE_ON} Hello There {cp.reset_font()} Bye
    
  {cp.set_font(1,196,231)} Note: {cp.reset_font()} Style.OFF only resets the styles options and not the Bg or Fg colors
          for the font. To reset the Bg and Fg colors, use the reset_font
          function or the Style.RESET_ALL class as shown in the examples above. 
          Be aware that Bg.OFF only turn off the Bg color and not the Fg color
          and vise versa. 
    '''
    print(message)



def unicode_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[25])
    
    message = f'''
    Unicode Class has a few options. More options can be found on website.

      {cp.set_font(1,209,16,1)}                                                {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_HORIZONTAL  {cp.Unicode.BOX_DRAWINGS_LIGHT_HORIZONTAL}             {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT  {cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT}     {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT  {cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT}      {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_VERTICAL            {cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL}     {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL  {cp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL}    {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL   {cp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL}     {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL {cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL} {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                                {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BLACK_UP_POINTING_TRIANGLE    {cp.Unicode.BLACK_UP_POINTING_TRIANGLE   }              {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} WHITE_UP_POINTING_TRIANGLE    {cp.Unicode.WHITE_UP_POINTING_TRIANGLE   }              {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BLAKC_RIGHT_POINTING_TRIANGLE {cp.Unicode.BLAKC_RIGHT_POINTING_TRIANGLE}              {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} WHITE_RIGHT_POINTING_TRIANGLE {cp.Unicode.WHITE_RIGHT_POINTING_TRIANGLE}              {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BLACK_DOWN_POINTING_TRIANGLE  {cp.Unicode.BLACK_DOWN_POINTING_TRIANGLE }              {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} WHITE_DOWN_POINTING_TRIANGLE  {cp.Unicode.WHITE_DOWN_POINTING_TRIANGLE }              {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BLACK_LEFT_POINTING_TRIANGLE  {cp.Unicode.BLACK_LEFT_POINTING_TRIANGLE }              {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} WHITE_LEFT_POINTING_TRIANGLE  {cp.Unicode.WHITE_LEFT_POINTING_TRIANGLE }              {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                                {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} RIGHT_ARROW                {cp.Unicode.RIGHT_ARROW}                 {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} LEFT_ARROW                 {cp.Unicode.LEFT_ARROW }                 {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} UP_ARROW                   {cp.Unicode.UP_ARROW   }                 {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} DOWN_ARROW                 {cp.Unicode.DOWN_ARROW }                 {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} UPWARDS_PAIRED_ARROWS      {cp.Unicode.UPWARDS_PAIRED_ARROWS   }                 {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} DOWNWARDS_PAIRED_ARROWS    {cp.Unicode.DOWNWARDS_PAIRED_ARROWS }                 {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} LEFTWARDS_PAIRED_ARROWS    {cp.Unicode.LEFTWARDS_PAIRED_ARROWS }                 {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} RIGHTWARDS_PAIRED_ARROWS   {cp.Unicode.RIGHTWARDS_PAIRED_ARROWS}                 {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BLACK_RIGHTWARDS_ARROWHEAD {cp.Unicode.BLACK_RIGHTWARDS_ARROWHEAD}                 {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                                {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} FIRE {cp.Unicode.FIRE}                                      {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} EYES  {cp.Unicode.EYES}                                     {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} POOP  {cp.Unicode.POOP}                                     {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} FACE {cp.Unicode.FACE}                                   {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} GHOST  {cp.Unicode.GHOST}                                    {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} CLOWN  {cp.Unicode.CLOWN}                                    {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BALLON  {cp.Unicode.BALLON}                                   {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BULLET {cp.Unicode.BULLET}                                     {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} COFFEE  {cp.Unicode.COFFEE}                                   {cp.reset_font()}       
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} EM_DASH {cp.Unicode.EM_DASH}                                    {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BLACK_CIRCLE {cp.Unicode.BLACK_CIRCLE}                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} WHITE_CIRCLE {cp.Unicode.WHITE_CIRCLE}                               {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} BLACK_DIAMOND   {cp.Unicode.BLACK_DIAMOND}                            {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} WHITE_DIAMOND   {cp.Unicode.WHITE_DIAMOND}                            {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} LOWERCASE_N_TILDE   {cp.Unicode.LOWERCASE_N_TILDE}                        {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} UPPERCASE_N_TILDE   {cp.Unicode.UPPERCASE_N_TILDE}                        {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} LEFT_CURLY_BRACKET  {cp.Unicode.LEFT_CURLY_BRACKET}                        {cp.reset_font()}
      {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} RIGHT_CURLY_BRACKET {cp.Unicode.RIGHT_CURLY_BRACKET}                        {cp.reset_font()}
      {cp.set_font(1,209,16,1)}                                                {cp.reset_font()}

      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import custom_print as cp  
                  print(cp.Unicode.FIRE) 

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()} {cp.Unicode.FIRE} 
      
    How Unicode Characters Work...!

    print Unicode with 2 digit value Use (\\x)
        1. print(\"\\x65\")  {cp.Unicode.RIGHT_ARROW}  \x65
        {cp.Unicode.EYES} \N{Eyes}
    
    print Unicode with 3 to 4 digit value Use (\\u)
        2. print(\"\\u0065\")  {cp.Unicode.RIGHT_ARROW}  \u0065
        3. print(\"\\u2757\")  {cp.Unicode.RIGHT_ARROW} \u2757

        
    print Unicode with 5 to 8 digit value Use (\\U)
        4. print(\"\\U00000065\")  {cp.Unicode.RIGHT_ARROW}  \U00000065
        5. print(\"\\U00002757\")  {cp.Unicode.RIGHT_ARROW}  \U00002757
        6. print(\"\\U0001F525 Fuego Code\")  {cp.Unicode.RIGHT_ARROW}  \U0001F525
        7. print(\"\\N{{FIRE}}   Fuego Name\")  {cp.Unicode.RIGHT_ARROW}  \N{FIRE}

        
    Print Unicode by Name: import unicodedata   -> may be necessary
        8. print("\\N{{LATIN SMALL LETTER A}}")         {cp.Unicode.RIGHT_ARROW}  \N{LATIN SMALL LETTER A}
        9. print("\\N{{NEGATIVE SQUARED CROSS MARK}}")  {cp.Unicode.RIGHT_ARROW}  \N{NEGATIVE SQUARED CROSS MARK}


    {cp.set_font(1,196,231)} Note: {cp.reset_font()} The U+2724 Unicode value is in Hexadecimal
        A. print(\"\\u2737\")         {cp.Unicode.RIGHT_ARROW}  \u2724
        B. print(\"\\U00002724\")     {cp.Unicode.RIGHT_ARROW}  \U00002724
        C. print(chr(0x2724))      {cp.Unicode.RIGHT_ARROW}  {chr(0x2724)}
        D. print(\"\\N{{HEAVY FOUR BALLOON-SPOKED ASTERISK}}\")  {cp.Unicode.RIGHT_ARROW}  \N{HEAVY FOUR BALLOON-SPOKED ASTERISK}

    {cp.set_font(1,190,16)} Reference: {cp.reset_font()} https://www.compart.com/en/unicode/category/So
                 https://www.vertex42.com/ExcelTips/unicode-symbols.html
                 https://unicodelookup.com
                 https://symbl.cc/en/unicode-table

    '''
    print(message)
    


# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: CURSOR_CLASS                                                                      |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  Cursor in custom_print Module                                                                  |
# +-------------------------------------------------------------------------------------------------+
def cursor_info():
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[26]) # Cursor
    mensaje =f'''
    All these functions are being used internally in the custom_print modules.
    It is available to the user if they find them usefull, otherwise, feel free
    to ignore them.

      Cursor can use the Move Class that has a few options.

      {cp.set_font(1,209,16,1)}             {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} DOWN     {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} LEFT     {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} RIGHT    {cp.reset_font()}
      {cp.set_font(1,209,16,1)}  {cp.Unicode.BULLET} UP       {cp.reset_font()}
      {cp.set_font(1,209,16,1)}             {cp.reset_font()}

      Note: These options can be replaced for the original values.

      {cp.Unicode.BULLET} DOWN   \u2192  \"down\"
      {cp.Unicode.BULLET} LEFT   \u2192  \"left\"
      {cp.Unicode.BULLET} RIGHT  \u2192  \"right\"
      {cp.Unicode.BULLET} UP     \u2192  \"up\"


    '''
    print(mensaje)
    jumpto_info()
    jumpxy_info()
    moveto_info()
    movexy_info()

def jumpto_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[27])
    message = f'''
   
      This method jumps rows or columns for the cursor in the terminal.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  crs = cp.Cursor()
      {cp.ins_chr(10)}  crs.jumpTo(qty=2,  direction = cp.Move.DOWN)
      {cp.ins_chr(10)}  print("I am down")
      {cp.ins_chr(10)}  crs.jumpTo(qty=20, direction = "right") 
      {cp.ins_chr(10)}  print("I am right")
      {cp.ins_chr(10)}  crs.jumpTo(1, cp.Move.UP)      
      {cp.ins_chr(10)}  print("I am up")
      {cp.ins_chr(10)}  crs.jumpTo(5, "down")                    
      {cp.ins_chr(10)}  print("GoodBye...!")

   '''
    print(message)

def jumpxy_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[28])
    message = f'''
   
      This method jumps the cursor to specific coordinates in the terminal.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  crs = cp.Cursor()
      {cp.ins_chr(10)}  crs.jumpToxy(0,0);     print("*** Start Here ***")
      {cp.ins_chr(10)}  crs.jumpToxy(20, 5);   print("GoodBye...!")      

   '''
    print(message)


def moveto_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[29])
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
    

def movexy_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[30])
    message = f'''
   
      This method moves the cursor to specific coordinates in the terminal.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  crs = cp.Cursor()
   '''
    message2 = '''                  print(f"{crs.movexy(15,40)}hello again")

      '''
    print(message)
    print(message2)



# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: FONTSTYLE_CLASS                                                                   |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  FontStyle in custom_print Module                                                               |
# +-------------------------------------------------------------------------------------------------+
def fontstyle_info():
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[31]) # Help Classes
    message = f'''
     This class contains 4 methods and the attributes and their default values
       are displays below.

    {cp.set_font(1,209,16,1)}                                                 {cp.reset_font()}
    {cp.set_font(1,209,16,1)}                General Use                      {cp.reset_font()}
    {cp.set_font(1,209,16,1)}                                                 {cp.reset_font()}
    {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} bg     = -1             {cp.Unicode.BULLET} bold      = False   {cp.reset_font()}
    {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} fg     = -1             {cp.Unicode.BULLET} underline = False   {cp.reset_font()}
    {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} dim    = False          {cp.Unicode.BULLET} blinking  = False   {cp.reset_font()}
    {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} hidden = False          {cp.Unicode.BULLET} italic    = False   {cp.reset_font()}
    {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} strike = False          {cp.Unicode.BULLET} inverse   = False   {cp.reset_font()}
    {cp.set_font(1,209,16,1)}                                                 {cp.reset_font()}
    {cp.set_font(1,209,16,1)}                Print_Style                      {cp.reset_font()}
    {cp.set_font(1,209,16,1)}                                                 {cp.reset_font()}
    {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} align = Align.JUSTIFY   {cp.Unicode.BULLET} bg_top_lines    = 0 {cp.reset_font()}
    {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} forced_align = False    {cp.Unicode.BULLET} bg_bottom_lines = 0 {cp.reset_font()}
    {cp.set_font(1,209,16,1)} {cp.Unicode.BULLET} indent = 0                                    {cp.reset_font()}    
    {cp.set_font(1,209,16,1)}                                                 {cp.reset_font()}
    

    {cp.set_font(1,196,231)} Note: {cp.reset_font()} indent is used for style_on and for print_style when using justify.
            indent → This defines how far we want to start to print the message
                     from the left of the terminal.

'''

    print(message)

    
    start_style_info()
    stop_style_info()
    print_style_info()
    reset_style_info()


def start_style_info(): 
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[32])
    print("start_style method")
def stop_style_info():  
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[33])
    print("stop_style method")
def print_style_info(): 
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[34])
    print("print_style method")
def reset_style_info(): 
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[35])
    print("reset_style method")


# all_topics = [
#     "Screen_Functions",  "clean", "clear","dimensions", "erase", "resize",                                                                                               # 0, 1, 2, 3, 4, 5,

#     "Internal_Functions", "ansi_colors", "ins_chr", "ins_newline", "set_reset_font", "terminal_bell",                                                                    # 6, 7, 8, 9, 10, 11

#     "Help_Classes",  "align", "length_bg", "ascii_letter", "line_style", "bg", "logo", "move", "divider_style", "no", "fg", "style", "layout", "unicode",                # 12 - 25,

#     "Cursor",  "jumpto", "jumpxy", "moveto", "movexy",                                                                                                                   # 26, 27, 28, 23, 30,

#     "Fontstyle",  "start_style", "stop_style", "print_style", "reset_style",                                                                                             # 31, 32, 33, 34, 35,

#     "FancyMessage",  "print_fancy_message", "print_fancy_note",                                                                                                          # 36, 37, 38,

#     "Pen",  "draw_line", "draw_rectangle",                                                                                                                               # 39, 40, 41,

#     "Divider",  "print_fancy_divider",                                                                                                                                   # 42, 43,

#     "FancyFormat",  "fancyformat", "print_fancy_format", "reset_fancy_format",                                                                                           # 44, 45, 46, 47,

#      "AsciiArt", "print_ascii_art", "print_multi_ascii_art", "print_ascii_logo_art", "print_reversed_ascii_logo_art"]                                                    # 48, 49, 50, 51, 52.
# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: FANCYMESSAGE_CLASS                                                                |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  FancyMessage in custom_print Module                                                            |
# +-------------------------------------------------------------------------------------------------+
def fancymessage_info():
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[12]) # Help Classes
    mensaje ='''
    neeed works here here here here here  All these functions are being used internally in the custom_print modules.
    It is available to the user if they find them usefull, otherwise, feel free
    to ignore them.
    '''
    print(mensaje)
    print_fancy_message_info()
    print_fancy_note_info()


def print_fancy_message_info(): print("print_fancy_message method")
def print_fancy_note_info():    print("print_fancy_note method")

# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: PEN_CLASS                                                                         |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  Pen in custom_print Module                                                                     |
# +-------------------------------------------------------------------------------------------------+
def pen_info():
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[12]) # Help Classes
    mensaje ='''
    neeed works here here here here here  All these functions are being used internally in the custom_print modules.
    It is available to the user if they find them usefull, otherwise, feel free
    to ignore them.
    '''
    print(mensaje)
    draw_line_info()
    draw_rectangle_info()

def draw_line_info():      print("draw_line method")
def draw_rectangle_info(): print("draw rectangle method")
# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: DIVIDER_CLASS                                                                     |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  Divider in custom_print Module                                                                 |
# +-------------------------------------------------------------------------------------------------+
def divider_info():
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[12]) # Help Classes
    mensaje ='''
    neeed works here here here here here  All these functions are being used internally in the custom_print modules.
    It is available to the user if they find them usefull, otherwise, feel free
    to ignore them.
    '''
    print(mensaje)
    print_fancy_divider_info()

def print_fancy_divider_info(): print("print_fancy_divider method")





# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: FANCYFORMAT_CLASS                                                                 |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  FancyFormat in custom_print Module                                                             |
# +-------------------------------------------------------------------------------------------------+
def fancyformat_info():
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[12]) # Help Classes
    mensaje ='''
    neeed works here here here here here  All these functions are being used internally in the custom_print modules.
    It is available to the user if they find them usefull, otherwise, feel free
    to ignore them.
    '''
    print(mensaje)
    print_fancy_format_info()
    reset_fancy_format_info()


def print_fancy_format_info(): print("print_fancy_format method")
def reset_fancy_format_info(): print("reset_fancy_format method")


# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: ASCIIART_CLASS                                                                    |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  AsciiArt in custom_print Module                                                                |
# +-------------------------------------------------------------------------------------------------+
def asciiart_info():
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[12]) # Help Classes
    mensaje ='''
    neeed works here here here here here  All these functions are being used internally in the custom_print modules.
    It is available to the user if they find them usefull, otherwise, feel free
    to ignore them.
    '''
    print(mensaje)
    print_ascii_art_info()
    print_multi_ascii_art_info()
    print_ascii_logo_art_info()
    print_reversed_ascii_logo_art_info()


def print_ascii_art_info():                print("ascii_art method")
def print_multi_ascii_art_info():          print("multi_ascii_art method")
def print_ascii_logo_art_info():           print("ascii_logo_art method")
def print_reversed_ascii_logo_art_info():  print("reversed_ascii_logo_art method")


if __name__ == '__main__':
    print(sys.argv)
    help_documentation()

# in the top insert a new line(group name) cp.ins_newline(1), before the divider
# in the top insert a newline for message and the tail a newline for the message
# at the end of the function or method add double newline.
# this will be the parttern for title and tail of the function class





#     message = '''
# '''
#     white_msg.print_fancy_note(message)

#     cp.ins_newline(2)

#     purple_msg.print_fancy_message("No Class")
#     message = f'''
#     If using the number is hard to remember the color, the No Class can be used to sustitute the
#     number for the name as the example below. Use the bg_ansi_colors or fg_ansi_colors methods
#     to learn the names of the colors available in custom_print.

#        {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
#                    print(cp.set_font(True,cp.No.DARKISH_YELLOW,cp.No.BLUE) + " Python is " +
#                     cp.set_font(False,cp.No.RED) + " Wonderful." + cp.reset_font())
#     '''
#     print(message)
#     print(f"       {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}\
# {cp.set_font(1,cp.No.DARKISH_YELLOW,cp.No.BLUE)} Python is {cp.set_font(False,cp.No.RED)} Wonderful. {cp.reset_font()}")
#     print()
#     message = '''Remember that we are still using the number, but using the name of the color.'''
#     white_msg.print_fancy_note(message)
#     print(){cp.set_font(1,209,16,1)}
#     print(f"{cp.Fg.AQUA}No Class {cp.Fg.OFF}can be used where a number color is required for example with FontStyle class,\
#  FancyMessage class, FancyFormat class, etc.\n")

#     purple_msg.print_fancy_message("Bg, Fg, and Style Classes")
#     print()
#     message =f'''
#        Style values:

#        1) bold=False      4) italic=False         7) blinking=False
#        2) inverse         5) underline=False      8) dim=False
#        3) hidden          6) strike=False

#        Bg and Fg colors name use the bg_ansi_colors function or fg_ansi_colors function
#        to learn more the name of the colors available in custom_print.

#        {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp'''

#     print(message)
#     print("                   print(f\"{cp.Bg.WHITE+cp.Fg.BLUEBERRY_PURPLE} Background and Foreground")
#     print("                   {cp.Bg.OFF} Only Foreground {cp.Fg.OFF} Normal....! \"\n")

#     print(f"       {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  {cp.Bg.WHITE+cp.Fg.BLUEBERRY_PURPLE} Background and Foreground {cp.Bg.OFF} Only Foreground {cp.Fg.OFF} Normal....!\n")

#     message = f'''       {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp'''
#     print(message)
#     print("                   print(f\"{cp.Style.UNDERLINE_ON} Underline Style {cp.Style.UNDERLINE_OFF} Normal\"")

#     print(f"\n       {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}",end="")
#     print(f" {cp.Style.UNDERLINE_ON} UnderOnly Style {cp.Style.UNDERLINE_OFF} Normal....! \"\n")
#     print("ansi_colors_info here")
