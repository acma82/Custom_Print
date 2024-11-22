# '''
# This is the Module Docstrings
# Trailing WhiteSpace refers to any whitespace characters at the end of a line of code or string.
# missing-final-newline refers to set a last empty line at the end of the code
# pylint practis.py
# '''
# def add_numbers(x,y):
#     '''
#     Add two numbers, This is the Docstrings for this functions
#     '''
#     return x+y

# if __name__ == "__main__":
#     #print("hello")
#     print(add_numbers(4,2))

#     # help(add_numbers)
#     print(add_numbers.__doc__)
#     # Inside the Interpreter python
#     # import practis
#     # print(practis.add_numbers(2,3))
#     # help(practis.add_numbers)           -> Call the help      -> q to exit
#     # print(practis.add_numbers.__doc__)  -> Call the Docstrings

import custom_print as cp
import enum
import os


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Layout is used for the Range, Set, Frozenset.                                                                                                -
#-----------------------------------------------------------------------------------------------------------------------------------------------
#class Move(str, enum.Enum): # python3.9.18
class Move(enum.StrEnum):    # python3.12.1
    UP    = "up"
    RIGHT = "right"
    DOWN  = "down"
    LEFT  = "left"


class Align(enum.StrEnum):
    LEFT     = "left"
    CENTER   = "center"
    RIGHT    = "right"
    JUSTIFY  = "justify"


class Length_bg(enum.Enum):
    ALL_ROW   = 1
    ONLY_WORD = 2


#-----------------------------------------------------------------------------------------------------------------------------------------------
def dimensions():
    cols, rows = os.get_terminal_size()
    return cols, rows


def erase():
    print("\033[2J",end="")


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Insert A Unicode Character n Times                                                                                                           -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def ins_chr(n=1, unicode=" "):
    sp = str(unicode)
   
    space = ""
    while n > 0:
        space += sp
        n -= 1
    return space



#-----------------------------------------------------------------------------------------------------------------------------------------------
# Insert n Newlines                                                                                                                            -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def ins_newline(n=1):
    while n > 0:
       n -= 1      
       print("")



#-----------------------------------------------------------------------------------------------------------------------------------------------
# Move Cursor to the Right. This function is used as the indentation for the print                                                             -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def _move_right(n=0,option_space=False):
    if (option_space == True):
        sp = ins_chr(n)
    else:
        if (n == 0):
            sp = ""
        else:
            sp = f"\033[{str(n)}C"
    return sp 



