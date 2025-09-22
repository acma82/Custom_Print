import custom_print as cp
fs = cp.FontStyle()
fs.fg        = 231
fs.bg        = 23
fs.bold      = True
fs.bg_bottom_lines = True
fs.bg_top_lines    = True
fs.forced_align    = True        # by default is set to False


def get_msg(option)->str:
    msg = f'''
 Custom_Print...! 
 Align.{option} 
 force_align = False 
 Python3.12 '''
    return msg

cp.ins_newline(1)

option = "LEFT"
msg = get_msg(option)
fs.align = cp.Align.LEFT
fs.print_style(msg)


option = "CENTER"
msg = get_msg(option)
fs.align = cp.Align.CENTER
fs.print_style(msg)


option = "RIGHT"
msg = get_msg(option)
fs.align = cp.Align.RIGHT
fs.print_style(msg)


option = "JUSTIFY"
msg = get_msg(option)
fs.align = cp.Align.JUSTIFY
fs.indent = 12
fs.print_style(msg)

cp.ins_newline(2)

fs.align = "none"
fs.indent = 8
msg = get_msg(option)
fs.print_style(msg)

cp.ins_newline(1)



