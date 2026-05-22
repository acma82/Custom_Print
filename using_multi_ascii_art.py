import custom_print as cp

# create the class and set the settings
msg = cp.Art()
msg.set_layout = cp.Layout.HORIZONTAL
# msg.set_layout = cp.Layout.VERTICAL
msg.set_bottom_line = True
msg.set_top_line    = True
msg.adj_indent = 2
msg.adj_left_space = 4
msg.adj_right_space = 6
msg.adj_middle_space = 2
msg.delay_ms = 100
msg.ascii_type = "Alpha"#"Doh"

# we have 3 data, we need 3 settings for every single data
data = [     ["A"], ["B"],["Y"]]
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

# We have to pass all the parameters since we don't know the number of data that we will be passing 
# This function is making a combination of the Art class.
msg.print_multi_ascii_art(data, bolds, bgs, fgs, italics, underlines, strikes, blinkings, dims, hiddens, inverses)

print("Hello")







