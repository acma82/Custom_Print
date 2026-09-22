import custom_print as cp

# create the class and set the settings
msg = cp.AsciiArt()
msg.set_layout = cp.Layout.HORIZONTAL
# msg.set_layout = cp.Layout.VERTICAL
msg.set_bottom_line = True
msg.set_top_line    = True
msg.adj_indent = 2
msg.adj_left_space = 3
msg.adj_middle_space = 0
msg.adj_right_space = 1
msg.delay_ms = 100
msg.ascii_type = cp.Ascii_Letter.BIG

# we have 3 data, we need 3 settings for every single data
# Note: If we add more data into the list, we will need more settings. In this case we have 3 items in the list data.
data = [     ["Py"], ["Th"],["On"]]
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



# This method print the Ascii letters in a loop reusing the print_ascii_art as many times as needed. 
# This is very important to understand that the spacing parameters will be affecting the group of data.
# In our example using the word Py Th On, Py group is being afectted by the 3 spacing variables
#  (adj_left_space, adj_middle_space, and adj_right_space) and the other 2 groups will be the same
# scenario.
# To visualize a better understanding the idea behind this methos let's check an example.



# Note it is recomended to the user to play with these 3 variables on this example for better understanding.

# Also if you decide to add another group of letters, remember to add the other parameters such as bgs, fgs,
# bolds, and so on.

