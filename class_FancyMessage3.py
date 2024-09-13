import fancyprint as fp
msg = fp.FancyMessage()
crs = fp.Cursor()

#---------------------------------------------------------------------------------------
# Another Way to Use FancyMessage Class with Some Manipulation                         -
#---------------------------------------------------------------------------------------
# def message_with_note(obj:fp.FancyMessage, note_msg:str="Warning", bg_note:int=231, fg_note:int=0,\
#                       align_note=fp.Align.CENTER, body_msg:str="Body", fg_body_msg:int=231, bg_body:int=23)->None:
#    # save original values
#    li_obj = obj.left_indent; fg_obj = obj.fg
#    bold_obj = obj.bold; bg_obj = obj.bg
#    # option for the body
#    obj.bg = bg_body; obj.fg = fg_body_msg

#    # settings for the body_msg
#    obj.left_indent = 1 + len(note_msg) + 1
#    n_lines, space_available, tncols = msg.get_msg_attribute(body_msg)


#    # n_lines, space_available, tncols are variables for reference to calculate the message
#    # comment these 2 lines, they are only for reference
#    # tncols, nrows = fp.dimensions()
#    print(f"n_lines: {n_lines} space_available: {space_available}  total_number_of_cols: {tncols}\n")
   
#    obj.print_fancy_msg(body_msg)
#    # settings for the note
#    if (align_note == fp.Align.LEFT):
#       print(f"{crs.move(qty=n_lines+obj.bottom_lines, direction=fp.Move.UP)}{fp.set_font(1,bg_note,fg_note)}{note_msg}")
#    elif (align_note == fp.Align.CENTER):
#       print(f"{crs.move(qty=n_lines+msg.bottom_lines, direction=fp.Move.UP)}{crs.move(qty=1,direction=fp.Move.RIGHT)}{fp.set_font(1,bg_note,fg_note)}{note_msg}")
#    elif (align_note == fp.Align.RIGHT):
#       print(f"{crs.move(qty=n_lines+msg.bottom_lines, direction=fp.Move.UP)}{crs.move(qty=2,direction=fp.Move.RIGHT)}{fp.set_font(1,bg_note,fg_note)}{note_msg}")
#    else:
#       print(f"{crs.move(qty=n_lines+obj.bottom_lines, direction=fp.Move.UP)}{fp.set_font(1,bg_note,fg_note)}{note_msg}")

#    crs.jump(qty=n_lines+obj.bottom_lines,direction=fp.Move.DOWN)
#    print(f"{fp.reset_font()}")

#    # putting back original values
#    obj.left_indent = li_obj; obj.fg = fg_obj; obj.bg = bg_obj; obj.bold = bold_obj; 

   
note = " Warning: "
#12345678901234567890123456789012345678901234567890123456789012345678901234567890
warning_body = f'''
"What is love?" is a question that has been asked in many novels, poems,      80
plays, and songs. The answer to the question may vary and could change        80
within a lifetime for each individual. Love is often considered complex, and  80
many philosophers and scientists have hypothesized about what it means.       80
                        
            Working with Python 3.12 and GNU/Linux/AlmaLinux 9.4

https://www.betterhelp.com/advice/love/how-to-last-through-the-5-stages-of-love'''

# msg.top_lines = 1
# msg.bottom_lines = 1
# msg.right_indent = 2
# message_with_note(obj=msg, note_msg=note, bg_note=90, fg_note=231, align_note=None, body_msg=warning_body, fg_body_msg=21, bg_body=231)
# fp.ins_newline(2)
#message_with_note(obj=msg, note_msg=note, body_msg=warning_body)
# msg.print_fancy_msg("Printing with the original values of the FancyMessage Class. Note that the Function \
#        message_with_note does not alter the values.")
# fp.ins_newline(2)


# msg.left_space_note = 2
# msg.right_space_note = 6


# msg.align_note = fp.Align.LEFT
# msg.align_note = fp.Align.RIGHT
# msg.align_note = fp.Align.CENTER
# msg.align_note = fp.Align.JUSTIFY
# msg.position_note = 4
# msg.italic_note = True
# msg.top_lines = 2
msg.bottom_lines = 2
# msg.help_lines = True

msg.print_fancy_note(" Note: ",warning_body )
# print(msg.left_indent)
