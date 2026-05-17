# import time

# from custom_print.fancy_functions import ins_chr
# from custom_print.fancy_functions import set_font
# from custom_print.pylo import PyLO

# import custom_print.Alpha_Letters as AL
# import custom_print.Doh_Letters as DL


# # +------------------------------------------------------------------------------------------------------------------------------------+
# # |  Creating the Ascii Word                                                                                                           |
# # |  --------------------------------------------------------------------------------------------------------------------------------  |
# # +------------------------------------------------------------------------------------------------------------------------------------+
# class Art:
#     def __init__(self):
#         self.bold     = True
#         self.bold     = False;    self.bg = -1;              self.fg = -1
#         self.italic   = False;    self.underline = False;    self.strike = False
#         self.blinking = False;    self.dim = False;          self.hidden = False
#         self.inverse  = False
              
#         self.adj_indent = 0;      self.adj_space  = 0;       self.delay_ms   = 0
#         self.set_layout = "vertical"
#         self.set_top_line    = False
#         self.set_bottom_line = False
        

#     def print_ascii_art(self, word_list=["P","Y"], self.ascii_type="Doh"):
#         # Defining variables
#         rows = 0;           result = [];   copy_word_list = []
#         tempo_row = "";     retardo = self.delay_ms/1000
#         key_letter = "";    skip_top_row = self.set_top_line
#         color = set_font(self.bold, self.bg, self.fg, self.italic, self.underline, self.strike,
#                         self.blinking, self.dim, self.hidden, self.inverse)


#         # Creating the copy list (deep copy)
#         for i in word_list:
#             copy_word_list.append(i)

#         pylo = PyLO()
#         # -------------------------------------------------------- Finding the Type of Ascii Letters
#         if self.ascii_type == "Alpha":
#             # this only have uppercase available
#             rows = AL.height
#             key_letter = "AL."
#             result = pylo.update_case(data=copy_word_list, header_case=pylo.Case.UPPER, data_case=pylo.Case.UPPER, update=True)
#             # print(copy_word_list)
#             # print(result)
#             # we convert the copy_word_list to all capital

#         elif self.ascii_type == "Doh":
#             rows = DL.height
#             key_letter = "DL."

#         elif self.ascii_type == "Big":
#             rows = AL.height
#         else:                 pass
#         # -------------------------------------------------------- Ending Finding the Type of Ascii Letters
      
#         #--------------------------------------------------------- Making the list result in vertical form
#         if self.set_layout == "vertical":
#             if self.set_bottom_line == False: rows = rows - 1
#             for r in range(rows):
#                 if skip_top_row == False: pass
#                 else:
#                     for l in range(len(copy_word_list)):
#                         try:
#                             row_info = key_letter + self.ascii_type + "_" + copy_word_list[l] + "[" + str(r) + "]"
#                             tempo_row = tempo_row + eval(row_info) + ins_chr(self.adj_space)
#                         except:
#                             pass
#                             row_info = key_letter + self.ascii_type + "_NA" + "[" + str(r) + "]"
#                             tempo_row = tempo_row + eval(row_info) + ins_chr(self.adj_space)

#                 if skip_top_row == False: skip_top_row = True
#                 else:
#                     result.append([f"{ins_chr(self.adj_indent)}{color}{ins_chr(self.adj_space)}{tempo_row}\033[0m"])
#                 tempo_row = ""

#             # +-------------------------------------------------------------------------------------+
#             # | Printing the ASCII Letters in vertical form                                         |
#             # +-------------------------------------------------------------------------------------+
#             for row in result:
#                 for col in row:
#                     time.sleep(retardo); print(col)

#         #--------------------------------------------------------- Making the list result in horizontal form
#         elif self.set_layout == "horizontal":
#             move_up = rows
#             move_right = self.adj_indent

#             if self.set_bottom_line == False:
#                 rows    -= 1
#                 move_up -= 1 
#             if self.set_top_line == False:
#                 move_up -= 1


