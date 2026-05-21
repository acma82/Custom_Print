import custom_print as cp
#-------------------------------------------------------------------------------------------------------------------------------
def art_logo_1(dato, option):
    msg = cp.Art()
    msg.set_bottom_line = True
    msg.set_top_line    = True
    # msg.set_layout = "horizontal"
    msg.delay_ms = 10
    msg.bold = True
    msg.bg = 87
    msg.fg = 16
    msg.ascii_type = option
    msg.adj_left_space = 4
    msg.adj_right_space = 6
    msg.adj_middle_space = 1
    msg.print_ascii_art(dato)


#-------------------------------------------------------------------------------------------------------------------------------
def art_logo_2(data, option, ctrl=0):
    # create the class and set the settings
    multi_msg = cp.Art()
    
    multi_msg.set_layout = cp.Layout.HORIZONTAL
    # multi_msg.set_layout = cp.Layout.VERTICAL

    multi_msg.set_bottom_line  = True;                 multi_msg.set_top_line   = True
    multi_msg.adj_middle_space = 2;                    multi_msg.adj_indent     = 4
    multi_msg.adj_right_space  = 6;                    multi_msg.adj_left_space = 4
    multi_msg.delay_ms = 10;                           multi_msg.ascii_type     = option



    # we have 3 data, we need 3 settings for every single data
    #data       = [["A"], ["B"], ["Y"]]
    bolds      = [True,  True,  True]
    bgs        = [90,     231,    21]
    fgs        = [231,     16,     11]
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
    #     multi_msg.adj_indent = 64
    #     bgs = [231]
    #     fgs = [16]
    #     ctrl += 1
    # else:
    #     multi_msg.adj_indent = 4

    cp.print_multi_ascii_art(multi_msg, data, bolds, bgs, fgs, italics, underlines, strikes, blinkings, dims, hiddens, inverses)

#-------------------------------------------------------------------------------------------------------------------------------



# We have to pass all the parameters since we don't know the number of data that we will be passing 
# This function is making a combination of the Art class.
if __name__ == "__main__":
    # art_logo_1("@B?AZO|","Alpha");         #print("\n Next Line Art \n")
    # art_logo_1("@B? AZO|","Alpha");         #print("\n Next Line Art \n")
    sp1 = cp.ins_chr(21," ")
    sp2 = cp.ins_chr(12," ")
    art_logo_2([["Yuo"], ["CAn"]], cp.Ascii_Letter.Alpha,0)
    cp.ins_newline(1)
    art_logo_2([[f"do{sp1}"],[f"it{sp2}"]], cp.Ascii_Letter.Alpha,1)
    # art_logo_2([["Fr"], ["ie"], ["nd"]], cp.Ascii_Letter.Alpha,2)






