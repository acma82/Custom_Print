import time

from custom_print.fancy_functions import ins_chr
from custom_print.fancy_functions import set_font
from custom_print.fancy_functions import ins_newline
from custom_print.fancy_functions import move_cursor_right

from custom_print           import Move
from custom_print           import FancyFormat
from custom_print           import Line_Style
from custom_print.pylo      import PyLO
from custom_print           import Cursor
from custom_print.ref_names import Layout, Ascii_Letter


# importing the files with the ascii_art
import custom_print.Alpha_Letters
import custom_print.ANSI_Shadow_Letters
import custom_print.Big_Letters
import custom_print.Blocks_Letters
import custom_print.Bulbhead_Letters
import custom_print.Colossal_Letters
import custom_print.Crazy_Letters
import custom_print.Doh_Letters
import custom_print.Doom_Letters
import custom_print.Epic_Letters
import custom_print.Graceful_Letters
import custom_print.Larry_Letters
import custom_print.Roman_Letters
import custom_print.Standard_Letters
import custom_print.Sweet_Letters
import custom_print.Logos

# +------------------------------------------------------------------------------------------------------------------------------------+
# |  Creating the Ascii Word                                                                                                           |
# |  --------------------------------------------------------------------------------------------------------------------------------  |
# +------------------------------------------------------------------------------------------------------------------------------------+
class Art:
    def __init__(self):        
        self.bold     = False;                self.bg = -1;                           self.fg = -1
        self.italic   = False;                self.underline = False;                 self.strike = False
        self.blinking = False;                self.dim = False;                       self.hidden = False
        self.inverse  = False;                self.ascii_type = Ascii_Letter.Big
              
        self.adj_indent = 0;                  self.adj_space  = 0;                    self.delay_ms   = 0
        self.set_layout = Layout.VERTICAL;    self.set_top_line = False;              self.set_bottom_line = False; 
        self.adj_left_space = 0;              self.adj_middle_space = 0;              self.adj_right_space = 0
        
    def description_ascii_letters(self):
        tbl = FancyFormat()
        ascii_letter_description = [["Type", "Uppercase", "Lowercase","Shiff_On", "Shift_Off"],
                                    [Ascii_Letter.Alpha,       "Yes", "No",  "No",  "No" ],
                                    [Ascii_Letter.ANSI_Shadow, "Yes", "No",  "Yes", "Yes"],
                                    [Ascii_Letter.Big,         "Yes", "Yes", "Yes", "Yes"]]
        
        
        tbl.title_align = "center"; tbl.title_msg   = "  Description of Ascii Letters  "
        tbl.title_bg    = 231;       tbl.title_fg = 21;   tbl.title_bold = True
        
        tbl.footnote_align = "right"; tbl.footnote_msg = " Table Ascii Letters "
        tbl.footnote_bold  = True;    tbl.footnote_bg  = 90;  tbl.footnote_fg = 231

        tbl.adj_bottom_margin = 2; tbl.adj_top_margin = 2
        tbl.adj_bottom_space  = 0; tbl.adj_top_space  = 2

        tbl.print_fancy_format(data=ascii_letter_description, style=Line_Style.WHITE_BLACK_PURPLE)

    # +--------------------------------------------------------------------------------------------------------------------------------+
    # |    Only One Setting for Bold, Bg, Fg, italic, underline, strike, blinking, dim, and inverse                                    |
    # +--------------------------------------------------------------------------------------------------------------------------------+
    def print_ascii_art(self, msg="AB"):
        # Defining variables
        rows = 0;                        result = []
        tempo_row = "";                  retardo = self.delay_ms/1000
        key_letter = "";                 skip_top_row = self.set_top_line
        left_sp = self.adj_left_space;   middle_sp = self.adj_middle_space
        right_sp = self.adj_right_space
        
        symbol_chrs = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=",
                       "[", "]", "\\", ";", "'",  ",", ".", "/",
                       "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|",  ":", "\"", "<", ">", "?", " "]
        
        symbol_name = ["backtick", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero", "minus", "equal",
                       "open_bracket", "closed_bracket", "backward_slash", "semicolon", "apostrophe", "comma", "period", "forward_slash",
                       "tilde", "exclamation", "arroba", "pound", "dollar", "percent", "caret", "ampersand", "asterisk",  "open_parenthesis",
                       "closed_parenthesis", "underscore", "plus", "pipe", "open_curly", "closed_curly", "colon", "quotation","less_than",
                       "greater_than", "question", "space"]

        color = set_font(self.bold, self.bg, self.fg, self.italic, self.underline, self.strike,
                        self.blinking, self.dim, self.hidden, self.inverse)
        
        data = msg
        pylo = PyLO()
        key_letter = "custom_print."+self.ascii_type + "_Letters."

        # Make sure always exist a letter A or a in all the Letters Type
        try:
            list_name = eval("custom_print."+self.ascii_type+"_Letters."+self.ascii_type+"_NA")
            rows = len(list_name)
        except:
            list_name = eval("custom_print."+self.ascii_type+"_Letters."+self.ascii_type+"_space")
            rows = len(list_name) 

        # ------------------------------------------------------------ Finding the Type of Ascii Letters       
        if self.ascii_type == Ascii_Letter.Alpha:
            #  Alpha only have uppercase available
            if type(msg) is list:
                result = pylo.update_case(data=data, header_case=pylo.Case.UPPER, data_case=pylo.Case.UPPER, update=True )
            else:
                data = msg.upper()
            

        elif self.ascii_type == Ascii_Letter.Crazy:
            # Crazy Only have lowercase available
            if type(msg) is list:
                result = pylo.update_case(data=data, header_case=pylo.Case.LOWER, data_case=pylo.Case.LOWER, update=True )
            else:
                data = msg.lower()

        else:
            # Other letters that have uppercase and lower case
            list_name = eval("custom_print."+self.ascii_type+"_Letters."+self.ascii_type+"_A")
        # -------------------------------------------------------- Ending Finding the Type of Ascii Letters


        # +------------------------------------------------------            error_layout = []
            error_layout.append("                                                                    ")
            error_layout.append("   ______                       _                             _     ")
            error_layout.append("  |  ____|                     | |                           | |    ")
            error_layout.append("  | |__   _ __ _ __ ___  _ __  | |     __ _ _   _  ___  _   _| |_   ")
            error_layout.append("  |  __| | '__| '__/ _ \\| '__| | |    / _` | | | |/ _ \\| | | | __|  ")
            error_layout.append("  | |____| |  | | | (_) | |    | |___| (_| | |_| | (_) | |_| | |_   ")
            error_layout.append("  |______|_|  |_|  \\___/|_|    |______\\__,_|\\__, |\\___/ \\__,_|\\__|  ")
            error_layout.append("                                             __/ |                  ")
            error_layout.append("                                            |___/                   ")
            error_layout.append("                                                                    ")
            for row in error_layout:
                print(f"    {color}{row}\033[0m")
            print("    Form more help visit: ")
            print("    https://github.com/acma82/Custom_Print/tree/main/readme ")
            print("    Thank you for using custom_print")



        # +---------------------------------------------------------------------------------------------------+
        # |                          Making the list result in vertical form                                  |
        # +---------------------------------------------------------------------------------------------------+
        if self.set_layout == Layout.VERTICAL:
            if len(data) == 1: middle_sp = left_sp
            else:              pass

            if self.set_bottom_line == False: rows = rows - 1
            for r in range(rows):
                if skip_top_row == False: pass
                else:
                    for l in range(len(data)):
                        try:
                            row_info = key_letter + self.ascii_type + "_" + data[l] + "[" + str(r) + "]"

                            if l == (len(data)-1):
                                tempo_row = tempo_row + ins_chr(middle_sp) + eval(row_info) + ins_chr(right_sp)   # last item
                            elif l >= 1:
                                tempo_row = tempo_row + ins_chr(middle_sp) + eval(row_info) #+ ins_chr(middle_sp) # middle items
                            else:
                                tempo_row = tempo_row + ins_chr(left_sp) + eval(row_info) #+ ins_chr(middle_sp)   # first item
                        
                        except:
                            
                            if data[l] in symbol_chrs:
                                position = symbol_chrs.index(data[l])
                                symbol_chr = symbol_name[position]
                            
                            
                                try:
                                    row_info = eval(key_letter + self.ascii_type + "_" + symbol_chr + "[" + str(r) + "]")
                                except:
                                    row_info = eval(key_letter + self.ascii_type + "_NA" + "[" + str(r) + "]")
                            else:
                                row_info = eval(key_letter + self.ascii_type + "_NA" + "[" + str(r) + "]")

                            if l == (len(data)-1):
                                tempo_row = tempo_row + ins_chr(middle_sp) + row_info + ins_chr(right_sp)   # last item
                            elif l >= 1:
                                tempo_row = tempo_row + ins_chr(middle_sp) + row_info # + ins_chr(middle_sp) # middle items
                            else:
                                tempo_row = tempo_row + ins_chr(left_sp) + row_info   # + ins_chr(middle_sp)   # first item

                if skip_top_row == False: skip_top_row = True
                else:
                    result.append([f"{move_cursor_right(self.adj_indent)}{color}{tempo_row}\033[0m"])
                tempo_row = ""

            # +-------------------------------------------------------------------------------------+
            # | Printing the ASCII Letters in vertical form                                         |
            # +-------------------------------------------------------------------------------------+
            for row in result:
                for col in row:
                    time.sleep(retardo); print(col)

        # +---------------------------------------------------------------------------------------------------+
        # |                          Making the list result in horizontal form                                |
        # +---------------------------------------------------------------------------------------------------+
        elif self.set_layout == Layout.HORIZONTAL:
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
                    if data[w] in symbol_chrs:
                        position = symbol_chrs.index(data[w])
                        symbol_chr = symbol_name[position]
                        
                        list_letter = eval(key_letter + self.ascii_type + "_" + symbol_chr)

                    else:
                        list_letter = eval(key_letter + self.ascii_type + "_" + data[w])    
                except: 
                        list_letter = eval(key_letter + self.ascii_type + "_" + "NA")

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
            # +-------------------------------------------------------------------------------------+
            # | LayOut NOT Specified                                                                |
            # +-------------------------------------------------------------------------------------+
            color = set_font(True, 196, 231)
            error_layout = []
            error_layout.append("                                                                    ")
            error_layout.append("   ______                       _                             _     ")
            error_layout.append("  |  ____|                     | |                           | |    ")
            error_layout.append("  | |__   _ __ _ __ ___  _ __  | |     __ _ _   _  ___  _   _| |_   ")
            error_layout.append("  |  __| | '__| '__/ _ \\| '__| | |    / _` | | | |/ _ \\| | | | __|  ")
            error_layout.append("  | |____| |  | | | (_) | |    | |___| (_| | |_| | (_) | |_| | |_   ")
            error_layout.append("  |______|_|  |_|  \\___/|_|    |______\\__,_|\\__, |\\___/ \\__,_|\\__|  ")
            error_layout.append("                                             __/ |                  ")
            error_layout.append("                                            |___/                   ")
            error_layout.append("                                                                    ")
            for row in error_layout:
                print(f"    {color}{row}\033[0m")
            print("    Form more help visit: ")
            print("    https://github.com/acma82/Custom_Print/tree/main/readme ")
            print("    Thank you for using custom_print")
            exit()







    # +--------------------------------------------------------------------------------------------------------------------------------+
    # |    Multiple Settings for Bold, Bg, Fg, italic, underline, strike, blinking, dim, and inverse                                   |
    # +--------------------------------------------------------------------------------------------------------------------------------+
    def print_multi_ascii_art(self,lista, sets_bold, sets_bg, sets_fg, sets_italic, sets_underline, sets_strike, sets_blinking, sets_dim, sets_hidden, sets_inverse ):
        # adj_indent cannot be changed or it will be messy
        crs = Cursor()
        key_word = "custom_print." + self.ascii_type + "_Letters." + self.ascii_type + "_"
        ctrl_dist = 0
        symbol_chrs = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "[", "]", "\\", ";", "'",  ",", ".", "/",
                        "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|",  ":", "\"", "<", ">", "?", " "]
        
        symbol_name = ["backtick", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero", "minus", "equal",
                        "open_bracket", "close_bracket", "backward_slash", "semicolon", "apostrophe", "comma", "period",   "forwad_slash",
                        "tilde", "exclamation", "arroba", "pound", "dollar", "percent", "caret", "ampersand", "asterisk",  "open_parenthesis",
                        "close_parenthesis", "underscore", "plus", "pipe", "open_curly", "close_curly", "colon", "quotation","less_than",
                        "greater_than", "question", "space"]

            # ------------------------------------------------------------ Finding the Type of Ascii Letters       
        pylo = PyLO()

        if self.ascii_type == Ascii_Letter.Alpha:
            #  Alpha only have uppercase available
            result = pylo.update_case(data=lista, header_case=pylo.Case.UPPER, data_case=pylo.Case.UPPER, update=False)
            

        elif self.ascii_type == Ascii_Letter.Crazy:
            # Crazy Only have lowercase available
            result = pylo.update_case(data=lista, header_case=pylo.Case.LOWER, data_case=pylo.Case.LOWER, update=False)
            
        else:
            # Other letters that have uppercase and lower case
            result = pylo.update_case(data=lista, header_case=pylo.Case.UPPER, data_case=pylo.Case.UPPER, update=False)
        # -------------------------------------------------------- Ending Finding the Type of Ascii Letters

        for row in range(len(lista)):
            self.bold = sets_bold[row]
            self.bg   = sets_bg[row]
            self.fg   = sets_fg[row]

            self.italic    = sets_italic[row]
            self.underline = sets_underline[row]
            self.strike    = sets_strike[row]
            self.blinking  = sets_blinking[row]
            self.dim       = sets_dim[row]
            self.hidden    = sets_hidden[row]
            self.inverse   = sets_inverse[row]

            for col in range(len(result[row])):
                self.print_ascii_art(result[row][col])
                text = result[row][col]
                for n in text:
                    try:
                        list_name =  eval(key_word + n)
                        letter_width = len(list_name[0])
                        ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row. (Letters or Numbers)


                    except:
                        if n in symbol_chrs:
                            position = symbol_chrs.index(n)
                            symbol_chr = symbol_name[position]
                            try:
                                list_name  = eval(key_word + symbol_chr)
                                letter_width = len(list_name[0])
                                ctrl_dist = ctrl_dist + letter_width # contains all the width of the letters inside the row. (Symbols)
                            except:
                                list_name = eval(key_word + "NA")
                                letter_width = len(list_name[0])
                                ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row, if the letter does not exist, here


                        else:
                            list_name = eval(key_word + "NA") # key_word. => Alpha_Letters.Alpha_NA
                            letter_width = len(list_name[0])
                            ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row, if the letter does not exist, here


            if (len(result[row])) >= 2: self.adj_indent = self.adj_indent+self.adj_left_space+ ctrl_dist+self.adj_middle_space+self.adj_right_space
            else:                      self.adj_indent = self.adj_indent+self.adj_left_space+ ctrl_dist+self.adj_right_space
            ctrl_dist = 0

            # Make sure always exist a letter: A or a in all the Letters Type
            letter_height = 0

            try:
                list_name = eval(key_word + "A") # eval(key_word+self.ascii_type+"_A")
                letter_height = len(list_name)
            except:
                list_name = eval(key_word + "a") # eval(key_word+self.ascii_type+"_a")
                letter_height = len(list_name) 

            crs.jumpTo(qty=letter_height, direction = Move.UP)  # Letter_height

        crs.jumpTo(qty=letter_height, direction = Move.DOWN)




    # +--------------------------------------------------------------------------------------------------------------------------------+
    # |    Only One Setting for Bold, Bg, Fg, italic, underline, strike, blinking, dim, and inverse for the customized logos.          |
    # |    For the specific logos like Linux, Debian, Alma, and so on. No settings will be applied for them.                           |
    # +--------------------------------------------------------------------------------------------------------------------------------+
    def print_image_ascii_art(self):
        retardo = self.delay_ms/1000;           key_letter = "";

        color = set_font(self.bold, self.bg, self.fg, self.italic, self.underline, self.strike,
                        self.blinking, self.dim, self.hidden, self.inverse)
        
        defined_logos = ["Windows","Apple","Unix_Logo","Linux", "Red_Hat", "Centos", "Alma","Fedora", "Archict", "Kalib", "Python"]

        if self.ascii_type in defined_logos: key_letter = eval("custom_print." + "Logos." + self.ascii_type)
        else:                                key_letter = self.ascii_type

        if self.set_layout == Layout.VERTICAL:
            for n in range(len(key_letter)):
                print(move_cursor_right(self.adj_indent)+color+ins_chr(self.adj_left_space)+key_letter[n]+ins_chr(self.adj_right_space)+"\033[0m")
                time.sleep(retardo)
        
        elif self.set_layout == Layout.HORIZONTAL:
            crs = Cursor()
            ctrl_cols = 0
            n_rows = len(key_letter)
            n_cols = len(key_letter[0])
            for col in range(n_cols):
                for row in range(n_rows):
                    if col == 0:  # first col
                        print(move_cursor_right(self.adj_indent)+color+ins_chr(self.adj_left_space)+key_letter[row][col]+"\033[0m")
                    elif col == (n_cols - 1 ): # last col
                        print(move_cursor_right(self.adj_indent+self.adj_left_space+ctrl_cols)+color+key_letter[row][col]+ins_chr(self.adj_right_space)+"\033[0m")
                        # input("enter")
                    else: # middle cols
                        print(move_cursor_right(self.adj_indent+self.adj_left_space+ctrl_cols)+color+key_letter[row][col]+"\033[0m")
                ctrl_cols += 1                
                time.sleep(retardo)
                if col == (n_cols -1): pass
                else:                  crs.jumpTo(qty = n_rows, direction= Move.UP)
            # crs.jumpTo(qty = n_rows, direction= Move.DOWN)

        else:
            # +-------------------------------------------------------------------------------------+
            # | LayOut NOT Specified                                                                |
            # +-------------------------------------------------------------------------------------+
            color = set_font(True, 196, 231)
            error_layout = []
            error_layout.append("                                                                    ")
            error_layout.append("   ______                       _                             _     ")
            error_layout.append("  |  ____|                     | |                           | |    ")
            error_layout.append("  | |__   _ __ _ __ ___  _ __  | |     __ _ _   _  ___  _   _| |_   ")
            error_layout.append("  |  __| | '__| '__/ _ \\| '__| | |    / _` | | | |/ _ \\| | | | __|  ")
            error_layout.append("  | |____| |  | | | (_) | |    | |___| (_| | |_| | (_) | |_| | |_   ")
            error_layout.append("  |______|_|  |_|  \\___/|_|    |______\\__,_|\\__, |\\___/ \\__,_|\\__|  ")
            error_layout.append("                                             __/ |                  ")
            error_layout.append("                                            |___/                   ")
            error_layout.append("                                                                    ")
            for row in error_layout:
                print(f"    {color}{row}\033[0m")
            print("    Form more help visit: ")
            print("    https://github.com/acma82/Custom_Print/tree/main/readme ")
            print("    Thank you for using custom_print")
            exit()

  

    # +--------------------------------------------------------------------------------------------------------------------------------+
    # |    Only One Setting for Bold, Bg, Fg, italic, underline, strike, blinking, dim, and inverse for the customized logos.          |
    # |    For the specific logos like Linux, Debian, Alma, and so on. No settings will be applied for them.                           |
    # +--------------------------------------------------------------------------------------------------------------------------------+
    def print_reversed_image_ascii_art(self):
        retardo = self.delay_ms/1000;           key_letter = "";      crs = Cursor()

        color = set_font(self.bold, self.bg, self.fg, self.italic, self.underline, self.strike,
                        self.blinking, self.dim, self.hidden, self.inverse)
        
        defined_logos = ["Windows","Apple","Unix_Logo","Linux", "Red_Hat", "Centos", "Alma","Fedora", "Archict", "Kalib", "Python"]

        if self.ascii_type in defined_logos: key_letter = eval("custom_print." + "Logos." + self.ascii_type)
        else:                                key_letter = self.ascii_type


        if self.set_layout == Layout.VERTICAL:
            pos_crs = len(self.ascii_type) - 1
            ins_newline(len(self.ascii_type))
            

            for n in  range(len(key_letter)):
                print(move_cursor_right(self.adj_indent)+color+ins_chr(self.adj_left_space)+key_letter[pos_crs]+ins_chr(self.adj_right_space)+"\033[0m")
                crs.jumpTo(qty = 2, direction= Move.UP)
                time.sleep(retardo)
                pos_crs -= 1
            crs.jumpTo(qty = (len(self.ascii_type)), direction= Move.DOWN)

        
        elif self.set_layout == Layout.HORIZONTAL:
            ctrl_cols = 1
            n_rows = len(key_letter);           n_cols = len(key_letter[0])           
            x = n_cols

            for col in range(n_cols):
                x -= 1
                for row in range(n_rows):
                    if col == 0:  # first col
                        print(move_cursor_right(self.adj_indent)+color+ins_chr(self.adj_left_space+n_cols-1)+key_letter[row][x]+ins_chr(self.adj_right_space)+"\033[0m")
                    elif col == (n_cols - 1 ): # last col
                        print(move_cursor_right(self.adj_indent+self.adj_left_space)+color+key_letter[row][x]+"\033[0m")
                        
                    else: # middle cols
                        print(move_cursor_right(self.adj_indent+self.adj_left_space+n_cols-ctrl_cols)+color+key_letter[row][x]+"\033[0m")
                
                
                ctrl_cols += 1
                time.sleep(retardo)
                if col == (n_cols -1): pass
                else:                  crs.jumpTo(qty = n_rows, direction= Move.UP)
            # crs.jumpTo(qty = n_rows, direction= Move.DOWN)

        else:
            # +-------------------------------------------------------------------------------------+
            # | LayOut NOT Specified                                                                |
            # +-------------------------------------------------------------------------------------+
            error_layout = []
            error_layout.append("                                                                    ")
            error_layout.append("   ______                       _                             _     ")
            error_layout.append("  |  ____|                     | |                           | |    ")
            error_layout.append("  | |__   _ __ _ __ ___  _ __  | |     __ _ _   _  ___  _   _| |_   ")
            error_layout.append("  |  __| | '__| '__/ _ \\| '__| | |    / _` | | | |/ _ \\| | | | __|  ")
            error_layout.append("  | |____| |  | | | (_) | |    | |___| (_| | |_| | (_) | |_| | |_   ")
            error_layout.append("  |______|_|  |_|  \\___/|_|    |______\\__,_|\\__, |\\___/ \\__,_|\\__|  ")
            error_layout.append("                                             __/ |                  ")
            error_layout.append("                                            |___/                   ")
            error_layout.append("                                                                    ")
            for row in error_layout:
                print(f"    {color}{row}\033[0m")
            print("    Form more help visit: ")
            print("    https://github.com/acma82/Custom_Print/tree/main/readme ")
            print("    Thank you for using custom_print")
            exit()

  
