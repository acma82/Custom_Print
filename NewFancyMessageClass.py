import enum
import os
#-----------------------------------------------------------------------------------------------------------------------------------------------
class Move(enum.Enum):
   UP    = 1
   RIGHT = 2
   DOWN  = 3
   LEFT  = 4
#-----------------------------------------------------------------------------------------------------------------------------------------------  
class Length_bg(enum.Enum):
   ALL_ROW   = 1
   ONLY_WORD = 2
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Move Right n Times The CursorInsert Empty Spaces                                                                                                                          -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def ins_chr(n_space=0):
   space = ""
   while n_space > 0:
      space +=" "
      n_space -= 1
   return space
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Insert Newlines, nl                                                                                                                          -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def ins_newline(nl=0):
   while nl > 0:
      nl -= 1      
      print("")


def move_right(n=0):  return f"\033[{str(n)}C"

#-----------------------------------------------------------------------------------------------------------------------------------------------
# Set Settings for the Font: Bold, Background, and Foreground                                                                                  -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def set_font(bold=False,bg=-1,fg=-1):
  # bg_color, fg_color, and bold are int values but we convert then to str values
   reset = "\033[0m"
   if bg < 0 or bg > 255:
      bgc = "reset"
   else:
      bgc = str(bg)    

   if fg < 0 or fg > 255:
      fgc = "reset"
   else:
      fgc = str(fg)  


   if (bold == True):
      if (bgc == "reset" and fgc == "reset"):
         settings = reset + "\033[1m"

      elif bgc == "reset" and fgc != "reset":
         settings = reset+"\033[1;38;5;"+fgc+"m"
      
      elif bgc != "reset" and fgc == "reset":
         settings = reset+"\033[1;48;5;"+bgc+"m"

      elif bgc != "reset" and fgc != "reset":
         settings = reset+"\033[1;48;5;"+bgc+";38;5;"+fgc+"m"

      else:
         settings = reset

   elif (bold == False):
      if (bgc == "reset" and fgc == "reset"):
         settings = reset

      elif bgc == "reset" and fgc != "reset":
         settings = reset+"\033[0;38;5;"+fgc+"m"
      
      elif bgc != "reset" and fgc == "reset":
         settings = reset+"\033[0;48;5;"+bgc+"m"

      elif bgc != "reset" and fgc != "reset":
         settings = reset+"\033[0;48;5;"+bgc+";38;5;"+fgc+"m"

      else:
         settings = reset
   else:
      settings = reset

   return settings
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Reset Settings for the Font: Bold, Background, and Foreground                                                                                -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def reset_font():
   return "\033[0m"