#             for w in range(len(copy_word_list)):
#                 try:    list_letter = eval(key_letter + self.ascii_type + "_" + copy_word_list[w])
#                 except: list_letter = eval(key_letter + self.ascii_type + "_" + "NA")

#                 for r in range(rows):
#                     if skip_top_row == False: skip_top_row = True
#                     else:
#                         print(f"\033[{str(move_right-1)}C{color}{ins_chr(self.adj_space)}{list_letter[r]}{ins_chr(self.adj_space)}\033[0m")


#                 move_right = move_right + len(list_letter[0]) + self.adj_space


#                 print(f"\033[{str(move_up)}A",end="")
#                 skip_top_row = self.set_top_line
#                 time.sleep(retardo)
#             print(f"\033[{rows}B",end="")
            

#         else:
#             result.append(["Error Layout"])
#             # +-------------------------------------------------------------------------------------+
#             # | Printing the ASCII Letters in Horizontal form                                       |
#             # +-------------------------------------------------------------------------------------+
#             for row in result:
#                 for col in row:
#                     time.sleep(retardo); print(self.adj_indent+col)




import time

from custom_print.fancy_functions import ins_chr
from custom_print.fancy_functions import move_cursor_right
from custom_print.fancy_functions import set_font

import custom_print.Alpha_Letters as AL
import custom_print.Doh_Letters as DL


