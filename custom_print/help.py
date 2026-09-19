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
    "Screen_Functions",  "clean", "clear","dimensions", "erase", "resize",

    "Internal_Functions", "ansi_colors", "get_list_type", "ins_chr", "ins_newline", "move_cursor_right", "set_reset_font", "subscript", "superscript", "terminal_bell",

    "Help_Classes",  "Align", "Ascii_Letter", "Bg", "Divider_Style", "Fg", "Layout", "Length_Bg", "Line_Style", "Logo", "Move",  "No",  "Style",  "Unicode",

    "Cursor",  "jumpTo", "jumpxy", "moveTo", "movexy",

    "Fontstyle",  "style_on_off", "reset_style", "print_style",

    "FancyMessage",  "print_fancy_message", "print_fancy_note", "get_message_attributes",

    "Pen",  "draw_line", "draw_rectangle",

    "Divider",  "print_fancy_divider",

    "FancyFormat", "print_fancy_format", "reset_fancy_format",

     "AsciiArt", "print_ascii_art", "print_multi_ascii_art", "print_ascii_logo_art", "print_reversed_ascii_logo_art"]


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

    tbl.title_italic = True
    tbl.title_bold   = True
    tbl.title_bg = 90
    tbl.title_fg = 231
    tbl.title_align = cp.Align.CENTER

    # classes and methods for custom_print module
    screen_funs        = [[" Screen_Functions "], ["clean"], ["clear"], ["dimensions"], ["erase"], ["resize"]]

    internal_functions = [["ansi_colors", "set_reset_font"], ["get_list_type", "subscript"], ["ins_chr", "superscript"], ["ins_newline", "terminal_bell"], ["move_cursor_right", "    "]]


    help_classes       = [["Align", "Line_Style"], ["Ascii_Letter", "Logo"],["Bg", "Move"], ["Divider_Style", "No"],["Fg", "Style"],["Layout", "Unicode"],["Length_Bg", "    "]]

    cmcpp1 = [["Cursor",    "FontStyle",       "FancyMessage",             "Pen"           ],
              ["jumpTo",    "style_on_off",    "print_fancy_message",      "draw_line"     ],
              ["jumpxy",    "reset_style",     "print_fancy_note"   ,      "draw_rectangle"],
              ["moveTo",    "print_style",     "get_message_attributes",   "    "          ],
              ["movexy",    "    ",            "    ",                     "    "          ]]

    cmcpp2 = [["Divider",              "FancyFormat"       ],
              ["print_fancy_divider",  "print_fancy_format"],
              ["    ",                 "reset_fancy_format"],
              ["    ",                 "    "              ],
              ["    ",                 "    "              ]]


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
    crs.jumpTo(qty=8,direction=cp.Move.UP)
    tbl.header_horizontal_line_on = False

    tbl.title_msg  = " Internal_Functions "
    tbl.header_bg  = -1; tbl.header_bold = False
    tbl.print_fancy_format(internal_functions)
    tbl.adj_indent = 2
    cp.ins_newline(n=1)
    mensaje = "Classes and Methods in custom_print Module"
    blue_msg.left_indent = int(((cols)-(len(mensaje)))/2)
    blue_msg.print_fancy_message(mensaje)
    cp.ins_newline(n=1)


    tbl.header_italic = False
    tbl.header_bold   = False
    tbl.header_bg = -1
    tbl.header_fg = -1
    tbl.header_align = cp.Align.JUSTIFY

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


    print("   To display help for a specific function or method just pass the name of the\n   parameter as shown above.")
    cp.ins_newline(1)
    print(f"{fst.style_on()} Example 1: {fst.style_off()}  custom_print clean")

    note=" Note: "
    #                   20                   40                   60                   80   85   90
    message_note = '''
 It is possible to display the documentation for multiple
 functions or methods simultaneously by passing them as parameters.
 Alternatively, you can display the documentation for all methods
 within a specific group, a class, or any combination of these.
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
    print(f"{fst.style_on()} Example 2: {fst.style_off()}  custom_print screen_functions ins_chr movexy\n" )


    message = f'''       Notice that on\033[1m example 2\033[0m, is being called a group (screen_functions),
       a function (ins_chr) and a method (movexy). For the group, it will be
       displayed all the documentation that belong to
       that group.

       {fst.style_on()} screen_functions: clean, clear, dimensions, erase, resize. {fst.style_off()}

       It will display the documentation for the function \033[1;48;5;22m ins_chr \033[0m as well.

       Documentation for the method \033[1;48;5;22;1m movexy \033[0m will be called as well.

       The above tables show all the groups for functions and classes with their
       methods.

{fst.style_on()} example 3: {fst.style_off()}  custom_print cursor

       It will call  all the documentation for the entire group.

    {fst.style_on()} cursor: jumpTo, jumpxy, moveTo, movexy. {fst.style_off()}

   {cp.set_font(1,196,231)} Note: {cp.reset_font()} If you only wish to see the documentation of the class (cursor),
           then we have to add the word \033[1;48;5;22;1m _only \033[0m as show below.

{fst.style_on()} example 3: {fst.style_off()}  custom_print cursor_only

       It's possible to display the complete documentation help by passing
       \"all\" or \"documentation\" as a parameter.

{fst.style_on()} example 4: {fst.style_off()}  custom_print all
                 custom_print documentation

    '''
    print(message)
    message = f'''
    \N{BULLET} custom_print module has been tested on RedHat 9, Centos Stream 9,
      AlmaLinux 9, and Windows 10.

    \N{BULLET} custom_print module requires python3.12 or greater.

    \N{BULLET} https://github.com/acma82/Custom_Print/tree/main/readme
    '''


    blue_msg.body_bg   = 90
    blue_msg.body_fg   = 231
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
    pen_info()
    divider_info()
    fancyformat_info()
    asciiart_info()




# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: SCREEN_FUNCTIONS                                                                  |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  Screen_Functions in custom_print Module                                                        |
# +-------------------------------------------------------------------------------------------------+
def screen_functions_only_info():
    ''' It uses ansi code or OS command to manipulate the screen on the terminal. '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[0])
    mensaje = f'''
      There are five functions to manipulate the screen on the terminal.
      It is used \"ansi code\" or \"OS command\" to manipulate the screen on the terminal.
      Be aware that on some OS some of these functions may NOT work properly.

      {cp.set_font(1,196,231)} Note: {cp.reset_font()}

      {cp.set_font(1,231,196)} clean      : {cp.reset_font()}  This function uses the ansi code.
      {cp.set_font(1,231,196)} clear      : {cp.reset_font()}  This functions uses the OS command.
      {cp.set_font(1,231,196)} dimensions : {cp.reset_font()}  This functions uses the OS command.
      {cp.set_font(1,231,196)} erase      : {cp.reset_font()}  This function uses the ansi code.
      {cp.set_font(1,231,196)} resize     : {cp.reset_font()}  This functions uses the OS command.

      {cp.set_font(1,231,22)} resize {cp.reset_font()} This functionality is verified for GNOME and Xfce terminals;
               compatibility with other terminal emulators, such as Konsole, is
               not guaranteed.
    '''
    print(mensaje)


def screen_functions_info():
    ''' It uses ansi code to manipulate the screen on the terminal. '''
    screen_functions_only_info()
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
    message = f'''
      It clears the terminal and returns the cursor to home.
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
    menssage =f'''
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
    menssage = f'''
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
    message = f'''
      It resizes the terminal size.
    '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[5]+"(rows=25, cols=80)")
    print(message)
    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp")
    print(f"{cp.ins_chr(18)}cp.resize(rows=20, cols=120)\n")





# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: INTERNAL_FUNCTIONS                                                                |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  Internal_Functions in custom_print Module                                                      |
# +-------------------------------------------------------------------------------------------------+
def internal_functions_only_info():
    ''' These functions are used for the classes. '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[6])
    message =f'''
    All these functions are used internally by the Custom_Print module. However,
    they are also exposed to the user. Feel free to use them if you find them
    useful, or simply ignore them if not needed.

    '''
    print(message)


def internal_functions_info():
    ''' These functions are used for the classes. '''
    internal_functions_only_info()
    ansi_colors_info()
    get_list_type_info()
    ins_chr_info()
    ins_newline_info()
    move_cursor_right_info()
    set_reset_font_info()
    subscript_info()
    superscript_info()
    terminal_bell_info()

#------------------------------------------------------------------------------------------------
# ansi_colors                                                                                   -
#------------------------------------------------------------------------------------------------
def ansi_colors_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[7])
    message = f'''
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  bg_ansi_colors(bold=False, fg=-1, n_line=0)  {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  bg colors available in the ansi code         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
    '''
    print(message)
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
        print (u"\u001b[0m")

    message = f'''
      This function displays all available background colors using ANSI codes.
      The following options improve visualization:

      1. bold (bool): Apply bold font (True/False).
      2. fg: Foreground color used when displaying the background colors.
      3. n_line: Number of blank lines to insert between the colors.


      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  cp.bg_ansi_colors(bold=True, fg=22, n_line=1)
    '''
    print(message)

    cp.ins_newline(2)

    message = f'''
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  fg_ansi_colors(bold=False, bg=-1, n_line=0)  {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  fg colors available in the ansi code         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
    '''
    print(message)
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        print (u"\u001b[0m")


    message = f'''
      This function displays all available foreground colors using ANSI codes.
      The following options improve visualization:

      1. bold (bool): Apply bold font (True/False).
      2. bg: Background color used when displaying the foreground colors.
      3. n_line: Number of blank lines to insert between the colors.


      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  cp.fg_ansi_colors(bold=True, bg=22, n_line=1)
    '''
    print(message)

    message = f'''
      {cp.set_font(1,196,231)} Note: {cp.reset_font()} These 2 functions will display the name and number of the colors.
              It will be handy when the user start using the Help_Classes. To
              set the default color for bg or fg, set the value to -1 or 256.
    '''
    print(message)



#------------------------------------------------------------------------------------------------
# get_list_type                                                                                 -
#------------------------------------------------------------------------------------------------
def get_list_type_info():
    ''' return the type list according to FancyFormat Class. '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[8])
    message = f'''
      {cp.set_font(0,53,231,0)}                                   {cp.ins_chr(38," ")}{cp.reset_font()}
      {cp.set_font(0,53,231,0)}  get_list_type(my_list:list)->str {cp.ins_chr(38," ")}{cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                   {cp.ins_chr(38," ")}{cp.reset_font()}

      This function return the type of list according to FancyFormat class.

      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  List = l              Return                       Example             {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}   {cp.set_font(1,231,21,True)} Case 0: {cp.set_font(0,53,231,0)} {cp.ins_chr(60," ")}{cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  not a list type    \"incorrect_variable_type\"     get_list_type(25)     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}   {cp.set_font(1,231,21,True)} Case 1: {cp.set_font(0,53,231,0)} {cp.ins_chr(60," ")}{cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  []                 \"empty_list\"                  get_list_type([])     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}   {cp.set_font(1,231,21,True)} Case 2: {cp.set_font(0,53,231,0)} {cp.ins_chr(60," ")}{cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  [1]                \"one_item_no_row\"             get_list_type([1])    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}   {cp.set_font(1,231,21,True)} Case 3: {cp.set_font(0,53,231,0)} {cp.ins_chr(60," ")}{cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  [1,2,3]             \"multiple_items_no_row\"      get_list_type(l)      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}   {cp.set_font(1,231,21,True)} Case 4: {cp.set_font(0,53,231,0)} {cp.ins_chr(60," ")}{cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  [[1]]               \"one_item_one_row\"           get_list_type([l])    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}   {cp.set_font(1,231,21,True)} Case 5: {cp.set_font(0,53,231,0)} {cp.ins_chr(60," ")}{cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  [[1,2,3]]           \"multiple_items_one_row\"     get_list_type([l])    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}   {cp.set_font(1,231,21,True)} Case 6: {cp.set_font(0,53,231,0)} {cp.ins_chr(60," ")}{cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  [[1],[4],[7]]       \""multiple_items_multiple_rows\"  get_list_type([l]){cp.reset_font()}
      {cp.set_font(0,53,231,0)}  [[1,2,3],[4,5,6],[7,8,9]]                                              {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  [[1],[1,2,3],[5,4,7,8]]                                                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  [[1,2,3],[[2],3,4],[5,[6,7]]]                                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  any combination of this is case 6                                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}   {cp.set_font(1,231,21,True)} Case 7: {cp.set_font(0,53,231,0)} {cp.ins_chr(60," ")}{cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  [5,6,[1,2,3],[1,0,3]]     \"mix_items\"            get_list_type([l])    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  [[1,2],[1,2,[1]],[1,2,3]]                                              {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  any combination of this is case 7                                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}


      {cp.set_font(1,231,0)} Example 1: {cp.reset_font()}  import custom_print as cp
                    lista_type = cp.get_list_type([1,2,3])
                    print(lista_type)

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}    multiple_items_no_row

    '''
    print(message)


#------------------------------------------------------------------------------------------------
# ins_chr                                                                                       -
#------------------------------------------------------------------------------------------------
def ins_chr_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[9])
    message = f'''
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  ins_chr(n=1)                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}

      There are 7 Cases.


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
    green_div.print_fancy_divider(all_topics[10])
    message = f'''
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  ins_newline(n=1)                             {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}

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
# move_cursor_right                                                                             -
#------------------------------------------------------------------------------------------------
def move_cursor_right_info():
    ''' Move cursor to right '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[11])
    message = f'''
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  move_cursor_right(n=20, option_space=True)   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  option True, it will print spaces n times.   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  option False, it won't print spaces only     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  will move the cursor.                        {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: {cp.reset_font()} import custom_print as cp
                 print(f\"{{cp.move_cursor_right(n=12, option_space=True)}}Hello")
                 print(f\"{{cp.move_cursor_right(n=12, option_space=False)}}Hello")

    '''
    print(message)
#------------------------------------------------------------------------------------------------
# set_font and reset_font                                                                       -
#------------------------------------------------------------------------------------------------
def set_reset_font_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[12])
    message = f'''
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  set_font(parameters)                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  reset_font()                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}

      Colors range goes from -1 to 256.
      To set the default color from the system use -1 or 256,
      for both bg and fg.

      blinking might not work in all the OS. We use Red Hat Family.


       reset_font()   This function resets the font attributes to the default
                      values when we use the set_font() function.

       set_font()     This function changes the font attributes, bg, fg,
                      bold, italic, and so on.


       {cp.set_font(1,231,16)} Default Values {cp.reset_font()}

       1)  bold    = False    4) italic    = False    7) blinking = False
       2)  bg      = -1       5) underline = False    8) dim      = False
       3)  fg      = -1       6) strike    = False    9) hidden   = False
       10) inverse = False

       This function allows you to configure multiple font attributes. However,
       passing all these parameters can be cumbersome. For a more convenient
       approach, use the Bg, Fg, or Style classes described in the Font Color
       section, or use the Font_Style class instead.

       It is recommended to only pass the first three parameters, as shown in
       the example below.

       {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                   print(cp.set_font(1,11,21) + " Python is " +
                   cp.set_font(0,1) + " Wonderful." + cp.reset_font()) +
                   " Default."

        {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  {cp.set_font(1,11,21)} Python is {cp.set_font(0,1)} Wonderful. {cp.reset_font()} Default.


      {cp.set_font(1,196,231)} Note: {cp.reset_font()} These functions are being used by some classes.
              Feel free to ignore them if not useful to you.
    '''
    print(message)

#------------------------------------------------------------------------------------------------
# subscript                                                                                     -
#------------------------------------------------------------------------------------------------
def subscript_info():
    ''' It Prints Subscript Mode'''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[13])
    message = f'''
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  subscript(x)                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  x can be any type as long as it exist in the {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  subscript dictionary.                        {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  print(f\"Water: H{{cp.subscript("2+x")}}O\" + 5")
                  print(f\"Water: H{{cp.subscript(2)}}O\" + 5")


      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  Water: H{cp.subscript("2x")}O + 5
                  Water: H{cp.subscript(2)}O + 5

      {cp.set_font(1,196,231)} Note: {cp.reset_font()}     If the symbol digit is not in the subscript_map, then it
                  will set to ? which is the default value.


        {cp.set_font(1,231,22,1)} subscript_map contains the following characters: {cp.reset_font()}
        a, e, h, i, j, k, l, m, n, o, p, r, s, t, u, v, x,
        0, 1, 2, 3, 4, 5, 6, 7, 8' 9, +, -, =, (, )


        {cp.set_font(1,231,22,1)} subscript_map DOES NOT contains the following characters: {cp.reset_font()}
        b, c, d, f, g, q, w, y, z,
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T,
        U, V, W, X, Y, Z
    '''
    print(message)

#------------------------------------------------------------------------------------------------
# superscript                                                                                   -
#------------------------------------------------------------------------------------------------
def superscript_info():
    ''' It Prints Superscript Mode'''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[14])
    message = f'''
      {cp.set_font(0,53,231,0)}                                                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  superscript(x)                                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  x can be any type as long as it exists in the {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  superscript dictionary.                       {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  print(f\"Power: X{{cp.superscript("5+v")}} + 5\")
                  print(f\"Power: X{{cp.superscript(5)}} + 5\")

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  Power: X{cp.superscript("5+v")} + 5
                  Power: X{cp.superscript(5)} + 5

      {cp.set_font(1,196,231)} Note: {cp.reset_font()}     If the symbol digit is not in the superscript_map, then it
                  will set to ? which is the default value.


        {cp.set_font(1,231,22,1)} superscript_map contains the following characters: {cp.reset_font()}
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, r, s, t, u, v, w, x, y,
        A, B, D, E, G, H, I, J, K, L, M, N, O, P, R, T, U, V, W,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        +, -, =, (, )


        {cp.set_font(1,231,22,1)} superscript_map DOES NOT contains the following characters: {cp.reset_font()}
        q, z,
        C, F, Q, S, X, Y,
        Z
   '''
    print(message)


#------------------------------------------------------------------------------------------------
# terminal_bell                                                                                 -
#------------------------------------------------------------------------------------------------
def terminal_bell_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[15])
    message = f'''
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  terminal_bell()                              {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}

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
def help_classes_only_info():
    ''' It helps to the other class. '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[16])
    mensaje ='''
    These classes are designed to help users avoid misspelling instructions
    when using other classes, methods, or functions. While you can still use
    default values directly, it is strongly recommended to use these helper
    classes.
    '''
    print(mensaje)


def help_classes_info():
    ''' It helps to the other class. '''
    help_classes_only_info()
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

#------------------------------------------------------------------------------------------------
# align                                                                                         -
#------------------------------------------------------------------------------------------------
def align_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[17])
    message = f'''
      This class is used where alignment is needed. It contains 4 options.

      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Align.RIGHT      {cp.Unicode.BULLET} Align.CENTER            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Align.LEFT       {cp.Unicode.BULLET} Align.JUSTIFY           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                               {cp.reset_font()}

      This class makes the alignment for data.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  msg = cp.FancyMessage()
                  msg.title_align = cp.Align.CENTER
                  msg.footnote_align = "right"
                # msg.footnote_align = "r"  -> Same as above


      {cp.set_font(1,196,231)} Note: {cp.reset_font()} Although {cp.set_font(1,231,22,1)} Align.NONE {cp.reset_font()} exist, it is only used with the FontStyle
              Class using the method {cp.set_font(1,231,22,1)} print_style. {cp.reset_font()} For examples check their
              documentation.

      '''
    print(message)
    lista = [["Align.RIGHT","Align.LEFT", "Align.CENTER","Align.JUSTIFY"],
             ['\"right\"','\"left\"','\"center\"','\"justify\"'],
             ['\"r\"', '\"l\"', '\"c\"', '\"j\"']]
    tbl.print_fancy_format(data=lista, style=cp.Line_Style.TURQUOISE_BLACK)
    print(f"\n      {cp.set_font(1,196,231)} Note: {cp.reset_font()} See FancyFormat Class or FancyMessage Class to visualize \n              a complete example.\n\n")


#------------------------------------------------------------------------------------------------
# ascii_letter                                                                                  -
#------------------------------------------------------------------------------------------------
def ascii_letter_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[18])
    message = f'''
      This class is used mainly with AsciiArt class. It contains 23 options.

      {cp.set_font(0,53,231,0)}                                           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Alpha            {cp.Unicode.BULLET} Larry               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} ANSI_Shadow      {cp.Unicode.BULLET} Money_NE            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Big              {cp.Unicode.BULLET} Money_NW            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Blocks           {cp.Unicode.BULLET} Money_SE            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Bulbhead         {cp.Unicode.BULLET} Money_SW            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Classy           {cp.Unicode.BULLET} Mono                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Colosal          {cp.Unicode.BULLET} Moon                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Crazy            {cp.Unicode.BULLET} Moon2               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Doh              {cp.Unicode.BULLET} Roman               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Doom             {cp.Unicode.BULLET} Standard            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Epic             {cp.Unicode.BULLET} Sweet               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Graceful                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                           {cp.reset_font()}

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
    print(f"\n  {cp.set_font(1,196,231)} Note: {cp.reset_font()} See the AsciiArt Class to visualize a complete example.\n\n")


#------------------------------------------------------------------------------------------------
# bg                                                                                            -
#------------------------------------------------------------------------------------------------
def bg_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[19])
    message = f'''
      This class is mainly used where background color is needed.

      {cp.set_font(0,53,231,0)}                                                            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} See \"ansi_colors\" function to see all the bg color names {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                            {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp  '''
    print(message)
    print("                  print(f\"{cp.Bg.SEA_BLUE} Hello There {cp.Bg.OFF} Bye \" )")

    message = f'''
      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  {cp.Bg.SEA_BLUE} Hello There {cp.Bg.OFF} Bye

    '''
    print(message)
    # cp.bg_ansi_colors(bold=True, fg=0, n_line=1)


#------------------------------------------------------------------------------------------------
# divider_style                                                                                 -
#------------------------------------------------------------------------------------------------
def divider_style_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[20])
    message = f'''
      This class is with Divider class. It contains 10 options.

      {cp.set_font(0,53,231,0)}                                           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} CUSTOMIZED   = \"customized\"            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SINGLE_LINE  = \"single_line\"           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SINGLE_BOLD  = \"single_bold\"           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SINGLE_HEAVY = \"single_heavy\"          {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} DOUBLE_LINE  = \"double_line\"           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} DASH_1       = \"dash_1\"                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} DASH_2       = \"dash_2\"                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SQ_BRACKETS  = \"sq_brackets\"           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} BLUE_WHITE_1 = \"blue_white_1\"          {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} BLUE_WHITE_2 = \"blue_white_2\"          {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                           {cp.reset_font()}

      This class select the type of style for the divider to be used.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  div = cp.Divider()
                  div.print_fancy_divider(message = " Custom Print Divider",
                                          style   = cp.Divider_Style.DASH_2)
      '''
    print(message)
    print(f"\n      {cp.set_font(1,196,231)} Note: {cp.reset_font()} See the Divider class to visualize a complete example.\n\n")


#------------------------------------------------------------------------------------------------
# fg                                                                                            -
#------------------------------------------------------------------------------------------------
def fg_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[21])
    message = f'''
      This class is mainly used where foreground color is needed.

      {cp.set_font(0,53,231,0)}                                                            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} See ansi_colors function to see all the fg color names   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                            {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp  '''
    print(message)
    print("                  print(f\"{cp.Fg.SEA_BLUE} Hello There {cp.Fg.OFF} Bye \" )")

    message = f'''
      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}  {cp.Fg.SEA_BLUE} Hello There {cp.Fg.OFF} Bye
    '''
    print(message)


#------------------------------------------------------------------------------------------------
# layout                                                                                        -
#------------------------------------------------------------------------------------------------
def layout_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[22])

    message = f'''
      This class is used with FancyFormat class.

      {cp.set_font(0,53,231,0)}                                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Layout.HORIZONTAL           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Layout.VERTICAL             {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: Range type, vertical layout {cp.reset_font()}

                  import custom_print as cp
                  tbl  = cp.FancyFormat()
                  x    = range(0,16,2)

                  tbl.set_layout   = cp.Layout.VERTICAL
                  tbl.title_msg    = " Range Data"
                  tbl.footnote_msg = " Case 5 "
                  tbl.print_fancy_format(x)


      {cp.set_font(1,196,231)} Note: {cp.reset_font()} These 2 options can be replaced by their original values.

      {cp.ins_chr(10)}  Layout.HORIZONTAL   \u2192  \"horizontal\"
      {cp.ins_chr(10)}  Layout.VERTICAL     \u2192  \"vertical\"

'''
    print(message)
    print(f"\n      {cp.set_font(1,196,231)} Note: {cp.reset_font()} See the FancyFormat class to visualize a complete example.")
    print("              Layout works with Range, Set, Frozenset and Dictionary types.")


#------------------------------------------------------------------------------------------------
# length_bg                                                                                     -
#------------------------------------------------------------------------------------------------
def length_bg_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[23])

    message = f'''
      This class is used with FancyMessage class.

      {cp.set_font(0,53,231,0)}                            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} ALL_ROW   = 1           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} ONLY_WORD = 2           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                            {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: Range type, vertical layout {cp.reset_font()}

                  import custom_print as cp
                  msg = cp.FancyMessage()
                  paragraph1 = \" First paragraph,  Last  paragraph \"
                  msg.length = cp.Length_Bg.ONLY_WORD
                  msg.print_fancy_message(paragraph1)

      {cp.set_font(1,196,231)} Note: {cp.reset_font()} These 2 options can be replaced by their original values.

      {cp.ins_chr(10)}  ALL_ROW   \u2192 1
      {cp.ins_chr(10)}  ONLY_WORD \u2192 2


              See FancyFormat class to visualize a complete example.

      '''
    print(message)


#------------------------------------------------------------------------------------------------
# line_style                                                                                    -
#------------------------------------------------------------------------------------------------
def line_style_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[24])
    message = f'''
      Style_Line Class is used with FancyFormat Class. There are many options.

      {cp.set_font(0,53,231,0)}                                                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} CUSTOMIZED    {cp.Unicode.BULLET} DESIGN_1                              {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} DASH_LINE     {cp.Unicode.BULLET} DESIGN_2      {cp.Unicode.BULLET} PURPLE_WHITE          {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SINGLE_LINE   {cp.Unicode.BULLET} DESIGN_3      {cp.Unicode.BULLET} WHITE_BLACK_1         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SINGLE_BOLD   {cp.Unicode.BULLET} DESIGN_4      {cp.Unicode.BULLET} WHITE_BLACK_2         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SINGLE_HEAVY  {cp.Unicode.BULLET} DESIGN_5      {cp.Unicode.BULLET} WHITE_PURPLE          {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} DOUBLE_LINE   {cp.Unicode.BULLET} DESIGN_6      {cp.Unicode.BULLET} TURQUOISE_BLACK       {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SQ_BRACKETS   {cp.Unicode.BULLET} DESIGN_7      {cp.Unicode.BULLET} TURQUOISE_WHITE       {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} NONE          {cp.Unicode.BULLET} DESIGN_8      {cp.Unicode.BULLET} WHITE_BLACK_PURPLE    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SPACE_0       {cp.Unicode.BULLET} DESIGN_9      {cp.Unicode.BULLET} GRAY_TEAL_WHITE       {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SPACE_1       {cp.Unicode.BULLET} DESIGN_10     {cp.Unicode.BULLET} BLUE_PURPLE_WHITE_1   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SPACE_2       {cp.Unicode.BULLET} RED_WHITE     {cp.Unicode.BULLET} BLUE_PURPLE_WHITE_2   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SPACE_3       {cp.Unicode.BULLET} BLUE_WHITE    {cp.Unicode.BULLET} GREEN_GREEN_BLACK     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SPACE_4       {cp.Unicode.BULLET} TEAL_WHITE    {cp.Unicode.BULLET} OLIVE_GREEN           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} SPACE_5       {cp.Unicode.BULLET} SPACE_6                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                          {cp.reset_font()}

      {cp.set_font(1,196,231)} Note: {cp.reset_font()} These options can be replaced for the original values.

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
      {cp.Unicode.BULLET} SPACE_6      \u2192 \"space_6\"           {cp.Unicode.BULLET} OLIVE_GREEN  \u2192 \"olive_green\"

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



      {cp.set_font(True,196,231)}   Note:  {cp.reset_font()}  Options {cp.set_font(True,-1,14)}SPACE_X,{cp.reset_font()} use colors to visualize the effect
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
      {cp.ins_chr(10)}  tbli.title_msg = " SPACE_6 "
      {cp.ins_chr(10)}  tbli.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_6)

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
    tbli.title_msg = " SPACE_6 "
    tbli.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_6)

    print(f"\n{cp.ins_chr(10)}{cp.set_font(1,231,90)} \u25CF To see more examples regarding FancyFormat, check FancyFormat  {cp.reset_font()}\n"
           f"{cp.ins_chr(10)}{cp.set_font(1,231,90)}   class documentation.{cp.ins_chr(43)}{cp.reset_font()}")

    print()
#------------------------------------------------------------------------------------------------
# logo                                                                                          -
#------------------------------------------------------------------------------------------------
def logo_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[25])
    message = f'''
      Logo Class has a few options.

      {cp.set_font(0,53,231,0)}                  {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Logo_Centos   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Logo_Debian   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Logo_Linux    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Logo_RedHat   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} Logo_Unix     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                  {cp.reset_font()}



      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import custom_print as cp
      {cp.ins_chr(10)}  art_logo = cp.AsciiArt()
      {cp.ins_chr(10)}  art_logo.ascii_type = cp.Logo_Centos

      {cp.set_font(1,196,231)} Note: {cp.reset_font()}     See AsciiArt Class for more options.
    '''
    print(message)


#------------------------------------------------------------------------------------------------
# move                                                                                          -
#------------------------------------------------------------------------------------------------
def move_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[26])
    message = f'''
      Move Class has a few options.

      {cp.set_font(0,53,231,0)}             {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} DOWN     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} LEFT     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} RIGHT    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} UP       {cp.reset_font()}
      {cp.set_font(0,53,231,0)}             {cp.reset_font()}

      {cp.set_font(1,196,231)} Note: {cp.reset_font()} These options can be replaced for the original values.

      {cp.Unicode.BULLET} DOWN   \u2192  \"down\"
      {cp.Unicode.BULLET} LEFT   \u2192  \"left\"
      {cp.Unicode.BULLET} RIGHT  \u2192  \"right\"
      {cp.Unicode.BULLET} UP     \u2192  \"up\"


      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import custom_print as cp
      {cp.ins_chr(10)}  crs = cp.Cursor()
      {cp.ins_chr(10)}  crs.jumpTo(8, \"down\")
      {cp.ins_chr(10)}  crs.jumpTo(2, cp.Move.DOWN)

      {cp.set_font(1,196,231)} Note: {cp.reset_font()} See Cursor class for more examples.
    '''
    print(message)


#------------------------------------------------------------------------------------------------
# no                                                                                            -
#------------------------------------------------------------------------------------------------
def no_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[27])
    message = f'''
      {cp.set_font(0,53,231,0)}                                                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} No class has 256 options. To see them run the following code:  {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                   {cp.reset_font()}

      import custom_print as cp
      cp.bg_ansi_colors(bold=True, fg=0,  n_line=1)
      cp.fg_ansi_colors(bold=True, bg=-1, n_line=1)


      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import custom_print as cp
      {cp.ins_chr(10)}  blue_msg = cp.FancyMessage()
      {cp.ins_chr(10)}  blue_msg.body_bg   = cp.No.VERY_LIGHT_BLUE
      {cp.ins_chr(10)}  blue_msg.body_fg   = cp.No.GO_GREEN
      {cp.ins_chr(10)}  blue_msg.print_fancy_message(" This is a DEMO...! ")

      {cp.set_font(1,196,231)} Note: {cp.reset_font()} These options can be replaced for the original values.

      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import custom_print as cp
      {cp.ins_chr(10)}  blue_msg = cp.FancyMessage()
      {cp.ins_chr(10)}  blue_msg.body_bg   = 14
      {cp.ins_chr(10)}  blue_msg.body_fg   = 35
      {cp.ins_chr(10)}  blue_msg.print_fancy_message(" This is a DEMO...! ")

      {cp.set_font(0,53,231,0)}                                                        {cp.reset_font()}
      {cp.set_font(0,53,231,0)} This class is used where a color needs to be assigned. {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                        {cp.reset_font()}
'''
    print(message)


#------------------------------------------------------------------------------------------------
# style                                                                                         -
#------------------------------------------------------------------------------------------------
def style_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[28])
    message = f'''
      The Style class allows you to customize the font style directly.
      The following are the available options:

      {cp.set_font(0,53,231,0)}                                        {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} BOLD_ON           {cp.Unicode.BULLET}  BOLD_OFF       {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} DIM_ON            {cp.Unicode.BULLET}  DIM_OFF        {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} ITALIC_ON         {cp.Unicode.BULLET}  ITALIC_OFF     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} UNDERLINE_ON      {cp.Unicode.BULLET}  UNDERLINE_OFF  {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} BLINKING_ON       {cp.Unicode.BULLET}  BLINKING_OFF   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} INVERSE_ON        {cp.Unicode.BULLET}  INVERSE_OFF    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} HIDDEN_ON         {cp.Unicode.BULLET}  HIDDEN_OFF     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} STRIKE_ON         {cp.Unicode.BULLET}  STRIKE_OFF     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} RESET_ALL         {cp.Unicode.BULLET}  OFF            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                        {cp.reset_font()}

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

      {cp.set_font(1,196,231)} Note: {cp.reset_font()} Style.OFF only resets the style options and does not affect the
              background (bg) or foreground (fg) colors. To fully reset the
              font colors, use the reset_font() function or Style.RESET_ALL.

              Be aware that Bg.OFF only disables the background color, while
              Fg.OFF only disables the foreground color (and vice versa).
    '''
    print(message)


#------------------------------------------------------------------------------------------------
# unicode                                                                                       -
#------------------------------------------------------------------------------------------------
def unicode_info():
    ''' The Unicode class provides several predefined options '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[29])

    message = f'''
    The Unicode class provides several predefined options. Additional options
    and symbols can be found on the project's website.

      {cp.set_font(0,53,231,0)}                                                              {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_HORIZONTAL  {cp.Unicode.BOX_DRAWINGS_LIGHT_HORIZONTAL}                           {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT  {cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT}                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT  {cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT}                    {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_VERTICAL            {cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL}                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL  {cp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL}                  {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL   {cp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL}                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL {cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL}               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                              {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BLACK_UP_POINTING_TRIANGLE    {cp.Unicode.BLACK_UP_POINTING_TRIANGLE   }                            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} WHITE_UP_POINTING_TRIANGLE    {cp.Unicode.WHITE_UP_POINTING_TRIANGLE   }                            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BLAKC_RIGHT_POINTING_TRIANGLE {cp.Unicode.BLAKC_RIGHT_POINTING_TRIANGLE}                            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} WHITE_RIGHT_POINTING_TRIANGLE {cp.Unicode.WHITE_RIGHT_POINTING_TRIANGLE}                            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BLACK_DOWN_POINTING_TRIANGLE  {cp.Unicode.BLACK_DOWN_POINTING_TRIANGLE }                            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} WHITE_DOWN_POINTING_TRIANGLE  {cp.Unicode.WHITE_DOWN_POINTING_TRIANGLE }                            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BLACK_LEFT_POINTING_TRIANGLE  {cp.Unicode.BLACK_LEFT_POINTING_TRIANGLE }                            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} WHITE_LEFT_POINTING_TRIANGLE  {cp.Unicode.WHITE_LEFT_POINTING_TRIANGLE }                            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                              {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} RIGHT_ARROW                {cp.Unicode.RIGHT_ARROW}                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} LEFT_ARROW                 {cp.Unicode.LEFT_ARROW }                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} UP_ARROW                   {cp.Unicode.UP_ARROW   }                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} DOWN_ARROW                 {cp.Unicode.DOWN_ARROW }                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} UP_DOWN_ARROW              {cp.Unicode.UP_DOWN_ARROW }                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} UPWARDS_PAIRED_ARROWS      {cp.Unicode.UPWARDS_PAIRED_ARROWS   }                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} DOWNWARDS_PAIRED_ARROWS    {cp.Unicode.DOWNWARDS_PAIRED_ARROWS }                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} LEFTWARDS_PAIRED_ARROWS    {cp.Unicode.LEFTWARDS_PAIRED_ARROWS }                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} RIGHTWARDS_PAIRED_ARROWS   {cp.Unicode.RIGHTWARDS_PAIRED_ARROWS}                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BLACK_RIGHTWARDS_ARROWHEAD {cp.Unicode.BLACK_RIGHTWARDS_ARROWHEAD}                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                              {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} FIRE {cp.Unicode.FIRE}                                                    {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} EYES  {cp.Unicode.EYES}                                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} POOP  {cp.Unicode.POOP}                                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} FACE {cp.Unicode.FACE}                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} GHOST  {cp.Unicode.GHOST}                                                  {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} CLOWN  {cp.Unicode.CLOWN}                                                  {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BALLON  {cp.Unicode.BALLON}                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BULLET {cp.Unicode.BULLET}                                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} COFFEE  {cp.Unicode.COFFEE}                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} EM_DASH {cp.Unicode.EM_DASH}                                                  {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} LOWERCASE_N_TILDE   {cp.Unicode.LOWERCASE_N_TILDE}                                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} UPPERCASE_N_TILDE   {cp.Unicode.UPPERCASE_N_TILDE}                                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} LEFT_CURLY_BRACKET  {cp.Unicode.LEFT_CURLY_BRACKET}                                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} RIGHT_CURLY_BRACKET {cp.Unicode.RIGHT_CURLY_BRACKET}                                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                              {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SUBSCRIPT_ALPHA   {cp.Unicode.SUBSCRIPT_ALPHA  }          {cp.Unicode.BULLET} SUPERSCRIPT_ALPHA   {cp.Unicode.SUPERSCRIPT_ALPHA  }       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SUBSCRIPT_BETA    {cp.Unicode.SUBSCRIPT_BETA   }          {cp.Unicode.BULLET} SUPERSCRIPT_BETA    {cp.Unicode.SUPERSCRIPT_BETA   }       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SUBSCRIPT_GAMMA   {cp.Unicode.SUBSCRIPT_GAMMA  }          {cp.Unicode.BULLET} SUPERSCRIPT_GAMMA   {cp.Unicode.SUPERSCRIPT_GAMMA  }       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SUBSCRIPT_DELTA   {cp.Unicode.SUBSCRIPT_DELTA  }          {cp.Unicode.BULLET} SUPERSCRIPT_DELTA   {cp.Unicode.SUPERSCRIPT_DELTA  }       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SUBSCRIPT_EPSILON {cp.Unicode.SUBSCRIPT_EPSILON}          {cp.Unicode.BULLET} SUPERSCRIPT_EPSILON {cp.Unicode.SUPERSCRIPT_EPSILON}       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SUBSCRIPT_THETA   {cp.Unicode.SUBSCRIPT_THETA  }          {cp.Unicode.BULLET} SUPERSCRIPT_THETA   {cp.Unicode.SUPERSCRIPT_THETA  }       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SUBSCRIPT_IOTA    {cp.Unicode.SUBSCRIPT_IOTA   }          {cp.Unicode.BULLET} SUPERSCRIPT_IOTA    {cp.Unicode.SUPERSCRIPT_IOTA   }       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SUBSCRIPT_PHO     {cp.Unicode.SUBSCRIPT_PHO    }          {cp.Unicode.BULLET} SUPERSCRIPT_PHO     {cp.Unicode.SUPERSCRIPT_PHO    }       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SUBSCRIPT_PHI     {cp.Unicode.SUBSCRIPT_PHI    }          {cp.Unicode.BULLET} SUPERSCRIPT_PHI     {cp.Unicode.SUPERSCRIPT_PHI    }       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SUBSCRIPT_PSI     {cp.Unicode.SUBSCRIPT_PSI    }          {cp.Unicode.BULLET} SUPERSCRIPT_PSI     {cp.Unicode.SUPERSCRIPT_PSI    }       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SUBSCRIPT_CHI     {cp.Unicode.SUBSCRIPT_CHI    }          {cp.Unicode.BULLET} SUPERSCRIPT_CHI     {cp.Unicode.SUPERSCRIPT_CHI    }       {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                              {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BLACK_DIAMOND {cp.Unicode.BLACK_DIAMOND}              {cp.Unicode.BULLET} WHITE_DIAMOND   {cp.Unicode.WHITE_DIAMOND}           {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BLACK_DIAMOND_MINUS {cp.Unicode.BLACK_DIAMOND_MINUS}        {cp.Unicode.BULLET} WHITE_DIAMOND   {cp.Unicode.BLACK_SMALL_DIAMOND}           {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} LARGE_BLUE_DIAMON {cp.Unicode.LARGE_BLUE_DIAMOND}         {cp.Unicode.BULLET} LARGE_ORANGE_DIAMON {cp.Unicode.LARGE_ORANGE_DIAMOND}      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                              {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} RED_SQUARE          {cp.Unicode.RED_SQUARE}       {cp.Unicode.BULLET} RED_CIRCLE    {cp.Unicode.RED_CIRCLE}            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BLUE_SQUARE         {cp.Unicode.BLUE_SQUARE}       {cp.Unicode.BULLET} BLUE_CIRCLE   {cp.Unicode.BLUE_CIRCLE}            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} ORANGE_SQUARE       {cp.Unicode.ORANGE_SQUARE}       {cp.Unicode.BULLET} ORANGE_CIRCLE {cp.Unicode.ORANGE_CIRCLE}            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} YELLOW_SQUARE       {cp.Unicode.YELLOW_SQUARE}       {cp.Unicode.BULLET} YELLOW_CIRCLE {cp.Unicode.YELLOW_CIRCLE}            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} GREEN_SQUARE        {cp.Unicode.GREEN_SQUARE}       {cp.Unicode.BULLET} GREEN_CIRCLE  {cp.Unicode.GREEN_CIRCLE}           {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} PURPLE_SQUARE       {cp.Unicode.PURPLE_SQUARE}       {cp.Unicode.BULLET} PURPLE_CIRCLE {cp.Unicode.PURPLE_CIRCLE}            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BROWN_SQUARE        {cp.Unicode.BROWN_SQUARE}      {cp.Unicode.BULLET} BROWN_CIRCLE  {cp.Unicode.BROWN_CIRCLE}            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BLACK_SQUARE        {cp.Unicode.BLACK_SQUARE}      {cp.Unicode.BULLET} BLACK_CIRCLE  {cp.Unicode.BLACK_CIRCLE}            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} WHITE_SQUARE        {cp.Unicode.WHITE_SQUARE}      {cp.Unicode.BULLET} WHITE_CIRCLE  {cp.Unicode.WHITE_CIRCLE}            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} BLACK_SQUARE_BUTTON {cp.Unicode.BLACK_SQUARE_BUTTON}       {cp.Unicode.BULLET} WHITE_START_CIRCLE {cp.Unicode.WHITE_START_CIRCLE}        {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} WHITE_SQUARE_BUTTON {cp.Unicode.WHITE_SQUARE_BUTTON}       {cp.Unicode.BULLET} HEAVY_CIRCLE {cp.Unicode.HEAVY_CIRCLE}             {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                              {cp.reset_font()}

      {cp.set_font(True,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  print(cp.Unicode.FIRE)
                  print(cp.Unicode.POOP)

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()} {cp.Unicode.FIRE}
                 {cp.Unicode.POOP}

    How Unicode Characters Work...!

    {cp.Unicode.LARGE_BLUE_DIAMOND} print Unicode value with 2 digits,  Use (\\x)
        1. print(\"\\x65\")  {cp.Unicode.RIGHT_ARROW}  \x65
        {cp.Unicode.EYES} \N{Eyes}

    {cp.Unicode.LARGE_BLUE_DIAMOND} print Unicode value from 2 to 4 digits, Use (\\u)
        2. print(\"\\u0065\")  {cp.Unicode.RIGHT_ARROW}  \u0065
        3. print(\"\\u2757\")  {cp.Unicode.RIGHT_ARROW} \u2757


    {cp.Unicode.LARGE_BLUE_DIAMOND} print Unicode value with 5 to 8 digits, Use (\\U)
        4. print(\"\\U00000065\")  {cp.Unicode.RIGHT_ARROW}  \U00000065
        5. print(\"\\U00002757\")  {cp.Unicode.RIGHT_ARROW}  \U00002757
        6. print(\"\\U0001F525 Fuego Code\")  {cp.Unicode.RIGHT_ARROW}  \U0001F525
        7. print(\"\\N{{FIRE}}   Fuego Name\")  {cp.Unicode.RIGHT_ARROW}  \N{FIRE}


    {cp.Unicode.LARGE_BLUE_DIAMOND} Print Unicode by Name: {cp.set_font(1,231,16)} import unicodedata {cp.reset_font()} It may be necessary.
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
                 https://codeshack.io/arrow-symbols
                 http://xahlee.info/comp/unicode_arrows.html
                 https://www.w3.org/TR/xml-entity-names/025.html
                 https://www.alt-codes.net/diamond-symbols
    '''
    print(message)




# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: CURSOR_CLASS                                                                      |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  Cursor in custom_print Module                                                                  |
# +-------------------------------------------------------------------------------------------------+
def cursor_only_info():
    ''' It moves the cursor to a specific location on the terminal. '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[30]) # Cursor
    mensaje =f'''
    All these functions are used internally by the Custom_Print module. However,
    they are also exposed to the user. Feel free to use them if you find them
    useful, or simply ignore them if not needed.

      Cursor can use the Move Class that has 4 options.

      {cp.set_font(0,53,231,0)}             {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} DOWN     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} LEFT     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} RIGHT    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}  {cp.Unicode.BULLET} UP       {cp.reset_font()}
      {cp.set_font(0,53,231,0)}             {cp.reset_font()}

      {cp.set_font(1,196,231)} Note: {cp.reset_font()} These options can be replaced for the original values.

      {cp.Unicode.BULLET} DOWN   \u2192  \"down\"   \u2192  \"d\"
      {cp.Unicode.BULLET} LEFT   \u2192  \"left\"   \u2192  \"l\"
      {cp.Unicode.BULLET} RIGHT  \u2192  \"right\"  \u2192  \"r\"
      {cp.Unicode.BULLET} UP     \u2192  \"up\"     \u2192  \"u\"


    '''
    print(mensaje)


def cursor_info():
    ''' It moves the cursor to a specific location on the terminal. '''
    cursor_only_info()
    jumpto_info()
    jumpxy_info()
    moveto_info()
    movexy_info()


#------------------------------------------------------------------------------------------------
# jumpTo                                                                                        -
#------------------------------------------------------------------------------------------------
def jumpto_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[31])
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


#------------------------------------------------------------------------------------------------
# jumpToxy                                                                                      -
#------------------------------------------------------------------------------------------------
def jumpxy_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[32])
    message = f'''

      This method jumps the cursor to specific coordinates in the terminal.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp
      {cp.ins_chr(10)}  crs = cp.Cursor()
      {cp.ins_chr(10)}  crs.jumpToxy(0,0);     print("*** Start Here ***")
      {cp.ins_chr(10)}  crs.jumpToxy(20, 5);   print("GoodBye...!")

   '''
    print(message)


#------------------------------------------------------------------------------------------------
# moveTo                                                                                        -
#------------------------------------------------------------------------------------------------
def moveto_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[33])
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


#------------------------------------------------------------------------------------------------
# movexy                                                                                        -
#------------------------------------------------------------------------------------------------
def movexy_info():
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[34])
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
def fontstyle_only_info():
    ''' It prints font in a style way. '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[35])
    message = f'''
     This class contains 4 methods.

      {cp.set_font(1,231,16)} Default Values {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                General Use                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} bg     = -1             {cp.Unicode.BULLET} bold      = False   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} fg     = -1             {cp.Unicode.BULLET} underline = False   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} dim    = False          {cp.Unicode.BULLET} blinking  = False   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} hidden = False          {cp.Unicode.BULLET} italic    = False   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} strike = False          {cp.Unicode.BULLET} inverse   = False   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                Print_Style                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} align = Align.JUSTIFY   {cp.Unicode.BULLET} bg_top_lines    = 0 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} forced_align = False    {cp.Unicode.BULLET} bg_bottom_lines = 0 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} indent = 0                                    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                 {cp.reset_font()}

      indent   This defines how far we want to start to print the message
               from the left of the terminal.

      {cp.set_font(1,196,231)} Note: {cp.reset_font()} indent is used for style_on and for print_style when using
              justify as an option for the align. For the other \"align\" options
              (left, right, center), only \"print_style\" make use of them.
    '''
    print(message)


