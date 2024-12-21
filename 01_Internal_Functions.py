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

blue_msg = cp.FancyMessage()
blue_msg.bold = True
blue_msg.bg   = 14
blue_msg.fg   = 0

# terminal bell
cp.terminal_bell()


# bg_ansi_colors function
cp.ins_newline(1)
blue_msg.print_fancy_message(" Background Available in Ansi Code...! ")
cp.ins_newline(1)
cp.bg_ansi_colors(bold=True, fg=0, n_line=1)


# fg_ansi_colors function
cp.ins_newline(2)
blue_msg.print_fancy_message(" Foreground Available in Ansi Code...! ")
cp.ins_newline(2)
cp.fg_ansi_colors(bold=True, bg=-1, n_line=1)


# set_font() and reset_font() functions
cp.ins_newline(2)
print(cp.set_font(1,11,21) + " Python is " + cp.set_font(0,1) + " Wonderful." + cp.reset_font())


# ins_chr() function
color1 = cp.set_font(1,90,231)
color2 = cp.set_font(1,231,-1)
color3 = cp.set_font(1,14,0)
cp.ins_newline(1)
print(f"{color1} Python {color2}{cp.ins_chr(12)}{color3} Amazing...! {cp.reset_font()}")
cp.ins_newline(1)