# +------------------------------------------------------------------------------------------------------------------------------------+
# |  Creating the Ascii Word                                                                                                           |
# |  --------------------------------------------------------------------------------------------------------------------------------  |
# +------------------------------------------------------------------------------------------------------------------------------------+
class Art:
    def __init__(self):
        self.bold     = True
        self.bold     = False;        self.bg = -1;              self.fg = -1
        self.italic   = False;        self.underline = False;    self.strike = False
        self.blinking = False;        self.dim = False;          self.hidden = False
        self.inverse  = False;        self.ascii_type="Doh"
              
        self.adj_indent = 0;          self.adj_space  = 0;       self.delay_ms   = 0
        self.set_layout = "vertical"; self.set_top_line = False; self.set_bottom_line = False; 

        self.adj_left_space = 0;      self.adj_middle_space = 0; self.adj_right_space = 0
        

    def print_ascii_art(self, msg="AB"):
        # Defining variables
        rows = 0;                        result = []
        tempo_row = "";                  retardo = self.delay_ms/1000
        key_letter = "";                 skip_top_row = self.set_top_line
        left_sp = self.adj_left_space;   middle_sp = self.adj_middle_space
        right_sp = self.adj_right_space
        
        color = set_font(self.bold, self.bg, self.fg, self.italic, self.underline, self.strike,
                        self.blinking, self.dim, self.hidden, self.inverse)
        
        data = msg
        # -------------------------------------------------------- Finding the Type of Ascii Letters
        if self.ascii_type == "Alpha":
            # this only have uppercase available
            rows = AL.height
            key_letter = "AL."
            data = msg.upper()
            

        elif self.ascii_type == "Doh":
            rows = DL.height
            key_letter = "DL."

        elif self.ascii_type == "Big":
            rows = AL.height
        else:                 pass
        # -------------------------------------------------------- Ending Finding the Type of Ascii Letters
      
        #--------------------------------------------------------- Making the list result in vertical form
        if self.set_layout == "vertical":
            if len(data) == 1: middle_sp = left_sp
            else:              pass

            if self.set_bottom_line == False: rows = rows - 1
            for r in range(rows):
                if skip_top_row == False: pass
                else:
                    for l in range(len(data)):
                        try:
                            if data[l] == " ": row_info = key_letter + self.ascii_type + "_space" + "[" + str(r) + "]"
                            else:              row_info = key_letter + self.ascii_type + "_" + data[l] + "[" + str(r) + "]"

                            if l == (len(data)-1):
                                tempo_row = tempo_row + ins_chr(middle_sp) + eval(row_info) + ins_chr(right_sp)   # last item
                            elif l >= 1:
                                tempo_row = tempo_row + ins_chr(middle_sp) + eval(row_info) #+ ins_chr(middle_sp) # middle items
                            else:
                                tempo_row = tempo_row + ins_chr(left_sp) + eval(row_info) #+ ins_chr(middle_sp)   # first item
                        
                        except:
                            row_info = key_letter + self.ascii_type + "_NA" + "[" + str(r) + "]"
                            if l == (len(data)-1):
                                tempo_row = tempo_row + ins_chr(middle_sp) + eval(row_info) + ins_chr(right_sp)   # last item
                            elif l >= 1:
                                tempo_row = tempo_row + ins_chr(middle_sp) + eval(row_info) #+ ins_chr(middle_sp) # middle items
                            else:
                                tempo_row = tempo_row + ins_chr(left_sp) + eval(row_info) #+ ins_chr(middle_sp)   # first item

                if skip_top_row == False: skip_top_row = True
                else:
                    # result.append([f"{ins_chr(self.adj_indent)}{color}{tempo_row}\033[0m"])
                    result.append([f"{move_cursor_right(self.adj_indent)}{color}{tempo_row}\033[0m"])
                tempo_row = ""

            # +-------------------------------------------------------------------------------------+
            # | Printing the ASCII Letters in vertical form                                         |
            # +-------------------------------------------------------------------------------------+
            for row in result:
                for col in row:
                    time.sleep(retardo); print(col)

        #--------------------------------------------------------- Making the list result in horizontal form
        elif self.set_layout == "horizontal":
            # left_sp = self.adj_left_space; middle_sp = self.adj_middle_space; right_sp = self.adj_right_space
            if len(data) == 1: middle_sp = left_sp
            else:              pass

            move_up = rows
            move_right = self.adj_indent

            if self.set_bottom_line == False:
                rows    -= 1
                move_up -= 1 
            if self.set_top_line == False:
                move_up -= 1


            for w in range(len(data)):
                try:    
                    if data[w] == " ":
                        list_letter = eval(key_letter + self.ascii_type + "_space")
                    else:
                        list_letter = eval(key_letter + self.ascii_type + "_" + data[w])    
                except: list_letter = eval(key_letter + self.ascii_type + "_" + "NA")

                for r in range(rows):
                    if skip_top_row == False: skip_top_row = True
                    else:
                        if (len(data)) == 1:
                            print(f"{move_cursor_right(self.adj_indent)}{color}{ins_chr(left_sp)}{list_letter[r]}{ins_chr(right_sp)}\033[0m")  # first item
                        else:
                            if w == 0:               print(f"{move_cursor_right(self.adj_indent)}{color}{ins_chr(left_sp)}{list_letter[r]}{ins_chr(middle_sp)}\033[0m")  # first item
                            elif w == (len(data)-1): print(f"{color}\033[{str(move_right)}C{list_letter[r]}{ins_chr(right_sp)}\033[0m")                        # last item
                            else:                    print(f"{color}\033[{str(move_right)}C{list_letter[r]}{ins_chr(middle_sp)}\033[0m")                       # middle items# w >= 1:
                   
                if w == 0: move_right = move_right + left_sp + len(list_letter[0]) + middle_sp  # first item
                else:      move_right = move_right + len(list_letter[0]) + middle_sp            # middle item

                print(f"\033[{str(move_up)}A",end="")
                skip_top_row = self.set_top_line
                time.sleep(retardo)
            print(f"\033[{rows}B",end="")
            

        else:
            result.append(["Error Layout"])
            # +-------------------------------------------------------------------------------------+
            # | Printing the ASCII Letters in Horizontal form                                       |
            # +-------------------------------------------------------------------------------------+
            for row in result:
                for col in row:
                    time.sleep(retardo); print(self.adj_indent+col)
