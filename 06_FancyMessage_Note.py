import fancyprint as fp
msg = fp.FancyMessage()


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
ncols, nrows = fp.dimensions()
fp.resize(35, 100)
fp.clear()
#msg.help_lines = True
msg.top_lines = 2
msg.bottom_lines = 2
msg.position_note = 12  # by default is on row 0
msg.align_note = fp.Align.CENTER
msg.left_space_note = 6; msg.right_space_note = 6
msg.left_indent = 25; msg.right_indent = 20
# msg.help_lines = True
msg.print_fancy_note(body_msg=poem)

msg.left_indent = len(msg.note_msg) + msg.left_space_note + msg.right_space_note

msg.bold_body = 11; msg.italic_body = True; msg.fg_body = 190
msg.top_lines = 0; msg.bottom_lines = 1

msg.print_fancy_message("Author: Federico García Lorca")

print("\n")

input("enter to exit:")

fp.resize(nrows,ncols)


# Note that the counter start in the bg color. Adding more bottom_lines
# and top_lines, the number of position_note increases as well.




















# Example 2
# Comment Example 1 and uncoment Solution 1 and run the script
# This example deal in case our terminal is not big enough to fit 
# all the message in the actual size. 
# Note: Ansi Code for position change as the terminal size change.
#       position_note will not work if the screen is not big enough,
#       but it will work if we use any of the solution presente (1 or 2)

# Solution 1: 
# make bigger the termial
# position_note = 5
# make terminal: resize -s 12 100
# Notice that the note is note is not on position 5
# make terminal: resize -s 30 100
# now it works the note is on positon 5


# Solution 2: 
# Comment the solution 1 and uncoment solution 2
# Break the Message in two part as show below
# make terminal: resize -s 12 100
# break the poem in 2 parts. you need to update the 
# left_space_note with the size of the title (note) and 
# add the left_indent for the second part to work.
# As we print in the terminal the enumeration for 
# rows and cols change that is why it does not work.
# solution 1 is better approach

Author = " Jean Toomer 1894 - 1967 "
title = " Her Lips Are Copper Wire "
poem = f'''
whisper of yellow globes
gleaming on lamp-posts that sway
like bootleg licker drinkers in the fog

and let your breath be moist against me
like bright beads on yellow globes

telephone the power-house
that the main wires are insulate

(her words play softly up and down
dewy corridors of billboards)

then with your tongue remove the tape
and press your lips to mine
till they are incandescent
'''


poemP1 = '''
whisper of yellow globes
gleaming on lamp-posts that sway
like bootleg licker drinkers in the fog

and let your breath be moist against me
like bright beads on yellow globes
'''
poemP2 ='''
telephone the power-house
that the main wires are insulate

(her words play softly up and down
dewy corridors of billboards)

then with your tongue remove the tape
and press your lips to mine
till they are incandescent
'''


# # Solution 1
# msg.italic = True
# back = msg.left_space_note
# msg.left_space_note = len(title) + back
# msg.bottom_lines = 0
# msg.left_space_note = back
# msg.bottom_lines = 1
# msg.position_note = 5
# msg.print_fancy_note(title, poem)
# msg.top_lines = 1; msg.bold = True
# msg.fg = 222
# msg.left_indent = len (title) + msg.left_space_note + 1# + msg.right_space_note
# msg.print_fancy_msg(Author)


# # Solution 2
# msg.italic = True
# back = msg.left_space_note
# msg.left_space_note = len(title) + back
# msg.bottom_lines = 0
# msg.left_space_note = back
# msg.bottom_lines = 1
# msg.position_note = 5
# msg.print_fancy_note(title, poemP1)
# msg.left_space_note = msg.left_indent + len(title)
# msg.print_fancy_note("",poemP2)
# msg.top_lines = 1; msg.bold = True
# msg.fg = 222
# msg.left_indent = len (title) + msg.left_space_note + 1# + msg.right_space_note
# msg.print_fancy_msg(Author)

