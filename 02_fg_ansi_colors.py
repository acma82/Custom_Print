import fancyprint as fp

mns = f'''
----------------------------------------------------------------------------
   import fancyprint as fp
   fp.fg_ansi_colors(bold=0, bg=-1)
   
   This function displays all foreground colors available in the fancyprint
     module. Two options for better visualization:
   
   1.- The option bold helps for font.
   2.- The option bg to visualize the foreground colors with a specific
         background color.

   Colors range from -1 to 256.
   To set the default color use -1 or 256.

   Example:
            fp.fg_ansi_colors(0,22)
           {fp.set_font(1,22,15)} fp.fg_ansi_colors(bg=32, bold=1) {fp.reset_font()}
----------------------------------------------------------------------------
'''
print(mns)

# fp.fg_ansi_colors(0,32)
fp.fg_ansi_colors(bold=1, bg=149, n_line=2)