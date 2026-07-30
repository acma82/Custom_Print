#!/usr/bin/python3.12
'''
Documentation for fancyprint module...!
python3.12 cp_documentation.py
'''

import sys
import custom_print as cp

# standar size on the terminal is -> 24 by 80
# resize -s 50 80



def  Welcome_Message():
    pylo = cp.PyLO()
    # result = pylo.sort_rows_by_col(data=help_classes, ref_col=0, reversed_order=False, update=False)

    cols, rows = cp.dimensions()
    welcome_msg = "Documentation For custom_print Module....!"

    tbl = cp.FancyFormat()         # for lists    
    crs = cp.Cursor()              # Cursor Object
    blue_msg  = cp.FancyMessage()  # for titles

    screen_funs        = [[" Screen_Functions "], ["clean"], ["clear"], ["dimensions"], ["erase"], ["resize"]]

    internal_functions = [[" Internal_Functions "], ["ansi_colors"], ["ins_chr"], ["ins_newline"], ["set_font & reset_font"], ["terminal_bell"]]

    help_classes       = [["Align", "Length_bg"], ["Ascii_Letter", "Line_Style"],["Bg", "Move"], ["Divider Style", "No"],["Fg", "Style"],["Layout", "Unicode"]]

    ref_names          = [[" Referece_Names "],["Bg "],["Color_Names"],["Fg"],["No"]]
    
    # classes and methods for custom_print module
    cmcpp1 = [["Cursor",  "FontStyle"   ,  "FancyMessage"       ,  "Pen"           ],  
              ["jumpTo",  "start_style" ,  "print_fancy_message",  "draw_line"     ],  
              ["jumpxy",  "stop_style"  ,  "print_fancy_note"   ,  "draw_rectangle"],  
              ["moveTo",  "print_style" ,  "----"               ,  "----"          ],  
              ["movexy",  "reset_style" ,  "----"               ,  "----"          ]]

    cmcpp2 = [["FancyFormat"       ,  "Art"],
              ["print_fancy_format",  "print_ascii_art"],
              ["reset_fancy_format",  "print_multi_ascii_art"],
              ["----"              ,  "print_ascii_logo_art"],
              ["----"              ,  "print_reversed_ascii_logo_art"]]


    li = int(((cols)-(len(welcome_msg)))/2)
    blue_msg.left_indent = li
    blue_msg.body_bold   = True
    blue_msg.title_bold  = True
    blue_msg.italic_body = True
    blue_msg.print_fancy_message(welcome_msg)
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
    cp.ins_newline(n=2)



    tbl.header_horizontal_line_on = False;               tbl.header_italic = False
    tbl.header_bg    = -1;      tbl.header_fg = -1;      tbl.header_align = cp.Align.JUSTIFY
    tbl.header_bold  = False;   

    tbl.title_align = cp.Align.CENTER;                  tbl.title_italic = True
    tbl.title_bg    = 90;      tbl.title_fg = 231;      tbl.title_bold   = True
    tbl.title_msg   = " Help_Classes "
    tbl.print_fancy_format(help_classes)

    cp.ins_newline(n=2)

    crs.jumpTo(qty=10, direction=cp.Move.UP)
    tbl.adj_indent = 42
    tbl.title_msg = ""; tbl.header_horizontal_line_on = True
    tbl.header_italic = True; tbl.header_bold = True
    tbl.header_bg = 90; tbl.header_fg = 231
    tbl.print_fancy_format(ref_names)

    cp.ins_newline(n=2)
    blue_msg.length = cp.Length_bg.ONLY_WORD
    blue_msg.print_fancy_message("  Classes and Methods in fancyprint Module ")
    cp.ins_newline(n=1)

    tbl.adj_indent = 2
    tbl.header_all_cell_bg = True; tbl.header_align = cp.Align.CENTER
    # tbl.print_fancy_format(data=cmcpp1, style=cp.Line_Style.PURPLE_WHITE)
    tbl.print_fancy_format(data=cmcpp1)
    cp.ins_newline(n=2)
    tbl.adj_indent = 8
    tbl.print_fancy_format(data=cmcpp2)

    cp.ins_newline(n=2)

if __name__ == '__main__':
    Welcome_Message()
    