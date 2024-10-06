#-----------------------------------------------------------------------------------------------------------------------------------------------
# Required Modules                                                                                                                             -
#-----------------------------------------------------------------------------------------------------------------------------------------------
import os
import enum
import platform
#-----------------------------------------------------------------------------------------------------------------------------------------------
# For Help:
#   inside the python interpreter
   
#   import fancyprint as fp
#   fun = fp.FancyPrint()
  
#   help(fp.bg_ansi_colors(bold=1, fg=22))   for a function of the module
#   help(fun.fancy_print())                  for a function of the module inside the classs FancyList

#   for the terminal is 80 width with any height for better visualization.

#-----------------------------------------------------------------------------------------------------------------------------------------------
# Layout is used for the Range, Set, Frozenset.                                                                                                -
#-----------------------------------------------------------------------------------------------------------------------------------------------
class Move(enum.StrEnum):
   UP    = "up"
   RIGHT = "right"
   DOWN  = "down"
   LEFT  = "left"


class Align(enum.StrEnum):
   LEFT     = "left"
   CENTER   = "center"
   RIGHT    = "right"
   JUSTIFY  = "justify"


class Layout(enum.StrEnum):
   HORIZONTAL = "horizontal"
   VERTICAL =   "vertical"


class Length_bg(enum.Enum):
   ALL_ROW   = 1
   ONLY_WORD = 2


class Line_Style(enum.StrEnum):
   CUSTOMIZED   = "customized"
   SINGLE       = "single"
   SINGLE_BOLD  = "single_bold"
   SINGLE_HEAVY = "single_heavy"
   DOUBLE       = "double"
   DASH         = "dash"
   SQ_BRACKETS = "sq_brackets"
   

#-----------------------------------------------------------------------------------------------------------------------------------------------
# Screen Functions                                                                                                                             -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def clean():
   '''
----------------------------------------------------------------------------      
   It cleans the terminal and return the cursor to home.
   It uses ansi code.
----------------------------------------------------------------------------
   '''
   print("\033[2J",end="")  # clean the terminal
   print("\033[H",end="")   # return home the cursor


if os.name == 'nt' and (platform.release() == '10' or platform.release == "11"):
   OS_Windows = True
   OS_Linux = False
   # Fix ANSI color in Windows 10 version 10.0.14393 (Windows Anniversary Update)
   import ctypes
   kernel32 = ctypes.windll.kernel32
   kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
   def clear():
     '''
   ----------------------------------------------------------------------------      
      It cleans the terminal and return the cursor  to home.
      It uses the system command.
   ----------------------------------------------------------------------------
     '''
     os.system("cls")
   
   # it may disable the scroll bar on the Command Prompt or the Windows PowerShell
   # to enable the scroll bar, got to Properties-> Layout-> Screen Buffer Size-> Set Height to 1000
   
   def resize(rows:int=25, cols:int=80)->None:
      '''
   ----------------------------------------------------------------------------      
      It resizes the terminal.
   ----------------------------------------------------------------------------
      '''
      #os.system(f"mode con:cols={cols} lines={rows}")
      os.system(f"mode {cols}, {rows}")


elif (os.name == 'posix'):
   OS_Windows = False
   OS_Linux = True
   def clear():
      '''
   ----------------------------------------------------------------------------      
      It cleans the terminal and return the cursor to home.
      It uses the system command.
   ----------------------------------------------------------------------------
      '''
      os.system("clear")
   
   def resize(rows:int=25, cols:int=80)->None:
      '''
   ----------------------------------------------------------------------------      
      It resizes the terminal.
   ----------------------------------------------------------------------------
      '''
      os.system(f"resize -s {rows} {cols}")


else:
   def clear():
      '''
   ----------------------------------------------------------------------------      
      It cleans the terminal and return the cursor to home.
      It uses the system command.
   ----------------------------------------------------------------------------
      '''
      print("\033[2J",end="")  # clean the terminal
      print("\033[H",end="")   # return home the cursor

   def resize(rows:int=25, cols:int=80)->None:
      '''
   ----------------------------------------------------------------------------      
      It resizes the terminal.
   ----------------------------------------------------------------------------
      '''
      os.system(f"resize -s {rows} {cols}")


#-----------------------------------------------------------------------------------------------------------------------------------------------
def dimensions():
   '''
----------------------------------------------------------------------------      
   It returns the size of the actual terminal: cols, rows.
----------------------------------------------------------------------------
   '''
   cols, rows = os.get_terminal_size()
   return cols, rows


def erase():
   '''
----------------------------------------------------------------------------      
   It cleans the terminal and the cursor remain in the same position.
   It uses ansi code.
----------------------------------------------------------------------------
   '''
   print("\033[2J",end="")



#-----------------------------------------------------------------------------------------------------------------------------------------------
# Linux Background Color Option List                                                                                                           -
#----------------------------------------------------------------------------------------------------------------------------------------------- 
def bg_ansi_colors(bold=False, fg=-1, n_line=0):
   '''
----------------------------------------------------------------------------
   This function displays all background colors available with ansi code.
----------------------------------------------------------------------------
'''

   msg = " bg color number "
   reset = "\033[0m"; ctrl = 0; space = "   "

   if fg < 0 or fg > 256: fg_color = "-1"
   else:                  fg_color = str(fg)  
  
   if bold == True: b = "1"
   else:         b = "0" 
   
   for color in range(257):
      if color <= 9:
         space = "   "
      elif color <= 99 and color >=10:
         space = "  "
      else:
         space = " "
    
      if ctrl <= 1:
         ctrl += 1
         if fg_color == "-1":
            print(f"\033[{b};48;5;{color}m {msg} {reset}{color}",end=space)
         else:
            print(f"\033[{b};48;5;{color};38;5;{fg_color}m {msg} {reset}{color}",end=space)
      else:
         ctrl = 0
         if fg_color == "-1":
            if n_line > 0: print(f"\033[{b};48;5;{color}m {msg} {reset}{color}"); ins_newline(n_line)
            else:             print(f"\033[{b};48;5;{color}m {msg} {reset}{color}")
         else:
            if n_line > 0: print(f"\033[{b};48;5;{color};38;5;{fg_color}m {msg} {reset}{color}"); ins_newline(n_line)
            else:                 print(f"\033[{b};48;5;{color};38;5;{fg_color}m {msg} {reset}{color}")
   
   print("\x1B[0m  bg default color  -1")


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Linux Foreground Color Option List                                                                                                           -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def fg_ansi_colors(bold=False, bg=-1, n_line=0):
   '''
----------------------------------------------------------------------------
   This function displays all foreground colors available with ansi code
----------------------------------------------------------------------------
'''

   msg = " fg color number "
   reset = "\033[0m"; ctrl = 0; space = "   "

   if bg < 0 or bg > 256: bg_color = "-1"
   else:                  bg_color = str(bg)  
  
   if bold == True: b = "1"
   else:         b = "0" 

   for color in range(257):
      if color <= 9:
         space = "   "
      elif color <= 99 and color >=10:
         space = "  "
      else:
         space = " "
    
      if ctrl <= 1:
         ctrl += 1
         if bg_color == "-1":
            print(f"\033[{b};38;5;{color}m {msg} {reset}{color}",end=space)
         else:
            print(f"\033[{b};48;5;{bg_color};38;5;{color}m {msg} {reset}{color}",end=space)
      else:
         ctrl = 0
         if bg_color == "-1":
            if (n_line > 0): print(f"\033[{b};38;5;{color}m {msg} {reset}{color}"); ins_newline(n_line)
            else:              print(f"\033[{b};38;5;{color}m {msg} {reset}{color}")
         else:
            if (n_line > 0): print(f"\033[{b};48;5;{bg_color};38;5;{color}m {msg} {reset}{color}"); ins_newline(n_line)
            else:              print(f"\033[{b};48;5;{bg_color};38;5;{color}m {msg} {reset}{color}")
   
   print("\x1B[0m  fg default color  -1")


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Move Right n Times The CursorInsert Empty Spaces                                                                                                                          -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def ins_space(n_space=1):
   '''
----------------------------------------------------------------------------
   This function inserts x number of spaces.
----------------------------------------------------------------------------   
   Example: 
            import fancyprint as fp  
            fp.ins_space(x)
            print(f"Hello{fp.ins_space(40)}There")


'''
   space = ""
   while n_space > 0:
      space +=" "
      n_space -= 1
   return space


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Insert Newlines, nl                                                                                                                          -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def ins_newline(nl=1):
   '''
----------------------------------------------------------------------------
   This function inserts x number of lines.
----------------------------------------------------------------------------   
   example:
           import fancyprint as fp 
           print("Python 3")
           fp.ins_newline(3)
           print("is amazing...!")

   '''
   
   while nl > 0:
      nl -= 1      
      print("")