#-----------------------------------------------------------------------------------------------------------------------------------------------
# NewFancyMessage Class                                                                                                                        -
#-----------------------------------------------------------------------------------------------------------------------------------------------
class NewFancyMessage():
   def __init__(self):
      self.bold = False
      self.bg = 4
      self.fg = 231

      self.left_indent = 0
      self.right_indent = 0

      self.length = Length_bg.ALL_ROW
      self.lines = 1
      self.adj_bg_lines_to_right_indent = False
      self.adj_bg_msg_to_space_available = False




   def print_fancy_msg(self,data="Message"):
      if (isinstance(data, str)): msg=data
      else:                       msg=str(data)

      def print_bg_lines(bg_format_line_color="\0m"):
         n = self.lines
         while n>0:
            print(bg_format_line_color)
            n -= 1
   
      color = set_font(self.bold, self.bg, self.fg)
      tncols, tnrows = os.get_terminal_size()
      space_available = tncols - self.left_indent - self.right_indent
      msg_type = "single_line"; new_msg = ""
      longest_line = 0;  quotient = 0; residue = 0; letter_counter=0
      number_letter_line_list = []; quotient_number_letter_line_list = []
      adj_diff_space = []; carry_number_letter_line_list = []
      residue_number_letter_line_list = []; fit_number_letter_line_list = []
      result_multi_lines = []
      
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

      longest_line = max(number_letter_line_list)     

      #----------------------------------------------------------------------------------------------------------------------------------------------
      # if (self.length == Length_bg.ALL_ROW):
      #    bg_format_line_color = f"{color}{ins_chr(tncols)}{reset_font()}"
      #    print_bg_lines(bg_format_line_color) # bg_line

         
      #    carry = 0; last_one = len(number_letter_line_list) - 1
      #    print(f"{color}{ins_chr(self.left_indent)}",end="") # different

      #    # start printing the message
      #    for nl in range(len(number_letter_line_list)):
      #       for n in range(number_letter_line_list[nl]):            
      #          print(f"{new_msg[carry+n]}",end="")
            
      #       carry += number_letter_line_list[nl]
            
      #       #------------------------------------------------------------------------------------------
      #       for n in range(adj_diff_space[nl]+self.right_indent):
      #          print(" ",end="")
      #       #------------------------------------------------------------------------------------------
            
      #       print()            
      #       if (last_one == nl): pass
      #       else:                print(f"{color}{ins_chr(self.left_indent)}",end="") # diferent

      #    print_bg_lines(bg_format_line_color) # bg_line 


      
      # elif (self.length == Length_bg.ONLY_WORD):
      #    # self.adj_bg_lines_to_right_indent by default = False
      #    if (self.adj_bg_lines_to_right_indent == True):    bg_format_line_color = f"{color}{move_right(self.left_indent)}{ins_chr(space_available)}{reset_font()}"
      #    elif (self.adj_bg_lines_to_right_indent == False): bg_format_line_color = f"{move_right(self.left_indent)}{color}{ins_chr(longest_line)}{reset_font()}"         
      #    print_bg_lines(bg_format_line_color) # bg_line
 

      #    carry = 0; last_one = len(number_letter_line_list) - 1
      #    print(f"{move_right(self.left_indent)}{color}",end="") # diferente
         
      #    # start printing the message
      #    for nl in range(len(number_letter_line_list)):
      #       for n in range(number_letter_line_list[nl]):            
      #          print(f"{new_msg[carry+n]}",end="")
            
      #       carry += number_letter_line_list[nl]
            
      #      #------------------------------------------------------------------------------------------
      #       # fmsg.adj_bg_msg_to_space_available by default = True
      #       if (self.adj_bg_msg_to_space_available == True):    
      #          for n in range(space_available -  number_letter_line_list[nl]):
      #             print(" ",end="")
           
      #       elif (self.adj_bg_msg_to_space_available == False): pass           
      #       print(f"{reset_font()}",end="")  # diferent
      #       #------------------------------------------------------------------------------------------

      #       print()
      #       if (last_one == nl): pass
      #       else:                print(f"{move_right(self.left_indent)}{color}",end="") # diferent


      #    print_bg_lines(bg_format_line_color) # bg_line 
      # else:
      #    pass
      

      if (self.length == Length_bg.ALL_ROW):
         bg_format_line_color = f"{color}{ins_chr(tncols)}{reset_font()}"
         start_line = f"{color}{ins_chr(self.left_indent)}" # different


      elif (self.length == Length_bg.ONLY_WORD):
         # self.adj_bg_lines_to_right_indent by default = False
         if (self.adj_bg_lines_to_right_indent == True):    bg_format_line_color = f"{color}{move_right(self.left_indent)}{ins_chr(space_available)}{reset_font()}"
         elif (self.adj_bg_lines_to_right_indent == False): bg_format_line_color = f"{move_right(self.left_indent)}{color}{ins_chr(longest_line)}{reset_font()}"         
         start_line = f"{move_right(self.left_indent)}{color}" # diferente

      else: pass

      carry = 0; last_one = len(number_letter_line_list) - 1
      # start printing the message      
      print_bg_lines(bg_format_line_color) # bg_line
      print(start_line,end="")

      for nl in range(len(number_letter_line_list)):
         for n in range(number_letter_line_list[nl]):
            print(f"{new_msg[carry+n]}",end="")
         
         carry += number_letter_line_list[nl]

         if (self.length == Length_bg.ALL_ROW):
            #------------------------------------------------------------------------------------------
            for n in range(adj_diff_space[nl]+self.right_indent):
               print(" ",end="")
            #------------------------------------------------------------------------------------------
         elif (self.length == Length_bg.ONLY_WORD):
            #------------------------------------------------------------------------------------------
            # fmsg.adj_bg_msg_to_space_available by default = True
            if (self.adj_bg_msg_to_space_available == True):    
               for n in range(space_available -  number_letter_line_list[nl]):
                  print(" ",end="")
           
            elif (self.adj_bg_msg_to_space_available == False): pass           
            print(f"{reset_font()}",end="")  # diferent
            #------------------------------------------------------------------------------------------
         else:
            pass

         print()
         if (last_one == nl): pass
         else:                print(start_line,end="") # diferent

      print_bg_lines(bg_format_line_color) # bg_line






      
      print("space_available:                 ",space_available)
      print("number_letter_line_list:         ",number_letter_line_list)
      print("fit_letter_line_list:            ",fit_number_letter_line_list)
      print("quotient_number_letter_line_list:",quotient_number_letter_line_list)
      print("residue_number_letter_line_list: ",residue_number_letter_line_list)
      print("carry_number_letter_line_list:   ",carry_number_letter_line_list)
      print("result_multi_lines:              ",result_multi_lines)
      print("letter_counter:                  ",letter_counter)
      print("adj_diff_space:                  ",adj_diff_space)
      print("suma result: ", sum(result_multi_lines))
      print("suma number letter:", sum(number_letter_line_list))
      print("longest_line:      ",longest_line)
      # print(new_msg)
      print()
