import custom_print as cp
#-------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    frog = []
    frog.append("           .--._.--.           ")  # 35
    frog.append("          ( O     O )          ")
    frog.append("          /   . .   \\          ")
    frog.append("         .`._______.'.         ")
    frog.append("        /(           )\\        ")
    frog.append("      _/  \\  \\   /  /  \\_      ") #####
    frog.append("   .~   `  \\  \\ /  /  '   ~.   ")
    frog.append("  {    -.   \\  V  /   .-    }  ")
    frog.append("_ _`.    \\  |  |  |  \\/    .'_ ")
    frog.append(">_       _} |  |  | {_       _<")
    frog.append(" /. - ~ ,_-'  .^.  `-_, ~ - .\\ ")
    frog.append("         '-'|/   \\|`-`         ")
    frog.append("                               ")


                      
                 
                 
    art_logo = cp.Art()
    crs = cp.Cursor()

    art_logo.bg = 90; art_logo.fg = 231; art_logo.delay_ms = 20; art_logo.bold = True
    art_logo.adj_indent = 10;  #art_logo.adj_left_space = 2; art_logo.adj_right_space = 4
    # art_logo.set_layout = cp.Layout.HORIZONTAL
    art_logo.ascii_type = cp.Alpha_M # mym

    back_up = len(cp.Alpha_M)
    width = len(cp.Alpha_M[0])
    art_logo.print_reversed_image_ascii_art()

    crs.jumpTo(qty=back_up, direction=cp.Move.UP)
    art_logo.ascii_type = cp.Alpha_E # mye
    art_logo.adj_indent = 10 + width ; art_logo.adj_right_space = 2
    art_logo.print_reversed_image_ascii_art()


    cp.ins_newline(4)

    art_logo.bg = 22; art_logo.fg = 231; art_logo.delay_ms = 20
    art_logo.adj_indent = 10+(2*art_logo.adj_left_space)+(len(cp.Alpha_E));  art_logo.adj_left_space = 2;  art_logo.adj_right_space = 2
    art_logo.set_layout = cp.Layout.HORIZONTAL
    art_logo.ascii_type = cp.Alpha_E # mym

    back_up = len(cp.Alpha_E)
    width = len(cp.Alpha_M[0])
    art_logo.print_reversed_image_ascii_art()


    crs.jumpTo(qty=back_up, direction=cp.Move.UP)
    art_logo.bg = 208; art_logo.fg = 16
    art_logo.ascii_type = cp.Alpha_M # mye               # one of the green and the other of the orange
    art_logo.adj_indent = art_logo.adj_indent - width - (2*art_logo.adj_left_space); art_logo.adj_right_space = 2
    art_logo.print_reversed_image_ascii_art()


    cp.ins_newline(2)
    art_logo.ascii_type = frog
    art_logo.print_reversed_image_ascii_art()