def clean():
   '''
----------------------------------------------------------------------------      
   It cleans the terminal and return the cursor to home.
   It uses ansi code.
----------------------------------------------------------------------------
   '''


def clear():
   '''
----------------------------------------------------------------------------      
   It cleans the terminal and return the cursor to home.
   It uses the system command.
----------------------------------------------------------------------------
   '''


def erase():
   '''
----------------------------------------------------------------------------      
   It cleans the terminal and the cursor remain in the same position.
   It uses ansi code.
----------------------------------------------------------------------------
   '''


def dimensions():
   '''
----------------------------------------------------------------------------      
   It returns the size of the actual terminal: cols, rows.
----------------------------------------------------------------------------
   '''


def resize(rows:int=25, cols:int=80)->None:
   '''
----------------------------------------------------------------------------      
   It resizes the terminal.
----------------------------------------------------------------------------
   '''


def ins_chr(n_space=1):
   '''
----------------------------------------------------------------------------
   import fancyprint as fp
   
   fp.ins_chr(x)

   This function inserts x number of spaces between words.
   
   Example:
           print(f"Hello{fp.ins_chr(40)}There")
           
           print("Hello"+fp.ins_chr(40)+"There")
----------------------------------------------------------------------------
'''


def ins_newline(nl=1):
   '''
----------------------------------------------------------------------------
   import fancyprint as fp

   fp.ins_newline(int)

   This function inserts x number of lines.    
   
   Example:
           print("Python 3")
           fp.ins_newline(3)
           print("is amazing...!")
----------------------------------------------------------------------------
'''


def bg_ansi_colors(bold=False, fg=-1, n_line=0):
   '''
----------------------------------------------------------------------------
   import fancyprint as fp
   
   fp.bg_ansi_colors(bool, int, int)
   
   This function displays all background colors available in the fancyprint
      module. Three options for better visualization:
   
   1.- The option bold for the font (True/False).
   2.- The option fg to visualize the background colors with a specific
         foreground color.
   3.- It insert lines to have space between them.

   Colors range from -1 to 256.
   To set the default color use -1 or 256.

   Example:
            fp.bg_ansi_colors(0,22,1)
            fp.bg_ansi_colors(fg=0, bold=1, n_line=1)
----------------------------------------------------------------------------
'''


def fg_ansi_colors(bold=False, bg=-1, n_line=0):
   '''
----------------------------------------------------------------------------
   import fancyprint as fp

   fl.fg_ansi_colors(bool, int, int)
   
   This function displays all foreground colors available in the fancyprint
      module. Two options for better visualization:
   
   1.- The option bold helps for font.
   2.- The option bg to visualize the foreground colors with a specific
         background color.
   3.- It insert lines to have space between them.

   Colors range from -1 to 256.
   To set the default color use -1 or 256.

   Example:
            fl.fg_ansi_colors(0,22,1)
            fl.fg_ansi_colors(bg=32, bold=0, n_line=1)
----------------------------------------------------------------------------
'''


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


def terminal_bell():
   '''
----------------------------------------------------------------------------
   This function makes sound of the terminal bell.  
----------------------------------------------------------------------------
'''
