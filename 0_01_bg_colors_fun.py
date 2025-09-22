'''
Internal Functions Available
    
    reset_font()
    terminal_bell()
    ins_newline(n=1)
    ins_chr(n=1, unicode=" ")
    bg_ansi_colors(bold, fg, n_line)
    fg_ansi_colors(bold, bg, n_line)
    set_font(bold=False,bg=-1,fg=-1,italic=False,
             underline=False,strike=False,blinking=False,
             dim=False,hidden=False,inverse=False)
    
    
'''
import custom_print as cp
crs = cp.Cursor()
blue_msg = cp.FancyMessage()
blue_msg.bold = True
blue_msg.bg   = 14
blue_msg.fg   = 0

cp.terminal_bell()

# cols, rows = cp.dimensions()
#
#       Note:   if we use the Linux shortcuts for moving or resizing the terminal, 
#               the comand will not work because it is locked with the shortcut command.
#               uncomment line 26, 30, 71, and 73 to check the resize function.
#
# cp.resize(25,100)

cp.ins_newline(2)
blue_msg.print_fancy_message(" Background Available in Ansi Code...! ")
cp.ins_newline(2)

#+-----------------------------------------------------------------------------------+
#|    bg_ansi_colors function                                                        |
#+-----------------------------------------------------------------------------------+
cp.bg_ansi_colors(bold=True, fg=0, n_line=1)
