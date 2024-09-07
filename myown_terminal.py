# import time

# print('''
# Terminal...!
# ''')
# a=1
# while(a>0):
#    enter = input("<<< ")

#    if enter == "hello":
#       print("doing hello\n")


#    elif (enter == "goodbye"):
#       print("doing goodbye")

#    elif (enter == "q"):
#       a=0

#    else:
#       print("not in dict")




class FontStyle():   
   def __init__(self):
      # self.reset = "\033[0m"
      self.bg = -1
      self.fg = -1
      self.bold  = False      
      self.dim   = False
      self.italic= False
      self.underline = False
      self.blinking  = False
      self.inverse   = False
      self.hidden    = False
      self.strike    = False
      self.indent    = 0
      self.next_line = True

      
   def set_font(self)->str:
      '''
   ----------------------------------------------------------------------------
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

      if (self.hidden == True): settings = settings + "\033[8m"
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


fs = FontStyle()
fs.bold = True
fs.dim = True
fs.blinking = True
fs.underline = True
fs.strike = True
fs.italic = True
fs.fg = 11
fs.bg = 90
fs.indent = 10
# fs.hidden = True
# fs.next_line = False

fs.print_style("hello there")

print("hello")


print(f"{fs.get_style()}hello there{fs.reset_style()}")

print(f"{fs.get_style()}\033[7m hello there{fs.reset_style()}")

