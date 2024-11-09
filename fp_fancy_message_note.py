'''
FancyMessage Class
Method Available:
    print_fancy_note(msg_body:str="Paragraph Body")->None)
    print_fancy_message(self, msg_body:str="Paragraph Body")->None    
'''

import fancyprint as fp

msg = fp.FancyMessage()
crs = fp.Cursor()

# Example 1

msg.msg_note = " To Find a Kiss of Yours "
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
ncols, nrows = fp.dimensions()
fp.resize(35, 100)
fp.clear()
#msg.help_lines = True
msg.top_lines     = 2
msg.bottom_lines  = 2
msg.position_note = 12  # by default is on row 0
msg.align_note    = fp.Align.CENTER
msg.left_space_note = 6
msg.right_space_note = 6
msg.left_indent = 25
msg.right_indent = 20
# msg.help_lines = True
msg.print_fancy_note(msg_body=poem)

msg.left_indent = len(msg.msg_note) + msg.left_space_note + msg.right_space_note


msg.bold_body    = 11
msg.italic_body  = True
msg.fg_body      = 190
msg.top_lines    = 0
msg.bottom_lines = 1

crs.jumpTo(qty=1, direction=fp.Move.UP)

msg.print_fancy_message("Author: Federico García Lorca")

print("\n")

input("enter to exit:")

fp.resize(nrows,ncols)


# Note that the counter start in the bg color. Adding more bottom_lines
# and top_lines, the number of position_note increases as well.
