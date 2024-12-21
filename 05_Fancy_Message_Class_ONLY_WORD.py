'''
FancyMessage Class
Method Available:
    print_fancy_note(msg_body:str="Paragraph Body")->None)
    print_fancy_message(self, msg_body:str="Paragraph Body")->None    
'''

import source.custom_print as cp

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
msg.bg_title = 14
msg.fg_title = 0
msg.bold_title  = True
msg.align_title = cp.Align.CENTER



# body
# msg.underline_body = True
msg.italic_body = True
msg.bg_body = 14
msg.fg_body = 0
# msg.bold_body = True
# msg.dim_body = True  # this is ignored when bold is on
# msg.inverse_body  = True
# msg.blinking_body = True

# footnote
msg.lines_body_footnote = 1
# msg.msg_footnote = "FootNote"
msg.bg_footnote = 14
msg.fg_footnote = 0
msg.bold_footnote = True
msg.bottom_lines = 1
msg.align_footnote = cp.Align.JUSTIFY


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