#--------------------------------------------------------------------------------------------------
message1 = "hello"                            # len(message1) = 5
message2 = "I am Miguel Angel \
            aguilar Cuesta ACMA82\
            I am trying to make it very big string."                  # len(message2) = 102

message3 = '''
        I should probably collect a list of the best         t
        romantic poems ever written, and maybe I will.
        This is not that. I mostly talk about writing
        books, but I noticed most of the other big
        writing sites actually get most of the their

        traffic from this keyword, because everybody
        is interested in romantic poetry! When you
        want to tell her how you feel, but do not
        have the words to express all that emotion...!
'''

message4 = '''
        I should probably collect a list of the best         t        romantic poems ever written, and maybe I will.
        This is not that. I mostly talk about writing
        books, but I noticed most of the other big
        writing sites actually get most of the their

        traffic from this keyword, because everybody
        is interested in romantic poetry! When you
        want to tell her how you feel, but do not
        have the words to express all that emotion...!
'''

msg = NewFancyMessage()
# fmsg.length = Length_bg.ONLY_WORD
# fmsg.adj_bg_lines_to_right_indent = True
# fmsg.adj_bg_msg_to_space_available = True

# fmsg.left_indent = 35
# fmsg.right_indent =35
# fmsg.left_indent = 15
# fmsg.right_indent =15

# fmsg.print_fancy_msg(message1)
# fmsg.print_fancy_msg(message2)
# fmsg.print_fancy_msg(message3)
# fmsg.print_fancy_msg(message4)

msg.bold = True; msg.bg = 95; msg.fg = 0
msg.left_indent = 8; msg.right_indent = 8  # it's for the string 
msg.lines = 3                              # how many lines above and below the string
msg.adj_bg_lines_to_right_indent =  15     # 
#msg.adj_bg_msg_to_space_available = 15     # 

msg.print_fancy_msg(message1)
print("\n");     
# msg.length = Length_bg.ONLY_WORD
msg.print_fancy_msg(message1)