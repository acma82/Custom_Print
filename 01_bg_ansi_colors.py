import fancyprint as fp

mns = f'''
----------------------------------------------------------------------------
   import fancyprint as fp
   fp.bg_ansi_colors(bold=0, fg=-1)
   
   This function displays all background colors available in the fancyprint
     module. Two options for better visualization:
   
   1.- The option bold for the font.
   2.- The option fg to visualize the background colors with a specific
         foreground color.

   Colors range from -1 to 256.
   To set the default color use -1 or 256.

   Example:
            fp.bg_ansi_colors(0,22)
           {fp.set_font(1,22,15)} fp.bg_ansi_colors(fg=0, bold=1) {fp.reset_font()}
----------------------------------------------------------------------------
'''
print(mns)

#fp.bg_ansi_colors(0,22)
fp.bg_ansi_colors(fg=0, bold=True, n_line=2)