def fontstyle_info():
    ''' It prints font in a style way. '''
    fontstyle_only_info()
    style_on_off_info()
    reset_style_info()
    print_style_info()


#------------------------------------------------------------------------------------------------
# style_on_off                                                                                  -
#------------------------------------------------------------------------------------------------
def style_on_off_info():
    ''' These methods are useful if we are using the style in many rows. '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[36])
    message = f'''
      These methods are useful if we are using the style in many rows.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  fs = cp.FontStyle()
                  fs.fg        = 231
                  fs.bg        = 22
                  fs.indent    = 23
                  fs.bold      = True
                  fs.underline = True
                  fs.strike    = True
                  fs.italic    = True

                  print(fs.style_on() + " Font Style " + fs.style_off())
                  print(fs.style_on() + "            " + fs.style_off())
                  print(f\"{{fs.style_on()}} Font Style {{fs.style_off()}}\")

'''

    print(message, end="")
    fs = cp.FontStyle()
    fs.fg        = 231
    fs.bg        = 22
    fs.indent    = 23
    fs.bold      = True
    fs.underline = True
    fs.strike    = True
    fs.italic    = True

    print(f"       {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()} \n")
    print(fs.style_on() + " Font Style " + fs.style_off())
    print(fs.style_on() + "            " + fs.style_off())
    print(f"{fs.style_on()} Font Style {fs.style_off()}")


#------------------------------------------------------------------------------------------------
# reset_style                                                                                   -
#------------------------------------------------------------------------------------------------
def reset_style_info():
    ''' This method reset all the values to the default ones for object. '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[37])
    message = f'''
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  fs = cp.FontStyle()
                  fs.bg = 21
                  fs.fg = 231

                  cp.ins_newline(2)

                  print(f\"{{fs.style_on()}} Font Style Line 1 \")
                  print(f\" Font Style Line 2 \")
                  print(f\" Font Style Line 3 {{fs.style_off()}}\\n\")
                  fs.reset_style()
                  print(f\"{{fs.style_on()}} Default Style {{fs.style_off()}}\")

'''
    print(message)
    print(f"       {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()} \n")
    fs = cp.FontStyle()
    fs.bg = 21
    fs.fg = 231

    cp.ins_newline(2)

    print(f"{fs.style_on()} Font Style Line 1")
    print(f" Font Style Line 2 ")
    print(f" Font Style Line 3 {fs.style_off()}\n" )
    fs.reset_style()
    print(f"{fs.style_on()} Default Style {fs.style_off()}")
    print()


#------------------------------------------------------------------------------------------------
# print_style                                                                                   -
#------------------------------------------------------------------------------------------------
def print_style_info():
    ''' This method align the customized text on the screen with the position specified.  '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[38])
    message = f'''
       This method aligns the customized text on the screen with the position
       specified.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  fs = cp.FontStyle()
                  fs.fg        = 231;        fs.bg_bottom_lines = 1
                  fs.bg        = 23;         fs.bg_top_lines    = 1
                  fs.bold      = True;       fs.forced_align    = False '''
    print(message)
    message = '''
                  def get_msg(option, align)->str:
                  msg = f\'\'\'
                  Custom_Print...!
                  Align.{option}
                  force_align = {align}
                  Python3.12\'\'\'
                  return msg

                  option = "LEFT"; align = "False"
                  msg = get_msg(option,align)
                  fs.align = cp.Align.LEFT
                  fs.print_style(msg)

                  cp.ins_newline(3)

                  fs.forced_align = True
                  option = "LEFT"; align = "True"
                  msg = get_msg(option,align)
                  fs.align = cp.Align.LEFT
                  fs.print_style(msg)
    '''
    print(message)

    print(f"       {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()} \n")
    fs = cp.FontStyle()
    fs.fg        = 231
    fs.bg        = 23
    fs.bold      = True
    fs.bg_bottom_lines = 1
    fs.bg_top_lines    = 1
    fs.forced_align    = False


    def get_msg(option, align)->str:
        msg = f'''
    Custom_Print...!
    Align.{option}
    force_align = {align}
    Python3.12 '''
        return msg


    option = "LEFT"; align = "False"
    msg = get_msg(option,align)
    fs.align = cp.Align.LEFT
    fs.print_style(msg)

    cp.ins_newline(3)

    fs.forced_align = True
    option = "LEFT"; align = "True"
    msg = get_msg(option,align)
    fs.align = cp.Align.LEFT
    fs.print_style(msg)
    cp.ins_newline(1)




# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: FANCYMESSAGE_CLASS                                                                |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  FancyMessage in custom_print Module                                                            |
# +-------------------------------------------------------------------------------------------------+
def fancymessage_only_info():
    ''' This class contains 3 methods'''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[39])
    message = f'''
      This class contains 3 methods: print_fancy_message, print_fancy_note, and
      get_message_attributes.

      {cp.set_font(1,231,16)} Default Values {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  Body Section                                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} body_bg = 4                 {cp.Unicode.BULLET} body_dim = False                {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} body_fg = 231               {cp.Unicode.BULLET} body_italic = False             {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} body_msg = "Body Msg"       {cp.Unicode.BULLET} body_hidden = False             {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} body_bold = False           {cp.Unicode.BULLET} body_strike = False             {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} help_lines = False          {cp.Unicode.BULLET} body_inverse = False            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} left_indent = 2             {cp.Unicode.BULLET} body_blinking = False           {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} right_indent = 2            {cp.Unicode.BULLET} body_underline = False          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} top_lines = 1               {cp.Unicode.BULLET} bottom_lines = 1                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} length = Length_Bg.ALL_ROW                                    {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} adj_bg_lines_to_right_indent = False                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} adj_bg_msg_to_space_available = False                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  Note Section                                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} note_bg = 231               {cp.Unicode.BULLET} note_dim = False                {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} note_fg = 0                 {cp.Unicode.BULLET} note_italic = False             {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} note_msg = "Note:"          {cp.Unicode.BULLET} note_hidden = False             {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} note_bold = False           {cp.Unicode.BULLET} note_strike = False             {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} note_position = 1           {cp.Unicode.BULLET} note_inverse = False            {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} note_left_space = 2         {cp.Unicode.BULLET} note_blinking = False           {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} note_right_space = 2        {cp.Unicode.BULLET} note_underline = False          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} note_align = Align.JUSTIFY                                    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  Title Section                                                  {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} title_bg = 4                 {cp.Unicode.BULLET} title_dim = False              {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} title_fg = 231               {cp.Unicode.BULLET} title_italic = False           {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} title_msg = ""               {cp.Unicode.BULLET} title_hidden = False           {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} title_bold = False           {cp.Unicode.BULLET} title_strike = False           {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} title_indent = 2             {cp.Unicode.BULLET} title_inverse = False          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} title_body_lines = 1         {cp.Unicode.BULLET} title_blinking = False         {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} title_align = Align.LEFT     {cp.Unicode.BULLET} title_underline = False        {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  Footnote Section                                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} footnote_bg = 4              {cp.Unicode.BULLET} footnote_dim = False           {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} footnote_fg = 231            {cp.Unicode.BULLET} footnote_italic = False        {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} footnote_msg = ""            {cp.Unicode.BULLET} footnote_hidden = False        {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} footnote_bold = False        {cp.Unicode.BULLET} footnote_strike = False        {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} footnote_indent = 2          {cp.Unicode.BULLET} footnote_inverse = False       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} footnote_body_lines = 1      {cp.Unicode.BULLET} footnote_blinking = False      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} footnote_align = Align.RIGHT {cp.Unicode.BULLET} footnote_underline = False     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                 {cp.reset_font()}


      {cp.set_font(1,196,231)} Note: {cp.reset_font()} title_indent      works with Align.JUSTIFY.
              footnote_indent   works with Align.JUSTIFY.

              These 2 options \"adj_bg_lines_to_right_indent\" and
              \"adj_bg_msg_to_space_available\" do not do anything when
              length = Length_Bg.All_ROW

              {cp.set_font(1,231,22,True)} Body Section {cp.reset_font()} is being used by both methods print_fancy_message
              and print_fancy_note.
    '''
    print(message)


def fancymessage_info():
    ''' This class contains 3 methods'''

    fancymessage_only_info()
    print_fancy_message_info()
    print_fancy_note_info()
    get_message_attributes_info()


#------------------------------------------------------------------------------------------------
# print_fancy_message                                                                           -
#------------------------------------------------------------------------------------------------
def print_fancy_message_info():
    ''' This method customized text on the screen for better visualization.  '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[40])
    message = f'''
      This method customized text on the screen for better visualization.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  msg = cp.FancyMessage()
                  paragraph = \'\'\'
                  Guido van Rossum, a Dutch programmer, created Python in the
                  late 1980s as a hobby project.
                  He started working on it in December 1989 at Centrum Wiskunde
                  & Informatica (CWI) in the Netherlands.

                  Python was first released on February 20, 1991.
                  Python was named after the 1970s BBC comedy sketch
                  series Monty Python's Flying Circus.\'\'\'

                  msg.title_msg = "TITLE"
                  msg.footnote_msg = "FOOTNOTE"
                  msg.body_bg = 40
                  msg.body_fg = 16

                  msg.length = cp.Length_Bg.All_ROW
                  msg.print_fancy_message(paragraph)	    #  Option 1

                  msg.length = cp.Length_Bg.ONLY_WORD       #  Option 2
                  msg.print_fancy_message(paragraph)

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
    '''
    print(message)
    msg = cp.FancyMessage()
    paragraph = '''
        Guido van Rossum, a Dutch programmer, created Python in the
        late 1980s as a hobby project.
        He started working on it in December 1989 at Centrum Wiskunde
        & Informatica (CWI) in the Netherlands.

        Python was first released on February 20, 1991.
        Python was named after the 1970s BBC comedy sketch
        series Monty Python's Flying Circus.'''

    msg.title_msg = "TITLE"
    msg.footnote_msg = "FOOTNOTE"
    msg.body_bg = 40
    msg.body_fg = 16
    msg.length = cp.Length_Bg.ALL_ROW
    msg.print_fancy_message(paragraph)		#  Method 1
    print()
    msg.length = cp.Length_Bg.ONLY_WORD
    msg.print_fancy_message(paragraph)		#  Method 2
    print()

    diagram_description_fancy_message()


