import custom_print as cp

art_logo = cp.AsciiArt()




# Printing the Logo_Unix
art_logo.bg = 16
art_logo.fg = 231
art_logo.delay_ms = 10
art_logo.bold = True
art_logo.set_layout ="v" #cp.Layout.HORIZONTAL
# art_logo.set_layout = cp.Layout.VERTICAL
art_logo.adj_indent = 4
art_logo.adj_right_space = 2
art_logo.adj_left_space = 2
art_logo.adj_middle_space = 6


ascii_logos = [cp.Logo_Unix, cp.Logo_Debian, cp.Logo_Centos, cp.Logo_RedHat, cp.Logo_Linux]
bg_colors   = [16, 231, 21, 16, 4] 
ctrl = 0
for logo in ascii_logos:
    art_logo.ascii_type = logo
    art_logo.bg = bg_colors[ctrl]
    art_logo.print_ascii_art_logo(cp.Direction.UP_DOWN)
    ctrl += 1



Pyramid = []
Pyramid.append("                .                       ") # Top()
Pyramid.append("               /=\\\\                     ")
Pyramid.append("              /===\\ \\                   ")
Pyramid.append("             /=====\\' \\                 ")
Pyramid.append("            /=======\\'' \\               ")
Pyramid.append("           /=========\\ ' '\\             ")
Pyramid.append("          /===========\\''   \\           ")
Pyramid.append("         /=============\\ ' '  \\         ")
Pyramid.append("        /===============\\   ''  \\       ")
Pyramid.append("       /=================\\' ' ' ' \\     ")
Pyramid.append("      /===================\\' ' '  ' \\   ")
Pyramid.append("     /=====================\\' '   ' ' \\ ")
Pyramid.append("    /=======================\\  '   ' /  ")
Pyramid.append("   /=========================\\   ' /    ")
Pyramid.append("  /===========================\\'  /     ")
Pyramid.append(" /=============================\\/       ")
Pyramid.append("                                        ") # Bottom()



Frog = []
Frog.append("           .--._.--.           ")
Frog.append("          ( O     O )          ")
Frog.append("          /   . .   \\          ")
Frog.append("         .`._______.'.         ")
Frog.append("        /(           )\\        ")
Frog.append("      _/  \\  \\   /  /  \\_      ")
Frog.append("   .~   `  \\  \\ /  /  '   ~.   ")
Frog.append("  {    -.   \\  V  /   .-    }  ")
Frog.append("_ _`.    \\  |  |  |  \\/    .'_ ")
Frog.append(">_       _} |  |  | {_       _<")
Frog.append(" /. - ~ ,_-'  .^.  `-_, ~ - .\\ ")
Frog.append("         '-'|/   \\|`-`         ")
Frog.append("                               ")


logo = cp.AsciiArt()
logo.bg = 53
logo.fg = 231
logo.delay_ms = 60
logo.ascii_type = Pyramid
logo.adj_indent = 0
logo.adj_left_space = 4
logo.adj_right_space = 4
logo.print_ascii_art_logo(direction=cp.Direction.UP_DOWN)
# logo.print_ascii_art_logo(direction=cp.Direction.LEFT_RIGHT)
# logo.print_ascii_art_logo(direction=cp.Direction.RIGHT_LEFT)
# logo.print_ascii_art_logo(direction=cp.Direction.DOWN_UP)
