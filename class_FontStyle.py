import fancyprint as fp
import time
fs = fp.FontStyle()

fs.bold = True; 
fs.blinking = True
fs.underline = True
fs.strike = True
fs.italic = True
fs.fg = 231
fs.bg = 90
fs.indent = 10
# fs.dim = True
# fs.hidden = True
# fs.next_line = False

fs.print_style(" hello there ")
fp.terminal_bell()


print(f"{fs.get_style()}hello there{fs.reset_style()}")