#------------------------------------------------------------------------------------------------
# print_fancy_note                                                                              -
#------------------------------------------------------------------------------------------------
def print_fancy_note_info():
    ''' This method customized notes on the screen for better visualization.  '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[41])
    message = f'''
      This method customized text on the screen for better visualization.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  msg = cp.FancyMessage()
                  paragraph = \'\'\'
                  1898 - 1936, translated by Sarah Arvio

                  To find a kiss of yours
                  what would I give
                  A kiss that strayed from your lips
                  dead to love

                  My lips taste
                  the dirt of shadows

                  To gaze at your dark eyes
                  what would I give
                  Dawns of rainbow garnet
                  fanning open before God—

                  The stars blinded them
                  one morning in May

                  And to kiss your pure thighs
                  what would I give
                  Raw rose crystal
                  sediment of the sun
                    \'\'\'
                  # msg.help_lines = True
                  msg.top_lines = 1
                  msg.note_bold = True
                  msg.note_position = 12  # by default is on row 0
                  msg.note_align    = cp.Align.CENTER
                  msg.note_left_space  = 4
                  msg.note_right_space = 4
                  msg.left_indent  = 25
                  msg.right_indent = 8
                  msg.print_fancy_note(body_msg=poem)
                  print()
                  msg.body_bold    = True
                  msg.left_indent  = len(msg.note_msg) +
                                     msg.note_left_space +
                                     msg.note_right_space
                  msg.body_italic  = True
                  msg.body_fg      = 190
                  msg.top_lines    = 0
                  msg.bottom_lines = 1
                  msg.left_indent  = 4
                  msg.right_indent = 0
                  msg.top_lines    = 2
                  msg.bottom_lines = 1
                  msg.print_fancy_message("Author: Federico García Lorca")
                  print()


      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
    '''
    print(message)

    msg = cp.FancyMessage()
    msg.note_msg = " To Find a Kiss of Yours "
    poem = f'''
1898 - 1936, translated by Sarah Arvio

To find a kiss of yours
what would I give
A kiss that strayed from your lips
dead to love

My lips taste
the dirt of shadows

To gaze at your dark eyes
what would I give
Dawns of rainbow garnet
fanning open before God

The stars blinded them
one morning in May

And to kiss your pure thighs
what would I give
Raw rose crystal
sediment of the sun

'''
    #msg.help_lines = True
    msg.top_lines = 1
    msg.note_bold = True
    msg.note_position = 12  # by default is on row 0
    msg.note_align    = cp.Align.CENTER
    msg.note_left_space  = 4
    msg.note_right_space = 4
    msg.left_indent  = 25
    msg.right_indent = 8
    msg.print_fancy_note(body_msg=poem)
    print()
    msg.body_bold    = True
    msg.left_indent  = len(msg.note_msg) + msg.note_left_space + msg.note_right_space
    msg.body_italic  = True
    msg.body_fg      = 190
    msg.top_lines    = 0
    msg.bottom_lines = 1
    msg.left_indent  = 4
    msg.right_indent = 0
    msg.top_lines    = 2
    msg.bottom_lines = 1
    msg.print_fancy_message("Author: Federico García Lorca")
    print()

    diagram_description_fancy_note()


#------------------------------------------------------------------------------------------------
# get_message_attributes                                                                        -
#------------------------------------------------------------------------------------------------
def get_message_attributes_info():
    ''' This method customized notes on the screen for better visualization.  '''
    cp.ins_newline(1)
    green_div.print_fancy_divider(all_topics[42])
    message = f'''
       This method collect all the attributes of the paragraph.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  msg = cp.FancyMessage()
                  paragraph = \'\'\'
                  Guido van Rossum, a Dutch programmer, created Python in the
                  late 1980s as a hobby project.
                  He started working on it in December 1989 at Centrum Wiskunde
                  & Informatica (CWI) in the Netherlands.

                  Python was first released on February 20, 1991. Python was
                  named after the 1970s BBC comedy sketch series Monty Python's
                  Flying Circus. \'\'\'

                  att = cp.FancyMessage()
                  att.length = cp.Length_Bg.ONLY_WORD
                  cp.ins_newline(2)
                  att.print_fancy_message(paragraph)

                  attributes, words = att.get_message_attributes(
                          body_msg=message, print_attributes=True)

                  print(f\" {{cp.set_font(True, 231, 22, True)}} Atributes:\"
                        f\" {{cp.reset_font()}}\")
                  print(attributes)

                  print(f\" {{cp.set_font(True, 231, 22, True)}} Words:\"
                        f\" {{cp.reset_font()}}\")
                      print(words)

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
    '''
    print(message)

    message = '''
    Guido van Rossum, a Dutch programmer, created Python in the
    late 1980s as a hobby project.
    He started working on it in December 1989 at Centrum Wiskunde
    & Informatica (CWI) in the Netherlands.
    Python was first released on February 20, 1991. Python was
    named after the 1970s BBC comedy sketch series Monty Python's
    Flying Circus.    '''

    att = cp.FancyMessage()
    att.length = cp.Length_Bg.ONLY_WORD

    cp.ins_newline(2)
    att.print_fancy_message(message)
    attributes, words = att.get_message_attributes(
        body_msg=message, print_attributes=True)

    print(f" {cp.set_font(True, 231, 22, True)} Atributes:"
          f" {cp.reset_font()}")
    print(f"{attributes}\n")

    print(f" {cp.set_font(True, 231, 22, True)} Words:"
          f" {cp.reset_font()}")
    print(f"{words}\n")



def diagram_description_fancy_message():

    pen = cp.Pen()
    crs = cp.Cursor()

    print(f"\n     {cp.set_font(True,231,0)} Diagram Description {cp.reset_font()}\n")
    ex_msg = cp.FancyMessage()
    ex_msg.body_bg = 229;             ex_msg.title_bg = 229;            ex_msg.footnote_bg = 229
    ex_msg.body_fg = 0;               ex_msg.title_fg = 21;             ex_msg.footnote_fg = 21
    ex_msg.body_italic = True;        ex_msg.footnote_italic = True;    ex_msg.title_italic = True
    ex_msg.body_bold   = True;        ex_msg.footnote_bold = 1;         ex_msg.title_bold = True
    ex_msg.left_indent = 15;          ex_msg.right_indent = 15;         ex_msg.title_align = cp.Align.CENTER
    ex_msg.top_lines   = 4;           ex_msg.bottom_lines = 3;          ex_msg.footnote_align = cp.Align.CENTER
    ex_msg.title_body_lines = 3
    ex_msg.footnote_body_lines = 3
    ex_msg.title_msg ="TITLE";        ex_msg.footnote_msg = "FOOTNOTE"; ex_msg.help_lines = True


    ex_fst = cp.FontStyle()
    ex_fst.fg = 128;       ex_fst.bg = 229;      ex_fst.bold = True
    ex_fst.indent = 0


    message = '''
Guido van Rossum, a Dutch programmer, create
  Python in the late 1980s as a hobby project.
  He started working on it in December 1989 at
  Centrum Wiskunde & Informatica (CWI) in the
  Netherlands.

Python was first released on February 20, 1991.
  Python was named after the 1970s BBC comedy
  sketch series Monty Python's Flying Circus.
'''
# Paragraph Description
    ex_msg.print_fancy_message(message)

    crs.jumpTo(qty=18, direction=cp.Move.UP)
    pen.draw_line(size=3, tail=ex_fst.style_on()+cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT, body=" left indent ",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)

    pen.draw_line(size=3, tail=f"{ex_fst.style_on()}\u2500", body=f"{cp.ins_chr(19,'\u2500')} body_msg {cp.ins_chr(19,'\u2500')}",\
                   head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)


    pen.draw_line(size=3, tail=f"{ex_fst.style_on()} ", body=f"{ex_fst.style_on()}right indent ",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT)

    print(f"{ex_fst.style_on()}")

    pen.adj_indent = 45
    crs.jumpTo(qty=8, direction=cp.Move.UP)
    crs.jumpTo(qty=45, direction=cp.Move.LEFT)

    pen.draw_line(size=5, layout=cp.Layout.VERTICAL, tail=ex_fst.style_on()+cp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                 body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)

    pen.draw_line(size=3, layout=cp.Layout.VERTICAL, tail=ex_fst.style_on()+cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL,\
                 body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=cp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL)

    print()
    crs.jumpTo(qty=6, direction=cp.Move.UP)
    pen.adj_indent = 29
    pen.draw_line(size=3, layout=cp.Layout.VERTICAL, tail=ex_fst.style_on()+"       top lines", body= " ", head="title_body_lines")


    crs.jumpTo(qty=11, direction=cp.Move.DOWN)
    pen.adj_indent = 55
    pen.draw_line(size=4, layout=cp.Layout.VERTICAL, tail=ex_fst.style_on()+cp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                 body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)

    pen.draw_line(size=3, layout=cp.Layout.VERTICAL, tail=ex_fst.style_on()+cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL,\
                 body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=cp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL)

    pen.adj_indent = 56
    crs.jumpTo(qty=6, direction=cp.Move.UP)
    pen.draw_line(size=3, layout=cp.Layout.VERTICAL, tail=ex_fst.style_on()+"footnote_body_lines", body= "\n\n", head="bottom lines")

    crs.jumpTo(qty=1, direction=cp.Move.DOWN)
    pen.adj_indent = 0
    ex_fst.bg = 196
    ex_fst.fg = 231
    print(f"{ex_fst.style_on()}help_lines {cp.Unicode.RIGHT_ARROW} {ex_fst.style_off()}\n")


def diagram_description_fancy_note():
    pen = cp.Pen()
    crs = cp.Cursor()


    # Note Description
    message = '''
Guido van Rossum, a Dutch programmer, create Python
  in the late 1980s as a hobby project. He started
  working on it in December 1989 at Centrum Wiskunde
  & Informatica (CWI) in the Netherlands.

Python was first released on February 20, 1991.
  Python was named after the 1970s BBC comedy
  sketch series Monty Python's Flying Circus.

'''
    print(f"\n     {cp.set_font(True,231,0)} Diagram Description {cp.reset_font()}\n")
    ex_msg = cp.FancyMessage()
    ex_msg.title_bg = 229
    ex_msg.title_fg = 21
    ex_msg.title_bold = True
    ex_msg.title_italic = True
    ex_msg.title_align = cp.Align.CENTER
    ex_msg.title_msg ="TITLE"

    ex_msg.footnote_bg = 229
    ex_msg.footnote_fg = 21
    ex_msg.footnote_italic = True
    ex_msg.footnote_bold = 1;
    ex_msg.footnote_body_lines = 3
    ex_msg.footnote_align = cp.Align.CENTER
    ex_msg.footnote_msg = "FOOTNOTE"


    ex_msg.note_align = cp.Align.CENTER;                   ex_msg.body_bg = 229
    ex_msg.note_msg = " Python ";                          ex_msg.body_fg = 0
    ex_msg.note_position = 8;                              ex_msg.body_italic = True
    ex_msg.note_bold = True;                               ex_msg.body_bold   = True
    ex_msg.note_left_space = 4
    ex_msg.note_right_space = 4
    ex_msg.note_align = cp.Align.CENTER
    ex_msg.note_bg = 231
    ex_msg.note_fg = 196

    ex_msg.left_indent = 15
    # ex_msg.title_body_lines = 3 # this does not exist on print_fancy_note
    # ex_msg.left_indent = 25;    # it exist but it is calculated (self.left_indent = self.note_left_space + len_note_msg + self.note_right_space)
                                  # and it is only used to print the help_lines variable
    ex_msg.right_indent = 6;
    ex_msg.top_lines   = 4;           ex_msg.bottom_lines = 3
    ex_msg.help_lines = True


    ex_fst = cp.FontStyle()
    ex_fst.fg = 128;       ex_fst.bg = 229;      ex_fst.bold = True
    ex_fst.indent = 0

    ex_msg.print_fancy_note(message)

    print()
    crs.jumpTo(qty=14, direction=cp.Move.UP)


    pen.draw_line(size=3, tail=ex_fst.style_on()+cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT, body=" A ",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)

    pen.draw_line(size=3, tail=f"{ex_fst.style_on()}", body=" Note ",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)

    pen.draw_line(size=3, tail=f"{ex_fst.style_on()} ", body="B ",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)


    pen.draw_line(size=3, tail=f"{ex_fst.style_on()}\u2500{cp.ins_chr(19,'\u2500')} body_msg {cp.ins_chr(19,'\u2500')}",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL)

    pen.draw_line(size=3, tail="", body=ex_fst.style_on()+"right indent",\
                 head=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT)

    print()
    crs.jumpTo(qty=5, direction=cp.Move.UP)
    pen.adj_indent = 35

    pen.draw_line(size=5, layout=cp.Layout.VERTICAL, tail=ex_fst.style_on()+cp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                 body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=ex_fst.style_on()+cp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL)

    crs.jumpTo(qty=3, direction=cp.Move.UP)

    print(f"{ex_fst.style_on()}{crs.moveTo(22,cp.Move.RIGHT)}top_lines --{cp.Unicode.BLAKC_RIGHT_POINTING_TRIANGLE}")
    crs.jumpTo(10,cp.Move.DOWN)

    pen.adj_indent = 71
    pen.draw_line(size=3, layout=cp.Layout.VERTICAL, tail=ex_fst.style_on()+cp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                 body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=cp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL+ex_fst.style_off())

    crs.jumpTo(qty=2, direction=cp.Move.UP)
    print(f"{crs.moveTo(55,cp.Move.RIGHT)}{ex_fst.style_on()}bottom_lines --{cp.Unicode.BLAKC_RIGHT_POINTING_TRIANGLE}{ex_fst.style_off()}")



    crs.jumpTo(qty=1, direction=cp.Move.UP)
    print(f"{ex_fst.style_on()}  A --{cp.Unicode.BLAKC_RIGHT_POINTING_TRIANGLE} note_left_space {ex_fst.style_off()}",end="")
    print(f"{ex_fst.style_on()},  B --{cp.Unicode.BLAKC_RIGHT_POINTING_TRIANGLE} note_right_space{ex_fst.style_off()}")
    crs.jumpTo(qty=4, direction=cp.Move.DOWN)
    ex_fst.bg = 196
    ex_fst.fg = 231
    crs.jumpTo(qty=2, direction=cp.Move.UP)
    print(f"{ex_fst.style_on()}help_lines {cp.Unicode.RIGHT_ARROW} {ex_fst.style_off()}\n")




# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: PEN_CLASS                                                                         |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  Pen in custom_print Module                                                                     |
# +-------------------------------------------------------------------------------------------------+
def pen_only_info():
    ''' pen only is able to draw a line and a rectangle'''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[43])
    message = f'''
      Pen class will draw lines nad squares. This class contains 2 methods.

      {cp.set_font(1,231,16)} Default Values {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  General Use Section                                                    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} adj_indent = 0                                                        {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} draw_line_bold = False                                                {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} draw_line_bg = -1                                                     {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} draw_line_fg = -1                                                     {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} fill_color = False                                                    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(1,53,231,0)} Rectangle Section                                                       {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(1,53,155,1)} Horizontal Line                  |                                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} top_horizontal_line_chr = "-"  |  {cp.Unicode.BULLET} bottom_horizontal_line_chr = "-"  {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                  |                                      {cp.reset_font()}
      {cp.set_font(1,53,155,1)} Vertical Line                    |                                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} left_vertical_line_chr  = "|"  |  {cp.Unicode.BULLET} right_vertical_line_chr = "|"     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                  |                                      {cp.reset_font()}
      {cp.set_font(1,53,155,1)} Corner Line                      |                                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} top_left_corner_chr     = "+"  |  {cp.Unicode.BULLET} self.top_right_corner_chr   = "+" {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} bottom_right_corner_chr = "+"  |  {cp.Unicode.BULLET} self.bottom_left_corner_chr = "+" {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}

      {cp.set_font(1,196,231)} Note: {cp.reset_font()} adj_indent   space from the terminal to the box.
