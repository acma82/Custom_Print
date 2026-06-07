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
    msg.set_layout = cp.Layout.HORIZONTAL
    # msg.set_layout = cp.Layout.VERTICAL
    msg.adj_indent = 2
    msg.delay_ms = 40
    msg.bold = True
    msg.bg = 87
    msg.fg = 16
    # msg.ascii_type = cp.Ascii_Letter.Alpha
    # msg.ascii_type = cp.Ascii_Letter.ANSI_Shadow
    # msg.ascii_type = cp.Ascii_Letter.Big
    # msg.ascii_type = cp.Ascii_Letter.Blocks
    # msg.ascii_type = cp.Ascii_Letter.Bulbhead
    msg.ascii_type = cp.Ascii_Letter.Colossal

    msg.adj_left_space = 4
    msg.adj_right_space = 6
    msg.adj_middle_space = 2
    msg.print_ascii_art(dato)




lista = [["ABCDE"],["FGHIJ"],[f"KLMN{cp.Unicode.UPPERCASE_N_TILDE}"],["OPQRS"],["TUVWX"],["YZ"],  # 27
         ["abcde"],["fghij"],[f"klmn{cp.Unicode.LOWERCASE_N_TILDE}"],["opqrs"],["tuvwx"],["yz"],  # 27
         ["`123"] ,["4567"] ,["890-"], ["=[]\\"],[";',./"],                                       # 21
         ["~!@#"], ["$%^&"], ["*()_"], [f"+{cp.Unicode.LEFT_CURLY_BRACKET}{cp.Unicode.RIGHT_CURLY_BRACKET}|"],[":\"<>? "]] # 22


ctrl = 0
for row in range(len(lista)):
    for col in range(len(lista[row])):
        if ctrl == 0:    print(f"  {cp.set_font(1,231,21)} Letters: {lista[row][col]} {cp.reset_font()}")
        elif ctrl == 25: input(f"  {cp.set_font(1,231,21)} Enter to Continue with: {lista[row][col]}and space {cp.reset_font()}")
        else:            input(f"  {cp.set_font(1,231,21)} Enter to Continue with: {lista[row][col]} {cp.reset_font()}")
        art(dato=lista[row][col])
    ctrl += 1
    

