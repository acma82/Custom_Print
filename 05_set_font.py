import fancyprint as fp

msg = '''
----------------------------------------------------------------------------
   import fancyprint as fp

   This function changes the attributes of the font (bold, bg, fg).
   
   Example:
            print(fp.set_font(1,11,21)+ " Python is " + fp.set_font(0,1)+
               " Wonderful."+fp.reset_font())
            
            print(f"{fp.set_font(bold=0, bg=22, fg=0)} Python
               {fp.set_font(1,90,7)} Language.{fp.reset_font()}")
----------------------------------------------------------------------------
'''
print(msg)
print(fp.set_font(1,11,21)+ " Python is " + fp.set_font(1,231,0)+\
       " Wonderful."+fp.reset_font())
print()
print(f"{fp.set_font(bold=True, bg=22, fg=231)} Python\
       {fp.set_font(1,90,7)} Language.{fp.reset_font()}")

fp.ins_newline(2)
style1 = fp.set_font(bold=True, bg=90, fg=231, italic=True, underline=True, blink=True, strike=False)
print(f"{style1} Author of fancyprint module.....! {fp.reset_font()}")

fp.ins_newline(1)
style1 = fp.set_font(bold=True, bg=90, fg=231, italic=True, underline=False, blink=False, strike=True)
print(f"{style1} Author of fancyprint module.....! {fp.reset_font()}")

fp.ins_newline(1)
style1 = fp.set_font(bold=True, bg=90, fg=231, italic=True, underline=False, blink=False, strike=False)
print(f"{style1} Author of fancyprint module.....! {fp.reset_font()}")