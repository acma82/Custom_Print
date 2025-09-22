'''
FancyMessage Class
Method Available:
    print_fancy_note(body_msg:str="Paragraph Body")->None)
    print_fancy_message(self, body_msg:str="Paragraph Body")->None    
'''

import custom_print as cp

msg = cp.FancyMessage()
crs = cp.Cursor()

# Example 1

msg.note_msg = " To Find a Kiss of Yours "
poem = '''
1898 - 1936, translated by Sarah Arvio

To find a kiss of yours
what would I give
A kiss that strayed from your lips
dead to love

My lips taste
the dirt of shadows     

To gaze at your dark eyes
what would I give
Dawns of rainbow garnet  
fanning open before God— 

The stars blinded them
one morning in May

And to kiss your pure thighs
what would I give
Raw rose crystal  
sediment of the sun
'''
ncols, nrows = cp.dimensions()
cp.resize(35, 100)
cp.clear()
#msg.help_lines = True
msg.top_lines     = 2
msg.bottom_lines  = 2
msg.note_position = 12  # by default is on row 0
msg.note_align    = cp.Align.CENTER
msg.note_left_space = 6
msg.note_right_space = 6
msg.left_indent = 25
msg.right_indent = 20
# msg.help_lines = True
msg.print_fancy_note(body_msg=poem)

msg.left_indent = len(msg.note_msg) + msg.note_left_space + msg.note_right_space


msg.body_bold    = 11
msg.body_italic  = True
msg.body_fg      = 190
msg.top_lines    = 0
msg.bottom_lines = 1

crs.jumpTo(qty=1, direction=cp.Move.UP)

msg.print_fancy_message("Author: Federico García Lorca")

print("\n")

input("enter to exit:")

cp.resize(nrows,ncols)


# Note that the counter start in the bg color. Adding more bottom_lines
# and top_lines, the number of note_position increases as well.
