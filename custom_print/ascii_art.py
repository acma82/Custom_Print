import time

from custom_print.fancy_functions import ins_chr
from custom_print.fancy_functions import set_font
from custom_print.fancy_functions import ins_newline
from custom_print.fancy_functions import move_cursor_right

from custom_print                 import Move
from custom_print                 import FancyFormat
from custom_print                 import Line_Style
from custom_print                 import Cursor
from custom_print.ref_names       import Layout, Ascii_Letter

from custom_print.ascii_letters   import*
# from custom_print.Logos           import*
# from custom_print.pylo            import PyLO

# +------------------------------------------------------------------------------------------------------------------------------------+
# |  Creating the Ascii Word                                                                                                           |
# |  --------------------------------------------------------------------------------------------------------------------------------  |
# +------------------------------------------------------------------------------------------------------------------------------------+
class AsciiArt:
    def __init__(self):        
        self.bold     = False;                self.bg = -1;                           self.fg = -1
        self.italic   = False;                self.underline = False;                 self.strike = False
        self.blinking = False;                self.dim = False;                       self.hidden = False
        self.inverse  = False;                self.ascii_type = Ascii_Letter.STANDARD
              
        self.adj_indent = 0;                  self.delay_ms   = 0
        self.set_layout = Layout.VERTICAL;    self.set_top_line_on = True;            self.set_bottom_line_on = True; 
        self.adj_left_space = 0;              self.adj_middle_space = 0;              self.adj_right_space = 0
        
    # +--------------------------------------------------------------------------------------------------------------------------------+
    # |    Only One Setting for Bold, Bg, Fg, italic, underline, strike, blinking, dim, and inverse                                    |
    # +--------------------------------------------------------------------------------------------------------------------------------+
    def print_ascii_art(self, msg="ABC"):
        # Defining variables
        rows = 0;                            result = []
        tempo_row = "";                      retardo = self.delay_ms/1000            
        skip_top_row = self.set_top_line_on;    left_sp = self.adj_left_space
        middle_sp = self.adj_middle_space;   right_sp = self.adj_right_space
        
        symbol_chrs = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=",
                       "[", "]", "\\", ";", "'",  ",", ".", "/",
                       "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "|","{", "}", ":", "\"", "<", ">", "?", " "]
        
        symbol_name = ["backtick", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero", "minus", "equal",
                       "open_bracket", "closed_bracket", "backward_slash", "semicolon", "apostrophe", "comma", "period", "forward_slash",
                       "tilde", "exclamation", "arroba", "pound", "dollar", "percent", "caret", "ampersand", "asterisk",  "open_parenthesis",
                       "closed_parenthesis", "underscore", "plus", "pipe", "open_curly", "closed_curly", "colon", "quotation","less_than",
                       "greater_than", "question", "space"]
      
        data = msg

        ascii_letter_options = [Ascii_Letter.ALPHA,    Ascii_Letter.ANSI_SHADOW,  Ascii_Letter.BIG,
                                Ascii_Letter.BLOCKS,   Ascii_Letter.BULBHEAD,     Ascii_Letter.CLASSY,
                                Ascii_Letter.COLOSSAL, Ascii_Letter.CRAZY,        Ascii_Letter.DOH,
                                Ascii_Letter.DOOM,     Ascii_Letter.EPIC,         Ascii_Letter.GRACEFUL,
                                Ascii_Letter.LARRY,    Ascii_Letter.FONT_FONT,    Ascii_Letter.MONEY_NE,
                                Ascii_Letter.MONEY_NW, Ascii_Letter.MONEY_SE,     Ascii_Letter.MONEY_SW,
                                Ascii_Letter.MONO,     Ascii_Letter.MOON,         Ascii_Letter.MOON2,
                                Ascii_Letter.ROMAN,    Ascii_Letter.STANDARD,     Ascii_Letter.SWEET,
                               ]
        if self.ascii_type in ascii_letter_options: pass
        else:
            # +-------------------------------------------------------------------------------------+
            # | ascii_type NOT Supported                                                            |
            # +-------------------------------------------------------------------------------------+
            print("\n")
            color = set_font(True, 196, 231)
            error_ascii_type = []
            error_ascii_type.append("   _____                                                            ")
            error_ascii_type.append("  | ____|  _ __   _ __    ___    _ __   _                           ")
            error_ascii_type.append("  |  _|   | '__| | '__|  / _ \\  | '__| (_)                          ")
            error_ascii_type.append("  | |___  | |    | |    | (_) | | |     _                           ")
            error_ascii_type.append("  |_____| |_|    |_|     \\___/  |_|    (_)                          ")
            error_ascii_type.append("                                                                    ")
            error_ascii_type.append("                       _   _           _                            ")
            error_ascii_type.append("   __ _   ___    ___  (_) (_)         | |_   _   _   _ __     ___   ")
            error_ascii_type.append("  / _` | / __|  / __| | | | |         | __| | | | | | '_ \\   / _ \\  ")
            error_ascii_type.append(" | (_| | \\__ \\ | (__  | | | |         | |_  | |_| | | |_) | |  __/  ")
            error_ascii_type.append("  \\__,_| |___/  \\___| |_| |_|  _____   \\__|  \\__, | | .__/   \\___|  ")
            error_ascii_type.append("                              |_____|        |___/  |_|             ")
            error_ascii_type.append("                                                                    ")
            for row in error_ascii_type:
                print(f"    {color}{row}\033[0m")

            print("")
            print(f"    {self.ascii_type} ascii_type is NOT supported by custom_print Module")
            print("    Form more help visit: ")
            print("    https://github.com/acma82/Custom_Print/tree/main/readme ")
            print()
            print("    For help on the Terminal: custom_print AsciiArt")
            print()
            print("    Thank you for using custom_print")
            exit()

        # Make sure always exist space list in the Type of Letters Using
        rows = len(eval(self.ascii_type+"_space"))

   
        if self.ascii_type == Ascii_Letter.MOON2:
            color = set_font(self.bold, 0, self.fg, self.italic, self.underline, self.strike,
                        self.blinking, self.dim, self.hidden, self.inverse)
        else:
            color = set_font(self.bold, self.bg, self.fg, self.italic, self.underline, self.strike,
                        self.blinking, self.dim, self.hidden, self.inverse)


        # +---------------------------------------------------------------------------------------------------+
        # |                          Making the list result in vertical form                                  |
        # +---------------------------------------------------------------------------------------------------+
        if self.set_layout == Layout.VERTICAL:
            if len(data) == 1: middle_sp = left_sp
            else:              pass

            if self.set_bottom_line_on == False: rows = rows - 1
            for r in range(rows):
                if skip_top_row == False: pass
                else:
                    for l in range(len(data)):
                        try:                            
                            row_info = self.ascii_type + "_" + data[l] + "[" + str(r) + "]"

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
                                    row_info = eval(self.ascii_type + "_" + symbol_chr + "[" + str(r) + "]")
                                except:
                                    row_info = eval(self.ascii_type + "_NA" + "[" + str(r) + "]")
                            else:
                                row_info = eval(self.ascii_type + "_NA" + "[" + str(r) + "]")

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

            if self.set_bottom_line_on == False:
                rows    -= 1
                move_up -= 1 
            if self.set_top_line_on == False:
                move_up -= 1


            for w in range(len(data)):
                try:    
                    if data[w] in symbol_chrs:
                        position = symbol_chrs.index(data[w])
                        symbol_chr = symbol_name[position]
                        
                        list_letter = eval(self.ascii_type + "_" + symbol_chr)                        
                    else:
                        list_letter = eval(self.ascii_type + "_" + data[w])
                except: 
                        list_letter = eval(self.ascii_type + "_" + "NA")

                for r in range(rows):
                    if skip_top_row == False: skip_top_row = True
                    else:
                        if (len(data)) == 1:
                            print(f"{move_cursor_right(self.adj_indent)}{color}{ins_chr(left_sp)}{list_letter[r]}{ins_chr(right_sp)}\033[0m")       # first item
                        else:
                            if w == 0:
                                print(f"{move_cursor_right(self.adj_indent)}{color}{ins_chr(left_sp)}{list_letter[r]}{ins_chr(middle_sp)}\033[0m")  # first item
                            elif w == (len(data)-1):
                                print(f"{color}\033[{str(move_right)}C{list_letter[r]}{ins_chr(right_sp)}\033[0m")                                  # last item
                            else:
                                print(f"{color}\033[{str(move_right)}C{color}{list_letter[r]}{ins_chr(middle_sp)}\033[0m")                          # middle items# w >= 1:
                   
                if w == 0:
                    # Because Moon2 has predefined color and the length of those color is 12, we have to subtract 12
                    if self.ascii_type == Ascii_Letter.MOON2:
                        move_right = move_right + left_sp + len(list_letter[0]) + middle_sp - 12  # first item
                    else:
                        move_right = move_right + left_sp + len(list_letter[0]) + middle_sp       # first item   original
                    
                else:
                    if self.ascii_type == Ascii_Letter.MOON2:
                        move_right = move_right + len(list_letter[0]) + middle_sp - 12            # middle item
                    else:
                        move_right = move_right + len(list_letter[0]) + middle_sp                 # middle item (original)

                print(f"\033[{str(move_up)}A",end="")
                skip_top_row = self.set_top_line_on
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
            print("")
            print(f"    {self.ascii_type} ascii_type is NOT supported by custom_print Module")
            print("    Form more help visit: ")
            print("    https://github.com/acma82/Custom_Print/tree/main/readme ")
            print()
            print("    For help on the Terminal: custom_print AsciiArt")
            print()
            print("    Thank you for using custom_print")
            exit()







    # +--------------------------------------------------------------------------------------------------------------------------------+
    # |    Multiple Settings for Bold, Bg, Fg, italic, underline, strike, blinking, dim, and inverse                                   |
    # +--------------------------------------------------------------------------------------------------------------------------------+
    def print_multi_ascii_art(self,data):

        # self.adj_indent cannot be changed or it will be messy
        # self.ascii_type cannot be changed ot it will be messy because many ascii letters has different height
        # The following variables are not being alter their value: ascii_type, set_layout, set_top_line_on, set_bottom_line_on and set_delay_ms
        # Backup the variables
        #------------------------------------------------------------
        bu_bg   = self.bg
        bu_fg   = self.fg
        bu_dim  = self.dim
        bu_bold = self.bold
        bu_italic    = self.italic
        bu_underline = self.underline
        bu_strike    = self.strike
        bu_blinking  = self.blinking
        bu_hiddends  = self.hidden
        bu_inverse   = self.inverse
        bu_adj_left_space   = self.adj_left_space
        bu_adj_middle_space = self.adj_middle_space
        bu_adj_right_space  = self.adj_right_space
        bu_adj_indent       = self.adj_indent
        #------------------------------------------------------------
        # End of Backup
        crs = Cursor()
        ctrl_dist = 0
        letter_height = 0
        symbol_chrs = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "[", "]", "\\", ";", "'",  ",", ".", "/",
                        "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|",  ":", "\"", "<", ">", "?", " "]
        
        symbol_name = ["backtick", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero", "minus", "equal",
                        "open_bracket", "close_bracket", "backward_slash", "semicolon", "apostrophe", "comma", "period",   "forwad_slash",
                        "tilde", "exclamation", "arroba", "pound", "dollar", "percent", "caret", "ampersand", "asterisk",  "open_parenthesis",
                        "close_parenthesis", "underscore", "plus", "pipe", "open_curly", "close_curly", "colon", "quotation","less_than",
                        "greater_than", "question", "space"]

        for col in range(len(data[0])):
            self.bold      = data[1][col]
            self.bg        = data[2][col]
            self.fg        = data[3][col]
            self.italic    = data[4][col]
            self.underline = data[5][col]
            self.strike    = data[6][col]
            self.blinking  = data[7][col]
            self.dim       = data[8][col]
            self.hidden    = data[9][col]
            self.inverse   = data[10][col]

            self.adj_left_space   = data[11][col]
            self.adj_middle_space = data[12][col]
            self.adj_right_space  = data[13][col]

            self.print_ascii_art(data[0][col])
            text = data[0][col]

            for n in text:
                try:
                    list_name =  eval(self.ascii_type + "_" + n)
                    letter_width = len(list_name[0])
                    ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row. (Letters or Numbers)


                except:
                    if n in symbol_chrs:
                        position = symbol_chrs.index(n)
                        symbol_chr = symbol_name[position]
                        try:
                            list_name  = eval(self.ascii_type + "_" + symbol_chr)
                            letter_width = len(list_name[0])
                            ctrl_dist = ctrl_dist + letter_width # contains all the width of the letters inside the row. (Symbols)
                        except:
                            list_name = eval(self.ascii_type + "_" + "NA")
                            letter_width = len(list_name[0])
                            ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row, if the letter does not exist, here


                    else:
                        list_name = eval(self.ascii_type + "_" + "NA") # key_word. => Alpha_Letters.Alpha_NA
                        letter_width = len(list_name[0])
                        ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row, if the letter does not exist, here


            if (len(data[0][col])) >= 2: self.adj_indent = self.adj_indent + data[11][col] + ctrl_dist + data[12][col] + data[13][col]
            else:                        self.adj_indent = self.adj_indent + data[11][col] + ctrl_dist + data[13][col]
            ctrl_dist = 0

            # Make sure always exist space list into the type of letter using
            letter_height = len(eval(self.ascii_type + "_" + "space"))

            crs.jumpTo(qty=letter_height, direction = Move.UP)

        crs.jumpTo(qty=letter_height, direction = Move.DOWN)

        # Putting back the variables
        #------------------------------------------------------------
        self.bg    = bu_bg  
        self.fg    = bu_fg  
        self.dim   = bu_dim 
        self.bold  = bu_bold
        self.italic    = bu_italic   
        self.underline = bu_underline
        self.strike    = bu_strike   
        self.blinking  = bu_blinking 
        self.hidden    = bu_hiddends 
        self.inverse   = bu_inverse  
        self.adj_left_space   = bu_adj_left_space  
        self.adj_middle_space = bu_adj_middle_space
        self.adj_right_space  = bu_adj_right_space 
        self.adj_indent       = bu_adj_indent      
        #------------------------------------------------------------
        # End of putting back the variables




    # +--------------------------------------------------------------------------------------------------------------------------------+
    # |    Only One Setting for Bold, Bg, Fg, italic, underline, strike, blinking, dim, and inverse for the customized logos.          |
    # |    For the specific logos like Linux, Debian, Alma, and so on. No settings will be applied for them.                           |
    # +--------------------------------------------------------------------------------------------------------------------------------+
    def print_ascii_logo_art(self):
        # self.ascii_type -> Here it is a list we are passing rather than just the name of the letters to be used.
        # That is why we don't use the lovely function "eval" like in the print_ascii_art function or
        # the print_multi_ascii_art funtion. In those previous functions, we pass a string, the type of leeters to be used.
        # Then with that name and the string pass as a parameter we create the letter to be used, using the eval function.        
        # Note that in the print_multi_ascii_art is a list that we pass as a parameter while the print_ascii_art we pass a
        # string as a parameter.

        retardo = self.delay_ms/1000;
        
        color = set_font(self.bold, self.bg, self.fg, self.italic, self.underline, self.strike,
                        self.blinking, self.dim, self.hidden, self.inverse)

        if self.set_layout == Layout.VERTICAL:
            for n in range(len(self.ascii_type)):
                print(move_cursor_right(self.adj_indent)+color+ins_chr(self.adj_left_space)+self.ascii_type[n]+ins_chr(self.adj_right_space)+"\033[0m")
                time.sleep(retardo)
        
        elif self.set_layout == Layout.HORIZONTAL:
            crs = Cursor()
            ctrl_cols = 0
            n_rows = len(self.ascii_type)
            n_cols = len(self.ascii_type[0])
            for col in range(n_cols):
                for row in range(n_rows):
                    if col == 0:  # first col
                        print(move_cursor_right(self.adj_indent)+color+ins_chr(self.adj_left_space)+self.ascii_type[row][col]+"\033[0m")
                    elif col == (n_cols - 1 ): # last col
                        print(move_cursor_right(self.adj_indent+self.adj_left_space+ctrl_cols)+color+self.ascii_type[row][col]+ins_chr(self.adj_right_space)+"\033[0m")
                        # input("enter")
                    else: # middle cols
                        print(move_cursor_right(self.adj_indent+self.adj_left_space+ctrl_cols)+color+self.ascii_type[row][col]+"\033[0m")
                ctrl_cols += 1                
                time.sleep(retardo)
                if col == (n_cols -1): pass
                else:                  crs.jumpTo(qty = n_rows, direction= Move.UP)

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
            print("")
            print(f"    {self.ascii_type} ascii_type is NOT supported by custom_print Module")
            print("    Form more help visit: ")
            print("    https://github.com/acma82/Custom_Print/tree/main/readme ")
            print()
            print("    For help on the Terminal: custom_print AsciiArt")
            print()
            print("    Thank you for using custom_print")
            exit()

  

    # +--------------------------------------------------------------------------------------------------------------------------------+
    # |    Only One Setting for Bold, Bg, Fg, italic, underline, strike, blinking, dim, and inverse for the customized logos.          |
    # |    For the specific logos like Linux, Debian, Alma, and so on. No settings will be applied for them.                           |
    # +--------------------------------------------------------------------------------------------------------------------------------+
    def print_reversed_ascii_logo_art(self):
        retardo = self.delay_ms/1000;           key_letter = "";      crs = Cursor()

        color = set_font(self.bold, self.bg, self.fg, self.italic, self.underline, self.strike,
                        self.blinking, self.dim, self.hidden, self.inverse)

        if self.set_layout == Layout.VERTICAL:
            pos_crs = len(self.ascii_type) - 1
            ins_newline(len(self.ascii_type))
            

            for n in  range(len(self.ascii_type)):
                print(move_cursor_right(self.adj_indent)+color+ins_chr(self.adj_left_space)+self.ascii_type[pos_crs]+ins_chr(self.adj_right_space)+"\033[0m")
                crs.jumpTo(qty = 2, direction= Move.UP)
                time.sleep(retardo)
                pos_crs -= 1
            crs.jumpTo(qty = (len(self.ascii_type)), direction= Move.DOWN)

        
        elif self.set_layout == Layout.HORIZONTAL:
            ctrl_cols = 1
            n_rows = len(self.ascii_type);           n_cols = len(self.ascii_type[0])           
            x = n_cols

            for col in range(n_cols):
                x -= 1
                for row in range(n_rows):
                    if col == 0:  # first col
                        print(move_cursor_right(self.adj_indent)+color+ins_chr(self.adj_left_space+n_cols-1)+self.ascii_type[row][x]+ins_chr(self.adj_right_space)+"\033[0m")
                    elif col == (n_cols - 1 ): # last col
                        print(move_cursor_right(self.adj_indent+self.adj_left_space)+color+self.ascii_type[row][x]+"\033[0m")
                        
                    else: # middle cols
                        print(move_cursor_right(self.adj_indent+self.adj_left_space+n_cols-ctrl_cols)+color+self.ascii_type[row][x]+"\033[0m")
                
                
                ctrl_cols += 1
                time.sleep(retardo)
                if col == (n_cols -1): pass
                else:                  crs.jumpTo(qty = n_rows, direction= Move.UP)

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
            print("")
            print(f"    {self.ascii_type} ascii_type is NOT supported by custom_print Module")
            print("    Form more help visit: ")
            print("    https://github.com/acma82/Custom_Print/tree/main/readme ")
            print()
            print("    For help on the Terminal: custom_print AsciiArt")
            print()
            print("    Thank you for using custom_print")
            exit()

  
