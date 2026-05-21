import custom_print as cp
crs = cp.Cursor()

def print_multi_ascii_art(self,lista, sets_bold, sets_bg, sets_fg, sets_italic, sets_underline, sets_strike, sets_blinking, sets_dim, sets_hidden, sets_inverse ):
    # adj_indent cannot be changed or it will be messy
    ctrl_dist = 0
    symbol_chrs = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "[", "]", "\\", ";", "'",  ",", ".", "/",
                    "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|",  ":", "\"", "<", ">", "?", " "]
    
    symbol_name = ["backtick", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero", "minus", "equal",
                    "open_bracket", "close_bracket", "backward_slash", "semicolon", "apostrophe", "comma", "period",   "forwad_slash",
                    "tilde", "exclamation", "arroba", "pound", "dollar", "percent", "caret", "ampersand", "asterisk",  "open_parenthesis",
                    "close_parenthesis", "underscore", "plus", "pipe", "open_curly", "close_curly", "colon", "quotation","less_than",
                    "greater_than", "question", "space"]

        # ------------------------------------------------------------ Finding the Type of Ascii Letters       
    pylo = cp.PyLO()

    if self.ascii_type == cp.Ascii_Letter.Alpha:
        #  Alpha only have uppercase available
        result = pylo.update_case(data=lista, header_case=pylo.Case.UPPER, data_case=pylo.Case.UPPER, update=False)
        

    elif self.ascii_type == cp.Ascii_Letter.Crazy:
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

        # Deep copy
        tempo_lista = []



        for col in range(len(result[row])):
            self.print_ascii_art(result[row][col])
            text = result[row][col]
            for n in text:
                try:
                    list_name = eval("cp."+self.ascii_type+"_"+ n)
                    letter_width = len(list_name[0])
                    ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row. (Letters or Numbers)


                except:
                    if n in symbol_chrs:
                        position = symbol_chrs.index(n)
                        symbol_chr = symbol_name[position]
                        try:
                            list_name  = eval("cp."+self.ascii_type+"_"+ symbol_chr)
                            letter_width = len(list_name[0])
                            ctrl_dist = ctrl_dist + letter_width # contains all the width of the letters inside the row. (Symbols)
                        except:
                            list_name = eval("cp."+self.ascii_type+"_"+ "NA")
                            letter_width = len(list_name[0])
                            ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row, if the letter does not exist, here


                    else:
                        list_name = eval("cp."+self.ascii_type+"_"+ "NA")
                        letter_width = len(list_name[0])
                        ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row, if the letter does not exist, here


        if (len(result[row])) >= 2: self.adj_indent = self.adj_indent+self.adj_left_space+ ctrl_dist+self.adj_middle_space+self.adj_right_space
        else:                      self.adj_indent = self.adj_indent+self.adj_left_space+ ctrl_dist+self.adj_right_space
        ctrl_dist = 0

         # Make sure always exist a letter: A or a in all the Letters Type
        letter_height = 0

        try:
            list_name = eval("cp."+self.ascii_type+"_Letters."+self.ascii_type+"_A")
            letter_height = len(list_name)
        except:
            list_name = eval("cp."+self.ascii_type+"_Letters."+self.ascii_type+"_a")
            letter_height = len(list_name) 

        crs.jumpTo(qty=letter_height, direction = cp.Move.UP)  # Letter_height

    crs.jumpTo(qty=letter_height, direction = cp.Move.DOWN)