def terminal_bell():
   '''
----------------------------------------------------------------------------
   This function makes sound of the terminal bell.  
----------------------------------------------------------------------------
'''
   print("\a")
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Set Settings for the Font: Bold, Background, and Foreground                                                                                  -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def set_font(bold=False,bg=-1,fg=-1,italic=False,underline=False,strike=False,blinking=False,dim=False,hidden=False,inverse=False):
   '''
----------------------------------------------------------------------------
   import fancyprint as fp

   fl.set_font(bool, int, int)

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

   This function resets the font attributes to the defaults (bold, bg, fg).
   
   Example:
            print(fp.set_font(1,11,21)+ " Python is " + fp.set_font(0,1)+
               " Wonderful."+fp.reset_font())
            
            print(f"{fp.set_font(bold=0, bg=22, fg=0)} Python
               {fp.set_font(1,90,7)} Language.{fp.reset_font()}")

            print(fp.set_font(1,11,21)+ " Python is ")
            print(" Wonderful.")
            print(fp.reset_font()+"Bye")   
----------------------------------------------------------------------------
'''
   return "\033[0m"


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Move Cursor to the Right. This function is used as the indentation for the print                                                             -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def move_right(n=0,option_space=False):
   '''
----------------------------------------------------------------------------
   This function moves the cursor n spaces to the right.   
----------------------------------------------------------------------------
   '''
   if (option_space == True):
      sp = ins_space(n)
   else:
      sp = f"\033[{str(n)}C"
   return sp 

   
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Bool to List Type                                                                                                               -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def bool2list(my_bool):
   tempo_list = []
   tempo_list.append(my_bool)
   return tempo_list


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Integer to List Type                                                                                                            -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def int2list(my_int):
   tempo_list = []
   tempo_list.append(my_int)
   return tempo_list

   
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Float to List Type                                                                                                              -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def float2list(my_float):
   tempo_list = []
   tempo_list.append(my_float)
   return tempo_list


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Complex to List Type                                                                                                            -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def complex2list(my_complex):
   tempo_list = []
   tempo_list.append(my_complex)
   return tempo_list


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Convert From String to List Type                                                                                                             -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def str2list(my_str):
   tempo_list = []
   tempo_list.append(my_str)
   return tempo_list


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Dict to List Type                                                                                                               -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def dict2list(my_dict, key_title="key", value_title="value"):
   '''
   ----------------------------------------------------------------------------
   
   ----------------------------------------------------------------------------
   '''
   my_key_list = []; my_data_list = []

   my_key_list  = list(my_dict.keys())
   my_data_list = list(my_dict.values())
   
   complete_list = [];  tempo_list = []
   if (key_title == "key") and (value_title == "value"):
      if (len(my_key_list)) > 1:   complete_list.append(["Keys","Values"])
      else:                        complete_list.append(["Key","Value"])
   
   elif (key_title == "none" and value_title == "none"):
      pass

   else:
      complete_list.append([key_title,value_title])

   for d in range(len(my_dict)):
      tempo_list.append(my_key_list[d])
      tempo_list.append(my_data_list[d])
      complete_list.append(tempo_list)
      tempo_list = []
   
   return complete_list


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Set or Frozenset to List Type                                                                                                               -
#-----------------------------------------------------------------------------------------------------------------------------------------------
# set values are printed in aleatory order all the time
# frozenset values are printed in aleatory order all the time
def set2list(my_set:set, set_header = "none", layout:Layout=Layout.HORIZONTAL):
   tempo_list = []; cnt = 0; l = len(my_set)

   if (layout.lower() == Layout.VERTICAL):
      if set_header == "set" or set_header == "frozenset":
         if len(my_set) > 1:
            tempo_list.append([set_header+" Values"])
         else:
            tempo_list.append([set_header+" Value"])

      elif (set_header == "none"):
         pass
         
      else:
         tempo_list.append([set_header])

      while l > 0:
         dato = list(my_set)[cnt]
         tempo_list.append([dato])
         cnt += 1
         l   -= 1

   if (layout.lower() == Layout.HORIZONTAL):
      if set_header == "set" or set_header == "frozenset":
         if len(my_set) > 1:
            tempo_list.append("Set Values")
         else:
            tempo_list.append("Set Value")
      
      elif (set_header == "none"):
         pass
      
      else:
         tempo_list.append(set_header)

      while l > 0:
         dato = list(my_set)[cnt]
         tempo_list.append(dato)
         cnt += 1
         l   -= 1

   
   return tempo_list
     
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Range to List Type                                                                                                               -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def range2list(my_range:range, range_header = "none", layout:Layout=Layout.HORIZONTAL):
   tempo_list = []

   if (layout.lower() == Layout.VERTICAL):
      if range_header == "range":  tempo_list = [["Range"]]
      elif range_header == "none": pass
      else:                       tempo_list = [[range_header]]

      for n in my_range:
         tempo_list.append([n])
      
   if (layout.lower() == Layout.HORIZONTAL):
      if range_header == "range":  tempo_list = ["Range"]
      elif range_header == "none": pass
      else:                       tempo_list = [range_header]

      for n in my_range:
         tempo_list.append(n)


   return tempo_list


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Tuple to List Type                                                                                                               -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def tuple2list(my_tuple):
   tempo_list = []
   #-----------------------------------------------------------------------------------------------
   if (len(my_tuple) == 0):
      return tempo_list                

   #-----------------------------------------------------------------------------------------------
   elif (len(my_tuple) == 1):          
                                              # string              ("")         -> Case 0   String
                                              # "empty_tuple"       ("",)        -> Case 1   Empty
      tempo_list.append(my_tuple[0])          # "one_item_no_row"   ("Apple",)   -> Case 2   Tuple
      return tempo_list                       # "one_item_one_row"  (("Apple",)) -> Case 3   Tuple inside Tuple

   #-----------------------------------------------------------------------------------------------
   #elif len(my_tuple) > 1:
   else:
      type_type = []; lengths = []
      l = len(my_tuple); tuple_tuple = 0; tuple_other = 0

      for n in range(len(my_tuple)):
         if (isinstance(my_tuple[n], tuple)):
            tuple_tuple = 1            
            type_type.append("tuple")
            lengths.append(len(my_tuple[n]))
         
         else:
            tuple_other = 1
            type_type.append("other")
            lengths.append(1)
      
      # This is only for tuples inside the tuple ->
      # tupleData = (("hello","hello"),("hell",),("hi","bye","good"),([1,2],))        -> Case 4
      if (tuple_tuple == 1 and tuple_other == 0):
         tempo = []
         for col in my_tuple:
            for i in col:
               tempo.append(i)
            tempo_list.append(tempo)
            tempo = []

      # This is only for other types inside a tuple 
      # tupleData = ("hello","hell","hi",[1,2])                                       -> Case 5
      elif (tuple_tuple == 0 and tuple_other == 1):
         for n in my_tuple:
            tempo_list.append(n)     # for rows (Horizontal)
            #tempo_list.append([n])  # for cols (Vertical)
         
       

      # This is for combination tuple (tuple =1 and other = 1)                        -> Case 6
      # tupleData = (("hello","hello"),("hell",),("hi","bye","good"),[1,2], "hello")
      elif (tuple_tuple == 1 and tuple_other == 1):
         for n in range(l):
            if (lengths[n]) > 1:
               tempo = []
               for i in range(lengths[n]):
                  tempo.append(my_tuple[n][i])
               tempo_list.append(tempo)

            else:
               if (type_type[n] == "other"):
                  tempo_list.append([my_tuple[n]])
               else:
                  tempo_list.append([my_tuple[n][0]])
      else:
         tempo_list = []

   return tempo_list


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Get Data Type and Convert It to a List Type                                                                                                  -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def data2list(self,dato):
   data_list = []
   # it is already a list type
   if (isinstance(dato, list)):        return dato
   
   # bool type to list type
   elif (isinstance(dato, bool)):      data_list = bool2list(dato)
   
   # int to list type
   elif (isinstance(dato, int)):       data_list = int2list(dato)
   
   # float to list type
   elif (isinstance(dato, float)):     data_list = float2list(dato)
   
   # string type
   elif (isinstance(dato, str)):       data_list = str2list(dato)

   # complex type
   elif (isinstance(dato, complex)):   
      if (dato.imag < 0):
         data_list.append(str(dato.real)+"-"+str((dato.imag)*-1)+"j")
      else:
         data_list.append(str(dato.real)+"+"+str(dato.imag)+"j")

   # range type
   elif (isinstance(dato, range)):     
      data_list = range2list(dato,"none",self.set_layout)      
                                       
   # dictionary type
   elif (isinstance(dato, dict)):      data_list = dict2list(dato)
   
   # set type
   elif (isinstance(dato, set)):       data_list = set2list(dato,"none",self.set_layout)

   # frozenset type
   elif (isinstance(dato, frozenset)): data_list = set2list(dato,"none",self.set_layout)
   
   # tuple
   elif (isinstance(dato, tuple)):     data_list = tuple2list(dato)
   
   else:                               data_list = "none"
   # none: bytes, bytearray, memoryview(bytes(5))  

  
   return data_list



#-----------------------------------------------------------------------------------------------------------------------------------------------
# Get List Type                                                                                                                                -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def get_list_type(my_list):
   if not isinstance(my_list, list):
      return "incorrect_variable_type"                # [Not a List] Case 0
  #-----------------------------------------------------------------------------------------------

   if (len(my_list) == 0):
      return "empty_list"                             # []    Case 1

  #-----------------------------------------------------------------------------------------------

   if (len(my_list) == 1):
      if isinstance(my_list[0], list):
         if len(my_list[0]) > 1:
            return "multiple_items_one_row"           # [[1,2,3]]   Case 5
         else:
            return "one_item_one_row"                 # [[1]]  Case 4
      else:
         return "one_item_no_row"                     # [1]   Case 2

  #-----------------------------------------------------------------------------------------------
   if (len(my_list) > 1):
      items = 0; rows = 0
      for n in my_list:
         if not isinstance(n, list):
            items = 1
         else:
            rows = 1

      if (items ==  1 and rows == 0):
         return "multiple_items_no_row"               #  [1,2,3]  Case 3
      elif (items == 0 and rows == 1):
         return  "multiple_items_multiple_rows"       # [[1],[4],[7]]              Case 6
                                                      # [[1,2,3],[4,5,6],[7,8,9]]  Case 6
                                                      # [[1],[1,2,3],[5,4,7,8]]    Case 6
                                                      # any combination of this is Case 6
                                                      # [[1,2,3],[[2],3,4],[5,[6,7]]] Case 6
      else:
         return "mix_items"                           # [5,6,[1,2,3],[1,0,3]]      Case 7
                                                      # [[1,2],[1,2,[1]],[1,2,3]]  Case 7
                                                      # any combination of this is Case 7


