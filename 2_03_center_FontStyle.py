import custom_print as cp
fs = cp.FontStyle()
fs.fg = 231
fs.bg = 90

paragraph = '''
 This is the Module Docstrings 
 Trailing WhiteSpace refers to any whitespace characters 
 at the end of a line of code or string. 
 missing-final-newline refers to set 
 the last empty line at the end of the code 
 pylint practis.py 
'''

cp.ins_newline(2)

fs.align = cp.Align.CENTER
fs.forced_align = False
fs.bg_top_lines = 1
fs.bg_bottom_lines = 1
fs.print_style(paragraph)

cp.ins_newline(2)

fs.align = cp.Align.CENTER
fs.forced_align = True
fs.bg_top_lines = 3            # by default top and bottom lines are set to 0
fs.bg_bottom_lines = 3
fs.print_style(paragraph)