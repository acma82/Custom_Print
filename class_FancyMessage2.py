import fancyprint as fp
msg = fp.FancyMessage()
crs = fp.Cursor()

#---------------------------------------------------------------------------------------
# Another Way to Use FancyMessage Class with Some Manipulation                         -
#---------------------------------------------------------------------------------------
def message_with_title(obj:fp.FancyMessage, title_msg:str="Title", align_title:str=fp.Align.CENTER, fg_title:int=0,\
                       underline_title:bool=False, body_msg:str="Body", fg_body_msg:int=21, bg:int=231)->None:
   
   # save original data
   li_obj = obj.left_indent; fg_obj = obj.fg; tl = obj.top_lines; bl = obj.bottom_lines
   bold_obj = obj.bold; italic_obj = obj.italic; underline_obj = obj.underline; bg_obj = obj.bg
   # option for the title
   obj.bold = True; obj.italic = True
   if (underline_title == True): obj.underline = True
   else:                         obj.underline = False
   
   # setting for title
   obj.top_lines = 1; obj.bottom_lines = 0; obj.bg = bg; obj.fg = fg_title

   n_lines, space_available = msg.get_msg_attribute(body_msg)
   obj.bold = True; obj.bottom_lines = 1
   
   # n_lines, space_available, tncols are variables for reference to calculate the message
   # comment these 2 lines, they are only for reference
   tncols, nrows = fp.dimensions()
   print(f"n_lines: {n_lines} space_available: {space_available}  total_number_of_cols: {tncols}\n")

   if   (align_title == fp.Align.LEFT):   pass
   elif (align_title == fp.Align.CENTER): obj.left_indent = int((space_available - len(title_msg))/2)
   elif (align_title == fp.Align.RIGHT):  obj.left_indent = space_available - len(title_msg)
   else:                                  pass
   obj.print_fancy_msg(title_msg)

   # setting for body_msg
   obj.top_lines = 1; obj.bottom_lines = 1
   obj.bold = False; obj.left_indent = li_obj
   obj.bold = False; obj.italic = False; obj.underline = False
   obj.fg = fg_body_msg; obj.top_lines = 0
   
   obj.print_fancy_msg(body_msg)
   # putting back original values
   obj.fg = fg_obj; obj.top_lines = tl; obj.bottom_lines = bl; obj.bg = bg_obj
   obj.bold = bold_obj; obj.italic = italic_obj; obj.underline = underline_obj

   

   

#---------------------------------------------------------------------------------------
# Start the Script                                                                     -
#---------------------------------------------------------------------------------------
fp.ins_newline(2)
msg.left_indent = 4; msg.right_indent = 4
#                                                                                       # 87 space_available
title = "Love Poem"
warning_body = f'''
"What is love?" is a question that has been asked in many novels, poems, plays, and  87
songs. The answer to the question may vary and could change within a lifetime for    87
each individual. Love is often considered complex, and many philosophers and         87
scientists have hypothesized about what it means.

https://www.betterhelp.com/advice/love/how-to-last-through-the-5-stages-of-love'''
message_with_title(obj=msg, title_msg=title, align_title=fp.Align.RIGHT, fg_title=0,\
                   underline_title=True, body_msg=warning_body, fg_body_msg=21, bg=231)
fp.ins_newline(2)
message_with_title(obj=msg)
fp.ins_newline(2)
msg.print_fancy_msg("Printing with the original values of the FancyMessage Class. Note that the Function message_with_title does not alter the values")
fp.ins_newline(2)
