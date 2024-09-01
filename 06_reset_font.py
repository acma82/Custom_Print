import fancyprint as fp

print(fp.set_font(1,11,21)+ " Python is " + fp.set_font(0,1)+\
       " Wonderful."+fp.reset_font())
print()
print(f"{fp.set_font(bold=0, bg=22, fg=0)} Python\
       {fp.set_font(1,90,7)} Language.{fp.reset_font()}")

print()
print(fp.set_font(1,11,21)+ " Python is ")
print(" Wonderful.")
print(fp.reset_font()+"Bye")

'''
----------------------------------------------------------------------------
   import fancyprint as fp

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