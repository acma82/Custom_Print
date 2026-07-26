import custom_print as cp

# Printing you own Logo
sword = []
sword.append("                      __                        ")
sword.append("                     /  \\                       ")
sword.append("                    |    |                      ")
sword.append('(`----._____.-`"""`. \\__/ .`"""`-._____.----`)  ')
sword.append(" (____       .      `|  |'      .       ____)   ")
sword.append("   (___`----' .     _|  |_     . `----'___)     ")
sword.append("     (__`----'  _.-' |  | `-._  `----'__)       ")
sword.append("       `._____.'_    |  |    _`._____.'         ")
sword.append("              /o )-< |  | >-( o\\                ")
sword.append("             / .'    |  |    `. \\               ")
sword.append("            J J      |  |      L L              ")
sword.append("            | |      |  |      | |              ")
sword.append("            J J      |  |      F F              ")
sword.append("             \\ \\     |  |     / /               ")
sword.append("              \\ `.   |  |   .' /                ")
sword.append("               `. `-.|  |.-' .'                 ")
sword.append("                 `-. |.-' .-'                   ")
sword.append("                   .-' .-'.                     ")
sword.append("                 .' .-' |. `.                   ")
sword.append("                / .' |  | `. \\                  ")
sword.append("               / /   |  |   \\ \\                 ")
sword.append("              J J    |  |    L L                ")
sword.append("              | |    |  |    | |                ")
sword.append("              J J    |  |    F F                ")
sword.append("               \\ `.  |  |  .' /                 ")
sword.append("                `. `-|  !-' .'                  ")
sword.append("                  `-.!-' .-'                    ")
sword.append("                   .' .-|`.                     ")
sword.append("                  / .|  |. \\                    ")
sword.append("                 J J |  | L L                   ")
sword.append("                 | | |  | | |                   ")
sword.append("                 J J |  | F F                   ")
sword.append("                  `.\\|  |/.'                    ")
sword.append("                    `|  |'                      ")
sword.append("                     |  |                       ")
sword.append("                     |  |                       ")
sword.append("                     |  |                       ")
sword.append("                     `--'                       ")



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



