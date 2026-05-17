import custom_print as cp
crs = cp.Cursor()

# set_font(bold=False,bg=-1,fg=-1,italic=False,underline=False,strike=False,blinking=False,dim=False,hidden=False,inverse=False)

def print_multi_ascii_art(self,lista, sets_bold, sets_bg, sets_fg,):
    # adj_indent cannot be changed or it will be messy
    ctrl_dist = 0
    for row in range(len(lista)):
        self.bold = sets_bold[row]
        self.bg = sets_bg[row]
        self.fg = sets_fg[row]

        # self.underline = set_underline[row]               # you can add more settings here.
        # self.blinking = set_blinking[row]
        # self.italic = set_italic[row]

        for col in range(len(lista[row])):
            self.print_ascii_art(lista[row][col])
            text = lista[row][col]
            for n in text:
                try:
                    letter_width = eval("cp."+self.ascii_type+"_"+ n +"_width")
                    ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row, if the letter exist, here
                except:
                    letter_width = eval("cp."+self.ascii_type+"_"+ "NA" +"_width")
                    ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row, if the letter does not exist, here


        if (len(lista[row])) >= 2: self.adj_indent = self.adj_indent+self.adj_left_space+ ctrl_dist+self.adj_middle_space+self.adj_right_space
        else:                      self.adj_indent = self.adj_indent+self.adj_left_space+ ctrl_dist+self.adj_right_space
        ctrl_dist = 0

        crs.jumpTo(qty=eval("cp."+ self.ascii_type + "_Letters.height"), direction = cp.Move.UP)  # self.ascii_type is the name of the type following the name

    crs.jumpTo(qty=eval("cp."+ self.ascii_type + "_Letters.height"), direction = cp.Move.DOWN)




msg = cp.Art()
msg.set_layout = "horizontal"
msg.set_bottom_line = True
msg.set_top_line    = True
msg.adj_indent = 2
msg.adj_left_space = 4
msg.adj_right_space = 6
msg.adj_middle_space = 2
msg.delay_ms = 100
msg.ascii_type = "Doh"
data = [["A"],["B"],["Y"]]
# fun,    class, data, bold_settings      bg_settings  fg_settings, you can add more settings 
print_multi_ascii_art(msg, data, [False,True,False], [87,90,11], [16,231,21])