'''
    print(message)


def pen_info():
    ''' The Pen class can only draw lines and rectangles.'''
    pen_only_info()
    draw_line_info()
    draw_rectangle_info()


#------------------------------------------------------------------------------------------------
# draw_line                                                                                     -
#------------------------------------------------------------------------------------------------
def draw_line_info():
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[44])
    mensaje =f'''
      It draws a line with the parameters specified.

      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  Parameters                                                             {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} size     It refers to the size of the body.                           {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} layout   It refers how to set the line.                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} tail     It define the char for the end of the line.                  {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} body     It define the char for the body of the line.                 {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} head     It define the char for the starting of the line.             {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  msg = cp.Pen()
                  pen.adj_indent = 8
                  pen.draw_line(size=20, layout=cp.Layout.HORIZONTAL,
                                tail=cp.Unicode.BLACK_LEFT_POINTING_TRIANGLE,
                                body=cp.Unicode.EM_DASH,
                                head=cp.Unicode.BLAKC_RIGHT_POINTING_TRIANGLE)
                  cp.ins_newline(2)
                  pen.draw_line(size=6, layout=cp.Layout.VERTICAL,
                  tail=cp.Unicode.COFFEE, body=cp.Unicode.GHOST,
                  head=cp.Unicode.BALLON)


      {cp.set_font(1,196,231)} Note: {cp.reset_font()} layout   only accepts HORIZONTAL or VERTICAL options.

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
    '''
    print(mensaje)
    pen = cp.Pen()
    pen.adj_indent = 8
    pen.draw_line(size=20, layout=cp.Layout.HORIZONTAL, tail=cp.Unicode.BLACK_LEFT_POINTING_TRIANGLE,
                  body=cp.Unicode.EM_DASH, head=cp.Unicode.BLAKC_RIGHT_POINTING_TRIANGLE)
    cp.ins_newline(2)
    pen.draw_line(size=6, layout=cp.Layout.VERTICAL, tail=cp.Unicode.COFFEE,
                  body=cp.Unicode.GHOST, head=cp.Unicode.BALLON)
    print()


#------------------------------------------------------------------------------------------------
# draw_rectangle                                                                                -
#------------------------------------------------------------------------------------------------
def draw_rectangle_info():
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[45])
    mensaje =f'''
      It draws a rectangle with the parameters specified.

      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  Parameters                                                             {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} length   It define to the length of the rectangle.                    {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} width    It define to the width of the rectangle.                     {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} style    It define the style of the line to be used.                  {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                         {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  msg = cp.Pen()
                  pen.adj_indent = 16
                  pen.draw_rectangle(length=8, width=4,
                                     style=cp.Line_Style.DOUBLE_LINE)

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
    '''
    print(mensaje)
    pen = cp.Pen()
    pen.adj_indent = 16
    pen.draw_rectangle(length=8, width=4, style=cp.Line_Style.DOUBLE_LINE)




# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: DIVIDER_CLASS                                                                     |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  Divider in custom_print Module                                                                 |
# +-------------------------------------------------------------------------------------------------+
def divider_only_info():
    ''' It creates a divider through the terminal screen. '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[46])
    message =f'''
      The Divider class creates a divider line across the terminal screen.

      {cp.set_font(1,231,16)} Default Values {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  Corner Section                                                       {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} top_left_corner_chr     = " "   {cp.Unicode.BULLET} top_left_corner_fg      = -1      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} top_right_corner_chr    = " "   {cp.Unicode.BULLET} top_right_corner_fg     = -1      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} bottom_left_corner_chr  = " "   {cp.Unicode.BULLET} bottom_left_corner_fg   = -1      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} bottom_right_corner_chr = " "   {cp.Unicode.BULLET} bottom_right_corner_fg  = -1      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} top_left_corner_bg      = -1    {cp.Unicode.BULLET} all_corner_bg           = -1      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} top_right_corner_bg     = -1    {cp.Unicode.BULLET} all_corner_fg           = -1      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} bottom_left_corner_bg   = -1    {cp.Unicode.BULLET} all_corner_chr          = ""      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} bottom_right_corner_bg  = -1    {cp.Unicode.BULLET} all_corner_bold         = False   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  Horizontal Line Section                                              {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} top_horizontal_line_chr = " "   {cp.Unicode.BULLET} bottom_horizontal_line_chr = " "  {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} top_horizontal_line_bg  = -1    {cp.Unicode.BULLET} bottom_horizontal_line_bg = -1    {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} top_horizontal_line_fg  = -1    {cp.Unicode.BULLET} bottom_horizontal_line_fg = -1    {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} top_horizontal_line_on  = True  {cp.Unicode.BULLET} bottom_horizontal_line_on = True  {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} horizontal_line_bold    = False                                     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  Vertical Line Section                                                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} left_vertical_line_chr = " "    {cp.Unicode.BULLET} right_vertical_line_chr = " "     {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} left_vertical_line_bg  = -1     {cp.Unicode.BULLET} right_vertical_line_bg = -1       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} left_vertical_line_fg  = -1     {cp.Unicode.BULLET} right_vertical_line_fg = -1       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} vertical_line_bold     = False                                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  Data Section                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} msg_bg   = -1    {cp.Unicode.BULLET} msg_italic    = False    {cp.Unicode.BULLET} msg_inverse = False   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} msg_fg   = -1    {cp.Unicode.BULLET} msg_underline = False    {cp.Unicode.BULLET} msg_strike  = False   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} msg_bold = False {cp.Unicode.BULLET} msg_blinking  = False    {cp.Unicode.BULLET} msg_hidden  = False   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} msg_dim  = False {cp.Unicode.BULLET} msg_align = Align.CENTER {cp.Unicode.BULLET} adj_indent  = 2       {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  Fill Section                                                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} left_fill_bg  = -1           {cp.Unicode.BULLET} right_fill_bg = -1                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} left_right_fill_bg = -1                                             {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                       {cp.reset_font()}

      {cp.set_font(1,196,231)} Note: {cp.reset_font()}

      {cp.set_font(1,231,21,True)} Corner Section {cp.reset_font()}

      The {cp.set_font(1,22,231)} all_corner_* {cp.reset_font()} variables are set to their default values. However,
      if you assign a different value to any {cp.set_font(1,22,231)} all_corner_* {cp.reset_font()} variable, it takes
      priority over the four individual corner variables.

      For example, setting {cp.set_font(1,22,231)} all_corner_chr {cp.reset_font()} will apply the same character to all
      four corners:
      {cp.set_font(1,231,22)}                                                                   {cp.reset_font()}
      {cp.set_font(1,231,22)}  top_left_corner_chr         bottom_left_corner_chr               {cp.reset_font()}
      {cp.set_font(1,231,22)}  top_right_corner_chr        bottom_right_corner_chr              {cp.reset_font()}
      {cp.set_font(1,231,22)}                                                                   {cp.reset_font()}
      {cp.set_font(0,231,21)} Same apply for {cp.set_font(1,231,22)}all_corner_fg, all_corner_bg, and all_corner_bold. {cp.reset_font()}
      {cp.set_font(1,231,22)}                                                                   {cp.reset_font()}


      {cp.set_font(1,231,21,True)} Horizontal Line Section {cp.reset_font()}

      top_horizontal_line_on and bottom_horizontal_line_on can be off by setting
      them to False.

      horizontal_line_bold: Applies for both, top and bottom lines.

      {cp.set_font(1,231,21,True)} Vertical Line Section {cp.reset_font()}

      vertical_line_bold: Applies for both, left and right lines.

      {cp.set_font(1,231,21,True)} Fill Section {cp.reset_font()}

      Similar to the Corner section, left_fill_bg and right_fill_bg can be
      controlled collectively. Assigning a value to left_right_fill_bg will
      apply the same background color to both the left and right fill areas.

      {cp.set_font(1,231,21,True)}                                                           {cp.reset_font()}
      {cp.set_font(1,231,21,True)} adj_indent {cp.set_font(1,231,16)}only works when the align is set to JUSTIFY    {cp.reset_font()}
      {cp.set_font(1,231,21,True)}                                                           {cp.reset_font()}
    '''
    print(message)


def divider_info():
    ''' It creates a divider through the terminal screen. '''
    divider_only_info()
    print_fancy_divider_info()


#------------------------------------------------------------------------------------------------
# print_fancy_divider                                                                           -
#------------------------------------------------------------------------------------------------
def print_fancy_divider_info():
    ''' It prints a divider through the terminal screen. '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[47])
    div = cp.Divider()
    message = f'''
      The default values are intentionally kept simple. However, you can easily
      modify them to create a more fancy and customized visualization. Several
      ready-to-use templates are also provided for quick and attractive styling.

      {cp.set_font(0,53,231,0)}                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} CUSTOMIZED    {cp.Unicode.BULLET} DASH_1          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SINGLE_LINE   {cp.Unicode.BULLET} DASH_2          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SINGLE_BOLD   {cp.Unicode.BULLET} SQ_BRACKETS     {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} SINGLE_HEAVY  {cp.Unicode.BULLET} BLUE_WHITE_1    {cp.reset_font()}
      {cp.set_font(0,53,231,0)} {cp.Unicode.BULLET} DOUBLE_LINE   {cp.Unicode.BULLET} BLUE_WHITE_2    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                   {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  div = cp.Divider()
                  title = " Custom Print Divider "

                  div.print_fancy_divider(title, cp.Divider_Style.SINGLE_HEAVY)
                  cp.ins_newline(2)

                  div.print_fancy_divider(title, cp.Divider_Style.DOUBLE_LINE)
                  cp.ins_newline(2)

                  # Customizing a Divider
                  # Setting bg colors for corners
                  div.top_left_corner_bg     = 231
                  div.top_right_corner_bg    = 231
                  div.bottom_left_corner_bg  = 231
                  div.bottom_right_corner_bg = 231

                  setting fg colors for corners
                  div.top_left_corner_fg     = 16;
                  div.top_right_corner_fg    = 16;
                  div.bottom_left_corner_fg  = 16;
                  div.bottom_right_corner_fg = 16;

                  # Setting chr for corners
                  div.top_left_corner_chr     = "1";
                  div.top_right_corner_chr    = "4"
                  div.bottom_left_corner_chr  = "3"
                  div.bottom_right_corner_chr = "6"

                  Setting bold for corners
                  div.all_corner_bold = True

                  # +--------------------------------+
                  # | Horizontal line Settings       |
                  # +--------------------------------+
                  # Setting chr for horizontal lines
                  div.top_horizontal_line_chr    = "*"
                  div.bottom_horizontal_line_chr = "-"

                  # Setting bg colors for horizontal lines
                  div.top_horizontal_line_bg    = 231
                  div.bottom_horizontal_line_bg = 231

                  Setting fg colors for horizontal lines
                  div.top_horizontal_line_fg    = 16
                  div.bottom_horizontal_line_fg = 16

                  # +--------------------------------+
                  # | Vertical line Settings         |
                  # +--------------------------------+
                  # Setting chr for horizontal lines
                  div.left_vertical_line_chr  = "2"
                  div.right_vertical_line_chr = "5"
                  div.vertical_line_bold      = True

                  # Setting bg colors for Vertical lines
                  div.left_vertical_line_bg  = 231
                  div.right_vertical_line_bg = 231

                  # Setting fg colors for Vertical lines
                  div.left_vertical_line_fg  = 16
                  div.right_vertical_line_fg = 16

                  # +--------------------------------+
                  # | Message Settings               |
                  # +--------------------------------+
                  # Message
                  div.msg_bg = 231;    div.msg_italic = True
                  div.msg_fg = 234;    div.msg_bold   = True
                  div.adj_indent = 2;  div.align = cp.Align.CENTER;

                  # Fill blank
                  div.left_fill_bg  = cp.No.GLADE_GREEN
                  div.right_fill_bg = cp.No.BLAZE_ORANGE
                  # uncomment the line below to see the difference
                  # div.left_right_fill_bg = cp.No.DARK_OLIVE_GREEN

                  msg = "  My Divider Title Here...!  "
                  div.print_fancy_divider(message=msg,
                                            style=cp.Divider_Style.CUSTOMIZED)
      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}

    '''


    # +--------------------------------------------------------------------------------------------+
    # | Printing the Divider                                                                       |
    # +--------------------------------------------------------------------------------------------+
    print(message)

    div.print_fancy_divider(message=" Custom Print Divider ", style=cp.Divider_Style.SINGLE_HEAVY)
    cp.ins_newline(2)
    div.print_fancy_divider(message=" Custom Print Divider ", style=cp.Divider_Style.DOUBLE_LINE)
    cp.ins_newline(2)


    # +--------------------------------------------------------------------------------------------+
    # | Corner Settings                                                                            |
    # +--------------------------------------------------------------------------------------------+
    # Setting bg colors for corners              setting fg colors for corners
    div.top_left_corner_bg     = 231;              div.top_left_corner_fg     = 16;
    div.top_right_corner_bg    = 231;              div.top_right_corner_fg    = 16;
    div.bottom_left_corner_bg  = 231;              div.bottom_left_corner_fg  = 16;
    div.bottom_right_corner_bg = 231;              div.bottom_right_corner_fg = 16;

    # Setting chr for corners                    Setting bold for corners
    div.top_left_corner_chr     = "1";           div.all_corner_bold = True
    div.top_right_corner_chr    = "4"
    div.bottom_left_corner_chr  = "3"
    div.bottom_right_corner_chr = "6"

    # +--------------------------------------------------------------------------------------------+
    # | Horizontal line Settings                                                                   |
    # +--------------------------------------------------------------------------------------------+
    # Setting chr for horizontal lines      Setting bg colors for horizontal lines     Setting fg colors for horizontal lines
    div.top_horizontal_line_chr    = "*";   div.top_horizontal_line_bg    = 231;    div.top_horizontal_line_fg    = 16
    div.bottom_horizontal_line_chr = "-";   div.bottom_horizontal_line_bg = 231;    div.bottom_horizontal_line_fg = 16

    # +--------------------------------------------------------------------------------------------+
    # | Vertical line Settings                                                                     |
    # +--------------------------------------------------------------------------------------------+
    # Setting chr for horizontal lines   Setting bg colors for Vertical lines  Setting fg colors for Vertical lines
    div.left_vertical_line_chr  = "2";   div.left_vertical_line_bg  = 231;      div.left_vertical_line_fg  = 16
    div.right_vertical_line_chr = "5";   div.right_vertical_line_bg = 231;      div.right_vertical_line_fg = 16
    div.vertical_line_bold      = True


    # +--------------------------------------------------------------------------------------------+
    # | Message Settings                                                                           |
    # +--------------------------------------------------------------------------------------------+
    # Message
    div.msg_bg = 231;                   div.msg_fg = 234;                        div.msg_bold = True
    div.adj_indent = 2;                 div.align = cp.Align.CENTER;             div.msg_italic = True



    # Fill blank
    div.left_fill_bg = cp.No.GLADE_GREEN
    div.right_fill_bg = cp.No.BLAZE_ORANGE
    # div.left_right_fill_bg = cp.No.DARK_OLIVE_GREEN

    # Note: all_fill_bg takes priority over the left_fill_bg and right_fill_bg

    # +--------------------------------------------------------------------------------------------+
    # | Printing the Divider                                                                       |
    # +--------------------------------------------------------------------------------------------+
    msg = "  My Divider Title Here...!  "
    div.print_fancy_divider(message=msg, style=cp.Divider_Style.CUSTOMIZED)
    cp.ins_newline(1)




# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: FANCYFORMAT_CLASS                                                                 |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  FancyFormat in custom_print Module                                                             |
# +-------------------------------------------------------------------------------------------------+
def fancyformat_only_info():
    ''' It prints data in a table format. '''
    cp.ins_newline(1)
    tbl = cp.FancyFormat()
    crs = cp.Cursor()
    blue_div.print_fancy_divider(all_topics[48])

    message =f'''
      The FancyFormat class was primarily designed for formatting list-type
      variables, however, it also supports other data types. This method prints
      the variable in a table format. Various customizations can be applied to
      the table.



      {cp.set_font(1,231,0)} Default Values {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}
      {cp.set_font(1,53,231,0)}     Space Section                      Shortcut Section                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}
      {cp.set_font(0,53,231,0)} 1.  adj_top_margin     = 0        |    design_color   =  4             {cp.reset_font()}
      {cp.set_font(0,53,231,0)} 2.  top_space          = 0        |    bg_line_colors = -1             {cp.reset_font()}
      {cp.set_font(0,53,231,0)} 3.  adj_indent         = 2        |    fg_line_colors = -1             {cp.reset_font()}
      {cp.set_font(0,53,231,0)} 4.  adj_space          = 2        |    bold_lines     = False          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} 5.  adj_bottom_margin  = 0        |                                    {cp.reset_font()}
      {cp.set_font(0,53,231,0)} 6.  adj_bottom_space   = 0        |                                    {cp.reset_font()}
      {cp.set_font(0,53,231,0)} 7.  header_all_cell_bg = True     |                                    {cp.reset_font()}
      {cp.set_font(0,53,231,0)} 8.  data_all_cell_bg   = True     |                                    {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}

      1. Lines to be added between the top of the terminal and the title.
      2. Lines to be added between the title and the top of the table.
      3. Left margin (space from the beginning of the terminal to the start of
         the table).
      4. Horizontal padding inside the table (space between the left/right
         border and the header/data content).
      5. Lines to be added between the bottom of the table and the footnote.
      6. Lines to be added between the bottom of the table and the end of the
         terminal.
