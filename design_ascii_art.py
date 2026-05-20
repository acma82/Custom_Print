import custom_print as cp
#-------------------------------------------------------------------------------------------------------------------------------
def art_logo_1(dato, option):
    msg = cp.Art()
    msg.set_bottom_line = True
    msg.set_top_line    = True
    # msg.set_layout = "horizontal"
    msg.adj_indent = 2
    msg.delay_ms = 100
    msg.bold = True
    msg.bg = 87
    msg.fg = 16
    msg.ascii_type = option
    msg.adj_left_space = 4
    msg.adj_right_space = 6
    msg.adj_middle_space = 2
    msg.print_ascii_art(dato)


#-------------------------------------------------------------------------------------------------------------------------------
def art_logo_2(data, option):
    # create the class and set the settings
    multi_msg = cp.Art()
    
    # multi_msg.set_layout = cp.Layout.HORIZONTAL
    # multi_msg.set_layout = cp.Layout.VERTICAL

    multi_msg.set_bottom_line  = True;                 multi_msg.set_top_line   = True
    multi_msg.adj_middle_space = 2;                    multi_msg.adj_indent     = 4
    multi_msg.adj_right_space  = 6;                    multi_msg.adj_left_space = 4
    multi_msg.delay_ms = 80;                           multi_msg.ascii_type     = option

    # we have 3 data, we need 3 settings for every single data
    #data       = [["A"], ["B"], ["Y"]]
    bolds      = [True,  True,  True]
    bgs        = [1,     90,    21]
    fgs        = [7,     231,   11]
    italics    = [False, False, False]
    underlines = [False, False, False]
    strikes    = [False, False, False]
    blinkings  = [False, False, False]
    dims       = [False, False, False]
    hiddens    = [False, False, False]
    inverses   = [False, False, False]
    cp.print_multi_ascii_art(multi_msg, data, bolds, bgs, fgs, italics, underlines, strikes, blinkings, dims, hiddens, inverses)
#-------------------------------------------------------------------------------------------------------------------------------



# We have to pass all the parameters since we don't know the number of data that we will be passing 
# This function is making a combination of the Art class.
if __name__ == "__main__":
    art_logo_1("@B? O","Alpha");         print("\n Next Line Art \n")
    
    art_logo_2([["@A"], ["+"], ["?="]], cp.Ascii_Letter.Alpha)
    






