import fancyprint as fp

blue_msg = fp.FancyMessage()
blue_msg.bold = True; blue_msg.bg = 14; blue_msg.fg = 0

# terminal bell
fp.terminal_bell()


# bg_ansi_colors function
fp.ins_newline(1);      blue_msg.print_fancy_msg(" Background Available in Ansi Code...! ")
fp.ins_newline(1);      fp.bg_ansi_colors(bold=True, fg=0, n_line=1)


# fg_ansi_colors function
fp.ins_newline(2);      blue_msg.print_fancy_msg(" Foreground Available in Ansi Code...! ")
fp.ins_newline(2);      fp.fg_ansi_colors(bold=True, bg=-1, n_line=1)


# set_font() and reset_font() functions
fp.ins_newline(2)
print(fp.set_font(1,11,21) + " Python is " + fp.set_font(0,1) + " Wonderful." + fp.reset_font())


# ins_space() function
color1 = fp.set_font(1,90,231)
color2 = fp.set_font(1,231,-1)
color3 = fp.set_font(1,14,0)
fp.ins_newline(1)
print(f"{color1} Python {color2}{fp.ins_space(12)}{color3} Amazing...! {fp.reset_font()}")
fp.ins_newline(1)
