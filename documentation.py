import sys
import fancyprint as fp

lst = fp.FancyFormat()
blue_msg  = fp.FancyMessage()  # for titles
green_msg = fp.FancyMessage()  # for subtitles
darkg_msg= fp.FancyMessage()   # for warning
crs = fp.Cursor()

ncols, nrows = fp.dimensions()
if (fp.OS_Linux == True and fp.OS_Windows == False): fp.resize(rows=93, cols=93) #fp.resize(44, 90)
elif (fp.OS_Linux == False and fp.OS_Windows == True): pass
else:                                                  pass

fp.clear()



#------------------------------------------------------------------------------------------------
# All Functions and Classes in fancyprint Module                                                -
#------------------------------------------------------------------------------------------------
title = ''' All Functions, Classes and Methods in fancyprint Module  '''       
use_module = " import fancyprint as fp"
#------------------------------------------------------------------------------------------------
#  All Functions in fancyprint module                                                           -
#------------------------------------------------------------------------------------------------
screen_funs = [[" Screen Functions "],["fp.clean()"],["fp.clear()"],["fp.erase()"],["fp.dimensions()"],
               ["fp.resize(rows, cols)"]]

blue_msg.bold = True
blue_msg.print_fancy_msg(title)

blue_msg.italic = True
blue_msg.fg = 226
blue_msg.print_fancy_msg(use_module)
blue_msg.fg = 231

lst.bg_all_cell_header = False
lst.bold_header = True
lst.bg_header = 90
lst.fg_header = 231
lst.italic_header = True
# lst.underline_header = True
lst.print_fancy_format(screen_funs)
fp.ins_newline(2)

green_msg.bg = 2;  green_msg.fg = 0; green_msg.bold = True
#------------------------------------------------------------------------------------------------
# clean                                                                                         -
#------------------------------------------------------------------------------------------------
message = '''
   It cleans the terminal and return the cursor to home.
   It uses ansi code.
'''
green_msg.print_fancy_msg(screen_funs[1][0])
print(message)

#------------------------------------------------------------------------------------------------
# clear                                                                                         -
#------------------------------------------------------------------------------------------------
message = '''
    It cleans the terminal and return the cursor  to home.
    It uses the system command.
'''
green_msg.print_fancy_msg(screen_funs[2][0])
print(message)

#------------------------------------------------------------------------------------------------
# erase                                                                                         -
#------------------------------------------------------------------------------------------------
menssage = '''
   It cleans the terminal and the cursor remain in the same position.
   It uses ansi code.
'''
green_msg.print_fancy_msg(screen_funs[3][0])
print(menssage)

#------------------------------------------------------------------------------------------------
# dimensions                                                                                    -
#------------------------------------------------------------------------------------------------
menssage ='''
   It returns the size of the actual terminal: cols, rows.
   '''
green_msg.print_fancy_msg("ncols, nrows = "+screen_funs[4][0])
print(menssage)


#------------------------------------------------------------------------------------------------
# resize                                                                                        -
#------------------------------------------------------------------------------------------------
message = '''
      It resizes the terminal.
      '''
green_msg.print_fancy_msg(screen_funs[5][0])
print(message)

#------------------------------------------------------------------------------------------------
# reference for clean, clear, erase, dimensions and resize                                      -
#------------------------------------------------------------------------------------------------
def note_ref(bg, file_name):
   darkg_msg.bg = bg; darkg_msg.bold = True
   message = "Note:"
   darkg_msg.print_fancy_msg(message)
   darkg_msg.bold = False; darkg_msg.italic = True
   crs.jump(1,direction=fp.Move.UP)
   message = f'''
   For more reference, check {file_name} file.
             ''' 
   darkg_msg.print_fancy_msg(message)
   darkg_msg.italic = False
   print()

note_ref(bg=22, file_name="00_screen_funs.py")

#------------------------------------------------------------------------------------------------
font_funs = [[" Font Functions "],["fp.bg_ansi_colors(bold=False, fg=-1)"],["fp.fg_ansi_colors(bold=False, bg=-1)"],
             ["set_font(bold=True,bg=22,fg=231)"],["reset_font()"],["ins_space(sp)"],["isn_newline(nl)"]]
lst.print_fancy_format(font_funs)
fp.ins_newline(2)

