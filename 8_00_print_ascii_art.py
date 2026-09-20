import custom_print as cp

msg = cp.AsciiArt()
msg.set_layout = cp.Layout.VERTICAL
msg.adj_indent = 2
msg.delay_ms = 40
msg.bold = True
msg.bg = 21
msg.fg = 231

msg.print_ascii_art(msg=" Python 3.12 ")


                                                  