#-----------------------------------------------------------------------------------------------------------------------------------------------
# Help fancyprint Module                                                                                                                       -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def help():
   fun_list = [["import fancyprint as fp"], ["fp.bg_ansi_color(bold, fg)"], \
               ["  "], ["fp.bg_ansi_color(bold, fg)"], \
               ["  "], ["fp.move_right(n_space=0)"], ["  "], ["fp.ins_newline(nl=0)"], \
               ["  "], ["fp.set_font(bold=0,bg=-1,fg=-1)"], ["  "],  ["fp.reset_font()"], \
               ["  "], ["fp.send_msg(msg='message', bg=1, fg=7, bold=1, indent=2)"],\
               ]
   lista = FancyFormat()
   lista.bg_title = 11; lista.fg_title = 21; lista.align_title = "c"; lista.bold_title = 1
   lista.msg_title = " Function available for fancylist module "
   lista.bg_header =22; lista.fg_header = 7 #; lista.bold_header = 01
   lista.horizontal_line_under_header_on = 1
   #lista.horizontal_separator_line_on = 1
   
   class_fun = [["fun = fp.FancyList()"],\
                ["new_list = fun.read_csv_file(my_list, file_name)"],["  "],\
                ["fun_list.print_cvs_list(my_list)"],["  "],\
                ["fun_list.print_fancy_list(my_list)"]
               ]

   lista.print_fancy_list(fun_list)
   lista.msg_title = " Function available for FancyList Class module "
   print()
   lista.print_fancy_list(class_fun)

   

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#  Function Used by the FancyList Class                                                                                                        -
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Get Total Length of the Columns                                                                                                              -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def get_total_length(self,my_list):
   my_length = 0
   list_dimensions = get_list_type(my_list)
   if (list_dimensions == "one_item_no_row"):     # ["item"]
      # the *2 is because there are 2 adj_space one each size (left and right)
      # the +2 is because there are 2 vertical lines (left and right)
      my_length = len(my_list[0]) + (self.adj_space*2) + self.adj_indent + 2
      

   elif (list_dimensions == "one_item_one_row"):  # [[item]]
      # the *2 is because there are 2 adj_space one each size (left and right)
      # the adj_indent is because we have an indentation space at the begining
      # the +2 is because there are 2 vertical lines (left and right)
      my_length = len(my_list[0][0]) + (self.adj_space*2) + self.adj_indent + 2 
      

   elif (list_dimensions == "multiple_items_one_row") or (list_dimensions == "multiple_items_no_row"):
      # [1,2,3,4,5]  or [[1,2,3,4,5]]
      for item in my_list:
         my_length += len(item) + (self.adj_space*2) + 1  # this one is for the left vertical chr    
      my_length += 1                                      # this one is for the right vertical chr, last one
      my_length += self.adj_indent                        # this is for the indentation space

   else:    # multiples rows
      one_item_per_row = True

      for row in my_list:             # checking if we a list like [[1],[2],[3]], only one column
         if  len(row) != 1:
            one_item_per_row = False
            break

      if one_item_per_row == True:    # finding the greatest column size in characters 
         for row in my_list:
            for col in row:
               if my_length < len(col):
                  my_length = len(col)

         # the adj_indent is because we have an indentation space at the begining
         # the *2 is because there are 2 adj_space one each size (left and right), self.adj_space
         # the +2 is because there are 2 vertical lines (left and right)
         my_length += self.adj_indent + (self.adj_space*2) + 2
         
      
      else:
         # we have a matrix list something like this [[10,20,30],[40,50,60],[70,80,90]]. awsome.
         max_rows, max_cols = get_number_rows_cols_list(my_list)
         n_cols = []; tempo_cols = []

         # we create the transpose of the list but we save their lens in the transpose rather than the data
         for c in range(max_cols):
            for r in range(max_rows):
               tempo_cols.append(len(my_list[r][c]))
            n_cols.append(tempo_cols)
            tempo_cols = []
         
         longest_cols = []
         for col in n_cols:
            longest_cols.append(max(col)) # longest_cols keeps the size list of the longest columns in chr
            # making the complete sum of the all the length
            # the adj_indent is because we have an indentation space at the begining
            # sum(longest_cols) is suming all the longest cols in the list
            # the self.adj_space is multiply by 2 because we have to side, left and right, on each column then
            # we multiply by the number of columns in the list
            # the +1  is because there are 1 vertical lines no consiered in the list 
            # of longest_cols (left, middles, and right)
     
         my_length = self.adj_indent + sum(longest_cols) +\
            ((self.adj_space*2)*len(longest_cols)) + len(longest_cols) + 1
      
   return my_length    

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Print Title On Terminal with Its Attributes: Bold, Bg and Fg Color (title)                                                                   -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def print_title(self,my_list):

   if self.msg_title == "": return
   else: 
      settings = set_font(self.bold_title,self.bg_title, self.fg_title,self.italic_title,self.underline_title,self.strike_title,self.blinking_title,self.dim_title,self.hidden_title,self.inverse_title)

      # check for the length of the message
   total_length = get_total_length(self,my_list)

   
   if (self.align_title.lower() == "left") or (self.align_title.lower() == "l"):
      print(move_right(self.adj_indent)+settings+self.msg_title+reset_font())
   
   elif (self.align_title.lower() == "center") or (self.align_title.lower() == "c"):
      difference = (int((total_length)/2)) - (int(((len(self.msg_title) + self.adj_indent))/2))
      if difference <= 0:
         print(move_right(self.adj_indent)+settings+self.msg_title+reset_font()) # left align
      else:
         print(move_right(self.adj_indent+difference)+settings+self.msg_title+reset_font())

   elif (self.align_title.lower() == "right") or (self.align_title.lower() == "r"):
      # the 1 is for the vertical line
      difference = total_length - (len(self.msg_title) + (self.adj_space) + self.adj_indent + 1)
      if difference <= 0:
         print(move_right(self.adj_indent)+settings+self.msg_title+reset_font()) # left align
      else:
         print(move_right(self.adj_indent+self.adj_space+1+difference)+settings+self.msg_title+reset_font())

   elif (self.align_title.lower() == "justify") or (self.align_title.lower() == "j"):    
      difference = total_length - (len(self.msg_title) + (self.adj_space) + self.adj_indent + 1)
      if difference <= 0:
         print(move_right(self.adj_indent)+settings+self.msg_title+reset_font()) # left align
      else:
         print(move_right(self.adj_indent+self.adj_space+1)+settings+self.msg_title+reset_font())

   else:
      print(move_right(self.adj_indent)+settings+self.msg_title+reset_font())   # left align
   
   ins_newline(self.adj_top_space)    # space between the the title and the top list

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Print Footnote On Terminal with Its Attributes: Bold, Bg and Fg Color (footnote)                                                             -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def print_notefoot(self,my_list):
   
   if self.msg_footnote == "": return
   else: 
      settings = set_font(self.bold_footnote,self.bg_footnote, self.fg_footnote,self.italic_footnote,self.underline_footnote,\
                          self.strike_footnote,self.blinking_footnote,self.dim_footnote,self.hidden_footnote,self.inverse_footnote)

   # check for the length of the message
   total_length = get_total_length(self,my_list)

   ins_newline(self.adj_bottom_space)

   if (self.align_footnote.lower() == "left") or (self.align_footnote.lower() == "l"):
      print(move_right(self.adj_indent)+settings+self.msg_footnote+reset_font())
   
   elif (self.align_footnote.lower() == "center") or (self.align_footnote.lower() == "c"):
      difference = (int((total_length)/2)) - (int(((len(self.msg_footnote) + self.adj_indent))/2))
      if difference <= 0:
         print(move_right(self.adj_indent)+settings+self.msg_footnote+reset_font()) # left align
      else:
         print(move_right(self.adj_indent+difference)+settings+self.msg_footnote+reset_font())

   elif (self.align_footnote.lower() == "right") or (self.align_footnote.lower() == "r"):      
      difference = total_length - (len(self.msg_footnote) + (self.adj_space) + self.adj_indent + 1) # 1 is for the vertical line
      if difference <= 0:
         print(move_right(self.adj_indent)+settings+self.msg_footnote+reset_font()) # left align
      else:
         print(move_right(self.adj_indent+self.adj_space+1+difference)+settings+self.msg_footnote+reset_font())

   elif (self.align_footnote.lower() == "justify") or (self.align_footnote.lower() == "j"):    
      difference = total_length - (len(self.msg_footnote) + (self.adj_space) + self.adj_indent + 1)
      if difference <= 0:
         print(move_right(self.adj_indent)+settings+self.msg_footnote+reset_font()) # left align
      else:
         print(move_right(self.adj_indent+self.adj_space+1)+settings+self.msg_footnote+reset_font())

   else:
      print(move_right(self.adj_indent)+settings+self.msg_footnote+reset_font())   # left align
   

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Print Horizontal Line                                                                                                                        -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def print_horizontal_segment(self,start_chr,end_chr,times,indent,option):

   set_v = set_font(self.bold_vertical_line, self.bg_vertical_line, self.fg_vertical_line)
   set_h = set_font(self.bold_horizontal_line, self.bg_horizontal_line, self.fg_horizontal_line)
   set_c = set_font(self.bold_corner_chr, self.bg_corner_line, self.fg_corner_line)
   set_hd = set_font(self.bold_under_line_header, self.bg_under_line_header,self.fg_under_line_header)
   set_hdc = set_font(self.bold_corner_under_line_header, self.bg_corner_under_line_header,self.fg_corner_under_line_header)
   set_ic = set_font (self.bold_inner_corner_chr, self.bg_inner_corner_chr,self.fg_inner_corner_chr)
  
   # indentation adds the space is set up for the indentation 
   # we want the indentation space at the begining but not at the end of the line.
  
   if (indent == 1):
      print(move_right(self.adj_indent),end="")
  
   if option == "horizontal":
      print(set_v+start_chr+set_h,end="")

   elif option == "corner":    
      print(set_c+start_chr+set_h,end="")

   elif option == "horizontal_header":
      print(set_hdc+start_chr+set_hd,end="")    

   elif option == "inner_corner":
      print(set_ic+start_chr+set_h,end="")

   else:
      print(set_v+start_chr+set_h,end="")

   for n in range(times):
      print(end_chr,end="")
  
   print(reset_font(),end="")

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Print Single Element                                                                                                                         -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def print_single_element(self,my_list):
   
   if isinstance(my_list[0],list): item = my_list[0][0]
   else:                           item = my_list[0]

   ins_newline(self.adj_top_margin)
   # print title  
   print_title(self,my_list)
   
   # get all the settings for the list
   
   set_d = set_font(self.bold_data, self.bg_data, self.fg_data,self.italic_data,self.underline_data,self.strike_data,self.blinking_data,self.dim_data,self.hidden_data,self.inverse_data)
   set_v = set_font(self.bold_vertical_line, self.bg_vertical_line, self.fg_vertical_line)  
  
   # print the top horizontal line
   if  self.top_horizontal_line_on == True:
      indent = 1  # to add the space at the beginning ()  
      print_horizontal_segment(self, self.top_left_corner_chr, self.top_horizontal_line_chr, ((len(item))+(2*self.adj_space)), indent, "corner")
      indent = 0  # to don't add this space at the end or the middle
      print_horizontal_segment(self, self.top_right_corner_chr, self.top_horizontal_line_chr, 0, indent, "corner")
      print()
   else:
      pass

   #--------------------------------------------------------------------------------------------------------------------------------------------
   # print data with adjustments. We are missing vertical line color and horizontal line color and data color
   if (self.align_data.lower() == "left") or (self.align_data.lower() == "l"):
      print(move_right(self.adj_indent) + set_v+self.left_vertical_line_chr + set_d+ item + move_right((self.adj_space*2),self.bg_all_cell_data) + set_v +\
            self.right_vertical_line_chr + reset_font())

   elif (self.align_data.lower() == "right") or (self.align_data.lower() == "r"):
      print(move_right(self.adj_indent) + set_v+self.left_vertical_line_chr+set_d + move_right((self.adj_space*2),self.bg_all_cell_data)\
            + item + set_v + self.right_vertical_line_chr + reset_font())
  
   elif (self.align_data.lower() == "center") or (self.align_data.lower() == "c"):
      print(move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d+ move_right(self.adj_space,self.bg_all_cell_data) +\
            item + move_right(self.adj_space,self.bg_all_cell_data) + set_v+self.right_vertical_line_chr + reset_font())
  
   elif (self.align_data.lower() == "justify") or (self.align_data.lower() == "j"):
      print(move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d + move_right(self.adj_space,self.bg_all_cell_data) +\
            item + move_right(self.adj_space,self.bg_all_cell_data) + set_v+self.right_vertical_line_chr + reset_font())

   else:
      print(move_right(self.adj_indent) + set_v+self.left_vertical_line_chr + set_d+move_right(self.adj_space,self.bg_all_cell_data)+\
            item + move_right(self.adj_space,self.bg_all_cell_data) + set_v+self.right_vertical_line_chr + reset_font())
    
   #--------------------------------------------------------------------------------------------------------------------------------------------
   # print the bottom horizontal line
   if  self.bottom_horizontal_line_on == 1:
      indent = 1  # to add the space at the beginning (vertical line chr)
      print_horizontal_segment(self, self.bottom_left_corner_chr, self.bottom_horizontal_line_chr, ((len(item))+(2*self.adj_space)), indent, "corner")
      indent = 0  # to don't add this space at the end or the middle
      print_horizontal_segment(self, self.bottom_right_corner_chr, self.bottom_horizontal_line_chr, 0, indent, "corner")
      print()

   else:
      pass

   print_notefoot(self,my_list)
   ins_newline(self.adj_bottom_margin)
  
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Print Multiple Horizontal Items (One Row OR No Row)                                                                                          -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def print_multiple_horizontal_items(self,my_list):
   ins_newline(self.adj_top_margin)
   # print title
   print_title(self,my_list)
  
   # get all the settings for the list
   set_d = set_font(self.bold_data, self.bg_data, self.fg_data,self.italic_data,self.underline_data,self.strike_data,self.blinking_data,self.dim_data,self.hidden_data,self.inverse_data)
   set_v = set_font(self.bold_vertical_line, self.bg_vertical_line, self.fg_vertical_line)
   
   # drawing the top horizontal line
   if  self.top_horizontal_line_on == True:
      indent = 1  # to add the space at the beginning (indentation space)    
      for item in my_list:    
         if indent == 1:          # first segment
            print_horizontal_segment(self, self.top_left_corner_chr, self.top_horizontal_line_chr, (len(item) + (2*self.adj_space)), indent, "corner")
            indent = 0
         else:
            print_horizontal_segment(self, self.middle_top_corner_chr, self.top_horizontal_line_chr,(len(item) + (2*self.adj_space)), indent, "inner_corner")
            # corner or horizontal depends on what color to get if the corner colors or the horizontal_line
            # last segment, which is only the corner that's why it's 0 on value
      print_horizontal_segment(self, self.top_right_corner_chr, self.top_horizontal_line_chr, 0, indent, "corner") 
      print() # done top line, jump to next line to print data

   else:
      pass
   #---------------------------------------------------------------------------------------------------------------------------------------------
   # print the data with their alignments
   indent = 1
   for item in my_list:
      if (self.align_data.lower() == "left") or (self.align_data.lower() == "l"):
         if indent == 1:
            print(move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d + item +\
                  move_right((self.adj_space*2),self.bg_all_cell_data),end="")
            indent = 0
         else:
            print(set_v + self.middle_vertical_line_chr + set_d + item + move_right((self.adj_space*2),self.bg_all_cell_data),end="")

         #---------------------------------------------------------------------------------------------------------------------------------------
      elif (self.align_data.lower() == "right") or (self.align_data.lower() == "r"):
         if indent == 1:
            print(move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d+\
                  move_right((self.adj_space*2),self.bg_all_cell_data) + item,end="")
            indent = 0
         else:
            print(set_v + self.middle_vertical_line_chr + set_d + move_right((self.adj_space*2),self.bg_all_cell_data) + item,end="")
        
         #---------------------------------------------------------------------------------------------------------------------------------------
      elif (self.align_data.lower() == "justify") or (self.align_data.lower() == "j")\
           or (self.align_data.lower() == "center") or (self.align_data.lower() == "c"):
         if indent == 1:
            print(move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d +\
                  move_right(self.adj_space,self.bg_all_cell_data) + item + move_right(self.adj_space,self.bg_all_cell_data),end="")
            indent = 0
         else:
            print(set_v + self.middle_vertical_line_chr + set_d+move_right(self.adj_space,self.bg_all_cell_data) + item +\
                  move_right(self.adj_space,self.bg_all_cell_data),end="")

         #---------------------------------------------------------------------------------------------------------------------------------------
      else: # justify default one
         print(move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d + move_right(self.adj_space,self.bg_all_cell_data) +\
               item + move_right(self.adj_space,self.bg_all_cell_data),end="")

   print(set_v + self.right_vertical_line_chr + reset_font())

   #---------------------------------------------------------------------------------------------------------------------------------------------
   # print the bottom horizontal line
   if  self.bottom_horizontal_line_on == 1:
      indent = 1
      for item in my_list:    
         if indent == 1:
            print_horizontal_segment(self, self.bottom_left_corner_chr, self.bottom_horizontal_line_chr, (len(item) + (2*self.adj_space)),\
                              indent, "corner") # first segment
            indent = 0

         else:
            #"horizontal") # middle segments. "corner"
            print_horizontal_segment(self, self.middle_bottom_corner_chr, self.bottom_horizontal_line_chr, (len(item) + (2*self.adj_space)),\
                                indent, "inner_corner")
            # corner or horizontal depends on what color to get if the corner colors or the horizontal_line
            # last segment, which is only the corner that's why it's 0 on value  
      print_horizontal_segment(self, self.bottom_right_corner_chr, self.bottom_horizontal_line_chr, 0, indent, "corner") 
      print()

   print_notefoot(self,my_list)
   ins_newline(self.adj_bottom_margin)
  
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Get Number of Rows and Cols of the List                                                                                                      -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def get_number_rows_cols_list(my_list):
   n_rows = len(my_list)
   n_cols = 0

   for n in my_list:
      if len(n) > n_cols:
         n_cols = len(n)

   return n_rows, n_cols

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Complete Information in the List, if need it                                                                                                 -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def complete_info_list(self,my_list):
   n_rows, n_cols = get_number_rows_cols_list(my_list)
   row_tempo_list = []; matrix_update = []

   for row in range(n_rows):
      row_tempo_list = my_list[row]
      diff = n_cols - len(my_list[row])
      for col in range(diff):
         row_tempo_list.append(str(self.set_fill_chr))
      matrix_update.append(row_tempo_list)

   return matrix_update  

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Get the Odd or Even Space Adjustment for the Word                                                                                            -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def get_odd_even_space_adj(length,len_dato):
   sp_start = 0; sp_end=0
   odd_l = length%2
   odd_len_dato = len_dato%2

   if odd_l == 1:                      # if length word is odd    
      sp_start = (int(length/2))-(int(len_dato/2))

      if odd_len_dato == 1:             # if len_dato is odd
         sp_end = sp_start
      else:                             # if len_dato is even
         sp_end = sp_start + 1
      
   else:                                # if the length word is even
      sp_start = (int(length/2))-(int(len_dato/2))
    
      if odd_len_dato == 1:             # if len_dato is odd
         sp_end = sp_start - 1
      else:                             # if len_dato is even
         sp_end = sp_start

   return sp_start, sp_end

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Print Matrix List                                                                                                                            -
#-----------------------------------------------------------------------------------------------------------------------------------------------
def print_matrix_list(self,my_list):
   # d  :data,   v: vertical,   hcl: left_corner_header,   mch:middle_corner_header, rch:right_corner_header,   t:title(header)
   # get all the settings for the list
   set_d = set_font(self.bold_data, self.bg_data, self.fg_data,self.italic_data,self.underline_data,self.strike_data,self.blinking_data,self.dim_data,self.hidden_data,self.inverse_data)
   set_v = set_font(self.bold_vertical_line, self.bg_vertical_line, self.fg_vertical_line)
   set_hchr_v = set_font(self.bold_vertical_header_line_chr,\
                                    self.bg_vertical_header_line_chr,self.fg_vertical_header_line_chr)

   set_t = set_font(self.bold_header, self.bg_header, self.fg_header,self.italic_header,self.underline_header,self.strike_header,self.blinking_header,self.dim_header,self.hidden_header,self.inverse_header)   
   total_length = get_total_length(self,my_list)

   ins_newline(self.adj_top_margin)
   # print title  
   print_title(self,my_list)
   # this is the last part and we need to start printing the matrix
   if len(my_list[0]) == 1:
      # we are dealing with only one column    
      #-------------------------------------------------------------------------------------------------------------------------------------------
      #print_horizontal_segment(self,start_chr,end_chr,times,indent,option)
      # item is the longest column
      length = total_length - (self.adj_indent + (self.adj_space*2) + 2) # length is the longest column length

      # print the top horizontal line
      if  self.top_horizontal_line_on == True:
         indent = 1  # to add the space at the beginning ()
         print_horizontal_segment(self, self.top_left_corner_chr, self.top_horizontal_line_chr, length + (2*self.adj_space), indent, "corner")
         indent = 0  # to don't add this space at the end or the middle
         print_horizontal_segment(self, self.top_right_corner_chr, self.top_horizontal_line_chr, 0, indent, "corner")
         print()
      else:
         pass
      #-------------------------------------------------------------------------------------------------------------------------------------------
      # print data here
      ctrl_header = 0
      for row in my_list:
         for dato in row:
            if ctrl_header == 0:        # printing Header
               ctrl_header += 1          
               if (self.align_header.lower() == "left") or (self.align_header.lower() == "l"):
                  print(move_right(self.adj_indent) + set_hchr_v + self.left_vertical_header_line_chr + set_t + dato +\
                        move_right((self.adj_space*2)+(length-len(dato)),self.bg_all_cell_header) + set_hchr_v +\
                        self.right_vertical_header_line_chr + reset_font(),end="")

               elif (self.align_header.lower() == "right") or (self.align_header.lower() == "r"):
                  print(move_right(self.adj_indent) + set_hchr_v + self.left_vertical_header_line_chr + set_t +\
                        move_right((self.adj_space*2)+(length-len(dato)),self.bg_all_cell_header) + dato + set_hchr_v +\
                        self.right_vertical_header_line_chr + reset_font(),end="")
      
               elif (self.align_header.lower() == "center") or (self.align_header.lower() == "c"):
                  # add the extra space for the word odd or even space adjustment for start and the end
                  oe_sp_start, oe_sp_end = get_odd_even_space_adj(length,len(dato)) 
                  print(move_right(self.adj_indent) + set_hchr_v + self.left_vertical_header_line_chr + set_t +\
                        move_right(self.adj_space+oe_sp_start,self.bg_all_cell_header)+ dato +\
                        move_right(self.adj_space+oe_sp_end,self.bg_all_cell_header) +\
                        set_hchr_v+self.right_vertical_header_line_chr+reset_font(),end="")
      
               elif (self.align_header.lower() == "justify") or (self.align_header.lower() == "j"):
                  print(move_right(self.adj_indent) + set_hchr_v + self.left_vertical_header_line_chr + set_t +\
                        move_right(self.adj_space,self.bg_all_cell_header) + dato +\
                     move_right(self.adj_space+(length-len(dato)),self.bg_all_cell_header) + set_hchr_v +\
                     self.right_vertical_header_line_chr+reset_font(),end="")
               else:
                  print(move_right(self.adj_indent) + set_hchr_v + self.left_vertical_header_line_chr + set_t +\
                        move_right(self.adj_space,self.bg_all_cell_header) + dato +\
                        move_right(self.adj_space+(length-len(dato)),self.bg_all_cell_header) + set_hchr_v +\
                        self.right_vertical_header_line_chr + reset_font(),end="")
               print()
               # the horizontal line between the headers and the firs data row, only for matrix list
               #if self.horizontal_line_under_header_on == True or self.horizontal_separator_line_on == 1: 
               # the horizontal line between the headers and the firs data row, only for matrix list  
               if self.horizontal_line_under_header_on == True :             
                  indent = 1; print_horizontal_segment(self, self.left_corner_under_line_header_chr,\
                           self.horizontal_line_under_header_chr, length + (2*self.adj_space), indent, "horizontal_header")
                  indent = 0; print_horizontal_segment(self, self.right_corner_under_line_header_chr,\
                                                self.horizontal_line_under_header_chr, 0, indent, "horizontal_header")
                  print()
          
            else:                        # printing Data
               if (self.align_data.lower() == "left") or (self.align_data.lower() == "l"):
                  print(move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d + dato+\
                     move_right((self.adj_space*2)+(length-len(dato)),self.bg_all_cell_data) +\
                     set_v + self.right_vertical_line_chr + reset_font(),end="")

               elif (self.align_data.lower() == "right") or (self.align_data.lower() == "r"):
                  print(move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d +\
                        move_right((self.adj_space*2)+(length-len(dato)),self.bg_all_cell_data) +\
                           dato + set_v + self.right_vertical_line_chr + reset_font(),end="")
      
               elif (self.align_data.lower() == "center") or (self.align_data.lower() == "c"):
                  # add the extra space for the word odd or even space adjustment for start and the end
                  oe_sp_start, oe_sp_end = get_odd_even_space_adj(length,len(dato)) 
                  print(move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d +\
                        move_right(self.adj_space+oe_sp_start,self.bg_all_cell_data)+ dato +\
                        move_right(self.adj_space+oe_sp_end,self.bg_all_cell_data) + set_v +\
                        self.right_vertical_line_chr + reset_font(),end="")
      
               elif (self.align_data.lower() == "justify") or (self.align_data.lower() == "j"):
                  print(move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d +\
                        move_right(self.adj_space,self.bg_all_cell_data)+ dato +\
                        move_right(self.adj_space+length-len(dato),self.bg_all_cell_data)+\
                        set_v + self.right_vertical_line_chr + reset_font(),end="")
               else:
                  print(move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d +\
                        move_right(self.adj_space,self.bg_all_cell_data)+ dato +\
                        move_right(self.adj_space+length-len(dato),self.bg_all_cell_data) + set_v +\
                        self.right_vertical_line_chr + reset_font(),end="")
         
               print()
               # the horizontal line for all the rows, only for matrix list. 1 shows it and 0 hides it
               if self.horizontal_separator_line_on == 1: 
                  ctrl_header += 1
                  if ctrl_header == len(my_list):
                     pass
                  else:
                     indent = 1; print_horizontal_segment(self, self.left_lateral_corner_chr,\
                           self.horizontal_line_chr, length + (2*self.adj_space), indent, "inner_corner")
                     indent = 0; print_horizontal_segment(self, self.right_lateral_corner_chr,\
                           self.horizontal_line_chr, 0, indent, "inner_corner")
                     print()

      #-------------------------------------------------------------------------------------------------------------------------------------------
      # print the bottom horizontal line
      if  self.bottom_horizontal_line_on == 1:
         indent = 1  # to add the space at the beginning (vertical line chr)
         print_horizontal_segment(self, self.bottom_left_corner_chr, self.bottom_horizontal_line_chr,\
                              length + (2*self.adj_space), indent, "corner")
         indent = 0  # to don't add this space at the end or the middle
         print_horizontal_segment(self, self.bottom_right_corner_chr, self.bottom_horizontal_line_chr,\
                              0, indent, "corner")
         print() 
      else:
         pass
      #--------------------------------------------------------------------------------------------------------------------------------------------
      # we are dealing with a matrix list something like this [[10,20,30],[40,50,60],[70,80,90]]                                                  -
      # Awsome...!                                                                                                                                -
      #--------------------------------------------------------------------------------------------------------------------------------------------
   else:
      max_rows, max_cols = get_number_rows_cols_list(my_list)
      n_cols = []; tempo_cols = []
      # we create the transpose of the list but we save their lens in the transpose rather than the data
      for c in range(max_cols):
         for r in range(max_rows):
            tempo_cols.append(len(my_list[r][c]))
         n_cols.append(tempo_cols)
         tempo_cols = []

      longest_cols = []
      for col in n_cols:
         longest_cols.append(max(col)) # longest_cols keeps the size list of the longest columns in characters

      #-------------------------------------------------------------------------------------------------------------------------------------------      
      # drawing the top horizontal line
      if  self.top_horizontal_line_on == True:
         indent = 1  # to add the space at the beginning (indentation space)
         for item in longest_cols:    
            if indent == 1:
               print_horizontal_segment(self, self.top_left_corner_chr, self.top_horizontal_line_chr, (item+(2*self.adj_space)), indent, "corner")
               indent = 0
            else:   # corner or horizontal affect the color bg fg which variable will take into action
               print_horizontal_segment(self, self.middle_top_corner_chr, self.top_horizontal_line_chr, (item+(2*self.adj_space)), indent, "inner_corner")
      
         # last segment, which is only the corner that's why it's 0 on value
         print_horizontal_segment(self, self.top_right_corner_chr, self.top_horizontal_line_chr, 0, indent, "corner") 
         print() # done top line, jump to next line to print data
      else:
         pass
      #-------------------------------------------------------------------------------------------------------------------------------------------
      # print header only
      ctrl_col = 0
      vertical = move_right(self.adj_indent)+set_hchr_v+self.left_vertical_header_line_chr 
      for dato in my_list[0]:

         if (self.align_header.lower() == "left") or (self.align_header.lower() == "l"):
            print(vertical + set_t + dato + move_right((self.adj_space*2)+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_header) +\
                  reset_font(),end="")

         elif (self.align_header.lower() == "right") or (self.align_header.lower() == "r"):
            print(vertical + set_t + move_right((self.adj_space*2)+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_header) +\
                  dato + reset_font(),end="")
    
         elif (self.align_header.lower() == "center") or (self.align_header.lower() == "c"):
            # add the extra space for the word odd or even space adjustment for start and the end
            oe_sp_start, oe_sp_end = get_odd_even_space_adj(longest_cols[ctrl_col],len(dato))
            print(vertical + set_t + move_right(self.adj_space+oe_sp_start,self.bg_all_cell_header) + dato +\
                  move_right(self.adj_space+oe_sp_end,self.bg_all_cell_header) + reset_font(),end="")
    
         elif (self.align_header.lower() == "justify") or (self.align_header.lower() == "j"):
            print(vertical + set_t + move_right(self.adj_space,self.bg_all_cell_header) + dato +\
                  move_right(self.adj_space+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_header) + reset_font(),end="")

         else:
            print(vertical + set_t + move_right(self.adj_space,self.bg_all_cell_header) + dato +\
                  move_right(self.adj_space+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_header) + reset_font(),end="")

         vertical = set_hchr_v+self.middle_vertical_header_line_chr
         ctrl_col += 1
      print(set_hchr_v+self.right_vertical_header_line_chr+reset_font())
    
      #-------------------------------------------------------------------------------------------------------------------------------------------
      if self.horizontal_line_under_header_on == True : 
         # the horizontal line between the headers and the firs data row, only for matrix list
         indent = 1  # to add the space at the beginning (indentation space)
         # drawing the bottom horizontal line
         for item in longest_cols:    
            if indent == 1:
               print_horizontal_segment(self, self.left_corner_under_line_header_chr,\
                  self.horizontal_line_under_header_chr, (item+(2*self.adj_space)), indent,"horizontal_header") # first segment
               indent = 0
            else:
               print_horizontal_segment(self, self.middle_corner_under_line_header_chr,\
                  self.horizontal_line_under_header_chr, (item+(2*self.adj_space)), indent,"horizontal_header") # middle segments

         print_horizontal_segment(self, self.right_corner_under_line_header_chr,\
               self.horizontal_line_under_header_chr, 0, indent, "horizontal_header") 
            # last segment, which is only the corner that's why it's 0 on value
      
         print() # done top line, jump to next line to print data

      #-------------------------------------------------------------------------------------------------------------------------------------------
      # print data only   for datos in my_list[1:]:
      # ctrl_sep = 0
      # for datos in my_list:
      #   if ctrl_sep == 0:
      #     ctrl_sep = 1
      #     continue
      ctrl_sep = 1
      for datos in my_list[1:]:  # better way than the above
         ctrl_col = 0
         vertical = move_right(self.adj_indent)+set_v+self.left_vertical_line_chr
         for dato in datos:

            if (self.align_data.lower() == "left") or (self.align_data.lower() == "l"):
               print(vertical + set_d + dato + move_right((self.adj_space*2)+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_data) +\
                     reset_font(),end="")

            elif (self.align_data.lower() == "right") or (self.align_data.lower() == "r"):
               print(vertical + set_d + move_right((self.adj_space*2)+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_data) +\
                     dato + reset_font(),end="")
      
            elif (self.align_data.lower() == "center") or (self.align_data.lower() == "c"):
               # add the extra space for the word odd or even space adjustment for start and the end
               oe_sp_start, oe_sp_end = get_odd_even_space_adj(longest_cols[ctrl_col],len(dato)) 
               print(vertical + set_d + move_right(self.adj_space+oe_sp_start,self.bg_all_cell_data) + dato +\
                     move_right(self.adj_space+oe_sp_end,self.bg_all_cell_data) + reset_font(),end="")
      
            elif (self.align_data.lower() == "justify") or (self.align_data.lower() == "j"):
               print(vertical + set_d + move_right(self.adj_space,self.bg_all_cell_data) + dato +\
                     move_right(self.adj_space+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_data) + reset_font(),end="")

            else:
               print(vertical + set_d + move_right(self.adj_space,self.bg_all_cell_data) + dato +\
                     move_right(self.adj_space+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_data) + reset_font(),end="")

            vertical = set_v+self.middle_vertical_line_chr
            ctrl_col += 1        
         print(set_v+self.right_vertical_line_chr+reset_font())

         if self.horizontal_separator_line_on == 1:
            if (ctrl_sep == len(my_list)-1):
               # drawing the bottom horizontal line
               if  self.bottom_horizontal_line_on == 1:
                  indent = 1  # to add the space at the beginning (indentation space)
                        
                  for item in longest_cols:
                     if indent == 1:
                        # def print_horizontal_segment(self,start_chr,end_chr,times,indent,option):
                        print_horizontal_segment(self, self.bottom_left_corner_chr, self.bottom_horizontal_line_chr,\
                           (item+(2*self.adj_space)), indent, "corner") # first segment
                        indent = 0

                     else:
                        # def print_horizontal_segment(self,start_chr,end_chr,times,indent,option):
                        print_horizontal_segment(self, self.middle_bottom_corner_chr, self.bottom_horizontal_line_chr,\
                           (item+(2*self.adj_space)), indent, "inner_corner")#"horizontal",)#"corner") # middle segments              
                        # last segment, which is only the corner that's why it's 0 on value
                  print_horizontal_segment(self, self.bottom_right_corner_chr,\
                     self.bottom_horizontal_line_chr, 0, indent, "corner") 
                  
                  
               else:
                  pass
            else:     
               indent = 1  # to add the space at the beginning (indentation space)
                           # drawing the bottom horizontal line
               for item in longest_cols:
                  if indent == 1:
                     # def print_horizontal_segment(self,start_chr,end_chr,times,indent,option):
                     print_horizontal_segment(self, self.left_lateral_corner_chr, self.horizontal_line_chr, (item+(2*self.adj_space)), indent,"inner_corner")
                     indent = 0              

                  else:
                     print_horizontal_segment(self, self.middle_inner_corner_chr, self.horizontal_line_chr, (item+(2*self.adj_space)), indent, "inner_corner")

               print_horizontal_segment(self, self.right_lateral_corner_chr, self.horizontal_line_chr, 0, indent, "inner_corner")
            print()
         ctrl_sep += 1

      if self.horizontal_separator_line_on == 0:                        
         #-----------------------------------------------------------------------------------------------------------------------------------------
         if  self.bottom_horizontal_line_on == 1:
            indent = 1  # to add the space at the beginning (indentation space)
                     # drawing the bottom horizontal line
            for item in longest_cols:
               if indent == 1:
                  # first segment
                  print_horizontal_segment(self, self.bottom_left_corner_chr, self.bottom_horizontal_line_chr, (item+(2*self.adj_space)), indent, "corner")
                  indent = 0
               else:
                  #"horizontal")#"corner") # middle segments
                  print_horizontal_segment(self, self.middle_bottom_corner_chr, self.bottom_horizontal_line_chr, (item+(2*self.adj_space)), indent, "inner_corner")
               
                  # last segment, which is only the corner that's why it's 0 on value               
            print_horizontal_segment(self, self.bottom_right_corner_chr, self.bottom_horizontal_line_chr, 0, indent, "corner") 
            print()     # done top line, jump to next line to print data
         else:
            pass
            #----------------------------------------------------------------------------------------------------------------------------------------
   print_notefoot(self,my_list)
   ins_newline(self.adj_bottom_margin)



