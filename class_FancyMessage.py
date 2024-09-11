import os
import fancyprint as fp
msg = fp.FancyMessage()
crs = fp.Cursor()
name1 = " First Name, Last Name "

name2 = " First Name, Last Name   Come, \" The highway if full of big cars going nowhere \
fast and folks are smoking anything that  will burn. \""

name3 = '''
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

name4 = '''\
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

# Default Varibles
# bold = False           Values = True/False          
# fg = 4                 Values = from 0 to 255
# bg = 251               Values = from 0 to 255

# left_indent = 0        Values = depends on the width of the terminal
# right_indent = 0       Values = depends on the width of the terminal

# self.length = Length_bg.ALL_ROW   (All_ROW, ONLY_WORD)

#---------------------------------------------------------------------------------------
# self.adj_bg_lines_to_right_indent =  False    (False, True)
# self.adj_bg_msg_to_space_available = False    (False, True, None)
#---------------------------------------------------------------------------------------
# This is for name1 variable                                                           -
#---------------------------------------------------------------------------------------
msg.bold = True; msg.bg = 95; msg.fg = 0
msg.left_indent = 18; msg.right_indent = 8    # it's for the string 
msg.top_lines = 3                            # how many lines above and below the string
msg.bottom_lines = 2
msg.underline = True
msg.italic = True

msg.print_fancy_msg(name1)
print("\n"); 
msg.length = fp.Length_bg.ONLY_WORD          # type of bg
msg.adj_bg_lines_to_right_indent =  True     # True adjs to space available
                                             # when True, right_indent is considerd
                                             # False adjs bg to the string width

msg.adj_bg_msg_to_space_available = True     # True adjs string to space available
                                             # when True right_indent is considerd
                                             # False adjs bg to longest string width
                                             # None adjs bg to string length
# Note: .adj_bg_lines_to_right_indent and adj_bg_msg_to_space_available are more
# options when the string is presented in a form of paragraph type
msg.italic = False
msg.print_fancy_msg(name1)
fp.ins_newline(2)


#---------------------------------------------------------------------------------------
# This is for name2 variable                                                           -
#---------------------------------------------------------------------------------------
msg.bold = True; msg.bg = 95; msg.fg = 0
msg.left_indent = 8; msg.right_indent = 8      # it's for the string 
msg.lines = 3                                  # how many lines above and below the string
msg.underline = True
msg.strike = False
msg.length = fp.Length_bg.ALL_ROW              # type of bg
msg.print_fancy_msg(name2)
fp.ins_newline(2)

msg.length = fp.Length_bg.ONLY_WORD            # type of bg
msg.adj_bg_lines_to_right_indent =  True       # True adjs to space available
                                               # when True, right_indent is considerd
                                               # False adjs bg to the string width

msg.adj_bg_msg_to_space_available = True       # True adjs string to space available
                                               # when True right_indent is considerd
                                               # False adjs bg to longest string width
                                               # None adjs bg to string length
# Note: .adj_bg_lines_to_right_indent and adj_bg_msg_to_space_available are more
# options when the string is presented in a form of paragraph type
msg.print_fancy_msg(name2)
fp.ins_newline(2)


#---------------------------------------------------------------------------------------
# This is for name3 variable                                                           -
#---------------------------------------------------------------------------------------
msg.bold = True; msg.bg = 95; msg.fg = 0
msg.left_indent = 8; msg.right_indent = 8      # it's for the string 
msg.lines = 2                                  # how many lines above and below the string
msg.strike = True
msg.underline = False
msg.length = fp.Length_bg.ALL_ROW              # type of bg
msg.left_indent = 12
msg.print_fancy_msg(name3)
fp.ins_newline(2)

msg.length = fp.Length_bg.ONLY_WORD            # type of bg
msg.adj_bg_lines_to_right_indent =  False      # True adjs to space available
                                               # when True, right_indent is considerd
                                               # False adjs bg to the longest string's width

msg.adj_bg_msg_to_space_available = None       # True adjs string to space available
                                               # when True right_indent is considerd
                                               # False adjs bg to longest string width
                                               # None adjs bg to string length
# Note: .adj_bg_lines_to_right_indent and adj_bg_msg_to_space_available are more
# options when the string is presented in a form of paragraph type
msg.print_fancy_msg(name3)
fp.ins_newline(2)


