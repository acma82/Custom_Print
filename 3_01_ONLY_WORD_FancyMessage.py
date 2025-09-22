'''
FancyMessage Class
Method Available:
    print_fancy_note(body_msg:str="Paragraph Body")->None)
    print_fancy_message(self, body_msg:str="Paragraph Body")->None    
'''

import custom_print as cp

msg = cp.FancyMessage()
crs = cp.Cursor()

paragraph1 = "First paragraph,  Last  paragraph "

paragraph2 = " First paragraph, Last paragraph   Come, \" The highway if full of big cars going nowhere \
fast and folks are smoking anything that  will burn. \""

paragraph3 = '''

 I should probably collect a list of the best
 romantic poems ever written, and maybe I will.
 This is not that. I mostly talk about writing
 books, but I noticed most of the other big
 writing sites actually get most of the their

 traffic from this keyword, because everybody
 is interested in romantic poetry! When you
 want to tell her how you feel, but do not
 have the words to express all that emotion...! 

 '''

paragraph4 = '''\
    +---------------------------------------------------+    
    |    I should probably collect a list of the best   |    
    |    romantic poems ever written, and maybe I will. |    
    |    This is not that. I mostly talk about writing  |    
    |    books, but I noticed most of the other big     |    
    |    writing sites actually get most of the their   |    
    +---------------------------------------------------+    
    |   traffic from this keyword, because everybody    |    
    |   is interested in romantic poetry! When you      |    
    |   want to tell her how you feel, but do not       |    
    |   have the words to express all that emotion...!  |    
    +---------------------------------------------------+    
'''
#---------------------------------------------------------------------------------------
# This is for paragraph1 variable                                                           -
#---------------------------------------------------------------------------------------
# it's for the string
msg.left_indent = 15
msg.right_indent = 15

msg.top_lines = 1        # how many lines above and below the string

msg.lines_title_body = 1
msg.title_bg = 14
msg.title_fg = 0
msg.title_bold  = True
msg.title_align = cp.Align.CENTER



# body
# msg.body_underline = True
msg.body_italic = True
msg.body_bg = 14
msg.body_fg = 0
# msg.body_bold = True
# msg.body_dim = True  # this is ignored when bold is on
# msg.body_inverse  = True
# msg.body_blinking = True

# footnote
msg.footnote_lines_body = 1
# msg.footnote_msg = "FootNote"
msg.footnote_bg = 14
msg.footnote_fg = 0
msg.footnote_bold = True
msg.bottom_lines = 1
msg.footnote_align = cp.Align.JUSTIFY


# msg.help_lines = True
msg.length = cp.Length_bg.ONLY_WORD
msg.adj_bg_lines_to_right_indent =  False   # True make all the way to the space available
msg.adj_bg_msg_to_space_available = False   # True make all the way to the space available
# These two options are only available when using the msg.length = cp.Length_bg.ONLY_WORD
# otherwise they will make it to the longest line



msg.print_fancy_message(paragraph1)

cp.ins_newline(2)
msg.print_fancy_message(paragraph2)


cp.ins_newline(2)
msg.print_fancy_message(paragraph3)


cp.ins_newline(2)
msg.print_fancy_message(paragraph4)
