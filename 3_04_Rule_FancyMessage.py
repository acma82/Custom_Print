import math
import custom_print as cp


def print_rule():
    #----------------------------------------------------------------------------------------------
    cp.terminal_bell()
    cols, rows = cp.dimensions()
    crs = cp.Cursor()
    #----------------------------------------------------------------------------------------------
    fm = cp.FancyMessage()
    fm.body_bold = True;    fm.left_indent = 0;    fm.right_indent = 0
    space = (math.ceil((cols - len("New Math Calculation...!"))/2)) -1 #-3
    # minus 3 one for the left ins_chr another for the right ins_chr, and the last one for the jump line
    #----------------------------------------------------------------------------------------------
    # LEFT
    message = "New Math Calculation...!" + cp.ins_chr(space*2," ")
    fm.print_fancy_message(message)
    print()
    #----------------------------------------------------------------------------------------------
    # CENTER
    message = cp.ins_chr(space," ") + "New Math Calculation...!" + cp.ins_chr(space," ")
    fm.body_bg = 90; fm.body_fg = 231; fm.body_bold = True
    fm.print_fancy_message(message)
    print()
    #----------------------------------------------------------------------------------------------
    # RIGHT
    message = cp.ins_chr((space*2)+2," ") + "New Math Calculation...!"
    fm.body_bg = 231; fm.body_fg = 21; fm.body_bold = True
    fm.print_fancy_message(message)
    crs.jumpTo(qty=1, direction=cp.Move.UP)
    print(cp.ins_chr(len(message), " "))
    #----------------------------------------------------------------------------------------------
    # JUSTIFY (indentation)
    fm.left_indent = 35
    message = "New Math Calculation...!"
    fm.body_bg = 22; fm.body_fg = 231; fm.body_bold = True
    fm.print_fancy_message(message)
    print()
    #----------------------------------------------------------------------------------------------

print_rule()