import custom_print as cp

def art_logo_2(data, option, ctrl=0):
    # create the class and set the settings
    multi_msg = cp.Art()
    
    # multi_msg.set_layout = cp.Layout.HORIZONTAL
    multi_msg.set_layout = cp.Layout.VERTICAL

    multi_msg.set_bottom_line  = True;                 multi_msg.set_top_line   = True
    multi_msg.adj_middle_space = 0;                    multi_msg.adj_indent     = 4
    multi_msg.delay_ms = 10;                           multi_msg.ascii_type     = option



    # we have 3 data, we need 3 settings for every single data
    # Note: If we add more data into the list, we will need more settings. In this case we have 3 items in the list data.
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
    
    if ctrl == 0:
        multi_msg.adj_right_space  = 6
        multi_msg.adj_left_space   = 2
        # bgs = [196,     231,    22]
    elif ctrl == 1:
        multi_msg.adj_left_space   = 2
        multi_msg.adj_right_space  = 5
        # multi_msg.adj_middle_space = 0
        # bgs = [-1,     231,    -1]
    else:
            multi_msg.adj_right_space  = 2
            multi_msg.adj_left_space   = 2
            # bgs = [196,     231,    22]

    multi_msg.print_multi_ascii_art(data, bolds, bgs, fgs, italics, underlines, strikes, blinkings, dims, hiddens, inverses)





cp.ins_newline(n=2)
print("    Type of Letters.")
print("    Python: Doom, IS: Mono, PRETTY: Epic")
cp.ins_newline(n=2)

art_logo_2([["PY"], ["TH"], ["ON"]], cp.Ascii_Letter.Doom,0)
art_logo_2([[cp.ins_chr(n=15, unicode=" ")],[" Is"],[cp.ins_chr(n=15, unicode=" ")]], cp.Ascii_Letter.Mono, 1)
art_logo_2([["PR"], ["ET"], ["TY"]], cp.Ascii_Letter.Epic,2)