#-----------------------------------------------------------------------------------------------------------------------------------------------
# Set Settings for the Font: Bold, Background, and Foreground                                                                                  -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def set_font(bold=False,bg=-1,fg=-1,italic=False,underline=False,strike=False,blinking=False,dim=False,hidden=False,inverse=False):
   '''
----------------------------------------------------------------------------
   import fancyprint as fp

   fp.set_font(bool, int, int)

   This function changes the attributes of the font (bold, bg, fg).
   
   Colors range from -1 to 256.
   To set the default color use -1 or 256.
   
   Example:
            print(fp.set_font(1,11,21)+ " Python is " + fp.set_font(0,1)+
               " Wonderful."+fp.reset_font())
            
            print(f"{fp.set_font(bold=0, bg=22, fg=0)} Python
                 {fp.set_font(1,90,7)} Language.{fp.reset_font()}")
----------------------------------------------------------------------------
'''
   # bg_color and fg_color, are int values but we convert then to str values
   reset = "\033[0m"
   if bg < 0 or bg > 255:
      bgc = "reset"
   else:
      bgc = str(bg)

   if fg < 0 or fg > 255:
      fgc = "reset"
   else:
      fgc = str(fg)


   if (bgc == "reset" and fgc == "reset"):
      settings = reset

   elif bgc == "reset" and fgc != "reset":
      settings = reset+"\033[38;5;"+fgc+"m"
   
   elif bgc != "reset" and fgc == "reset":
      settings = reset+"\033[48;5;"+bgc+"m"

   elif bgc != "reset" and fgc != "reset":
      settings = reset+"\033[48;5;"+bgc+";38;5;"+fgc+"m"

   else:
      settings = reset
   

   if   (bold == True and dim == False): settings = settings + "\033[1m"
   elif (bold == True and dim == True):  settings = settings + "\033[1m"
   elif (bold == False and dim == True): settings = settings + "\033[2m"
   else: # (bold == False and dim == False): 
      pass
      
   if (italic == True):    settings = settings + "\033[3m"
   else:                   settings = settings + "\033[23m"

   if (underline == True): settings = settings + "\033[4m"
   else:                   settings = settings + "\033[24m"

   if (blinking == True):  settings = settings + "\033[5m"
   else:                   settings = settings + "\033[25m"

   if (hidden == True):    settings = settings + "\033[8m"
   else:                   settings = settings + "\033[28m"

   if (strike == True):    settings = settings + "\033[9m"
   else:                   settings = settings + "\033[29m"

   if (inverse == True):   settings = settings + "\033[7m"
   else:                   settings = settings + "\033[27m"

   return settings
   


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Reset Settings for the Font: Bold, Background, and Foreground                                                                                -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def reset_font():
   '''
----------------------------------------------------------------------------
   import fancyprint as fp

   fp.set_font()

   This function resets the font attributes to the default ones.
   
----------------------------------------------------------------------------
'''
   return "\033[0m"

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Fancy Message Class (Single line or a Paragraph Text in the Terminal)                                                                        -
#-----------------------------------------------------------------------------------------------------------------------------------------------
class FancyMessage(cp.Cursor):
   def __init__(self):
      super().__init__()       # Super Class to use all (vars and funs) from Cursor Class
                               # with the Initialization Draw Class(self), ex. self.gotoxy(x,y)
      self.bg_body        = 4;          self.underline_body = False     # 4         False
      self.fg_body        = 231;        self.blinking_body  = False     # 231       False
      self.bold_body      = False;      self.inverse_body   = False     # False     False
      self.dim_body       = False;      self.hidden_body    = False     # False     False
      self.italic_body    = False;      self.strike_body    = False     # False     False
      
      self.msg_body = "Body Msg";       self.help_lines = False

      self.left_indent = 2;             self.right_indent = 2
      self.top_lines = 1;               self.bottom_lines = 1

      self.length = Length_bg.ALL_ROW 
      # These two options don't do anything when length = Length_bg.All_ROW   
      self.adj_bg_lines_to_right_indent = False     # True or False
      self.adj_bg_msg_to_space_available = False    # True or False

      

      #--------------------------------------------------------------------
      # Note Settings Here, print_fancy_note
      self.msg_note = " Note: "
      self.align_note = Align.JUSTIFY;    self.position_note = 1 
      self.bg_note = 231;                 self.fg_note = 0;                 self.bold_note  = False
      self.dim_note = False;              self.italic_note = False;         self.underline_note = False
      self.blinking_note = False;         self.inverse_note = False;        self.hidden_note = False
      self.strike_note = False;           self.left_space_note = 2;         self.right_space_note = 2
      
      # Title Settings Here, print_fancy_message
      self.align_title = Align.LEFT;      self.title_indent = 2;            self.msg_title = "" # title_indent works with Align.JUSTIFY
      self.lines_title_body = 1;          self.strike_title = False
      self.bg_title = 4;                  self.fg_title = 231;              self.bold_title  = False
      self.dim_title = False;             self.italic_title = False;        self.underline_title = False
      self.blinking_title = False;        self.inverse_title = False;       self.hidden_title = False
      
      # Footnote Settings Here, print_fancy_message
      self.align_footnote = Align.RIGHT;  self.footnote_indent = 2;         self.msg_footnote = "" # footnote_indent works with Align.JUSTIFY
      self.lines_body_footnote = 1;       self.strike_footnote = False
      self.bg_footnote = 4;               self.fg_footnote = 231;           self.bold_footnote  = False
      self.dim_footnote = False;          self.italic_footnote = False;     self.underline_footnote = False
      self.blinking_footnote = False;     self.inverse_footnote = False;    self.hidden_footnote = False
      

   def _get_msg_attributes(self,data:str="Message"):
      msg = str(data)
      tncols, tnrows = os.get_terminal_size()
      
      space_available = tncols - self.left_indent - self.right_indent
      
      longest_line   = 0;                       quotient = 0
      letter_counter = 0;                       residue  = 0;                              
      msg_type       = "single_line";           new_msg  = ""
      

      quotient_number_letter_line_list = [];    fit_number_letter_line_list   = []
      residue_number_letter_line_list  = [];    carry_number_letter_line_list = []
      
      adj_diff_space     = [];                  number_letter_line_list = []
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

      return tnrows, tncols, space_available, number_letter_line_list, adj_diff_space, new_msg, len(number_letter_line_list)

   #---------------------------------------------------------------------------------------------------------------------------------------------------
   # Send the Data To the Terminal                                                                                                                    -   
   #---------------------------------------------------------------------------------------------------------------------------------------------------
   def _send_msg_terminal(self,data="Message"):
      def _print_bg_lines(lines, bg_format_line_color="\033[0m"):
         if (lines == 0):
            print("\033[0m",end="")
         else:
            n = lines
            while n>0:
               print(bg_format_line_color)
               n -= 1
      

      tnrows, tncols, space_available, number_letter_line_list, adj_diff_space, new_msg, n_lines = FancyMessage._get_msg_attributes(self,data)

      color = set_font(self.bold_body, self.bg_body, self.fg_body, self.italic_body, self.underline_body, self.strike_body,
                       self.blinking_body, self.dim_body, self.hidden_body, self.inverse_body)
      color2= set_font(bg=self.bg_body, fg=self.fg_body, inverse=self.inverse_body)

      # from here we need: tncols, space_available, number_letter_line_list, adj_diff_space, new_msg

      
      longest_line = max(number_letter_line_list)
      # self.adj_bg_lines_to_right_indent by default  = False
      # self.adj_bg_msg_to_space_available by default = False
      if (self.length == Length_bg.ALL_ROW):
         bg_format_line_color = f"{color2}{ins_chr(tncols)}{reset_font()}"
         # change color for color2 to delete at the beginning the strike, and/or underline option(s)
         start_line = f"{color2}{ins_chr(self.left_indent)}"

      elif (self.length == Length_bg.ONLY_WORD):         
         if (self.adj_bg_lines_to_right_indent == True):
            bg_format_line_color = f"{color2}{_move_right(self.left_indent)}{ins_chr(space_available)}{reset_font()}"  # change color for color2
         
         else:  # elif (self.adj_bg_lines_to_right_indent == False):
            bg_format_line_color = f"{_move_right(self.left_indent)}{color2}{ins_chr(longest_line)}{reset_font()}"     # change color for color2
         
         start_line = f"{_move_right(self.left_indent)}{color2}"                                                       # change color for color2

      else: pass

      carry = 0; last_one = n_lines - 1
      _print_bg_lines(self.top_lines, bg_format_line_color)     # bg_line
      

      print(start_line,end="")
      
      # start printing the message
      for nl in range(n_lines):
         for n in range(number_letter_line_list[nl]):
            print(f"{color}{new_msg[carry+n]}",end="")         # added color because the color2 can be slightly different

         carry += number_letter_line_list[nl]

         if (self.length == Length_bg.ALL_ROW):
            for n in range(adj_diff_space[nl]+self.right_indent):
               print(color2+" ",end="")                        # to delete at the end the strike, and/or underline option(s)

         elif (self.length == Length_bg.ONLY_WORD):
            if (self.adj_bg_msg_to_space_available == True):    
               for n in range(space_available -  number_letter_line_list[nl]):
                  print(color2+" ",end="")                     # to delete the strike we add color2
            else:                                              # elif (self.adj_bg_msg_to_space_available == False):
               for n in range(longest_line-number_letter_line_list[nl]):
                  print(color2+" ",end="")

            print(f"{reset_font()}",end="")
         else:
            pass

         print()
         if (last_one == nl): pass
         else:                print(start_line,end="")
      
      # end printing the message
      _print_bg_lines(self.bottom_lines, bg_format_line_color)   # bg_line

   #---------------------------------------------------------------------------------------------------------------------------------------------------
   # Print Fancy Note                                                                                                                                 -
   #---------------------------------------------------------------------------------------------------------------------------------------------------
   def print_fancy_note(self, msg_body:str="")->None:
      '''
      It prints the fancy note with the attributes defined

      print_fancy_note(msg_body)

      '''
      if (msg_body == ""):
         msg_body = self.msg_body


      # save original values
      li_obj = self.left_indent

      # settings for the msg_body
      if (self.msg_note == ""): len_msg_note = 0
      else:                     len_msg_note = len(self.msg_note)

      self.left_indent = self.left_space_note + len_msg_note + self.right_space_note
      tnrows, tncols, space_available, number_letter_line_list, adj_diff_space, new_msg, n_lines = self._get_msg_attributes(msg_body)

      
      total_back_lines = self.top_lines + n_lines + self.bottom_lines
      if   (self.position_note >= (total_back_lines)): lines_back = 0
      elif (self.position_note <= 0):                  lines_back = total_back_lines
      else:                                            lines_back = total_back_lines - self.position_note 
      
      self._send_msg_terminal(msg_body)

      # settings for the note
      settings_note = set_font(bold=self.bold_note, bg=self.bg_note, fg=self.fg_note, italic=self.italic_note,\
                               underline=self.underline_note, strike=self.strike_note, blinking=self.blinking_note,\
                               dim=self.dim_note, hidden=self.hidden_note, inverse=self.inverse_note)
      
      if (self.align_note == Align.LEFT or self.align_note == "l"):
         print(f"{self.moveTo(qty=lines_back, direction=Move.UP)}{settings_note}{self.msg_note}",end="")

      elif (self.align_note == Align.CENTER or self.align_note == "c"):
         myq = int((self.left_space_note+self.right_space_note)/2)
         print(f"{self.moveTo(qty=lines_back, direction=Move.UP)}{self.moveTo(qty=myq,direction=Move.RIGHT)}{settings_note}{self.msg_note}",end="")
                
      elif (self.align_note == Align.RIGHT or self.align_note == "r"):
         myq = self.left_space_note + self.right_space_note
         print(f"{self.moveTo(qty=lines_back, direction=Move.UP)}{self.moveTo(qty=myq,direction=Move.RIGHT)}{settings_note}{self.msg_note}",end="")
      
      else:  # JUSTIFY
         print(f"{self.moveTo(qty=lines_back, direction=Move.UP)}{self.moveTo(qty=self.left_space_note,direction=Move.RIGHT)}{settings_note}{self.msg_note}")         
      
      self.jumpTo(qty=lines_back-1, direction=Move.DOWN)
      print(f"{reset_font()}",end="")
      
      # putting back original values
      self.left_indent = li_obj
      # n_lines, space_available, tncols are variables for reference to calculate the message      
      if (self.help_lines == True):
         print(f"{ins_chr(self.left_indent)}Body_Lines:{n_lines}  Space_Available:{space_available}  N.Cols: {tncols}  N.Lines:{total_back_lines}")
         
      
   #---------------------------------------------------------------------------------------------------------------------------------------------------
   def print_fancy_message(self, msg_body:str="")->None:
      '''
      It prints the fancy message with the attributes defined

      print_fancy_message(msg_body)

      '''

      if (msg_body == ""):
         msg_body = self.msg_body


      # save original values      
      li_obj = self.left_indent;      bold_obj    = self.bold_body;            blinking_obj  = self.blinking_body
      tl_obj = self.top_lines;        italic_obj  = self.italic_body;          underline_ojb = self.underline_body
      bg_obj = self.bg_body;          strike_obj  = self.strike_body 
      fg_obj = self.fg_body;          hidden_obj  = self.hidden_body
      bl_obj = self.bottom_lines;     inverse_obj = self.inverse_body
      ti_obj = self.msg_title;        
      
      fnm_obj = self.msg_footnote
      dim_obj = self.dim_body
      
      # settings for title
      tnrows, tncols, space_available, number_letter_line_list, adj_diff_space, new_msg, n_lines = self._get_msg_attributes(msg_body)
      if not self.msg_title == "": #!= None:
         # working with the font color         
         self.bg_body     = self.bg_title;          self.underline_body = self.underline_title
         self.fg_body     = self.fg_title;          self.blinking_body  = self.blinking_title
         self.bold_body   = self.bold_title;        self.inverse_body   = self.inverse_title
         self.dim_body    = self.dim_title;         self.hidden_body    = self.hidden_title
         self.italic_body = self.italic_title;      self.strike_body    = self.strike_title
         
         if   (self.align_title == Align.LEFT or self.align_title == "l"):
            pass

         elif (self.align_title == Align.CENTER or self.align_title == "c"):
            sp = int((space_available - len(self.msg_title))/2)
            self.msg_title = ins_chr(sp) + self.msg_title

         elif (self.align_title == Align.RIGHT or self.align_title == "r"):
            sp = space_available - len(self.msg_title) # 1 for not jumping line and finished
            self.msg_title = ins_chr(sp) + self.msg_title

         else:                                         # Align.JUSTIFY
            self.msg_title = ins_chr(self.title_indent) + self.msg_title

            

         self.bottom_lines = self.lines_title_body
         self._send_msg_terminal(self.msg_title)
         # This is necessary because when is right alignment, it jumps automatically to the next row
         if (self.align_title == Align.RIGHT and self.msg_title != ""):
            print("\033[1A",end="")
            print(f"{ins_chr(tncols)}")
            print("\033[1A",end="")

         # settings for body (we recovered left_indent, and change bottom_lines and change top_lines)               
         
         if not (self.msg_footnote == ""):
            self.bottom_lines = 0
         else:                      self.bottom_lines = bl_obj

         self.left_indent = li_obj
         self.bg_body     = bg_obj;          self.underline_body = underline_ojb
         self.fg_body     = fg_obj;          self.blinking_body  = blinking_obj
         self.bold_body   = bold_obj;        self.inverse_body   = inverse_obj
         self.dim_body    = dim_obj;         self.hidden_body    = hidden_obj
         self.italic_body = italic_obj;      self.strike_body    = strike_obj

         if not (self.msg_title == ""): self.top_lines = 0
         else:                   self.top_lines = tl_obj   
         self.fg_body = fg_obj  # returning the color for the body
         
         self._send_msg_terminal(msg_body)
               
      else:         
         if not self.msg_footnote == "":   self.bottom_lines = self.lines_body_footnote
         else:                             self.bottom_lines = bl_obj       
         
         self._send_msg_terminal(msg_body)     


      if not self.msg_footnote == "":


         if   (self.align_footnote == Align.LEFT or self.align_footnote == "l"):
            pass

         elif (self.align_footnote == Align.CENTER or self.align_footnote == "c"):
            sp = int((space_available - len(self.msg_footnote))/2)
            self.msg_footnote = ins_chr(sp) + self.msg_footnote
         
         elif (self.align_footnote == Align.RIGHT or self.align_footnote == "r"):
            sp = space_available - len(self.msg_footnote) # 1 for not jumping line and finished
            self.msg_footnote = ins_chr(sp) + self.msg_footnote
         
         else:
            self.msg_footnote = ins_chr(self.footnote_indent) + self.msg_footnote # JUSTIFY
            
         self.top_lines = self.lines_body_footnote
         self.bottom_lines = bl_obj
         self.bg_body     = self.bg_footnote;          self.underline_body = self.underline_footnote
         self.fg_body     = self.fg_footnote;          self.blinking_body  = self.blinking_footnote
         self.bold_body   = self.bold_footnote;        self.inverse_body   = self.inverse_footnote
         self.dim_body    = self.dim_footnote;         self.hidden_body    = self.hidden_footnote
         self.italic_body = self.italic_footnote;      self.strike_body    = self.strike_footnote
         
         self._send_msg_terminal(self.msg_footnote)
         
         # This is necessary because when is right alignment, it jumps automatically to the next row
         if (self.align_footnote == Align.RIGHT and self.msg_footnote != ""):
            print("\033[1A",end="")
            print(f"{ins_chr(tncols)}")
            print("\033[1A",end="")

      else:
         pass


      # putting back original values
      self.top_lines = tl_obj;            self.left_indent = li_obj;            #  self.bottom_lines = bl_obj
      self.bg_body     = bg_obj;          self.underline_body = underline_ojb
      self.fg_body     = fg_obj;          self.blinking_body  = blinking_obj
      self.bold_body   = bold_obj;        self.inverse_body   = inverse_obj
      self.dim_body    = dim_obj;         self.hidden_body    = hidden_obj
      self.italic_body = italic_obj;      self.strike_body    = strike_obj
      self.msg_footnote = fnm_obj;        self.msg_title      = ti_obj

      # n_lines, space_available, tncols are variables for reference to calculate the message
      if (self.help_lines == True):
         total_lines = n_lines + self.top_lines + self.bottom_lines

         if (self.msg_title != ""):
            total_lines += 1 + self.lines_title_body
         
         if (self.msg_footnote != ""):
            total_lines += 1 + self.lines_body_footnote

         print(f"{ins_chr(self.left_indent)}Body_Lines:{n_lines}  Space_Available:{space_available}  N.Cols: {tncols}  N.Lines:{total_lines}")


