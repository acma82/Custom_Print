import custom_print as cp

#-----------------------------------------------------------------------------------------
msg = cp.Art()
# msg.set_bottom_line = True
# msg.set_top_line    = True
# msg.set_layout = "horizontal"
msg.adj_space  = 5
msg.adj_indent = 10
msg.delay_ms = 100

msg.bold = True
msg.bg = 87
msg.fg = 16
# option = "Doh"
option = "Alpha"
lista  = ["B","A","B","aY"]
# # lista  = ["B"]
# # lista = ["C","A","B"]
msg.print_ascii_art(lista, option)