msg.adj_bg_msg_to_space_available = False
msg.print_fancy_msg(name3)
fp.ins_newline(2)

msg.adj_bg_lines_to_right_indent = True
msg.adj_bg_msg_to_space_available = True
msg.print_fancy_msg(name3)
fp.ins_newline(2)


#---------------------------------------------------------------------------------------
msg.bold = True; msg.bg = 95; msg.fg = 0
msg.left_indent = 8; msg.right_indent = 18      # it's for the string 
msg.top_lines = 2                                  # how many lines above and below the string
msg.bottom_lines = 1
msg.strike = True
msg.length = fp.Length_bg.ALL_ROW              # type of bg
msg.print_fancy_msg(name4)
fp.ins_newline(2)

msg.length = fp.Length_bg.ONLY_WORD            # type of bg
msg.adj_bg_lines_to_right_indent =  False      # True adjs to space available
                                               # when True, right_indent is considerd
                                               # False adjs bg to the longest string width

msg.adj_bg_msg_to_space_available = None       # True adjs string to space available
                                               # when True right_indent is considerd
                                               # False adjs bg to longest string width
                                               # None adjs bg to string length
# Note: .adj_bg_lines_to_right_indent and adj_bg_msg_to_space_available are more
# options when the string is presented in a form of paragraph type
msg.print_fancy_msg(name4)





#---------------------------------------------------------------------------------------
# Another Way to Use FancyMessage Class with Some Manipulation                         -
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------   
warning = fp.FancyMessage()
# def warning2(obj:fp.FancyMessage,title:str, body:str, fg_title:int, bg_warning_msg:int, fg_body:int, sp:int)->int:
#    msg = str(body)
   
#    def print_bg_lines(lines, bg_format_line_color="\0m"):
#       n = lines
#       while n>0:
#          print(bg_format_line_color)
#          n -= 1
#    tncols, tnrows = os.get_terminal_size()
#    space_available = tncols - obj.left_indent - obj.right_indent
#    msg_type = "single_line"; new_msg = ""
#    longest_line = 0;  quotient = 0; residue = 0; letter_counter=0
#    number_letter_line_list = []; quotient_number_letter_line_list = []
#    adj_diff_space = []; carry_number_letter_line_list = []
#    residue_number_letter_line_list = []; fit_number_letter_line_list = []
#    result_multi_lines = []; 
   
#    for l in msg:
#       if (l=="\n"):
#          number_letter_line_list.append(letter_counter)            
#          letter_counter = 0
#          msg_type="multiple_lines"
      
#       else:
#          new_msg += l
#          letter_counter += 1

#    if (msg_type == "single_line"):
#       quotient = int(letter_counter/space_available)
#       residue  = letter_counter%space_available
#       while quotient>0:
#          number_letter_line_list.append(space_available)
#          quotient -= 1        
#       number_letter_line_list.append(residue)
      
#       for n in number_letter_line_list:
#          adj_diff_space.append(space_available - n)



#    else:   # multiple lines
#       number_letter_line_list.append(letter_counter) # the last one not added
#       longest_line = max(number_letter_line_list)
#       # first item when only enter it's deleted
#       if (number_letter_line_list[0] == 0):   number_letter_line_list.pop(0)
#       # last item when only enter it's deleted
#       if (number_letter_line_list[(len(number_letter_line_list))-1] == 0):
#          number_letter_line_list.pop((len(number_letter_line_list))-1)
         
               
#       if (space_available > longest_line):
#          for n in number_letter_line_list:
#             adj_diff_space.append(space_available-n)               

#       else:
#          for line in range(len(number_letter_line_list)):
#             if (number_letter_line_list[line] <= space_available):
#                fit_number_letter_line_list.append(number_letter_line_list[line])
               
#             else:
#                quotient = int(number_letter_line_list[line]/space_available)
#                residue  = number_letter_line_list[line]%space_available                  
#                n = quotient

#                while n > 0:                     
#                   quotient_number_letter_line_list.append(space_available)
#                   n -= 1

#                residue_number_letter_line_list.append(residue)
#                carry_number_letter_line_list.append(quotient+1)

#          ctrl = 0; first_time = 0
#          for r in number_letter_line_list:
#             if (r > space_available):                  
#                last_one = carry_number_letter_line_list[ctrl] - 1

