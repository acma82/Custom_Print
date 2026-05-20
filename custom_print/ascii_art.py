import custom_print as cp
crs = cp.Cursor()

def print_multi_ascii_art(self,lista, sets_bold, sets_bg, sets_fg, sets_italic, sets_underline, sets_strike, sets_blinking, sets_dim, sets_hidden, sets_inverse ):
    # adj_indent cannot be changed or it will be messy
    ctrl_dist = 0
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
        symbol_chrs = ["?","~","@","!"]
        symbol_name = ["question","uno","arroba","dos"] 


        ctrl_dist = 0
        for col in range(len(lista[row])):
            self.print_ascii_art(lista[row][col])
            text = lista[row][col]
            for n in text:
                try:
                    list_name = eval("cp."+self.ascii_type+"_"+ n)
                    letter_width = len(list_name[0])
                    ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row, if the letter exist, here


                except:
                    if n in symbol_chrs:
                        position = symbol_chrs.index(n)
                        symbol_chr = symbol_name[position]
                        list_name  = eval("cp."+self.ascii_type+"_"+ symbol_chr)
                        letter_width = len(list_name[0])
                        ctrl_dist = ctrl_dist + letter_width

                    else:
                        list_name = eval("cp."+self.ascii_type+"_"+ "NA")
                        letter_width = len(list_name[0])
                        ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row, if the letter does not exist, here


        if (len(lista[row])) >= 2: self.adj_indent = self.adj_indent+self.adj_left_space+ ctrl_dist+self.adj_middle_space+self.adj_right_space
        else:                      self.adj_indent = self.adj_indent+self.adj_left_space+ ctrl_dist+self.adj_right_space
        ctrl_dist = 0

        crs.jumpTo(qty=eval("cp."+ self.ascii_type + "_Letters." + self.ascii_type + "_height"), direction = cp.Move.UP)  # self.ascii_type is the name of the type following the name

    crs.jumpTo(qty=eval("cp."+ self.ascii_type + "_Letters." + self.ascii_type + "_height"), direction = cp.Move.DOWN)