'''
    print(message)
    lst = [["header_all_cell_bg = False"],["data_all_cell_bg = False"]]
    tbl.adj_indent = 42
    tbl.title_msg = "Header/Data"
    tbl.footnote_msg = "7,8"
    tbl.header_all_cell_bg = False
    tbl.data_all_cell_bg   = False
    tbl.header_bg = 4;        tbl.data_bg = 4
    tbl.header_fg = 231;      tbl.data_fg = 231

    tbl.print_fancy_format(lst)

    tbl.adj_indent = 6
    crs.jumpTo(qty=7, direction=cp.Move.UP)
    lst = [["header_all_cell_bg = True"],["data_all_cell_bg = True"]]
    tbl.header_all_cell_bg = True
    tbl.data_all_cell_bg = True

    tbl.print_fancy_format(lst)

    tbl.title_msg = ""
    tbl.footnote_msg = ""
    tbl.header_bg = -1;        tbl.data_bg = -1
    tbl.header_fg = -1;        tbl.data_fg = -1
    tbl.header_horizontal_line_on = False




    lst = [["H1","H2","H3"],[5,4,9],[3]]


    message = f'''
      {cp.set_font(1,196,231)} Note: {cp.reset_font()} For more reference see Diagrams (1 through 4).



      {cp.set_font(1,22,231,True)} design_color   {cp.reset_font()} Specifies the background (bg) colors to be applied to the
                       table for designs 1 through 10.

      {cp.set_font(1,22,231,True)} bg_line_colors {cp.reset_font()} Sets the background colors for all lines. If set to the
                       default value (-1 or 256), the style will use the
                       assigned bg color variable for every line instead.

      {cp.set_font(1,22,231,True)} fg_line_colors {cp.reset_font()} Sets the foreground colors for all lines. If set to the
                       default value (-1 or 256), the style will use the
                       assigned fg color variable for every line instead.

      {cp.set_font(1,22,231,True)} bold_lines     {cp.reset_font()} When set to True, all lines in the table will be
                       displayed in bold. When set to False, the style will use
                       the individually assigned bold value for each line.


{cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}
      {cp.set_font(1,53,231,0)}     Title Section                      Footnote Section                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}
      {cp.set_font(0,53,231,0)} T.  title_msg       = ""        |  F.  footnote_msg       = ""         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     title_bold      = False     |      footnote_bold      = False      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     title_bg        = -1        |      footnote_bg        = -1         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     title_fg        = -1        |      footnote_fg        = -1         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     title_align     = "justify" |      footnote_align     = "justify"  {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     title_italic    = False     |      footnote_italic    = False      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     title_underline = False     |      footnote_underline = False      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     title_strike    = False     |      footnote_strike    = False      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     title_blinking  = False     |      footnote_blinking  = False      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     title_dim       = False     |      footnote_dim       = False      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     title_hidden    = False     |      footnote_hidden    = False      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     title_inverse   = False     |      footnote_inverse   = False      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}
      {cp.set_font(1,53,231,0)}     Header Section                      Data Section                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}
      {cp.set_font(0,53,231,0)} H.  header_msg       = ""        |  D.  data_msg       = ""            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     header_bold      = False     |      data_bold      = False         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     header_bg        = -1        |      data_bg        = -1            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     header_fg        = -1        |      data_fg        = -1            {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     header_align     = "justify" |      data_align     = "justify"     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     header_italic    = False     |      data_italic    = False         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     header_underline = False     |      data_underline = False         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     header_strike    = False     |      data_strike    = False         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     header_blinking  = False     |      data_blinking  = False         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     header_dim       = False     |      data_dim       = False         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     header_hidden    = False     |      data_hidden    = False         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     header_inverse   = False     |      data_inverse   = False         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}
      {cp.set_font(1,53,231,0)}     General Use                                                        {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     set_fill_chr = "----"            | banded_row_bg      = -1         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}     set_layout   = Layout.HORIZONTAL | banded_row_fg      = -1         {cp.reset_font()}
      {cp.set_font(0,53,231,0)} S.  update_list  = False             | set_banded_row_on  = False      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                        {cp.reset_font()}


      When passing a list, FancyFormat automatically converts all elements to
      strings. If you use the update_list option with {cp.set_font(1,22,231,True)} update_list {cp.reset_font()}, be aware
      that the resulting list will contain only string elements. Note that the
      {cp.set_font(1,22,231,True)} update_list {cp.reset_font()} option only works with list-type variables. Additionally,
      if the list is incomplete or irregular (not a full matrix), FancyFormat
      will fill the missing spaces using the character(s) defined in the
      {cp.set_font(1,22,231,True)} set_fill_chr {cp.reset_font()} variable. See the example below.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  lst = [[\"H1\",\"H2\",\"H3\"],[5,4,9],[3]]
                  print(\"Original list: \",lst)

                  tbl = cp.FancyFormat()
                  tbl.update_list = True
                  tbl.print_fancy_format(lst)

                  print(lst)   # All the elements are string type now.
                               # The empty spaces are refill with the
                               # default value of set_fill_chr variable

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
      '''

    print(message)  # explanation: update_list, set_fill_chr
    print(f" Original list: {lst}\n")
    tbl.adj_indent = 16
    tbl.update_list = True
    tbl.print_fancy_format(lst)
    print()
    print(f" New list:      {lst}")
    print()

    message = f'''
      {cp.set_font(0,115,16)}                                                                       {cp.reset_font()}
      {cp.set_font(0,115,16)}   {cp.set_font(1,231,21,True)} Template Options: {cp.set_font(1,115,16)} FancyFormat includes several built-in templates {cp.reset_font()}
      {cp.set_font(1,115,16)}                       for quick styling. For more information and     {cp.reset_font()}
      {cp.set_font(1,115,16)}                       examples, refer to the print_fancy_format()     {cp.reset_font()}
      {cp.set_font(1,115,16)}                       method.                                         {cp.reset_font()}
      {cp.set_font(0,115,16)}                                                                       {cp.reset_font()}
    '''
    print(message)
    tbl.header_align = cp.Align.CENTER
    tbl.data_align = cp.Align.CENTER
    tbl.print_fancy_format(data=lst, style=cp.Line_Style.PURPLE_WHITE)


    message = f'''


      {cp.set_font(1,22,231,True)} set_layout {cp.reset_font()} set_layout can only be used with the following variable
                   types:
                          {cp.Unicode.BULLET} Dict             {cp.Unicode.BULLET} Range
                          {cp.Unicode.BULLET} Frozenset        {cp.Unicode.BULLET} set

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  tbl.title_msg = "Range Variable"
                  tbl.print_fancy_format(data=range(-5, 12, 5),
                                         style=cp.Line_Style.DOUBLE_LINE)

                  crs = cp.Cursor()
                  tbl.adj_indent = 50
                  crs.jumpTo(qty=4, direction="u")
                  tbl.set_layout = cp.Layout.VERTICAL
                  tbl.print_fancy_format(data=range(-5,12,5),
                                         style=cp.Line_Style.DOUBLE_LINE)


      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
    '''
    print(message) # explanation: set_layout
    tbl.title_msg = " Range Variable "
    tbl.print_fancy_format(data=range(-5, 12, 5),
                            style=cp.Line_Style.DOUBLE_LINE)

    tbl.set_layout = cp.Layout.VERTICAL
    tbl.adj_indent = 50
    crs.jumpTo(qty=4, direction="u")
    tbl.print_fancy_format(data=range(-5,12,5),
                           style=cp.Line_Style.DOUBLE_LINE)


    message = f'''
      {cp.set_font(0,115,16)}                                                                       {cp.reset_font()}
      {cp.set_font(0,115,16)}   {cp.set_font(1,231,21,True)} FancyFormat supports the following variable types: {cp.set_font(0,115,231,0)}                {cp.reset_font()}
      {cp.set_font(0,115,16)}                                                                       {cp.reset_font()}
      {cp.set_font(1,115,16)} {cp.Unicode.BULLET} bool        {cp.Unicode.BULLET} float          {cp.Unicode.BULLET} list       {cp.Unicode.BULLET} str  {cp.ins_chr(19)}{cp.reset_font()}
      {cp.set_font(1,115,16)} {cp.Unicode.BULLET} complex     {cp.Unicode.BULLET} flozenset      {cp.Unicode.BULLET} range      {cp.Unicode.BULLET} tuple{cp.ins_chr(19)}{cp.reset_font()}
      {cp.set_font(1,115,16)} {cp.Unicode.BULLET} dict        {cp.Unicode.BULLET} int            {cp.Unicode.BULLET} set               {cp.ins_chr(19)}{cp.reset_font()}
      {cp.set_font(0,115,16)}                                                                       {cp.reset_font()}
    '''
    print(message)


    message = f'''
      When {cp.set_font(1,22,231,True)} set_banded_row_on {cp.reset_font()} is set to True, the table will alternate row
      colors for the data rows. You can customize the alternating colors using
      the {cp.set_font(1,22,231,True)} banded_row_bg {cp.reset_font()} and {cp.set_font(1,22,231,True)} banded_row_fg {cp.reset_font()} variables. See the example below.


      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  tbl = cp.FancyFormat()
                  crs = cp.Cursor()

                  lst = [["set_banded_row_on = False"],["Data 1"],
                         ["Data 2"],["Data 3"],["Data 4"]]

                  tbl.adj_indent = 40
                  tbl.title_msg = "Banded Row Inactive"
                  tbl.header_bg = 4;          tbl.header_fg = 231
                  tbl.data_bg = 231;          tbl.data_fg = 16
                  tbl.header_horizontal_line_on = True

                  tbl.print_fancy_format(lst)

                  lst = [["set_banded_row_on = True"],["Data 1"],
                         ["Data 2"],["Data 3"],["Data 4"]]

                  tbl.adj_indent = 6
                  tbl.title_msg = "Banded Row Active"
                  tbl.set_banded_row_on = True
                  tbl.banded_row_bg = 208;    tbl.banded_row_fg = 16
                  crs.jumpTo(qty=8, direction=cp.Move.UP)

                  tbl.print_fancy_format(lst)

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
    '''

    print(message) # explanation: set_banded_row_on, banded_row_bg, banded_row_fg


    lst = [["set_banded_row_on = False"],["Data 1"],["Data 2"],["Data 3"],["Data 4"]]
    tbl.adj_indent = 40
    tbl.title_msg = "Banded Row Inactive"
    tbl.header_bg = 4;          tbl.header_fg = 231
    tbl.data_bg = 231;          tbl.data_fg = 16
    tbl.header_horizontal_line_on = True

    tbl.print_fancy_format(lst)

    tbl.adj_indent = 6
    tbl.set_banded_row_on = True
    tbl.banded_row_bg = 208;    tbl.banded_row_fg = 16
    crs.jumpTo(qty=9, direction=cp.Move.UP)

    tbl.title_msg = "Banded Row Active"
    lst = [["set_banded_row_on = True"],["Data 1"],["Data 2"],["Data 3"],["Data 4"]]
    tbl.print_fancy_format(lst)
    tbl.header_horizontal_line_on = False

    message = f'''

      {cp.set_font(1,196,231)} Note: {cp.reset_font()} To see all available attributes for the header, data, title, and
              footnote, refer to their respective sections above.
    '''
    print(message)


    message = f'''
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(1,53,231,0)}    Multi Color Section                                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    self.set_multi_bg_fg_on = False   |                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                      |                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    self.data_multi_bg_step  = 1      |    self.data_multi_fg_step  = 1   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    self.data_multi_bg_stop  = 255    |    self.data_multi_fg_stop  = 255 {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                      |                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}

       This option was created to make an effect to the table. When setting
       set_multi_bg_fg_on to True, the variables work as decribed below.

       data_multi_bg works as a range variable (start, stop, step).
       The start will be the the data_bg variable (describe on Data Section),
       the stop will be the data_multi_bg_stop and the step will be the
       variable data_bg_step.

       Let's assume you have a table with 5 data rows, and data_bg is set to 9,
       this is our start, the first row color will be the number 9, LIGHT_BLUE,
       check the ansi_colors function for more reference. Assume that our
       data_multi_bg_stop is set to 21. Now see the table below to see the
       behavior or the colors in the table.

       Rows        Start             Color
        1          data_bg = 12      PASTEL_RED            (9)
        2          data_bg += _step  ELECTRIC_LIGHT_GREEN  (10)
        3          14                DARKISH_YELLOW        (11)
        4          15                LIGHT_BLUE            (12)
        5          16                LIGHT_PURPLE          (13)


      {cp.set_font(1,196,231)} Note: {cp.reset_font()} The stop was set to 21,
      on this case the the data_multi_bg did not reach to the end. Now assume
      that the data_multi_bg_step is set to 4. See the behavior of the color
      in the following table.

       Rows        Start             Color
        1          data_bg = 12      PASTEL_RED            (9)
        2          data_bg += _step  LIGHT_PURPLE          (13)
        3          14                DARK_BLUE             (17)
        4          15                PASTEL_RED            (21) Restar (9)
        5          16                LIGHT_PURPLE          (13)

      Notice that the row fourth, reach the limit, However the color is
      restarted to the beginning which is the data_bg color, 9 (PASTEL_RED color).

      The data_multi_fg works exactly the same as the data_multi_bg.

      In the following example we keep the same background (step=0) to visualize
      the color in a better way. Also, notice that the header colors are NOT
      modified at all.



      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  tbl = cp.FancyFormat()

                  lst   = [["Header 1", "Header 2", "Header 3", "Header 4"],
                           ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
                           ["Data 2",   "Data 6",   "Data 7",   "Data 8"  ],
                           ["Data 3",   "Data 2",   "Data 3",   "Data 4"  ],
                           ["Data 4",   "Data 2",   "Data 3",   "Data 4"  ],
                           ["Data 5",   "Data 2",   "Data 3",   "Data 4"  ]]

                  tbl.header_bg = cp.No.VERY_DARK_MAGENTA
                  tbl.header_fg = cp.No.WHITE

                  tbl.data_bg   = cp.No.WHITE # 15
                  tbl.data_multi_bg_step = 0


                  tbl.set_multi_bg_fg_on = True
                  tbl.data_fg = 9               # start
                  tbl.data_multi_fg_step = 4
                  tbl.data_multi_fg_stop = 21
                  tbl.data_bold = True

                  tbl.print_fancy_format(data=my_list,
                                         style=cp.Line_Style.DASH_LINE)
      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
'''
    print(message)

    lst = [["Header 1", "Header 2", "Header 3", "Header 4"],
            ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
            ["Data 2",   "Data 6",   "Data 7",   "Data 8"  ],
            ["Data 3",   "Data 2",   "Data 3",   "Data 4"  ],
            ["Data 4",   "Data 2",   "Data 3",   "Data 4"  ],
            ["Data 5",   "Data 2",   "Data 3",   "Data 4"  ]]

    tbl.set_banded_row_on = False
    tbl.title_msg = "set_multi_bg_fg_on = True"
    tbl.header_bg = cp.No.VERY_DARK_MAGENTA
    tbl.header_fg = cp.No.WHITE

    tbl.data_bg   = cp.No.WHITE # 15
    tbl.data_multi_bg_step = 0


    tbl.set_multi_bg_fg_on = True
    tbl.data_fg = 9               # start
    tbl.data_multi_fg_step = 4
    tbl.data_multi_fg_stop = 21
    tbl.data_bold = True

    tbl.print_fancy_format(data=lst,
                            style=cp.Line_Style.DASH_LINE)

    message = f'''
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(1,53,231,0)}    Horizontal Line Section                Vertical Line Section          {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} b. top_horizontal_line_chr    = " "  | l. left_vertical_line_chr  = " "  {cp.reset_font()}
      {cp.set_font(0,53,231,0)} m. middle_horizontal_line_chr = " "  | n. middle_vertical_line_chr= " "  {cp.reset_font()}
      {cp.set_font(0,53,231,0)} t. bottom_horizontal_line_chr = " "  | o. right_vertical_line_chr = " "  {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    top_horizontal_line_on     = True |    right_vertical_line_on  = True {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    middle_horizontal_line_on  = False|    left_vertical_line_on   = True {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    bottom_horizontal_line_on  = True |    middle_vertical_line_on = True {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    horizontal_line_bold = False      |    vertical_line_fg   = -1        {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    horizontal_line_bg   = -1         |    vertical_line_bold = False     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    horizontal_line_fg   = -1         |    vertical_line_bg   = -1        {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(1,53,231,0)}    External Corner Section                Middle Corner Section          {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} a. top_left_corner_chr     = " "     | c. middle_top_corner_chr    = " " {cp.reset_font()}
      {cp.set_font(0,53,231,0)} d. top_right_corner_chr    = " "     | u. middle_bottom_corner_chr = " " {cp.reset_font()}
      {cp.set_font(0,53,231,0)} s. bottom_left_corner_chr  = " "     | p. middle_left_corner_chr  = " "  {cp.reset_font()}
      {cp.set_font(0,53,231,0)} v. bottom_right_corner_chr = " "     | q. middle_inner_corner_chr  = " " {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    outer_corner_bold = False         | r. middle_right_corner_chr = " "  {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    outer_corner_bg   = -1            |    inner_corner_bold = False      {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    outer_corner_fg   = -1            |    inner_corner_bg   = -1         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                      |    inner_corner_fg   = -1         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(1,53,231,0)}    Header Horizontal Line Section          Header Corner Section         {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} i. header_horizontal_line_chr = "-"  | h. header_left_corner_chr   = " " {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    header_horizontal_line_on  = True | j. header_middle_corner_chr = " " {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    header_horizontal_line_bold= False| k. header_right_corner_chr  = " " {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    header_horizontal_line_bg = -1    |    header_corner_bold = False     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    header_horizontal_line_fg = -1    |    header_corner_bg   = -1        {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    header_vertical_line_fg   = -1    |    header_corner_fg   = -1        {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(1,53,231,0)}    Header Vertical Line Section                                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} e. header_left_vertical_line_chr   = " " |  T {cp.Unicode.RIGHT_ARROW} title_msg                {cp.reset_font()}
      {cp.set_font(0,53,231,0)} f. header_middle_vertical_line_chr = " " |  H {cp.Unicode.RIGHT_ARROW} header                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} g. header_right_vertical_line_chr  = " " |  D {cp.Unicode.RIGHT_ARROW} data                     {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    header_vertical_line_bold   = False   |  S {cp.Unicode.RIGHT_ARROW} set_fill_chr             {cp.reset_font()}
      {cp.set_font(0,53,231,0)}    header_vertical_line_bg     = -1      |  F {cp.Unicode.RIGHT_ARROW} footnote_msg             {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(1,53,231,0)}  Space Section                                                           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} 1.  adj_top_margin = 0                   | 5.  adj_bottom_margin  = 0    {cp.reset_font()}
      {cp.set_font(0,53,231,0)} 2.  top_space      = 0                   | 6.  adj_bottom_space   = 0    {cp.reset_font()}
      {cp.set_font(0,53,231,0)} 3.  adj_indent     = 2                   | 7.  header_all_cell_bg = True {cp.reset_font()}
      {cp.set_font(0,53,231,0)} 4.  adj_space      = 2                   | 8.  data_all_cell_bg   = True {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
    '''
    print(message)
    message = f'''\033[1;48;5;232m


   \033[1;48;5;231;38;5;16m Diagram 1 \033[1;48;5;232;38;5;117m


  $█
               {cp.Unicode.UP_DOWN_ARROW} 1
               T           b      c         b         c         b
               {cp.Unicode.UP_DOWN_ARROW} 2         {cp.Unicode.DOWN_ARROW}      {cp.Unicode.DOWN_ARROW}         {cp.Unicode.DOWN_ARROW}         {cp.Unicode.DOWN_ARROW}         {cp.Unicode.DOWN_ARROW}
           a{cp.Unicode.RIGHT_ARROW} ╔═══════════════════╦═══════════════════╦══════════════════╗{cp.Unicode.LEFT_ARROW} d
           e{cp.Unicode.RIGHT_ARROW} ║        H       f{cp.Unicode.RIGHT_ARROW} ║         H         ║{cp.Unicode.LEFT_ARROW} f     H         ║{cp.Unicode.LEFT_ARROW} g
           h{cp.Unicode.RIGHT_ARROW} ╠═══════════════════╬═══════════════════╬══════════════════╣{cp.Unicode.LEFT_ARROW} k
           l{cp.Unicode.RIGHT_ARROW} ║ i{cp.Unicode.UP_ARROW}     D   m{cp.Unicode.DOWN_ARROW}  j\u2197 ║{cp.Unicode.LEFT_ARROW} n      D      j\u2197 ║{cp.Unicode.LEFT_ARROW} n    D          ║{cp.Unicode.LEFT_ARROW} o
           p{cp.Unicode.RIGHT_ARROW} ╠═══════════════════╬═══════════════════╬══════════════════╣{cp.Unicode.LEFT_ARROW} r
           l{cp.Unicode.RIGHT_ARROW} ║  m{cp.Unicode.UP_ARROW}    D    m{cp.Unicode.DOWN_ARROW} q\u2197 ║{cp.Unicode.LEFT_ARROW} n      D      q\u2197 ║{cp.Unicode.LEFT_ARROW} n    D          ║{cp.Unicode.LEFT_ARROW} o
           p{cp.Unicode.RIGHT_ARROW} ╠═══════════════════╬═══════════════════╬══════════════════╣{cp.Unicode.LEFT_ARROW} r
           l{cp.Unicode.RIGHT_ARROW} ║  m{cp.Unicode.UP_ARROW}    D   t{cp.Unicode.DOWN_ARROW}  q\u2197 ║{cp.Unicode.LEFT_ARROW} n     --S     q\u2197 ║{cp.Unicode.LEFT_ARROW} n   --S         ║{cp.Unicode.LEFT_ARROW} o
           s{cp.Unicode.RIGHT_ARROW} ╚═══════════════════╩═══════════════════╩══════════════════╝{cp.Unicode.LEFT_ARROW} v
  |<--------->|<----->|t{cp.Unicode.UP_ARROW}|<----->|{cp.Unicode.UP_ARROW}u       t{cp.Unicode.UP_ARROW}        u{cp.Unicode.UP_ARROW}              {cp.Unicode.UP_DOWN_ARROW} 5
        3         4          4             4                         F
              |<---------------->|                                   {cp.Unicode.UP_DOWN_ARROW} 6
                       7,8




   \033[1;48;5;231;38;5;16m Diagram 2 \033[1;48;5;232m                              \033[1;48;5;231;38;5;16m Diagram 4 \033[1;48;5;232;38;5;161m


  $█                                    |  $█
               {cp.Unicode.UP_DOWN_ARROW} 1                      |               {cp.Unicode.UP_DOWN_ARROW} 1
               T       b                |               T              b
               {cp.Unicode.UP_DOWN_ARROW} 2     {cp.Unicode.DOWN_ARROW}                |               {cp.Unicode.UP_DOWN_ARROW} 2            {cp.Unicode.DOWN_ARROW}
           a{cp.Unicode.RIGHT_ARROW} ╔══════════════════╗{cp.Unicode.LEFT_ARROW} d   |           a{cp.Unicode.RIGHT_ARROW} ╔══════════════════╗{cp.Unicode.LEFT_ARROW} d
           e{cp.Unicode.RIGHT_ARROW} ║  i{cp.Unicode.DOWN_ARROW}    H         ║{cp.Unicode.LEFT_ARROW} g   |           e{cp.Unicode.RIGHT_ARROW} ║         D        ║{cp.Unicode.LEFT_ARROW} o
           h{cp.Unicode.RIGHT_ARROW} ╠══════════════════╣{cp.Unicode.LEFT_ARROW} k   |           s{cp.Unicode.RIGHT_ARROW} ╚══════════════════╝{cp.Unicode.LEFT_ARROW} v
           l{cp.Unicode.RIGHT_ARROW} ║        D         ║{cp.Unicode.LEFT_ARROW} o   |  |<--------->|<----->|t{cp.Unicode.UP_ARROW}|<----->|{cp.Unicode.UP_DOWN_ARROW} 5
           p{cp.Unicode.RIGHT_ARROW} ╠══════════════════╣{cp.Unicode.LEFT_ARROW} r   |        3         4          4    F
           l{cp.Unicode.RIGHT_ARROW} ║ m{cp.Unicode.DOWN_ARROW}     D    m{cp.Unicode.UP_ARROW}   ║{cp.Unicode.LEFT_ARROW} o   |              |<---------------->|{cp.Unicode.UP_DOWN_ARROW} 6
           p{cp.Unicode.RIGHT_ARROW} ╠══════════════════╣{cp.Unicode.LEFT_ARROW} r   |                        8
           l{cp.Unicode.RIGHT_ARROW} ║ t{cp.Unicode.DOWN_ARROW}     D         ║{cp.Unicode.LEFT_ARROW} o   |
           s{cp.Unicode.RIGHT_ARROW} ╚══════════════════╝{cp.Unicode.LEFT_ARROW} v   |
  |<--------->|<----->|t{cp.Unicode.UP_ARROW}|<----->|{cp.Unicode.UP_DOWN_ARROW} 5   |
        3         4          4    F     |
              |<---------------->|{cp.Unicode.UP_DOWN_ARROW} 6   |
                      7,8               |




   \033[1;48;5;231;38;5;16m Diagram 3 \033[1;48;5;232;38;5;29m


  $█
              {cp.Unicode.UP_DOWN_ARROW} 1
              T      b         c         b        c         b
              {cp.Unicode.UP_DOWN_ARROW} 2    {cp.Unicode.DOWN_ARROW}         {cp.Unicode.DOWN_ARROW}         {cp.Unicode.DOWN_ARROW}        {cp.Unicode.DOWN_ARROW}         {cp.Unicode.DOWN_ARROW}
          a{cp.Unicode.RIGHT_ARROW} ╔═════════════════╦══════════════════╦══════════════════╗{cp.Unicode.LEFT_ARROW} d
          l{cp.Unicode.RIGHT_ARROW} ║   t{cp.Unicode.DOWN_ARROW}   D    n {cp.Unicode.RIGHT_ARROW} ║        D     n {cp.Unicode.RIGHT_ARROW} ║        D         ║{cp.Unicode.LEFT_ARROW} o
          s{cp.Unicode.RIGHT_ARROW} ╚═════════════════╩══════════════════╩══════════════════╝{cp.Unicode.LEFT_ARROW} v
  |<-------->|<----->| |<----->|         t{cp.Unicode.UP_ARROW}       u{cp.Unicode.UP_ARROW}              {cp.Unicode.UP_DOWN_ARROW} 5
       3         4         4                                      F
             |<--------------->|                                  {cp.Unicode.UP_DOWN_ARROW} 6
                     8


\033[0m
'''
    print(message)
    # self.middle_left_corner_chr  = " "        # chr only for matrix list (before: left_lateral_corner_chr  1.4V)
    # self.middle_right_corner_chr = " "        # chr only for matrix list (before: right_lateral_corner_chr 1.4V)


def fancyformat_info():
    ''' It prints data in a table format. '''
    fancyformat_only_info()
    print_fancy_format_info()
    reset_fancy_format_info()


# +--------------------------------------------------------------------------------------------+
# | print_fancy_format                                                                         |
# +--------------------------------------------------------------------------------------------+
def print_fancy_format_info():
    ''' The print_fancy_format() method prints any variable in a customized table format. '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[49])
    tbl = cp.FancyFormat()
    message = f'''
    The print_fancy_format() method prints any variable in a customized and
    visually appealing table format. It is highly flexible and can be
    customized to suit your preferences.

    * `print_fancy_format(data, style)`
    This function prints data using fancy formatting. By default, it uses a
    customized style.

    {cp.set_font(1,231,16)} **Parameters:** {cp.reset_font()}

    {cp.set_font(1,231,16)} data {cp.reset_font()} The data to be printed. It accepts `bool`, `int`, `float`, `complex`,
           `str`, `dict`, `range`, `set`, `frozenset`, or `tuple`.

    {cp.set_font(1,231,16)} style {cp.reset_font()} Controls the line style. Use the `Line_Style` class to access more
            options. See the demos for examples and reference.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  tbl.top_left_corner_chr = \"a\"
                  tbl.top_horizontal_line_chr = \"-\"
                  tbl.top_right_corner_chr = \"d\"
                  tbl.left_vertical_line_chr = f\"{{cp.Unicode.UP_DOWN_ARROW}}\"
                  tbl.bottom_left_corner_chr = \"s\"
                  tbl.bottom_right_corner_chr = \"v\"
                  tbl.bottom_horizontal_line_chr = \"-\"
                  tbl.right_vertical_line_chr = f\"{{cp.Unicode.UP_DOWN_ARROW}}\"
                  data = \" I am a Data (D) \"

                  tbl.print_fancy_format(data=data,
                                        style=cp.Line_Style.CUSTOMIZED)

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
    '''
    print(message)
    tbl.adj_indent = 18
    tbl.top_left_corner_chr = "a"
    tbl.top_horizontal_line_chr = "-"
    tbl.top_right_corner_chr = "d"
    tbl.left_vertical_line_chr = f"{cp.Unicode.UP_DOWN_ARROW}"
    tbl.bottom_left_corner_chr = "s"
    tbl.bottom_right_corner_chr = "v"
    tbl.bottom_horizontal_line_chr = "-"
    tbl.right_vertical_line_chr = f"{cp.Unicode.UP_DOWN_ARROW}"
    data = " I am a Data (D) "
    tbl.print_fancy_format(data=data,style=cp.Line_Style.CUSTOMIZED)


    message = f'''
    {cp.set_font(1,196,231)} Note: {cp.reset_font()} Remember that these are shortcuts for style customization.

            {cp.set_font(1,22,231,True)}                 {cp.reset_font()}
            {cp.set_font(1,22,231,True)} design_color    {cp.reset_font()}
            {cp.set_font(1,22,231,True)} bg_line_colors  {cp.reset_font()}
            {cp.set_font(1,22,231,True)} fg_line_colors  {cp.reset_font()}
            {cp.set_font(1,22,231,True)} bold_lines      {cp.reset_font()}
            {cp.set_font(1,22,231,True)}                 {cp.reset_font()}
'''
    print(message)

    message = f'''
    The customized option allows you to generate your own unique design. Refer
    to diagrams 1 through 4 to visualize how the FancyFormat variables are
    organized. Predefined templates for colors and line styles are also
    available. See the examples below.

      {cp.set_font(0,115,16)} DASH_LINE style {cp.reset_font()}

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  data = ["Data 1","Data 2","Data 3","Data 4"]
                  tbl.print_fancy_format(data=data,
                                         style=cp.Line_Style.DASH_LINE)
                  tbl.data_bg = 231
                  tbl.data_fg = 21

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
'''
    print(message)
    data = ["Data 1","Data 2","Data 3","Data 4"]
    tbl.data_bg = 231
    tbl.data_fg = 21
    tbl.print_fancy_format(data=data, style=cp.Line_Style.DASH_LINE)

    tbl.adj_indent = 2
    tbl.header_bg = 115; tbl.header_fg = 16

    message =f'''
      {cp.set_font(1,196,231)} Note: {cp.reset_font()} See the Line_Style class for additional available options

      {cp.set_font(1,231,16)} Style_Lines {cp.reset_font()} The Style_Lines class provides four types of templates.
      When using line-based templates (such as DASH, SINGLE_LINE, etc.) or
      DESIGN templates (1 through 10), the bg and fg colors for headers and
      data work normally. However, when using color templates (such as
      WHITE_PURPLE and similar), the bg and fg settings for headers and data
      are ignored, except when they apply to banded rows or data multi colors.
      For SPACE templates (0 through 6), you must specify the bg and fg colors
      for every element in the table. See the Line_Style class for examples.
      '''
    print(message)


    message = f'''
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  lst = [[\"Header 0\",\"Header 1\",\"Header 2\",\"Header 3\"],
                  [\"Col 0 Row 1\", \"Col 1 Row 1\", \"Col 2 Row 1\", \"Col 3 Row 1\"],
                  [\"Col 0 Row 2\", \"Col 1 Row 2\", \"Col 2 Row 2\", \"Col 3 Row 2\"],
                  [\"Col 0 Row 3\", \"Col 1 Row 3\", \"Col 2 Row 3\", \"Col 3 Row 3\"]]

                  tbl = cp.FancyFormat()
                  tbl.adj_top_margin = 2
                  tbl.header_align = cp.Align.CENTER
                  tbl.header_bold = True
                  tbl.data_align = cp.Align.LEFT
                  tbl.data_bg = 118
                  tbl.data_fg = 16
                  tbl.data_bold = True
                  tbl.title_msg = " Default Style = DASH_LINE "
                  tbl.print_fancy_format(lst)


                   tbl.title_msg   = " TURQUOISE_BLACK Template "
                   tbl.data_align = cp.Align.RIGHT
                   tbl.title_align = cp.Align.CENTER
                   tbl.title_bg = cp.No.DARK_WHITE
                   tbl.title_fg = 22
                   tbl.title_bold = True
                   tbl.print_fancy_format(data=lst,
                                          style=cp.Line_Style.TURQUOISE_BLACK)

      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
    '''



    print(message)
    lst = [["Header 0","Header 1","Header 2","Header 3"],
       ["Col 0 Row 1", "Col 1 Row 1", "Col 2 Row 1", "Col 3 Row 1"],
       ["Col 0 Row 2", "Col 1 Row 2", "Col 2 Row 2", "Col 3 Row 2"],
       ["Col 0 Row 3", "Col 1 Row 3", "Col 2 Row 3", "Col 3 Row 3"]]

    tbl.adj_top_margin = 2
    tbl.header_align = cp.Align.CENTER
    tbl.header_bold = True
    tbl.data_align = cp.Align.LEFT
    tbl.data_bg = 118
    tbl.data_fg = 16
    tbl.data_bold = True
    tbl.title_msg = " Default Style = DASH_LINE "
    tbl.print_fancy_format(lst)

    tbl.title_msg = " TURQUOISE_BLACK Template "
    tbl.data_align = cp.Align.RIGHT
    tbl.title_align = cp.Align.CENTER
    tbl.title_bg = cp.No.DARK_WHITE
    tbl.title_fg = 22
    tbl.title_bold = True
    tbl.print_fancy_format(data=lst,
                           style=cp.Line_Style.TURQUOISE_BLACK)




    message = f'''
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  tbl = cp.FancyFormat()

                  lst = [[\"Header 0\",\"Header 1\",\"Header 2\",\"Header 3\"],
                  [\"Col 0 Row 1\", \"Col 1 Row 1\", \"Col 2 Row 1\", \"Col 3 Row 1\"],
                  [\"Col 0 Row 2\", \"Col 1 Row 2\", \"Col 2 Row 2\", \"Col 3 Row 2\"],
                  [\"Col 0 Row 3\", \"Col 1 Row 3\", \"Col 2 Row 3\", \"Col 3 Row 3\"]]

                  tbl.design_color = 53
                  tbl.header_bg = 231;        tbl.header_fg = 16
                  tbl.data_bg   = 196;        tbl.data_fg = 231


                  tbl.data_align = cp.Align.CENTER
                  tbl.title_msg = " DESIGN_5 Template "

                  tbl.print_fancy_format(data=lst,
                                         style=cp.Line_Style.DESIGN_5)
      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
    '''
    print(message)

    tbl.design_color = 53
    tbl.data_align = cp.Align.CENTER
    tbl.title_msg = " DESIGN_5 Template "
    tbl.header_bg = 231; tbl.header_fg = 16
    tbl.data_bg = 196; tbl.data_fg = 231
    tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_5)

    message = f'''
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  tbl = cp.FancyFormat()

                  lst = [["Header 1", "Header 2", "Header 3", "Header 4"],
                         ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
                         ["Data 2",   "Data 6",   "Data 7",   "Data 8"  ],
                         ["Data 3",   "Data 2",   "Data 3",   "Data 4"  ],
                         ["Data 4",   "Data 2",   "Data 3",   "Data 4"  ],
                         ["Data 5",   "Data 2",   "Data 3",   "Data 4"  ]]

                  tbl.title_msg = " Line_Style.TEAL_WHITE "
                  tbl.title_align = cp.Align.CENTER
                  tbl.title_bg = cp.No.DARK_WHITE
                  tbl.title_fg = 22

                  tbl.header_bg = cp.No.VERY_DARK_MAGENTA
                  tbl.header_fg = cp.No.WHITE

                  tbl.data_align = cp.Align.CENTER
                  tbl.data_bold  = True
                  tbl.data_bg    = cp.No.WHITE # 15 (start)
                  tbl.data_fg    = 9           #    (start)

                  tbl.set_multi_bg_fg_on = True

                  tbl.data_multi_bg_step = 2
                  tbl.data_multi_bg_stop = 255  # This is the default value
                                                # just to undertand better.
                                                # Not necessary.
                  tbl.data_multi_fg_step = 4
                  tbl.data_multi_fg_stop = 121

                  tbl.print_fancy_format(data=lst,
                                        style=cp.Line_Style.TEAL_WHITE)
                  # TEAL_WHITE -> data_bg=231  data_fg=21
                  # How the design is done with the colors internally.
      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
'''
    print(message)
    tbl.title_msg = " Line_Style.TEAL_WHITE "

    lst = [["Header 1", "Header 2", "Header 3", "Header 4"],
           ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
           ["Data 2",   "Data 6",   "Data 7",   "Data 8"  ],
           ["Data 3",   "Data 2",   "Data 3",   "Data 4"  ],
           ["Data 4",   "Data 2",   "Data 3",   "Data 4"  ],
           ["Data 5",   "Data 2",   "Data 3",   "Data 4"  ]]

    tbl.header_bg = cp.No.VERY_DARK_MAGENTA
    tbl.header_fg = cp.No.WHITE

    tbl.data_bold = True
    tbl.data_bg   = cp.No.WHITE # 15 (start)
    tbl.data_fg   = 9           #    (start)

    tbl.set_multi_bg_fg_on = True

    tbl.data_multi_bg_step = 2
    tbl.data_multi_bg_stop = 255  # This is the default value
                                  # just to undertand better (Not necessary)

    tbl.data_multi_fg_step = 4
    tbl.data_multi_fg_stop = 121

    tbl.print_fancy_format(data=lst, style=cp.Line_Style.TEAL_WHITE)
    # TEAL_WHITE -> data_bg=231  data_fg=21

    message = f'''
      {cp.set_font(1,196,231)} Note: {cp.reset_font()} The colors for the TEAL_WHITE are set internally to data_bg = 231
              and data_fg = 21, that is the start colors. From that point the colors start to modified with the settings
              created in the code above using the variables:

      {cp.set_font(1,22,231,True)}                             {cp.reset_font()}
      {cp.set_font(1,22,231,True)}  set_multi_bg_fg_on = True  {cp.reset_font()}
      {cp.set_font(1,22,231,True)}                             {cp.reset_font()}
      {cp.set_font(1,22,231,True)}  data_multi_bg_step = 2     {cp.reset_font()}
      {cp.set_font(1,22,231,True)}  data_multi_bg_stop = 255   {cp.reset_font()}
      {cp.set_font(1,22,231,True)}                             {cp.reset_font()}
      {cp.set_font(1,22,231,True)}  data_multi_fg_step = 4     {cp.reset_font()}
      {cp.set_font(1,22,231,True)}  data_multi_fg_stop = 121   {cp.reset_font()}
      {cp.set_font(1,22,231,True)}                             {cp.reset_font()}

'''
    print(message)

# +--------------------------------------------------------------------------------------------+
# | reset_fancy_format                                                                         |
# +--------------------------------------------------------------------------------------------+
def reset_fancy_format_info():
    ''' It resets all the variables from the FancyFormat Class to their default values '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[50])

    tbl = cp.FancyFormat()
    tbl.adj_top_margin = 5

    message = f'''
      This method resets all FancyFormat variables back to their original
      default values.

      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
                  tbl = cp.FancyFormat()
                  tbl.adj_top_margin = 5
                  print("Assign: ", tbl.adj_top_margin)

                  tbl.reset_fancy_format()
                  print("\\nReset : ", tbl.adj_top_margin)


    {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}    Assign: {tbl.adj_top_margin}
    '''
    tbl.reset_fancy_format()
    print(message)
    print(f"                  Reset : {tbl.adj_top_margin}\n")





# +-------------------------------------------------------------------------------------------------+
# |                                                                                                 |
# |        GROUP: ASCIIART_CLASS                                                                    |
# |                                                                                                 |
# +-------------------------------------------------------------------------------------------------+
# |  AsciiArt in custom_print Module                                                                |
# +-------------------------------------------------------------------------------------------------+
def asciiart_only_info():
    print("it needs work")
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[51])
    art = cp.AsciiArt()

    message = f'''
        This class includes four different methods that allow you to print
        ASCII art in various styles.

            {cp.set_font(1,22,231,True)} Methods {cp.reset_font()}

            {cp.Unicode.BULLET} print_ascii_art             {cp.Unicode.BULLET} print_ascii_logo_art
            {cp.Unicode.BULLET} print_multi_ascii_art       {cp.Unicode.BULLET} print_reversed_ascii_logo_art


        The table below describes all the supported names for letters, numbers,
        and symbols available in the AsciiArt class.
        '''
    print(message)

    art.description_ascii_letters()

    message = f'''
        The table below describes all the supported logos in the AsciiArt class.
    '''
    print(message)

    art.description_ascii_logos()

    message = f'''
      {cp.set_font(1,231,16)} Default Values {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(1,53,231,0)} Letter Section                                                           {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} bg   = -1               strike = False                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} fg   = -1               hidden = False                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} dim  = -1               blinking   = False                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)} bold = False            underline  = False                               {cp.reset_font()}
      {cp.set_font(0,53,231,0)} italic  = False         delay_ms   = 0                                   {cp.reset_font()}
      {cp.set_font(0,53,231,0)} inverse = False         ascii_type = Ascii_Letter.Standard               {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}

      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(1,53,231,0)} Space Section                Line Section                                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
      {cp.set_font(0,53,231,0)} adj_indent = 0          |    set_layout = Layout.VERTICAL                {cp.reset_font()}
      {cp.set_font(0,53,231,0)} adj_space  = 0          |    set_top_line = True                         {cp.reset_font()}
      {cp.set_font(0,53,231,0)} adj_left_space   = 0    |    set_bottom_line = True                      {cp.reset_font()}
      {cp.set_font(0,53,231,0)} adj_middle_space = 0    |                                                {cp.reset_font()}
      {cp.set_font(0,53,231,0)} adj_right_space  = 0    |                                                {cp.reset_font()}
      {cp.set_font(0,53,231,0)}                                                                          {cp.reset_font()}
    '''
    print(message)

def asciiart_info():
    ''' The AsciiArt class converts letters, numbers, and symbols into ASCII art. '''
    asciiart_only_info()
    print_ascii_art_info()
    print_multi_ascii_art_info()
    print_ascii_logo_art_info()
    print_reversed_ascii_logo_art_info()


def print_ascii_art_info():
    ''' The AsciiArt class converts letters, numbers, and symbols into ASCII art. '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[52])

    print("ascii_art method")

def print_multi_ascii_art_info():
    ''' This method prints multi Ascii Art. '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[53])
    print("multi_ascii_art method")

def print_ascii_logo_art_info():
    ''' This method prints a logo in an Ascii Art. '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[54])
    print("ascii_logo_art method")

def print_reversed_ascii_logo_art_info():
    ''' This method prints a logo in an Ascii Art in reverse mode. '''
    cp.ins_newline(1)
    blue_div.print_fancy_divider(all_topics[55])
    print("reversed_ascii_logo_art method")

    message = f'''
      {cp.set_font(1,196,231)} Note: {cp.reset_font()}
      {cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp
      {cp.set_font(1,231,90)} \u25CF Output {cp.reset_font()}
    '''





def pylo_info():
    print("some work need here")













if __name__ == '__main__':
    print(sys.argv)
    help_documentation()

# in the top insert a new line(group name) cp.ins_newline(1), before the divider
# in the top insert a newline for message and the tail a newline for the message
# at the end of the function or method add double newline.
# this will be the parttern for title and tail of the function class