#                for n in range(carry_number_letter_line_list[ctrl]):
#                   if (last_one == n):                        
#                      result_multi_lines.append(residue_number_letter_line_list[ctrl])
#                      ctrl += 1
#                   else:
#                      result_multi_lines.append(space_available)
                  
#             else:
#                result_multi_lines.append(r)
#          number_letter_line_list = result_multi_lines

#          for n in number_letter_line_list:
#             adj_diff_space.append(space_available - n)

#    #------------------------------------------------------------------------------------------------------------------------------------------------
#    longest_line = max(number_letter_line_list)
#    # print("ncols                  :",tncols)
#    # print("longes_line            :",longest_line)
#    # print("space_available        :",space_available)
#    # print("number_letter_line_list:",number_letter_line_list)
#    # print("adj_diff_space         :", adj_diff_space)
#    # print()
#    # print(new_msg)
#    return len(number_letter_line_list)


def warning2(obj:fp.FancyMessage, body:str)->int:
   msg = str(body)
   
   tncols, tnrows = os.get_terminal_size()
   space_available = tncols - obj.left_indent - obj.right_indent
   msg_type = "single_line"; new_msg = ""
   longest_line = 0;  quotient = 0; residue = 0; letter_counter=0
   number_letter_line_list = []; quotient_number_letter_line_list = []
   adj_diff_space = []; carry_number_letter_line_list = []
   residue_number_letter_line_list = []; fit_number_letter_line_list = []
   result_multi_lines = []; 
   
   for l in msg:
      if (l=="\n"):
         number_letter_line_list.append(letter_counter)            
         letter_counter = 0
         msg_type="multiple_lines"
      
      else:
         new_msg += l
         letter_counter += 1

   if (msg_type == "single_line"):
      quotient = int(letter_counter/space_available)
      residue  = letter_counter%space_available
      while quotient>0:
         number_letter_line_list.append(space_available)
         quotient -= 1        
      number_letter_line_list.append(residue)
      
      for n in number_letter_line_list:
         adj_diff_space.append(space_available - n)



   else:   # multiple lines
      number_letter_line_list.append(letter_counter) # the last one not added
      longest_line = max(number_letter_line_list)
      # first item when only enter it's deleted
      if (number_letter_line_list[0] == 0):   number_letter_line_list.pop(0)
      # last item when only enter it's deleted
      if (number_letter_line_list[(len(number_letter_line_list))-1] == 0):
         number_letter_line_list.pop((len(number_letter_line_list))-1)
         
               
      if (space_available > longest_line):
         for n in number_letter_line_list:
            adj_diff_space.append(space_available-n)               

      else:
         for line in range(len(number_letter_line_list)):
            if (number_letter_line_list[line] <= space_available):
               fit_number_letter_line_list.append(number_letter_line_list[line])
               
            else:
               quotient = int(number_letter_line_list[line]/space_available)
               residue  = number_letter_line_list[line]%space_available                  
               n = quotient

               while n > 0:                     
                  quotient_number_letter_line_list.append(space_available)
                  n -= 1

               residue_number_letter_line_list.append(residue)
               carry_number_letter_line_list.append(quotient+1)

         ctrl = 0; first_time = 0
         for r in number_letter_line_list:
            if (r > space_available):                  
               last_one = carry_number_letter_line_list[ctrl] - 1

               for n in range(carry_number_letter_line_list[ctrl]):
                  if (last_one == n):                        
                     result_multi_lines.append(residue_number_letter_line_list[ctrl])
                     ctrl += 1
                  else:
                     result_multi_lines.append(space_available)
                  
            else:
               result_multi_lines.append(r)
         number_letter_line_list = result_multi_lines

         for n in number_letter_line_list:
            adj_diff_space.append(space_available - n)

   #------------------------------------------------------------------------------------------------------------------------------------------------
   longest_line = max(number_letter_line_list)
   # print("ncols                  :",tncols)
   # print("longes_line            :",longest_line)
   # print("space_available        :",space_available)
   # print("number_letter_line_list:",number_letter_line_list)
   # print("adj_diff_space         :", adj_diff_space)
   # print()
   # print(new_msg)
   return len(number_letter_line_list)
