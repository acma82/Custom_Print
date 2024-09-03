import os
import fancyprint as fp

lst = fp.FancyFormat()
msg = fp.FancyMessage()
crs = fp.Cursor()


ncols, nrows = fp.dimensions()
fp.resize(44, 90)
# os.system("resize -s 44 90")
fp.clear()
#------------------------------------------------------------------------------------------------
# All Functions and Classes in fancyprint Module                                                -
#------------------------------------------------------------------------------------------------
title = '''
        All Functions, Classes and Methods in fancyprint Module
        
        import fancyprint as fp
        '''

#------------------------------------------------------------------------------------------------
#  All Functions in fancyprint module                                                           -
#------------------------------------------------------------------------------------------------
fp_funs = [[" Functions "],["fp.clean()"],["fp.clear"],["fp.erase()"],
        ["fp.dimensions()"],["fp.bg_ansi_colors(bold=False, fg=-1)"],["fp.fg_ansi_colors(bold=False, bg=-1)"]]

lst.bg_all_cell_header = False
lst.bold_header = True
lst.bg_header = 90
lst.fg_header = 231

msg.bold = True
msg.print_fancy_msg(title)

lst.print_fancy_format(fp_funs)
fp.ins_newline(2)


msg.bg = 2;  msg.fg = 0
#------------------------------------------------------------------------------------------------
# clean                                                                                         -
#------------------------------------------------------------------------------------------------
message = '''
   It cleans the terminal and return the cursor to home.
   It uses ansi code.
'''
msg.print_fancy_msg(fp_funs[1][0])
print(message)

#------------------------------------------------------------------------------------------------
# clear                                                                                         -
#------------------------------------------------------------------------------------------------
message = '''
    It cleans the terminal and return the cursor  to home.
    It uses the system command.
'''
msg.print_fancy_msg(fp_funs[2][0])
print(message)

#------------------------------------------------------------------------------------------------
# erase                                                                                         -
#------------------------------------------------------------------------------------------------
menssage = '''
   It cleans the terminal and the cursor remain in the same position.
   It uses ansi code.
'''
msg.print_fancy_msg(fp_funs[3][0])
print(menssage)



#------------------------------------------------------------------------------------------------
# Explanation of the Functions                                                                  -
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
# Explanation of the Functions                                                                  -
#------------------------------------------------------------------------------------------------
lst.bg_all_cell_header = True
classes_methods = [["Classes","Mehtods"],["FancyFormat","print_fancy_format()"],
                   ["Cursor", ],[]]#[f"{fp.ins_space(10)}",]]
lst.print_fancy_format(classes_methods)




#------------------------------------------------------------------------------------------------
# print("\033[2m")
input(f"{crs.set_blink()} Enter to Continue: ")
print(crs.reset_blink())
# print(crs.reset_reverse())
# print("\033[22m")
os.system(f"resize -s {nrows} {ncols}")
fp.clean()