#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Defing a class without initial parameter but function with parameters                                                                        -
#-----------------------------------------------------------------------------------------------------------------------------------------------
class FancyFormat():
   def __init__(self):    
      #-------------------------------------------------------------------------------------------------------------------------------------------
      # defining variable names                  # values to take                                                                                #
      #-------------------------------------------------------------------------------------------------------------------------------------------
      # General Use  
      self.adj_top_margin  = 0                 # lines to be add between the terminal and the title
      self.adj_bottom_margin = 0               # lines to be add between the end of list or footnote and terminal
      self.adj_top_space   = 0                 # lines to be added between title and top list
      self.adj_indent      = 2                 # space from the terminal to the box
      self.adj_space       = 2                 # space from left to right side inside the box
      self.adj_bottom_space= 0                 # lines to be added between bottom list and footnote
      self.set_fill_chr    = "----"            # to fill the empty spots when the list is not complete
      self.set_layout      = Layout.HORIZONTAL # This is only for Range, Set, and SetFrozen type data
      self.update_list     = False             # if we want to save the data as it's presented, but string each element in list
                  
      #-------------------------------------------------------------------------------------------------------------------------------------------
      # Title Section
      self.msg_title   = ""                      # string value
      self.bold_title  = False                   # two values False and True (0 and 1)
      self.bg_title    = -1                      # values -1 to 255
      self.fg_title    = -1                      # values -1 to 255
      self.align_title = "justify"               # 4 values: justify(j),left(l), center(c), and right(r)

      self.italic_title    = False               # two values False and True (0 and 1)
      self.underline_title = False               # two values False and True (0 and 1)
      self.strike_title    = False               # two values False and True (0 and 1)
      self.blinking_title  = False               # two values False and True (0 and 1)
      self.dim_title       = False               # two values False and True (0 and 1)
      self.hidden_title    = False               # two values False and True (0 and 1)
      self.inverse_title   = False               # two values False and True (0 and 1)
    
      #-------------------------------------------------------------------------------------------------------------------------------------------
      # Footnote Section
      self.msg_footnote  = ""                    # string value
      self.bold_footnote = False                 # two values False and True (0 and 1)
      self.bg_footnote   = -1                    # values -1 to 255
      self.fg_footnote   = -1                    # values -1 to 255    
      self.align_footnote= "justify"             # 4 values: justify(j),left(l), center(c), and right(r)

      self.italic_footnote    = False            # two values False and True (0 and 1)
      self.underline_footnote = False            # two values False and True (0 and 1)
      self.strike_footnote    = False            # two values False and True (0 and 1)
      self.blinking_footnote  = False            # two values False and True (0 and 1)
      self.dim_footnote       = False            # two values False and True (0 and 1)
      self.hidden_footnote    = False            # two values False and True (0 and 1)
      self.inverse_footnote   = False            # two values False and True (0 and 1)


      #-------------------------------------------------------------------------------------------------------------------------------------------
      # Data Section
      self.bold_data  = False                    # two values False and True (0 and 1)
      self.bg_data    = -1                       # values -1 to 255
      self.bg_all_cell_data = True               # how long will be the bg (all the cell or only the data)
      self.fg_data    = -1                       # values -1 to 255
      self.align_data = "justify"                # 4 values: justify(j),left(l), center(c), and right(r)    
      self.horizontal_separator_line_on = False  # horizontal line for all the rows, only for matrix list. 1 shows it and 0 hides it
                                                 # two values False and True (0 and 1)

      self.italic_data    = False                # two values False and True (0 and 1)
      self.underline_data = False                # two values False and True (0 and 1)
      self.strike_data    = False                # two values False and True (0 and 1)
      self.blinking_data  = False                # two values False and True (0 and 1)
      self.dim_data       = False                # two values False and True (0 and 1)
      self.hidden_data    = False                # two values False and True (0 and 1)
      self.inverse_data   = False                # two values False and True (0 and 1)

      #-------------------------------------------------------------------------------------------------------------------------------------------
      # Horizontal Line Section
      self.top_horizontal_line_chr = "-"         # chr used to print the horizontal segment for the top line
      self.top_horizontal_line_on = True
      self.bottom_horizontal_line_chr="-"        # chr used to print the horizontal segment for the bottom line
      self.bottom_horizontal_line_on = True      # two values False and True (0 and 1)
      self.horizontal_line_chr = "-"             # chr used to print the horizontal segment horizontal. Only matrix list

      self.bold_horizontal_line = False          # two values False and True (0 and 1)
      self.bg_horizontal_line = -1               # values -1 to 255
      self.fg_horizontal_line = -1               # values -1 to 255
      #-------------------------------------------------------------------------------------------------------------------------------------------
      # Vertical Line Section    
      self.left_vertical_line_chr  = "|"         # used for the left vertical line only
      self.middle_vertical_line_chr = "|"         # all the vertical line in the middle between left and right. Only matrix
      self.right_vertical_line_chr = "|"         # used for the right vertical line only
    

      self.bold_vertical_line = False            # two values False and True (0 and 1)
      self.bg_vertical_line = -1                 # values -1 to 255
      self.fg_vertical_line = -1                 # values -1 to 255

      #-------------------------------------------------------------------------------------------------------------------------------------------
      # Corner Section 
      self.top_left_corner_chr = "+"             # chr for the top left corner
      self.top_right_corner_chr = "+"            # chr for the top right corner
      self.bottom_right_corner_chr="+"           # chr for the bottom right corner
      self.bottom_left_corner_chr="+"            # chr for the bottom left corner
      self.bold_corner_chr = False               # two values False and True (0 and 1)
      self.bg_corner_line = -1                   # values -1 to 255
      self.fg_corner_line = -1                   # values -1 to 255

      #-------------------------------------------------------------------------------------------------------------------------------------------
      # Corner Section
      self.middle_top_corner_chr =  "+"          # all the middle corners between top_left_corner_chr and top_right_corner_chr. Only matrix list
      self.middle_bottom_corner_chr = "+"        # all the middle corners between top_left_corner_chr and top_right_corner_chr. Only matrix list
      self.middle_inner_corner_chr =  "|"        # corner inside the matrix and sides but not top(left,right), or bottom(left, right). Only matrix list
      
      self.left_lateral_corner_chr =  "|"        # chr only for matrix list
      self.right_lateral_corner_chr = "|"        # chr only for matrix list    
      
      self.bold_inner_corner_chr = False         # two values False and True (0 and 1)
      self.bg_inner_corner_chr = -1              # values -1 to 255
      self.fg_inner_corner_chr = -1              # values -1 to 255

      #-------------------------------------------------------------------------------------------------------------------------------------------
      # Header Section  Only for Matrix List
      # attributes for the header text
      self.bold_header  = False                  # two values False and True (0 and 1)
      self.bg_header    = -1                     # values -1 to 255
      self.bg_all_cell_header = True             # how long will be the bg (all the cell or only the header)
      self.fg_header    = -1                     # values -1 to 255
      self.align_header = "justify"              # 4 values: justify(j),left(l), center(c), and right(r)

      self.italic_header    = False              # two values False and True (0 and 1)
      self.underline_header = False              # two values False and True (0 and 1)
      self.strike_header    = False              # two values False and True (0 and 1)
      self.blinking_header  = False              # two values False and True (0 and 1)
      self.dim_header       = False              # two values False and True (0 and 1)
      self.hidden_header    = False              # two values False and True (0 and 1)
      self.inverse_header   = False              # two values False and True (0 and 1)

      self.left_vertical_header_line_chr = "|"   # small_bullet u'\u2022'
      self.right_vertical_header_line_chr = "|"  # circle_bullet u'\u2B24'
      self.middle_vertical_header_line_chr = "|" # matrix list only

      self.bold_vertical_header_line_chr = False # two values False and True (0 and 1)
      self.bg_vertical_header_line_chr = -1      # values -1 to 255
      self.fg_vertical_header_line_chr = -1      # values -1 to 255

      #-------------------------------------------------------------------------------------------------------------------------------------------
      # Under Line Header Section  Only for Matrix List
      # attributes for the line below the header text
      self.horizontal_line_under_header_on = False     # horizontal line between headers and the firs data row. 1 shows it and 0 hides it
      self.horizontal_line_under_header_chr = "-"      # chr to be printed for theheader line
      self.bold_under_line_header = False              # values -1 to 255
      self.bg_under_line_header = -1                   # values -1 to 255
      self.fg_under_line_header = -1                   # values -1 to 255
      
      
      # attributes for the header corners (left, middles and right)    
      self.left_corner_under_line_header_chr = "+"     # only for header line
      self.right_corner_under_line_header_chr = "+"    # only for header line
      self.middle_corner_under_line_header_chr = "+"   # only for header line
      self.bold_corner_under_line_header = False       # two values False and True (0 and 1)
      self.bg_corner_under_line_header = -1            # values -1 to 255
      self.fg_corner_under_line_header = -1            # values -1 to 255


   #-----------------------------------------------------------------------------------------------------------------------------------------------
   #-----------------------------------------------------------------------------------------------------------------------------------------------
   # Defing a the main function to control the print of the list                                                                                  -
   #-----------------------------------------------------------------------------------------------------------------------------------------------    
   def print_fancy_format(self,data="none",style=Line_Style.CUSTOMIZED):
      if (style.lower() == Line_Style.CUSTOMIZED): pass
      else:
         # backup all the default values
         # Horizontal Line Section
         thlc = self.top_horizontal_line_chr;    bhlc = self.bottom_horizontal_line_chr;     hlc = self.horizontal_line_chr
         # Vertical Line Section    
         lvlc = self.left_vertical_line_chr;     mvlc = self.middle_vertical_line_chr;       rvlc = self.right_vertical_line_chr
         # Corner Section 
         tlcc = self.top_left_corner_chr;        trcc = self.top_right_corner_chr;           brcc = self.bottom_right_corner_chr
         blcc = self.bottom_left_corner_chr   
         #-------------------------------------------------------------------------------------------------------------------------------------------
         mtcc = self.middle_top_corner_chr;      mbcc = self.middle_bottom_corner_chr;       micc = self.middle_inner_corner_chr
         llcc = self.left_lateral_corner_chr;    rlcc = self.right_lateral_corner_chr
         # Header Section  Only for Matrix List         
         lvhlc = self.left_vertical_header_line_chr; rvhlc = self.right_vertical_header_line_chr; mvhlc = self.middle_vertical_header_line_chr
         # Under Line Header Section  Only for Matrix List
         hluhc = self.horizontal_line_under_header_chr                 
         # attributes for the header corners (left, middles and right)    
         lculhc = self.left_corner_under_line_header_chr; rculhc = self.right_corner_under_line_header_chr; mculhc = self.middle_corner_under_line_header_chr


         if (style.lower() == Line_Style.SINGLE):
            # Horizontal Line Section
            self.top_horizontal_line_chr = "\u2500";      self.bottom_horizontal_line_chr="\u2500";     self.horizontal_line_chr = "\u2500"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Vertical Line Section
            self.left_vertical_line_chr  = "\u2502";      self.middle_vertical_line_chr = "\u2502";     self.right_vertical_line_chr = "\u2502"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Outside Corner Section
            self.top_left_corner_chr = "\u250C";  self.top_right_corner_chr = "\u2510"; self.bottom_right_corner_chr="\u2518"; self.bottom_left_corner_chr="\u2514"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Middle Corner Section
            self.middle_top_corner_chr =  "\u252C";   self.middle_bottom_corner_chr = "\u2534"; self.middle_inner_corner_chr =  "\u253C"
            self.left_lateral_corner_chr =  "\u251C"; self.right_lateral_corner_chr = "\u2524"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Header Section  Only for Matrix List
            self.left_vertical_header_line_chr = "\u2502"; self.right_vertical_header_line_chr = "\u2502"; self.middle_vertical_header_line_chr = "\u2502"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Under Line Header Section  Only for Matrix List
            self.horizontal_line_under_header_chr = "\u2500";    self.left_corner_under_line_header_chr = "\u251C"
            self.right_corner_under_line_header_chr = "\u2524";  self.middle_corner_under_line_header_chr = "\u253C"
         
         elif (style.lower() == Line_Style.SINGLE_BOLD):
            # Horizontal Line Section
            self.top_horizontal_line_chr = "\u2501";      self.bottom_horizontal_line_chr="\u2501";     self.horizontal_line_chr = "\u2501"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Vertical Line Section
            self.left_vertical_line_chr  = "\u2503";      self.middle_vertical_line_chr = "\u2503";     self.right_vertical_line_chr = "\u2503"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Outside Corner Section
            self.top_left_corner_chr = "\u250F";  self.top_right_corner_chr = "\u2513"; self.bottom_right_corner_chr="\u251B"; self.bottom_left_corner_chr="\u2517"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Middle Corner Section
            self.middle_top_corner_chr =  "\u2533";   self.middle_bottom_corner_chr = "\u253B"; self.middle_inner_corner_chr =  "\u254B"
            self.left_lateral_corner_chr =  "\u2523"; self.right_lateral_corner_chr = "\u252B"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Header Section  Only for Matrix List
            self.left_vertical_header_line_chr = "\u2503"; self.right_vertical_header_line_chr = "\u2503"; self.middle_vertical_header_line_chr = "\u2503"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Under Line Header Section  Only for Matrix List
            self.horizontal_line_under_header_chr = "\u2501";    self.left_corner_under_line_header_chr = "\u2523"
            self.right_corner_under_line_header_chr = "\u252B";  self.middle_corner_under_line_header_chr = "\u254B"
 
         elif (style.lower() == Line_Style.SINGLE_HEAVY):
            # Horizontal Line Section
            self.top_horizontal_line_chr = "\u2586";      self.bottom_horizontal_line_chr="\u2586";     self.horizontal_line_chr = "\u2586"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Vertical Line Section
            self.left_vertical_line_chr  = "\u2588";      self.middle_vertical_line_chr = "\u2588";     self.right_vertical_line_chr = "\u2588"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Outside Corner Section
            self.top_left_corner_chr = "\u2586";  self.top_right_corner_chr = "\u2586"; self.bottom_right_corner_chr="\u2588"; self.bottom_left_corner_chr="\u2588"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Middle Corner Section
            self.middle_top_corner_chr =  "\u2586";   self.middle_bottom_corner_chr = "\u2588"; self.middle_inner_corner_chr =  "\u2588"
            self.left_lateral_corner_chr =  "\u2588"; self.right_lateral_corner_chr = "\u2588"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Header Section  Only for Matrix List
            self.left_vertical_header_line_chr = "\u2588"; self.right_vertical_header_line_chr = "\u2588"; self.middle_vertical_header_line_chr = "\u2588"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Under Line Header Section  Only for Matrix List
            self.horizontal_line_under_header_chr = "\u2586";    self.left_corner_under_line_header_chr = "\u2588"
            self.right_corner_under_line_header_chr = "\u2588";  self.middle_corner_under_line_header_chr = "\u2586"


         elif (style.lower() == Line_Style.DOUBLE):
            # Horizontal Line Section
            self.top_horizontal_line_chr = "\u2550";      self.bottom_horizontal_line_chr="\u2550";     self.horizontal_line_chr = "\u2550"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Vertical Line Section
            self.left_vertical_line_chr  = "\u2551";      self.middle_vertical_line_chr = "\u2551";     self.right_vertical_line_chr = "\u2551"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Outside Corner Section
            self.top_left_corner_chr = "\u2554";  self.top_right_corner_chr = "\u2557"; self.bottom_right_corner_chr="\u255D"; self.bottom_left_corner_chr="\u255A"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Middle Corner Section
            self.middle_top_corner_chr =  "\u2566";   self.middle_bottom_corner_chr = "\u2569"; self.middle_inner_corner_chr =  "\u256C"
            self.left_lateral_corner_chr =  "\u2560"; self.right_lateral_corner_chr = "\u2563"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Header Section  Only for Matrix List
            self.left_vertical_header_line_chr = "\u2551"; self.right_vertical_header_line_chr = "\u2551"; self.middle_vertical_header_line_chr = "\u2551"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Under Line Header Section  Only for Matrix List
            self.horizontal_line_under_header_chr = "\u2550";    self.left_corner_under_line_header_chr = "\u2560"
            self.right_corner_under_line_header_chr = "\u2563";  self.middle_corner_under_line_header_chr = "\u256C"

         elif (style.lower() == Line_Style.SQR_BRACKETS):
            # Horizontal Line Section
            self.top_horizontal_line_chr = " ";      self.bottom_horizontal_line_chr=" ";     self.horizontal_line_chr = " "
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Vertical Line Section
            self.left_vertical_line_chr  = "\u2502";      self.middle_vertical_line_chr = " ";     self.right_vertical_line_chr = "\u2502"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Outside Corner Section
            self.top_left_corner_chr = "\u250C";  self.top_right_corner_chr = "\u2510"; self.bottom_right_corner_chr="\u2518"; self.bottom_left_corner_chr="\u2514"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Middle Corner Section
            self.middle_top_corner_chr =  " ";   self.middle_bottom_corner_chr = " "; self.middle_inner_corner_chr =  " "
            self.left_lateral_corner_chr =  "\u2502"; self.right_lateral_corner_chr = "\u2502"
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Header Section  Only for Matrix List
            self.left_vertical_header_line_chr = "\u2502"; self.right_vertical_header_line_chr = "\u2502"; self.middle_vertical_header_line_chr = " "
            #-------------------------------------------------------------------------------------------------------------------------------------------
            # Under Line Header Section  Only for Matrix List
            self.horizontal_line_under_header_chr = " ";    self.left_corner_under_line_header_chr = "\u2502"
            self.right_corner_under_line_header_chr = "\u2502";  self.middle_corner_under_line_header_chr = " "

         elif (style.lower() == Line_Style.DASH):
            data_list = data2list(self,data)
            my_length = get_total_length(self, data_list)
            print(my_length)
   

         else: pass


      data_list = data2list(self, data)
      my_list = []
      # convert all elements in the list to strigs only because the int type will cause problems with len command    
      #-----------------------------------------------------------------------------------------------------------------------------------------
      list_type = get_list_type(data_list)
      
      #-----------------------------------------------------------------------------------------------------------------------------------------
      if list_type == "empty_list":                   # []
         data_list.append(" ")
         print_single_element(self,data_list)
         

      #-----------------------------------------------------------------------------------------------------------------------------------------
      elif list_type == "one_item_no_row":              # ["one"]
         my_list = [str(data_list[0])]
         print_single_element(self,my_list)
         
         if self.update_list == True and (isinstance (data, list)):     #  updte the list
            data_list[0] = str(data_list[0][0])
         
      #-----------------------------------------------------------------------------------------------------------------------------------------
      elif list_type == "one_item_one_row":             # [["one"]]
         my_list = [str(data_list[0][0])]
         print_single_element(self,my_list)
         
         if self.update_list == True and (isinstance (data, list)):     #  updte the list
            data_list[0] = str(data_list[0][0])

      #-----------------------------------------------------------------------------------------------------------------------------------------
      elif list_type == "multiple_items_one_row":       # [[1,2,3,4]]
         # we need to convert from one row many cols to many cols and no row
         # also convert the elements in my_list to string. all of them 
         for row in data_list:
            for n in row:
               my_list.append(str(n))        
     
         print_multiple_horizontal_items(self,my_list)

         # if we want to save the new list to into the old one as string
         if self.update_list == True and (isinstance (data, list)):
            data_list.clear()
            for n in my_list:          
               data_list.append(n)

        #---------------------------------------------------------------------------------------------------------------------------------------
      elif list_type == "multiple_items_no_row":        # [1,2,3,4]
         # also convert the elements in my_list to string. all of them
         for n in (data_list):
            my_list.append(str(n))

         print_multiple_horizontal_items(self,my_list)

         # if we want to save the new list to into the old one as string
         if self.update_list == True and (isinstance (data, list)):
            data_list.clear()
            for n in my_list:          
               data_list.append(n)

      # ----------------------------------------------------------------------------------------------------------------------------------------
      elif list_type == "mix_items":                    # [10,[50],[250],["H"],100]
                                                        # "C",["H","K","P","o"]]
         # also convert the elements in my_list to string. all of them
         for n in (data_list):
            my_list.append(str(n))

         print_multiple_horizontal_items(self,my_list)

         # if we want to save the new list to into the old one as string
         if self.update_list == True and (isinstance (data, list)):
            data_list.clear()
            for n in my_list:          
               data_list.append(n)

      # ----------------------------------------------------------------------------------------------------------------------------------------
      elif list_type == "multiple_items_multiple_rows":  # [[7,6],[5,4],[1,2,3]] or [[2],[3],[5]]
         # converting the data_list to string any single element into my_list
         # save the new matrix my_list and now we need to complete the matrix if necessary
         tempo_list1 = []; tempo_list2 = []
         for row in data_list:
            for col in row:
               tempo_list1.append(str(col))
            tempo_list2.append(tempo_list1)
            tempo_list1 = []

         my_list = complete_info_list(self,tempo_list2)  # make it complete
         #print(my_list)
         print_matrix_list(self,my_list)

           # if we want to save the new list to into the old one as string
         if self.update_list == True and (isinstance (data, list)):
            data_list.clear()
            for n in my_list:          
               data_list.append(n)

      # ----------------------------------------------------------------------------------------------------------------------------------------          
      else:
         print(list_type+": ",data_list) 

      if (style == Line_Style.CUSTOMIZED): pass
      else:
         # putting back all the default values
         # Horizontal Line Section
         self.top_horizontal_line_chr = thlc;    self.bottom_horizontal_line_chr = bhlc;     self.horizontal_line_chr = hlc
         # Vertical Line Section    
         self.left_vertical_line_chr = lvlc;     self.middle_vertical_line_chr = mvlc;       self.right_vertical_line_chr = rvlc
         # Corner Section 
         self.top_left_corner_chr = tlcc;        self.top_right_corner_chr = trcc;           self.bottom_right_corner_chr = brcc 
         self.bottom_left_corner_chr = blcc
         #-------------------------------------------------------------------------------------------------------------------------------------------
         self.middle_top_corner_chr = mtcc;      self.middle_bottom_corner_chr = mbcc;       self.middle_inner_corner_chr = micc
         self.left_lateral_corner_chr = llcc;    self.right_lateral_corner_chr = rlcc
         # Header Section  Only for Matrix List         
         self.left_vertical_header_line_chr = lvhlc; self.right_vertical_header_line_chr = rvhlc; self.middle_vertical_header_line_chr = mvhlc
         # Under Line Header Section  Only for Matrix List
         self.horizontal_line_under_header_chr = hluhc
         # attributes for the header corners (left, middles and right)    
         self.left_corner_under_line_header_chr = lculhc; self.right_corner_under_line_header_chr = rculhc
         self.middle_corner_under_line_header_chr = mculhc