#---------------------------------------------------------------------------------------------------------------------------------------------------
   def get_message_attributes(self, msg_body:str="", print_attributes=True)->list:
      tnrows, tncols, space_available, number_letter_line_list, adj_diff_space, list_words, n_lines = FancyMessage._get_msg_attributes(self,msg_body)

      if (msg_body == ""):  msg_body = self.msg_body

      smallest_line = min(number_letter_line_list)
      longest_line  = max(number_letter_line_list)
      words = msg_body.split()
      counter_words = len(words)
      total_characters = sum(number_letter_line_list)
      screen_size_xy = [tncols,tnrows]


      list_attributes = [["Description",              "Values"],
                        ["Screen Size_xy",             screen_size_xy],                    
                        ["Left Indent",                self.left_indent],
                        ["Right Indent",               self.right_indent],
                        ["Space Available",            space_available],
                        ["Longest Line",               longest_line],
                        ["Smallest Line",              smallest_line],
                        ["List Line Lengths",          number_letter_line_list],
                        ["List Line Spaces",           adj_diff_space],
                        ["Words Into a List",          "\'words\'"],
                        ["Total Number of Lines",      n_lines],
                        ["Total Number of Words",      counter_words],
                        ["Total Number of Characters", total_characters]]

      list_words = [["Position","Word"]]
      cnt = 0
      for n in words:
         list_words.append([cnt, n])
         cnt += 1

      if print_attributes == True:
         tbl = cp.FancyFormat()
         # Title
         tbl.msg_title = "  Attributes From The Message  "
         tbl.align_title = cp.Align.LEFT
         tbl.bold_title   = True;   tbl.bg_title = 231
         tbl.italic_title = True;   tbl.fg_title = 21
            # bg colors
         tbl.bg_horizontal_line = 21
         tbl.bg_vertical_line   = 21
         tbl.bg_corner_chr      = 21

         tbl.bg_inner_corner_chr  = 21
         tbl.bg_under_line_header = 21

         tbl.bg_corner_under_line_header = 21
         tbl.bg_vertical_header_line_chr = 21
    
         tbl.bg_header = 90
         tbl.fg_header = 231
         tbl.bold_header = True
    
         tbl.bg_data = 231
         tbl.fg_data = 0
         tbl.bold_data = True
    
    
         tbl.adj_top_margin = 2
         tbl.adj_indent = 4
         tbl.adj_space  = 4

         tbl.horizontal_line_under_header_on = True         
         tbl.adj_bottom_margin = 1
         tbl.print_fancy_format(data=list_attributes, style=cp.Line_Style.SPACE_COL_COLOR)         
         tbl.adj_top_margin = 1
         tbl.msg_title = "  Words of The Message Into a List  "
         tbl.print_fancy_format(list_words)
         
            

      return list_attributes, list_words


txt = "This is a First Line and Simple Text...!"
msg = '''
Guido van Rossum, a Dutch programmer, created Python in the late 1980s
as a hobby project. He started working on it in December 1989 at Cent-
rum Wiskunde & Informatica (CWI) in the Netherlands.

Python was first released on February 20, 1991. Python was named after
the 1970s BBC comedy sketch series Monty Python's Flying Circus.
'''


fm = FancyMessage()

fm.get_message_attributes(msg_body=msg, print_attributes=True)