if __name__ == "__main__":                     
    my_own_e = [] # rows = 10, cols = 20    
    my_own_e.append("      __.....__     ")
    my_own_e.append("  .-''         '.   ")
    my_own_e.append(" /     .-''\"'-.  `. ")
    my_own_e.append("/     /________\\   \\")
    my_own_e.append("|                  |")
    my_own_e.append("\\    .-------------'")
    my_own_e.append(" \\    '-.____...---.")
    my_own_e.append("  `.             .' ")
    my_own_e.append("    `''-...... -'   ")
    my_own_e.append("                    ")
                      
                 
    my_own_m = [] # rows = 10,  cols = 16
    my_own_m.append("                ")
    my_own_m.append(" __  __   ___   ")
    my_own_m.append("|  |/  `.'   `. ")
    my_own_m.append("|   .-.  .-.   '")
    my_own_m.append("|  |  |  |  |  |")
    my_own_m.append("|  |  |  |  |  |")
    my_own_m.append("|  |  |  |  |  |")
    my_own_m.append("|  |  |  |  |  |")
    my_own_m.append("|__|  |__|  |__|")
    my_own_m.append("                ")
                 
                 
    art_logo = cp.Art()
    crs = cp.Cursor()


    # Using Some Letters inside the module
    # Printing M
    heigh = len(cp.Alpha_M)
    width = len(cp.Alpha_M[0])
    art_logo.ascii_type = cp.Alpha_Letters.Alpha_A
    art_logo.print_ascii_logo_art()
    # Printin E
    crs.jumpTo(qty=heigh, direction=cp.Move.UP)
    art_logo.ascii_type = cp.Alpha_E
    art_logo.adj_indent = 10 + 2 + width ; art_logo.adj_right_space = 2
    art_logo.print_ascii_logo_art()

    cp.ins_newline(2)

    # Creating your own Letters
    art_logo.adj_indent = 2
    heigh = len(my_own_m)
    width = len(my_own_m[0])
    art_logo.ascii_type = my_own_m
    art_logo.print_ascii_logo_art()
    # Printin E
    crs.jumpTo(qty=heigh, direction=cp.Move.UP)
    art_logo.ascii_type = my_own_e
    art_logo.adj_indent = 4 + width ; art_logo.adj_right_space = 2
    art_logo.print_ascii_logo_art()

    cp.ins_newline(2)

    # Printing your own logos
    # Printing the Sword
    art_logo.bg = 231
    art_logo.fg = 21
    art_logo.bold = True
    art_logo.adj_indent = 4
    art_logo.ascii_type = sword
    art_logo.blinking = True
    art_logo.print_ascii_logo_art()

    cp.ins_newline(2)

    # Printing The Frog
    art_logo.blinking = False
    art_logo.bg = 23
    art_logo.fg = 231
    art_logo.bold = True
    art_logo.adj_indent = 16
    art_logo.ascii_type = Frog
    art_logo.print_ascii_logo_art()


    cp.ins_newline(2)

    # PurpleUgd
    word = []
    word.append("[0;91;1;40m                                                                           ")
    word.append("[0;91;1;40m ▄▄▄▄▄▄▄[0;37;40m          [0;91;1;40m▄▄▄▄▄▄▄▄[0;37;40m [0;91;1;40m▄▄▄▄▄▄▄▄[0;37;40m   [0;91;1;40m▄▄▄▄▄[0;37;40m [0;91;1;40m▄▄▄▄▄▄[0;37;40m    [0;91;1;40m▄▄▄▄▄[0;37;40m [0;91;1;40m▄▄▄▄▄▄▄▄[0;37;40m [0;91;1;40m▄▄▄▄▄▄▄ [0m")
    word.append("[0;37;40m  [0;31;40m▀██[0;91;1;41m▄[0;91;1;40m▀[0;37;40m            [0;31;40m▀██[0;91;1;41m▄▄[0;91;1;40m▀[0;37;40m   [0;31;40m▀██[0;91;1;41m▄[0;31;40m▀██[0;91;1;40m█[0;37;40m  [0;31;40m██[0;91;1;41m▄[0;91;1;40m▀[0;37;40m   [0;31;40m▀██[0;91;1;40m█[0;37;40m      [0;31;40m██[0;91;1;41m▄[0;91;1;40m▀[0;37;40m  [0;31;40m▀███[0;91;1;41m▄[0;91;1;40m▀[0;37;40m   [0;31;40m▀██[0;91;1;41m▄[0;91;1;40m▀ [0;37;40m [0m")
    word.append("[0;37;40m   [0;31;40m██[0;91;1;41m█[0;37;40m              [0;31;40m██[0;91;1;41m█[0;37;40m      [0;31;40m██[0;91;1;41m█[0;37;40m  [0;31;40m█[0;91;1;40m█[0;37;40m  [0;31;40m██[0;91;1;40m█[0;37;40m     [0;31;40m██[0;91;1;40m█[0;37;40m      [0;31;40m██[0;91;1;40m█[0;37;40m    [0;31;40m██[0;91;1;41m█[0;37;40m     [0;31;40m▄█[0;91;1;41m▄[0;91;1;40m▀[0;37;40m   [0m")
    word.append("[0;37;40m   [0;31;40m██[0;91;1;40m█[0;37;40m              [0;31;40m██[0;91;1;41m▀[0;37;40m      [0;31;40m██[0;91;1;41m█[0;37;40m  [0;31;40m█[0;91;1;40m█[0;37;40m  [0;31;40m██[0;91;1;40m█[0;37;40m     [0;31;40m██[0;91;1;40m█[0;37;40m      [0;31;40m██[0;91;1;40m█[0;37;40m     [0;31;40m▀█[0;91;1;41m▀[0;91;1;40m▄[0;31;40m▄▄██[0;91;1;40m█[0;37;40m     [0m")
    word.append("[0;37;40m   [0;31;40m██[0;91;1;41m█[0;37;40m         [0;91;1;40m▄█[0;37;40m   [0;31;40m██[0;91;1;41m▄[0;37;40m      [0;31;40m██[0;91;1;41m█[0;37;40m  [0;31;40m█[0;91;1;41m▀[0;91;1;40m▄[0;37;40m [0;31;40m██[0;91;1;40m█[0;37;40m     [0;31;40m███[0;91;1;41m▀[0;31;40m▄▄▄▄███[0;91;1;40m█[0;37;40m    [0;31;40m▄███[0;91;1;41m▄[0;31;40m▀▀███[0;91;1;41m▀[0;91;1;40m▄ [0;37;40m  [0m")
    word.append("[0;31;40m ▄████[0;91;1;41m▀ [0;31;40m████████[0;91;1;40m█[0;37;40m [0;31;40m▄████[0;91;1;41m▀[0;91;1;40m▄[0;37;40m  [0;31;40m▄███[0;91;1;41m█[0;37;40m  [0;31;40m▀██████[0;91;1;41m▀[0;91;1;40m▄[0;37;40m    [0;31;40m▀▀██████▀▀[0;37;40m   [0;31;40m▄████[0;91;1;41m▀[0;91;1;40m▄[0;37;40m  [0;31;40m▄████[0;91;1;41m▀[0;91;1;40m▄ [0m")
    word.append("[0;91;1;40m                                                                           ")
    art_logo.ascii_type = word
    art_logo.print_ascii_logo_art()


    # Reference-> https://www.asciiart.eu/gallery