#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Cursor Class. Manipulate Cursor Around The Terminal                                                                                          -
#-----------------------------------------------------------------------------------------------------------------------------------------------
class Cursor():   
   def jumpTo(self,qty=0, direction=Move.DOWN):
      '''
   ----------------------------------------------------------------------------
      Moves the cursor n position to the Direction Specified
   ----------------------------------------------------------------------------
      '''
      print(Cursor.moveTo(self, qty, direction),end="")


   def moveTo(self,qty=0, direction=Move.DOWN):
      '''
   ----------------------------------------------------------------------------
      Moves the cursor n position to the Direction Specified
   ----------------------------------------------------------------------------
      '''
      if   direction == Move.UP    :  movement = f"\033[{str(qty)}A"
      elif direction == Move.DOWN  :  movement = f"\033[{str(qty)}B"
      elif direction == Move.RIGHT :  movement = f"\033[{str(qty)}C"
      elif direction == Move.LEFT  :  movement = f"\033[{str(qty)}D"
      else:                           movement = ""
      return movement


   def jumpxy(self,x=0,y=0):
      '''
   ----------------------------------------------------------------------------
      This function moves the cursor to a specific position (x,y)
   ----------------------------------------------------------------------------
      '''
      print(Cursor.moveTo(self, y, x),end="")

   
   def movexy(self,x=0, y=0):
      '''
   ----------------------------------------------------------------------------
      Moves the cursor to a specific position (x, y)
   ----------------------------------------------------------------------------
      '''
      if (y<=-1 or x<=-1):
         posi = ""
      else:
         posi = f"\033[{str(y)};{str(x)}H"
      
      return posi
   
   

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Font Style Class. Manipulate Font In The Terminal                                                                                            -
#-----------------------------------------------------------------------------------------------------------------------------------------------
# ansi codes 
# reset_all : "\033[0m"         Terminal_Bell : "\a"              
# bold_on   : "\033[1m"         underline_on  : "\033[4m"         hidden_on    : "\033[8m"
# bold_off  : "\033[22m"        underline_off : "\033[24m"        hidden_off   : "\033[28m"
# dim_on    : "\033[2m"         blinking_on   : "\033[5m"         strike_on    : "\033[9m"
# dim_off   : "\033[22m"        blinking_off  : "\033[25m"        strike_off   : "\033[29m"
# italic_on : "\033[3m"         reverse_on    : "\033[7m"         background   : "\033[48;5;{str(bg)}m"
# italic_off: "\033[23m"        reverse_off   : "\033[27m"        foreground   : "\033[38;5;{str(fg)}m"
# backspace : "\b"              horizontal tab: "\t"              vertical tab : "\v"

