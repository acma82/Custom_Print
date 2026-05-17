import custom_print as cp


# For Spanish Language (Mexico....!)
# print(cp.Unicode.UPPERCASE_N_TILDE) # Ñ
# print(cp.Unicode.LOWERCASE_N_TILDE) # ñ
# lista  = ["B","a",cp.Unicode.UPPERCASE_N_TILDE, cp.Unicode.LOWERCASE_N_TILDE]
# print(cp.Unicode.LOWERCASE_N_TILDE) # ñ
# print(cp.Unicode.UPPERCASE_N_TILDE) # Ñ

#-----------------------------------------------------------------------------------------
def art(dato):
    msg = cp.Art()
    msg.set_bottom_line = True
    msg.set_top_line    = True
    # msg.set_layout = cp.Layout.HORIZONTAL
    msg.adj_indent = 2
    msg.delay_ms = 100
    msg.bold = True
    msg.bg = 87
    msg.fg = 16
    msg.ascii_type = "Doh"
    msg.adj_left_space = 4
    msg.adj_right_space = 6
    msg.adj_middle_space = 2
    msg.print_ascii_art(dato)


dato = "ABC"
art(dato=dato)

