import custom_print as cp

msg = cp.Art()
msg.description_ascii_letters()


print(cp.reset_font())

cp.ins_newline(5)


msg = cp.Art()
msg.set_layout = cp.Layout.VERTICAL
msg.adj_indent = 2
msg.delay_ms = 40
msg.bold = True
msg.bg = 87
msg.fg = 16


msg.print_ascii_art("HELLO")


                                                  