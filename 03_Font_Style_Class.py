'''
FontStyle Class
Methods Available:
    print_style(msg)
    reset_style()
    start_style()
    stop_style()
'''

import source.custom_print as cp
fs = cp.FontStyle()

print("\n")
fs.bg = 21
fs.fg = 231
print(f"{fs.style_on()} Font Style Line 1 ")
print(f" Font Style Line 2 ")
print(f" Font Style Line 3 {fs.style_off()}")
fs.reset_style()
print(f"{fs.style_on()} Default Style {fs.style_off()}")

print("\n")


fs.fg        = 231
fs.bg        = 90
fs.indent    = 10
fs.bold      = True
fs.blinking  = True
fs.underline = True
fs.strike    = True
fs.italic    = True

cp.ins_newline(2)
fs.print_style(" FontStyle ")
print("  Normal Font...!")



cp.ins_newline(2)
print(f"{fs.style_on()}Font Style {fs.style_off()}")
print(fs.style_on() + "Font Style " + fs.style_off())


cp.ins_newline(2)
fs.print_style("Justify Using indent")
cp.ins_newline(2)
fs.reset_style()
fs.print_style("Justify Using indent")
cp.ins_newline(2)

fs.fg        = 231
fs.bg        = 23
fs.bold      = True
fs.bg_bottom_lines = 1
fs.bg_top_lines = 1

msg = f'''
Full Name Author Here...!
Align.OPTION
force_align = False
Python3.12
'''
fs.align = cp.Align.LEFT
fs.print_style(msg)

fs.align = cp.Align.CENTER
fs.print_style(msg)

fs.align = cp.Align.RIGHT
fs.print_style(msg)

fs.align = cp.Align.JUSTIFY
fs.indent = 7
fs.print_style(msg)
cp.ins_newline(2)

fs.align = "none"
fs.print_style(msg)
cp.ins_newline(2)


print(f"{cp.ins_chr(90,"-")}")

msg = f'''
Full Name Author Here...!
Align.OPTION
force_align = True
Python3.12
'''

cp.ins_newline(2)
fs.force_align = True
fs.align = cp.Align.LEFT
fs.print_style(msg)

fs.align = cp.Align.CENTER
fs.print_style(msg)

fs.align = cp.Align.RIGHT
fs.print_style(msg)

fs.align = cp.Align.JUSTIFY
fs.indent = 12
fs.print_style(msg)

cp.ins_newline(2)
fs.align = "none"
fs.print_style(msg)
