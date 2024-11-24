'''
FontStyle Class
Methods Available:
    print_style(msg)
    reset_style()
    start_style()
    stop_style()
'''

import custom_print as cp
fs = cp.FontStyle()

fs.fg        = 231
fs.bg        = 90
fs.indent    = 10
fs.bold      = True
fs.blinking  = True
fs.underline = True
fs.strike    = True
fs.italic    = True
# fs.dim = True
# fs.hidden = True
# fs.next_line = False

cp.ins_newline(2)
fs.print_style(" FontStyle ")
print("  Normal Font...!")



cp.ins_newline(2)
print(f"{fs.style_on()} Font Style {fs.style_off()}")
print(fs.style_on() + " Font Style " + fs.style_off())


cp.ins_newline(2)
fs.reset_style()
fs.print_style("Default Style ")
cp.ins_newline(2)
print(f"{fs.style_on()} Default Style {fs.style_off()}")