class FontStyle():   
   def __init__(self):
      self.bg = -1
      self.fg = -1
      self.bold  = False      
      self.dim   = False
      self.italic= False
      self.underline = False
      self.blinking  = False
      self.inverse   = False
      self.hidden = False
      self.strike    = False
      self.indent    = 0
      self.next_line = True

      
   def set_font(self)->str:
      '''
   --------------------------"Cursor","FontStyle","FancyMessage","FancyFormat"--------------------------------------------------
   Explanation update needed here
         import fancyprint as fp

      fs = fp.FontStyle()

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
      if self.bg < 0 or self.bg > 255:
         bgc = "reset"
      else:
         bgc = str(self.bg)

      if self.fg < 0 or self.fg > 255:
         fgc = "reset"
      else:
         fgc = str(self.fg)


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
      

      if   (self.bold == True and self.dim == False): settings = settings + "\033[1m"
      elif (self.bold == True and self.dim == True):  settings = settings + "\033[1m"
      elif (self.bold == False and self.dim == True): settings = settings + "\033[2m"
      else: # (bold == False and dim == False): 
         pass
         
      if (self.italic == True):    settings = settings + "\033[3m"
      else:                        settings =  settings + "\033[23m"

      if (self.underline == True): settings = settings + "\033[4m"
      else:                        settings = settings + "\033[24m"

      if (self.blinking == True):  settings = settings + "\033[5m"
      else:                        settings = settings + "\033[25m"

      if (self.inverse == True):   settings = settings + "\033[7m"
      else:                        settings = settings + "\033[27m"

      if (self.hidden == True):    settings = settings + "\033[8m"
      else:                        settings = settings + "\033[28m"

      if (self.strike == True):    settings = settings + "\033[9m"
      else:                        settings = settings + "\033[29m"
      

      if self.indent <= 0: pass
      else: settings = settings + f"\033[{str(self.indent)}C"

      return settings
   
   def print_style(self, msg)->None:
      settings = self.set_font()
      if self.next_line   == True:  print(settings+str(msg)+"\033[0m")
      elif self.next_line == False: print(settings+str(msg)+"\033[0m",end="")
      else:
         print(settings+str(msg)+"\033[0m")

   def get_style(self)->str:   return self.set_font()

   def reset_style(self)->str: return "\033[0m"

   

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Font Customize Class for Fancy Message Class                                                                                                 -
#-----------------------------------------------------------------------------------------------------------------------------------------------
# pending this class
class FontCustomization():
   def __init__(self):
      self.bg = 4
      self.fg = 231
      self.bold   = False      
      self.dim    = False
      self.italic = False
      self.underline = False
      self.blinking  = False
      self.inverse   = False
      self.hidden = False
      self.strike = False

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Fancy Message Class (Single line or a Paragraph Text in the Terminal)                                                                        -
#-----------------------------------------------------------------------------------------------------------------------------------------------
#class FancyMessage(FontCustomization):
#class FancyMessage():
class FancyMessage(Cursor):
   font_customization = FontCustomization()
   def __init__(self,obj=font_customization):
      super().__init__()       # Super Class to use all (vars and funs) from Cursor Class
                               # with the Initialization Draw Class(self), ex. self.gotoxy(x,y)
      self.bg        = obj.bg;          self.underline = obj.underline   # 4         False
      self.fg        = obj.fg;          self.blinking  = obj.blinking    # 231       False
      self.bold      = obj.bold;        self.inverse   = obj.inverse     # False     False
      self.dim       = obj.dim;         self.hidden    = obj.hidden;     # False     False
      self.italic    = obj.italic;      self.strike    = obj.strike      # False     False
            
      self.left_indent = 2;             self.right_indent = 2
      self.top_lines = 1;               self.bottom_lines = 1

      self.length = Length_bg.ALL_ROW     
      self.adj_bg_lines_to_right_indent = False     # True or False
      self.adj_bg_msg_to_space_available = False    # False, True or None
      #--------------------------------------------------------------------
      # here will go all the variables for the print_fancy_note
      self.align_note = Align.JUSTIFY;   self.help_lines = False;          self.position_note = 1 
      self.bg_note = 231;                self.fg_note = 0;                 self.bold_note  = 1
      self.dim_note = False;             self.italic_note = False;         self.underline_note = False
      self.blinking_note = False;        self.inverse_note = False;        self.hidden_note = False
      self.strike_note = False;          self.left_space_note = 2;         self.right_space_note = 2
      
      # here will go all the variables for the print_fancy_Message_letter
      self.align_title = Align.LEFT;  self.title_indent = 2 # title_indent works with Align.JUSTIFY
      self.lines_title_body = 1;         self.strike_title = False
      self.bg_title = 231;               self.fg_title = 0;                self.bold_title  = 1
      self.dim_title = False;            self.italic_title = False;        self.underline_title = False
      self.blinking_title = False;       self.inverse_title = False;       self.hidden_title = False
      
       
      self.align_footnote = Align.RIGHT;  self.footnote_indent = 2 # footnote_indent works with Align.JUSTIFY
      self.lines_body_footnote = 1;       self.strike_footnote = False
      self.bg_footnote = 231;             self.fg_footnote = 0;            self.bold_footnote  = 1
      self.dim_footnote = False;          self.italic_footnote = False;    self.underline_footnote = False
      self.blinking_footnote = False;     self.inverse_footnote = False;   self.hidden_footnote = False
      

   def get_msg_attribute(self,data:str="Message",all_attribute:bool=False):
      msg = str(data)
      # def set_font(bold=False,bg=-1,fg=-1,italic=False,underline=False,strike=False,blinking=False,dim=False,hidden=False,inverse=False):      
      # color = set_font(self.bold, self.bg, self.fg,self.italic,self.underline,self.strike,self.blinking,self.dim,self.hidden,self.inverse)
      # color2= set_font(bg=self.bg, fg=self.fg, inverse=self.inverse)
      tncols, tnrows = os.get_terminal_size()
      space_available = tncols - self.left_indent - self.right_indent
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
      if (all_attribute == True):
         return tncols, space_available, number_letter_line_list, adj_diff_space, new_msg, len(number_letter_line_list)
      else:
         return len(number_letter_line_list), space_available, tncols
      
   #---------------------------------------------------------------------------------------------------------------------------------------------------
   def print_fancy_msg(self,data="Message"):
      def print_bg_lines(lines, bg_format_line_color="\0m"):
         n = lines
         while n>0:
            print(bg_format_line_color)
            n -= 1

      tncols, space_available, number_letter_line_list, adj_diff_space, new_msg, n_lines = FancyMessage.get_msg_attribute(self,data,True)
      color = set_font(self.bold, self.bg, self.fg,self.italic,self.underline,self.strike,self.blinking,self.dim,self.hidden,self.inverse)
      color2= set_font(bg=self.bg, fg=self.fg, inverse=self.inverse)

      # from here we need: tncols, space_available, number_letter_line_list, adj_diff_space, new_msg

      
      longest_line = max(number_letter_line_list)
      # self.adj_bg_lines_to_right_indent by default = False
      # self.adj_bg_msg_to_space_available by default = False
      if (self.length == Length_bg.ALL_ROW):
         bg_format_line_color = f"{color2}{ins_space(tncols)}{reset_font()}"
         start_line = f"{color2}{ins_space(self.left_indent)}" # change color for color2 to delete at the beginning the strike, and/or underline option(s)

      elif (self.length == Length_bg.ONLY_WORD):         
         if (self.adj_bg_lines_to_right_indent == True):    bg_format_line_color = f"{color2}{move_right(self.left_indent)}{ins_space(space_available)}{reset_font()}"  # change color for color2
         elif (self.adj_bg_lines_to_right_indent == False): bg_format_line_color = f"{move_right(self.left_indent)}{color2}{ins_space(longest_line)}{reset_font()}"     # change color for color2
         start_line = f"{move_right(self.left_indent)}{color2}" # change color for color2

      else: pass

      carry = 0; last_one = n_lines - 1
      print_bg_lines(self.top_lines, bg_format_line_color) # bg_line
      

      print(start_line,end="")
      
      # start printing the message
      for nl in range(n_lines):
         for n in range(number_letter_line_list[nl]):
            print(f"{color}{new_msg[carry+n]}",end="")       # added color because the color2 can be slightly different

         carry += number_letter_line_list[nl]

         if (self.length == Length_bg.ALL_ROW):
            for n in range(adj_diff_space[nl]+self.right_indent):
               print(color2+" ",end="")                        # to delete at the end the strike, and/or underline option(s)

         elif (self.length == Length_bg.ONLY_WORD):
            if (self.adj_bg_msg_to_space_available == True):    
               for n in range(space_available -  number_letter_line_list[nl]):
                  print(color2+" ",end="")              # to delete the strike we add color2
            elif (self.adj_bg_msg_to_space_available == False):
               for n in range(longest_line-number_letter_line_list[nl]):
                  print(color2+" ",end="")
            elif (self.adj_bg_msg_to_space_available == None): pass

            print(f"{reset_font()}",end="")
         else:
            pass

         print()
         if (last_one == nl): pass
         else:                print(start_line,end="")
      # end printing the message
      print_bg_lines(self.bottom_lines, bg_format_line_color) # bg_line

   #---------------------------------------------------------------------------------------------------------------------------------------------------
   def print_fancy_note(self, note_msg:str="Warning", body_msg:str="Paragraph Body")->None:
      # save original values
      li_obj = self.left_indent
      # settings for the body_msg
      if (note_msg == None): len_note_msg = 0; note_msg = ""
      else: len_note_msg = len(note_msg)

      self.left_indent = self.left_space_note + len_note_msg + self.right_space_note
      n_lines, space_available, tncols = self.get_msg_attribute(body_msg)

      self.print_fancy_msg(body_msg)

      total_back_lines = self.top_lines + n_lines + self.bottom_lines # (2+8+2) = 12
      if   (self.position_note >= (total_back_lines)): lines_back = 0
      elif (self.position_note <= 0):                  lines_back = total_back_lines
      else:                                            lines_back = total_back_lines - self.position_note 

      # settings for the note
      settings_note = set_font(bold=self.bold_note, bg=self.bg_note, fg=self.fg_note, italic=self.italic_note, underline=self.underline_note,\
                               strike=self.strike_note, blinking=self.blinking_note, dim=self.dim_note, hidden=self.hidden_note, inverse=self.inverse_note)
      if (self.align_note == Align.LEFT or self.align_note == "l"):
         print(f"{self.moveTo(qty=lines_back, direction=Move.UP)}{settings_note}{note_msg}",end="")

      elif (self.align_note == Align.CENTER or self.align_note == "c"):
         myq = int((self.left_space_note+self.right_space_note)/2)
         print(f"{self.moveTo(qty=lines_back, direction=Move.UP)}{self.moveTo(qty=myq,direction=Move.RIGHT)}{settings_note}{note_msg}",end="")
                
      elif (self.align_note == Align.RIGHT or self.align_note == "r"):
         myq = self.left_space_note + self.right_space_note
         print(f"{self.moveTo(qty=lines_back, direction=Move.UP)}{self.moveTo(qty=myq,direction=Move.RIGHT)}{settings_note}{note_msg}",end="")
      
      else:  # JUSTIFY
         print(f"{self.moveTo(qty=lines_back, direction=Move.UP)}{self.moveTo(qty=self.left_space_note,direction=Move.RIGHT)}{settings_note}{note_msg}")         
      
      self.jumpTo(qty=lines_back-1, direction=Move.DOWN)
      print(f"{reset_font()}",end="")

      # putting back original values
      self.left_indent = li_obj
      # n_lines, space_available, tncols are variables for reference to calculate the message      
      if (self.help_lines == True):
         print(f"{ins_space(self.left_indent)}Body_Lines:{n_lines}  Space_Available:{space_available}  N.Cols: {tncols}  N.Lines:{total_back_lines}")
         
      
   #---------------------------------------------------------------------------------------------------------------------------------------------------   
   def print_fancy_header(self, title_msg:str=None, body_msg:str="Paragraph Body",footnote_msg:str=None)->None:
      # save original values
      li_obj = self.left_indent;      bl_obj = self.bottom_lines;  
      tl_obj = self.top_lines
      bg_obj      = self.bg;          underline_ojb = self.underline  # 4         False
      fg_obj      = self.fg;          blinking_obj  = self.blinking   # 231       False
      bold_obj    = self.bold;        inverse_obj   = self.inverse    # False     False
      dim_obj     = self.dim;         hidden_obj    = self.hidden     # False     False
      italic_obj  = self.italic;      strike_obj    = self.strike     # False     False
      
      # settings for title
      n_lines, space_available, tncols = self.get_msg_attribute(body_msg)
      if title_msg != None:
         # working with the font color         
         self.bg     = self.bg_title;          self.underline = self.underline_title   # 4         False
         self.fg     = self.fg_title;          self.blinking  = self.blinking_title    # 231       False
         self.bold   = self.bold_title;        self.inverse   = self.inverse_title     # False     False
         self.dim    = self.dim_title;         self.hidden    = self.hidden_title;     # False     False
         self.italic = self.italic_title;      self.strike    = self.strike_title      # False     False
         
         if   (self.align_title == Align.LEFT or self.align_title == "l"):
            pass
         elif (self.align_title == Align.CENTER or self.align_title == "c"):
            self.left_indent = int((self.left_indent + space_available - len(title_msg))/2)
         elif (self.align_title == Align.RIGHT or self.align_title == "r"):
            self.left_indent = self.left_indent + space_available - len(title_msg) - 1 # 1 for not jumping line and finished
         else:
            self.left_indent = self.title_indent # JUSTIFY                             # at the ending of right indent

         self.bottom_lines = self.lines_title_body
         self.print_fancy_msg(title_msg)
         # settings for body (we recovered left_indent, and change bottom_lines and change top_lines)               
         
         if (footnote_msg != None): self.bottom_lines = 0 # self.lines_body_footnote
         else:                      self.bottom_lines = bl_obj
         self.left_indent = li_obj
         self.bg     = bg_obj;          self.underline = underline_ojb   # 4         False
         self.fg     = fg_obj;          self.blinking  = blinking_obj    # 231       False
         self.bold   = bold_obj;        self.inverse   = inverse_obj     # False     False
         self.dim    = dim_obj;         self.hidden    = hidden_obj;     # False     False
         self.italic = italic_obj;      self.strike    = strike_obj      # False     False

         if (title_msg != None): self.top_lines = 0
         else:                   self.top_lines = tl_obj   
         self.fg = fg_obj  # returning the color for the body
         self.print_fancy_msg(body_msg)
               
      else:         
         if (footnote_msg !=None): self.bottom_lines = self.lines_body_footnote
         else:                     self.bottom_lines = bl_obj
         self.print_fancy_msg(body_msg)      
      
      if (footnote_msg != None):

         # settings for footnote (recovered bottom_lines and change top_lines)
         if   (self.align_footnote == Align.LEFT or self.align_footnote == "l"):
            pass         
         elif (self.align_footnote == Align.CENTER or self.align_footnote == "c"):
            self.left_indent = int((self.left_indent + space_available - len(footnote_msg))/2)
         elif (self.align_footnote == Align.RIGHT or self.align_footnote == "r"):
            self.left_indent = self.left_indent + space_available - len(footnote_msg) - 1 # 1 for not jumping line and finished
         else:
            self.left_indent = self.footnote_indent # JUSTIFY                             # at the ending of right indent

         self.top_lines = self.lines_body_footnote
         self.bottom_lines = bl_obj
         self.bg     = self.bg_footnote;          self.underline = self.underline_footnote   # 4         False
         self.fg     = self.fg_footnote;          self.blinking  = self.blinking_footnote    # 231       False
         self.bold   = self.bold_footnote;        self.inverse   = self.inverse_footnote     # False     False
         self.dim    = self.dim_footnote;         self.hidden    = self.hidden_footnote;     # False     False
         self.italic = self.italic_footnote;      self.strike    = self.strike_footnote      # False     False
         self.print_fancy_msg(footnote_msg)

      else:
         pass


      # putting back original values
      self.top_lines = tl_obj;       self.left_indent = li_obj;       #  self.bottom_lines = bl_obj
      self.bg     = bg_obj;          self.underline = underline_ojb   # 4         False
      self.fg     = fg_obj;          self.blinking  = blinking_obj    # 231       False
      self.bold   = bold_obj;        self.inverse   = inverse_obj     # False     False
      self.dim    = dim_obj;         self.hidden    = hidden_obj;     # False     False
      self.italic = italic_obj;      self.strike    = strike_obj      # False     False
      # n_lines, space_available, tncols are variables for reference to calculate the message      
      if (self.help_lines == True):
         print(f"{ins_space(self.left_indent)}Body_Lines:{n_lines}  Space_Available:{space_available}  N.Cols: {tncols}")

   
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Class Draw Pictures Around The Terminal                                                                                                      -
#-----------------------------------------------------------------------------------------------------------------------------------------------
class Draw(Cursor):            # Inheritance the Cursor Class here.   
   def __init__(self):         # Initializing Draw Class as self
      super().__init__()       # Super Class to use all (vars and funs) from Cursor Class
                               # with the Initialization Draw Class(self), ex. self.gotoxy(x,y)
      # square or rectangle
      # Horizontal Line Section
      self.top_horizontal_line_chr="-";  self.bottom_horizontal_line_chr="-"
      # Vertical Line Section    
      self.left_vertical_line_chr="|";   self.right_vertical_line_chr="|"
      # Corner Section 
      self.top_left_corner_chr="+";      self.top_right_corner_chr="+";       self.bottom_right_corner_chr="+";  self.bottom_left_corner_chr="+"     
      # Corner General 
      self.adj_height = 2
      self.adj_width  = 2
      self.bold_draw_chr = False               # two values False and True (0 and 1)
      self.bg_draw_line = -1                   # values -1 to 255
      self.fg_draw_line = -1                   # values -1 to 255

      # arrow and line
      self.tail_chr = "\u2223"#"\u27DD" # "\u251C"
      self.body_chr = "\u2014"
      self.head_chr = "\u2AAB" # "\u27A4" #"\u2A65" 279D

      self.body_length = 2

      # general
      self.adj_indent = 12                     # space from the terminal to the box
      
      
   def arrow(self,body_length=2, direction=Move.RIGHT):
      self.jumpTo(self.adj_indent, Move.RIGHT)
      print(self.tail_chr,end="")
      
      
      for n in range(self.body_length):
         print(self.body_chr,end="")

      print(self.head_chr)




   def line(self,x:int=-1,y:int=-1,size:int=1, layout:Layout=Layout.HORIZONTAL)->None:
      if (layout.lower() == Layout.HORIZONTAL):
         if (x == -1 and y == -1):
            pass
         elif (x <= -1 and y >= 0):
            self.gotoxy(0,y)
         elif (x >= 0 and y <= -1):
            self.gotoxy(x,0)
         else:
            self.gotoxy(x,y)
         
         print(self.tail,end="")

         for n in range(size):
            print(self.body,end="")
            
         print(self.head,end="")

      elif (layout.lower() == Layout.VERTICAL):
         for n in range(size):
            self.gotoxy(x,y)
            print(self.body)
            y += 1
      else:
         return

# if we are going to use this script as only module, delete this code
if (__name__ == "__main__"):
  fg_ansi_colors()
  bg_ansi_colors()