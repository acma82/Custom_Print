#!/usr/bin/python3.12
'''
Documentation for fancyprint module...!
python3.12 cp_documentation.py
'''

import sys
import custom_print as cp

# standar size on the terminal is -> 24 by 80
# resize -s 50 80



def  documentation_help():
    # pylo = cp.PyLO()
    # result = pylo.sort_rows_by_col(data=help_classes, ref_col=0, reversed_order=False, update=False)




    cols, rows = cp.dimensions()

    crs = cp.Cursor()               # Cursor Object
    fst = cp.FontStyle()            # FontStyle Object
    tbl = cp.FancyFormat()          # for lists
    blue_msg  = cp.FancyMessage()   # for titles

    fst.bold = True
    fst.fg   = 0
    fst.bg   = 231
    fst.indent = 3

    screen_funs        = [[" Screen_Functions "], ["clean"], ["clear"], ["dimensions"], ["erase"], ["resize"]]

    internal_functions = [[" Internal_Functions "], ["ansi_colors"], ["ins_chr"], ["ins_newline"], ["set_font & reset_font"], ["terminal_bell"]]

    help_classes       = [["Align", "Length_bg"], ["Ascii_Letter", "Line_Style"],["Bg", "Logo"], ["Color_Names", "Move"],["Divider_Style", "No"],["Fg", "Style"],["Layout", "Unicode"]]

    # classes and methods for custom_print module
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
    

    mensaje = "Documentation For custom_print Module....!"
    blue_msg.left_indent = int(((cols)-(len(mensaje)))/2)
    blue_msg.body_bold   = True
    blue_msg.title_bold  = True
    blue_msg.body_italic = True
    blue_msg.print_fancy_message(mensaje)
    cp.ins_newline()

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

    # blue_msg.length = cp.Length_bg.ONLY_WORD
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
    # tbl.print_fancy_format(data=cmcpp1, style=cp.Line_Style.PURPLE_WHITE)
    tbl.print_fancy_format(data=cmcpp1)
    cp.ins_newline(n=2)
    tbl.adj_indent = 13
    tbl.print_fancy_format(data=cmcpp2)


    cp.ins_newline(1)
    mensaje = "How to use the documentation in custom_print Module"
    blue_msg.left_indent = int(((cols)-(len(mensaje)))/2)
    blue_msg.print_fancy_message(mensaje)
    cp.ins_newline(n=1)


    print("   To display help for a specific function or method, just pass the name of the\n parameter as shown above.")
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


    blue_msg.length    = cp.Length_bg.ALL_ROW
    blue_msg.body_bold = False
    blue_msg.note_msg  = note
    blue_msg.note_bold = True
    blue_msg.body_bg   = 90
    blue_msg.note_position = 2
    blue_msg.print_fancy_note(message_note)
    cp.ins_newline(1)
    print(f"{fst.style_on()} Example 2: {fst.style_off()}  custom_print screen_functions art ins_chr movexy" )

# ----------------------------------------------------
    message = f'''     Notice that on\033[1m example 2\033[0m, is being called a group function, a class,
       a function and a method. For the group, it will be displayed all the
       documentation for all functions that belong to that group.

       {fst.style_on()} screen_functions: clean, clear, dimentsions, erase, resize. {fst.style_off()}
       
       I will display the documentation for all the methods that belong to that
       class. The above tables show all the classes with their methods.

       It will display the documentation for the function \033[1;48;5;1m ins_chr \033[0m as well.

       Documentation for the method \033[1;48;5;22;1m movexy \033[0m will be called as well.

       It's possible to display the complete documentation help by passing
       \"all\" as parameter. 

    '''

    
    cp.ins_newline(1)

    print(message)

    print(f"{fst.style_on()} example 3: {fst.style_off()}  custom_print all")

    cp.ins_newline(2)
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


#-- -------------------------------------------------------------------------------------------------
#   Variables in common for all the functions and classes                                           -
#-- -------------------------------------------------------------------------------------------------
div = cp.Divider()
# Message
div.msg_bg = 10;                  div.msg_fg = 0;                          div.msg_bold = True
div.adj_indent = 2;               div.align = cp.Align.CENTER;             div.all_fill_bg = 10
div.all_corner_bg = 10;           div.top_horizontal_line_bg = 10;         div.bottom_horizontal_line_bg = 10
div.left_vertical_line_bg = 10;   div.right_vertical_line_bg = 10


def all_documentation():
    print("all help is needed")

#-- -------------------------------------------------------------------------------------------------
#   Screen_Functions in fancyprint Module                                                           -
#-- -------------------------------------------------------------------------------------------------
def screen_functions():   
    print("help for screen functions")
    #   Clean_Function()
#     Clear_Function()
#     Erase_Function()
#     Dimensions_Function()
#     Resize_Function()


def clean():
   #------------------------------------------------------------------------------------------------
   # clean, It uses ansi code                                                                      -
   #------------------------------------------------------------------------------------------------   
    msg = f''' It cleans the terminal and returns the cursor to home. '''
    
    div.print_fancy_divider(message=msg, style=cp.Divider_Style.CUSTOMIZED)

    
    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import custom_print as cp")
    print(f"{cp.ins_chr(18)}cp.clean()\n")


def clear():
   #------------------------------------------------------------------------------------------------
   # clear,       It uses the system command                                                       -
   #------------------------------------------------------------------------------------------------
    message = '''
      It clears the terminal and returns the cursor to home.
    '''
    print(message)
    print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp")
    print(f"{cp.ins_chr(18)}cp.clear()\n")


# def Erase_Function():
#    #------------------------------------------------------------------------------------------------
#    # erase,       It uses ansi code                                                                -
#    #------------------------------------------------------------------------------------------------
#     menssage = '''
#       It erases the terminal and leaves the cursor in the current position.
#     '''
#     green_msg.print_fancy_message(screen_funs[3][0]+"()")
#     print(menssage)
#     print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp")
#     print(f"{cp.ins_chr(18)}cp.erase()\n")

# def Dimensions_Function():
#    #------------------------------------------------------------------------------------------------
#    # dimensions                                                                                    -
#    #------------------------------------------------------------------------------------------------
#     menssage ='''
#       It returns the dimensions of the terminal, cols and rows.
#      '''
#     green_msg.print_fancy_message(screen_funs[4][0]+"()")
#     print(menssage)
#     print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp")
#     print(f"{cp.ins_chr(18)}ncols, nrows = cp.dimensions()\n")

# def Resize_Function():
#    #------------------------------------------------------------------------------------------------
#    # resize                                                                                        -
#    #------------------------------------------------------------------------------------------------
#     message = '''
#       It resizes the terminal size.
#          '''
#     green_msg.print_fancy_message(screen_funs[5][0]+"(rows=25, cols=80)")
#     print(message)
#     print(f"{cp.ins_chr(6)}{cp.set_font(1,231,0)} Example: {cp.reset_font()}  import fancyprint as cp")
#     print(f"{cp.ins_chr(18)}cp.resize(rows=20, cols=120)")
#     cp.ins_newline(2)



if __name__ == '__main__':
    print(sys.argv)
    documentation_help()
