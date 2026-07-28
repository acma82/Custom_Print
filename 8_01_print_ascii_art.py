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
    # msg.set_layout = cp.Layout.HORIZONTAL
    msg.set_layout = cp.Layout.VERTICAL
    msg.adj_indent = 10
    msg.delay_ms = 40
    msg.bold = True
    msg.bg = 90
    msg.fg = 231
    # msg.ascii_type = cp.Ascii_Letter.Alpha        # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.ANSI_Shadow  # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Big          # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Blocks       # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Bulbhead     # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Classy       # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Colossal     # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Crazy        # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Doh          # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Doom         # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Epic         # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Graceful     # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Larry        # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Money_NE     # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Money_NW     # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Money_SE     # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Money_SW     # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Mono         # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Moon         # checked (spaces and invalid characters,\)
    msg.ascii_type = cp.Ascii_Letter.Moon2        # Does not respect bg and fg colors. # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Roman        # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Standard     # checked (spaces and invalid characters,\)
    # msg.ascii_type = cp.Ascii_Letter.Sweet        # checked (spaces and invalid characters,\)
    
    

    # msg.set_top_line    = False
    # msg.set_bottom_line = False
    
    msg.adj_left_space   = 1
    msg.adj_right_space  = 1
    msg.adj_middle_space = 2
    msg.print_ascii_art(dato)


# art("(")
# exit()
                                                                      



# ABC in group of 5 and 4
# lista = [["ABCDE"],["FGHIJ"],[f"KLMN{cp.Unicode.UPPERCASE_N_TILDE}"],["OPQRS"],["TUVWX"],["YZ"],  # 27  Upper Case
#          ["abcde"],["fghij"],[f"klmn{cp.Unicode.LOWERCASE_N_TILDE}"],["opqrs"],["tuvwx"],["yz"],  # 27  Lower Case
#          ["`123"] ,["4567"] ,["890-"], ["=[]\\"],[";',./"],                                       # 21  Symbols (Shift_Off)
#          ["~!@#"], ["$%^&"], ["*()_"], [f"+{cp.Unicode.LEFT_CURLY_BRACKET}{cp.Unicode.RIGHT_CURLY_BRACKET}|"],[":\"<>? "]] # 22 Symbols Shift_On

# ctrl = 0
# for row in range(len(lista)):
#     for col in range(len(lista[row])):
#         if ctrl == 0:    print(f"  {cp.set_font(1,231,21)} Letters: {lista[row][col]} {cp.reset_font()}")
#         elif ctrl == 25: input(f"  {cp.set_font(1,231,21)} Enter to Continue with: {lista[row][col]}and space {cp.reset_font()}")
#         else:            input(f"  {cp.set_font(1,231,21)} Enter to Continue with: {lista[row][col]} {cp.reset_font()}")
#         art(dato=lista[row][col])
#     ctrl += 1
    


# ABC individually
# lista = f"ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz`1234567890-=[]\\;',./~!@#$%^&*()_+{cp.Unicode.LEFT_CURLY_BRACKET}{cp.Unicode.RIGHT_CURLY_BRACKET}|:\"<>?"
# for l in lista:    
#     # print(f"{cp.set_font(1,231,21)} Letter:{l}, Enter to Continue {cp.reset_font()}")
#     input(f"{cp.set_font(1,231,21)} Letter:{l}, Enter to Continue {cp.reset_font()}")
#     art(dato=l)


art(f"AHXYENLL{cp.Unicode.UPPERCASE_N_TILDE}")
# print("\n\n")
# print("hello")
# print("pp _ _ \u0305")
# for l in cp.Moon2_Letters.Moon2_A:
#     print(f"{l}{cp.reset_font()}")



