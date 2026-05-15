import time

from custom_print.fancy_functions import ins_chr
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
        self.bold     = False;    self.bg = -1;              self.fg = -1
        self.italic   = False;    self.underline = False;    self.strike = False
        self.blinking = False;    self.dim = False;          self.hidden = False
        self.inverse  = False
              
        self.adj_indent = 0;      self.adj_space  = 0;       self.delay_ms   = 0
        self.set_layout = "vertical"
        self.set_top_line    = False
        self.set_bottom_line = False
        

    def print_ascii_art(self, word_list=["P","Y"], ascii_type="Doh"):
        # Defining variables
        rows = 0;           result = [];   copy_word_list = []
        tempo_row = "";     retardo = self.delay_ms/1000
        key_letter = "";    skip_top_row = self.set_top_line
        color = set_font(self.bold, self.bg, self.fg, self.italic, self.underline, self.strike,
                        self.blinking, self.dim, self.hidden, self.inverse)


        # Creating the copy list (deep copy)
        for i in word_list:
            copy_word_list.append(i)

        # -------------------------------------------------------- Finding the Type of Ascii Letters
        if ascii_type == "Alpha":
            rows = AL.height
            key_letter = "AL."
            # this only have uppercase available
            # we convert the copy_word_list to all capital

        elif ascii_type == "Doh":
            rows = DL.height
            key_letter = "DL."

        elif ascii_type == "Big":
            rows = AL.height
        else:                 pass
        # -------------------------------------------------------- Ending Finding the Type of Ascii Letters
      
        #--------------------------------------------------------- Making the list result in vertical form
        if self.set_layout == "vertical":
            if self.set_bottom_line == False: rows = rows - 1
            for r in range(rows):
                if skip_top_row == False: pass
                else:
                    for l in range(len(copy_word_list)):
                        try:
                            row_info = key_letter + ascii_type + "_" + copy_word_list[l] + "[" + str(r) + "]"
                            tempo_row = tempo_row + eval(row_info) + ins_chr(self.adj_space)
                        except:
                            pass
                            row_info = key_letter + ascii_type + "_NA" + "[" + str(r) + "]"
                            tempo_row = tempo_row + eval(row_info) + ins_chr(self.adj_space)

                if skip_top_row == False: skip_top_row = True
                else:
                    result.append([f"{ins_chr(self.adj_indent)}{color}{ins_chr(self.adj_space)}{tempo_row}\033[0m"])
                tempo_row = ""

            # +-------------------------------------------------------------------------------------+
            # | Printing the ASCII Letters in vertical form                                         |
            # +-------------------------------------------------------------------------------------+
            for row in result:
                for col in row:
                    time.sleep(retardo); print(col)

        #--------------------------------------------------------- Making the list result in horizontal form
        elif self.set_layout == "horizontal":
            move_up = rows
            move_right = self.adj_indent

            if self.set_bottom_line == False:
                rows    -= 1
                move_up -= 1 
            if self.set_top_line == False:
                move_up -= 1


            for w in range(len(copy_word_list)):
                try:    list_letter = eval(key_letter + ascii_type + "_" + copy_word_list[w])
                except: list_letter = eval(key_letter + ascii_type + "_" + "NA")

                for r in range(rows):
                    if skip_top_row == False: skip_top_row = True
                    else:
                        print(f"\033[{str(move_right-1)}C{color}{ins_chr(self.adj_space)}{list_letter[r]}{ins_chr(self.adj_space)}\033[0m")


                move_right = move_right + len(list_letter[0]) + self.adj_space


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

