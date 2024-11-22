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
import fancyprint as fp

blue_msg = fp.FancyMessage()
blue_msg.bold = True
blue_msg.bg   = 14
blue_msg.fg   = 0

# terminal bell
fp.terminal_bell()


# bg_ansi_colors function
fp.ins_newline(1)
blue_msg.print_fancy_message(" Background Available in Ansi Code...! ")
fp.ins_newline(1)
fp.bg_ansi_colors(bold=True, fg=0, n_line=1)


# fg_ansi_colors function
fp.ins_newline(2)
blue_msg.print_fancy_message(" Foreground Available in Ansi Code...! ")
fp.ins_newline(2)
fp.fg_ansi_colors(bold=True, bg=-1, n_line=1)


# set_font() and reset_font() functions
fp.ins_newline(2)
print(fp.set_font(1,11,21) + " Python is " + fp.set_font(0,1) + " Wonderful." + fp.reset_font())


# ins_chr() function
color1 = fp.set_font(1,90,231)
color2 = fp.set_font(1,231,-1)
color3 = fp.set_font(1,14,0)
fp.ins_newline(1)
print(f"{color1} Python {color2}{fp.ins_chr(12)}{color3} Amazing...! {fp.reset_font()}")
fp.ins_newline(1)
