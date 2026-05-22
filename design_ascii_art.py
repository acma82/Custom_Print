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
    bgs        = [196,     231,    17]
    fgs        = [231,     21,     1]
    italics    = [False, False, False]
    underlines = [False, False, False]
    strikes    = [False, False, False]
    blinkings  = [False, False, False]
    dims       = [False, False, False]
    hiddens    = [False, False, False]
    inverses   = [False, False, False]
    
    if ctrl == 0:
        multi_msg.adj_indent = 4
        ctrl += 1
    elif ctrl == 1:
        multi_msg.adj_indent = 56
        bgs = [231]
        fgs = [16]
        ctrl += 1
    else:
        multi_msg.adj_indent = 4

    multi_msg.print_multi_ascii_art(data, bolds, bgs, fgs, italics, underlines, strikes, blinkings, dims, hiddens, inverses)

#-------------------------------------------------------------------------------------------------------------------------------



# We have to pass all the parameters since we don't know the number of data that we will be passing 
# This function is making a combination of the Art class.
if __name__ == "__main__":
    art_logo_1("@B?AZO|","Alpha");         #print("\n Next Line Art \n")
    art_logo_1("@B?AZO|","Alpha");         #print("\n Next Line Art \n")
    # sp1 = cp.ins_chr(21," ")
    # sp2 = cp.ins_chr(12," ")
    # art_logo_2([["Da"], ["lt"],["On"]], cp.Ascii_Letter.Alpha,0)
    # art_logo_2([["My"]], cp.Ascii_Letter.Doh,1)
    # art_logo_2([["Fr"], ["ie"], ["nd"]], cp.Ascii_Letter.Alpha,2)

    # art_logo = cp.Art()
    # art_logo.ascii_type = "logo_monkey"
    # art_logo.print_logo_ascii_art("Debil")





