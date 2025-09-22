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
fs.bg = 21
fs.fg = 231

cp.ins_newline(2)

print(f"{fs.style_on()} Font Style Line 1 ")
print(f" Font Style Line 2 ")
print(f" Font Style Line 3 {fs.style_off()}")
fs.reset_style()
print(f"{fs.style_on()} Default Style {fs.style_off()}")

cp.ins_newline(2)

fs.fg        = 231
fs.bg        = 90
fs.indent    = 10
fs.bold      = True
fs.blinking  = True
fs.underline = True
fs.strike    = True
fs.italic    = True

cp.ins_newline(2)
print(f"{fs.style_on()}Font Style {fs.style_off()}")
print(fs.style_on() + "Font Style " + fs.style_off())

cp.ins_newline(2)

