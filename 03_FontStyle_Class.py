import fancyprint as fp
import time
fs = fp.FontStyle()

fs.fg = 231;         fs.bg = 90;            fs.indent = 10
fs.bold = True;      fs.blinking = True;    fs.underline = True
fs.strike = True;    fs.italic = True;        

# fs.dim = True;     fs.hidden = True;      fs.next_line = False

fp.ins_newline(2)
fs.print_style(" FontStyle ")
print("  Normal Font...!")



fp.ins_newline(2)
print(f"{fs.start_style()} Font Style {fs.stop_style()}")
print(fs.start_style() + " Font Style " + fs.stop_style())


fp.ins_newline(2)
fs.reset_style()
fs.print_style("Default Style ")
fp.ins_newline(2)
print(f"{fs.start_style()} Default Style {fs.stop_style()}")



