import custom_print as cp
#-------------------------------------------------------------------------------------------------------------------------------
def art_logo_1(dato, option):
    msg = cp.Art()
    msg.set_bottom_line = True
    msg.set_top_line    = True
    msg.set_layout = "horizontal"
    msg.delay_ms = 10
    msg.bold = True
    msg.bg = 87
    msg.fg = 16
    msg.ascii_type = option
    msg.adj_left_space   = 1
    msg.adj_right_space  = 1
    msg.adj_middle_space = 1
    msg.print_ascii_art(dato)


#-------------------------------------------------------------------------------------------------------------------------------
def art_logo_2(data, option, ctrl=0):
    # create the class and set the settings
    multi_msg = cp.Art()
    
    multi_msg.set_layout = cp.Layout.HORIZONTAL
    # multi_msg.set_layout = cp.Layout.VERTICAL

    multi_msg.set_bottom_line  = True;                 multi_msg.set_top_line   = True
    multi_msg.adj_middle_space = 1;                    multi_msg.adj_indent     = 4
    multi_msg.adj_right_space  = 1;                    multi_msg.adj_left_space = 1
    multi_msg.delay_ms = 10;                           multi_msg.ascii_type     = option



    # we have 3 data, we need 3 settings for every single data
    #data       = [["A"], ["B"], ["Y"]]
    bolds      = [True,  True,  True]
    bgs        = [196,     231,    22]
    fgs        = [231,     21,     231]
    italics    = [False, False, False]
    underlines = [False, False, False]
    strikes    = [False, False, False]
    blinkings  = [False, False, False]
    dims       = [False, False, False]
    hiddens    = [False, False, False]
    inverses   = [False, False, False]
    
    # if ctrl == 0:
    #     multi_msg.adj_indent = 4
    #     ctrl += 1
    # elif ctrl == 1:
    #     multi_msg.adj_indent = 56
    #     bgs = [231]
    #     fgs = [16]
    #     ctrl += 1
    # else:
    #     multi_msg.adj_indent = 4

    multi_msg.print_multi_ascii_art(data, bolds, bgs, fgs, italics, underlines, strikes, blinkings, dims, hiddens, inverses)

#-------------------------------------------------------------------------------------------------------------------------------



# We have to pass all the parameters since we don't know the number of data that we will be passing 
# This function is making a combination of the Art class.
if __name__ == "__main__":
    # art_logo_1("@B?AZO|","Alpha");         #print("\n Next Line Art \n")
    # art_logo_1("@B?AZO|","Alpha");         #print("\n Next Line Art \n")
    # sp1 = cp.ins_chr(21," ")
    # sp2 = cp.ins_chr(12," ")
    # art_logo_2([["me"], ["xi"],["co"]], cp.Ascii_Letter.Alpha,0)
    # art_logo_2([["Da"], ["lt"],["On"]], cp.Ascii_Letter.Alpha,0)
    # art_logo_2([["My"]], cp.Ascii_Letter.Doh,1)
    # art_logo_2([["Fr"], ["ie"], ["nd"]], cp.Ascii_Letter.Alpha,2)





    frog = []
    frog.append("           .--._.--.           ")  # 35
    frog.append("          ( O     O )          ")
    frog.append("          /   . .   \\          ")
    frog.append("         .`._______.'.         ")
    frog.append("        /(           )\\        ")
    frog.append("      _/  \\  \\   /  /  \\_       ")
    frog.append("   .~   `  \\  \\ /  /  '   ~.   ")
    frog.append("  {    -.   \\  V  /   .-    }  ")
    frog.append("_ _`.    \\  |  |  |  \\/    .'_ ")
    frog.append(">_       _} |  |  | {_       _<")
    frog.append(" /. - ~ ,_-'  .^.  `-_, ~ - .\\ ")
    frog.append("         '-'|/   \\|`-`         ")
    frog.append("                               ")


                      
    mye = []                 # 10     
    mye.append("      __.....__     ")
    mye.append("  .-''         '.   ")
    mye.append(" /     .-''\"'-.  `. ")
    mye.append("/     /________\\   \\")
    mye.append("|                  |")
    mye.append("\\    .-------------'")
    mye.append(" \\    '-.____...---.")
    mye.append("  `.             .' ")
    mye.append("    `''-...... -'   ")
    mye.append("                    ")
                      
                 
    mym = []             # rows = 10,  cols = 17
    mym.append("                ")
    mym.append(" __  __   ___   ")
    mym.append("|  |/  `.'   `. ")
    mym.append("|   .-.  .-.   '")
    mym.append("|  |  |  |  |  |")
    mym.append("|  |  |  |  |  |")
    mym.append("|  |  |  |  |  |")
    mym.append("|  |  |  |  |  |")
    mym.append("|__|  |__|  |__|")
    mym.append("                ")
                 
                 
    art_logo = cp.Art()
    crs = cp.Cursor()
    art_logo.bg = 90; art_logo.fg = 231; art_logo.delay_ms = 80
    art_logo.adj_indent = 10;  art_logo.adj_left_space = 2
    art_logo.set_layout = cp.Layout.HORIZONTAL
    art_logo.ascii_type = cp.Alpha_M # mym
    
    back_up = len(cp.Alpha_M)
    width = len(cp.Alpha_M[0])

    art_logo.print_image_ascii_art()


    crs.jumpTo(qty=back_up, direction=cp.Move.UP)
    art_logo.ascii_type = cp.Alpha_E # mye
    art_logo.adj_indent = 10 + 2 + width ; art_logo.adj_right_space = 2
    art_logo.print_image_ascii_art()


    art_logo.bg = 22
    art_logo.ascii_type = "Unix_Logo"
    art_logo.print_image_ascii_art()

    art_logo.bg = 196
    art_logo.ascii_type = frog; art_logo.adj_right_space = 28
    art_logo.print_image_ascii_art()