#------------------------------------------------------------------------------------------------
# reset_font()                                                                                  -
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
# ins_space()                                                                                   -
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
# ins_newline()                                                                                 -
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
# bg_ansi_colors                                                                                -
#------------------------------------------------------------------------------------------------
green_msg.print_fancy_msg(font_funs[1][0])
message = '''
   import fancyprint as fp
   
   fp.bg_ansi_colors(bool, int)
   
   This function displays all background colors available in the fancyprint
      module. Two options for better visualization:
   
   1.- The option bold for the font (True/False).
   2.- The option fg to visualize the background colors with a specific
         foreground color.


   Colors range from -1 to 256.
   To set the default color use -1 or 256.

   Example:
            fp.bg_ansi_colors(0,22)
            fp.bg_ansi_colors(fg=0, bold=1)
'''
print(message)
print(f"{fp.set_font(fg=118)}  For more reference check 01_bg_ansi_colosr.py file.\n")
#note_ref("01_bg_ansi_colors.py")

#------------------------------------------------------------------------------------------------
# fg_ansi_colors                                                                                -
#------------------------------------------------------------------------------------------------
green_msg.print_fancy_msg(font_funs[2][0])
message =    '''
   import fancyprint as fp

   fl.fg_ansi_colors(bool, int)
   
   This function displays all foreground colors available in the fancyprint
      module. Two options for better visualization:
   
   1.- The option bold helps for font.
   2.- The option bg to visualize the foreground colors with a specific
         background color.

   Colors range from -1 to 256.# lst = fp.FancyFormat()
   To set the default color use -1 or 256.

   Example:
            fl.fg_ansi_colors(0,22)
            fl.fg_ansi_colors(bg=32, bold=0)
'''
print(message)
#note_ref("02_fg_ansi_colors.py")
print(f"{fp.set_font(fg=118)}  For more reference check 02_fg_ansi_colosr.py file.\n")
#------------------------------------------------------------------------------------------------
# Explanation of the Functions                                                                  -
#------------------------------------------------------------------------------------------------
lst.bg_all_cell_header = True; lst.underline_header = False
classes_methods = [["Classes","Mehtods"],["FancyFormat","print_fa"]]# lst = fp.FancyFormat()
blue_msg  = fp.FancyMessage()  # for titles
green_msg = fp.FancyMessage()  # for subtitles
darkg_msg= fp.FancyMessage()   # for warning
crs = fp.Cursor()
lst.print_fancy_format(classes_methods)




#------------------------------------------------------------------------------------------------
# print("\033[2m")
input(f"{fp.bold_on()}{fp.reverse_on()}{fp.blink_on()} Enter to Continue: {fp.off_all()}")
fp.resize(nrows, ncols)

# print("\033[22m")
ncols, nrows = fp.dimensions()
if (fp.OS_Linux == True and fp.OS_Windows == False): fp.resize(nrows, ncols) #fp.resize(44, 90)
elif (fp.OS_Linux == False and fp.OS_Windows == True): pass
else:                                                  pass


import sys
# import fancyprint as fp

lst = fp.FancyFormat()
font = fp.FontCustomization()
font.set_bg = 22
font.set_fg = 231
font.set_bold = True
font.set_italic = True
title = ''' All Functions, Classes and Methods in fancyprint Module  '''  
blue_msg  = fp.FancyMessage(font)  # for titles
blue_msg.print_fancy_msg(title)
font.set_bg = 90

purple_msg  = fp.FancyMessage(font)  # for titles
purple_msg.print_fancy_msg(title)

blue_msg.fg = 0
blue_msg.bg = 231
blue_msg.print_fancy_msg(title)


print()
print(f"{fp.bg_on(22)} Miguelito {fp.fg_on(13)} I am here {fp.bold_on()} Hello Again. {fp.off_all()}")
print()
print(f"{fp.bold_on()}{fp.bg_on(90)} Miguelito  I am here {fp.fg_on(11)} Hello Again. {fp.reset_font()}")
print(f"{fp.reverse_on()}Miguel Angel{fp.reverse_off()}")

for i in range(0, 16):
   for j in range(0, 16):
      code = str(i * 16 + j)
      sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
   print (u"\u001b[0m")


for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
    print (u"\u001b[0m")