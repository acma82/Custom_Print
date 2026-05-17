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
    # msg.set_layout = "horizontal"
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


crs = cp.Cursor()




# def multi_art(lista=["A"]):
#     msg = cp.Art()
#     msg.set_bottom_line = True
#     msg.set_top_line    = True
#     # msg.set_layout = "horizontal"
#     msg.adj_indent = 2
#     msg.adj_left_space = 4
#     msg.adj_right_space = 6
#     msg.adj_middle_space = 2

#     msg.delay_ms = 100
#     msg.bold = True
#     msg.ascii_type = "Doh"


#     # Combining Colors and options    
#     set_bg = [87,90,11]  # we have 3 set of data
#     set_fg = [16,231,21]
#     # set_underline = [True,False,True]
#     # set_blinking = [True,True,False]
#     # set_italic = [True,False,True]

#     # adj_indent cannot be changed or it will be messy
#     ctrl_dist = 0
#     for row in range(len(lista)):
#         msg.bg = set_bg[row]
#         msg.fg = set_fg[row]
#         # msg.underline = set_underline[row]
#         # msg.blinking = set_blinking[row]
#         # msg.italic = set_italic[row]

#         for col in range(len(lista[row])):
#             msg.print_ascii_art(lista[row][col])
#             text = lista[row][col]
#             for n in text:
#                 try:
#                     letter_width = eval("cp."+msg.ascii_type+"_"+ n +"_width")
#                     ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row, if the letter exist, here
#                 except:
#                     letter_width = eval("cp."+msg.ascii_type+"_"+ "NA" +"_width")
#                     ctrl_dist = ctrl_dist + letter_width  # contains all the width of the letters inside the row, if the letter does not exist, here


#         if (len(lista[row])) >= 2: msg.adj_indent = msg.adj_indent+msg.adj_left_space+ ctrl_dist+msg.adj_middle_space+msg.adj_right_space
#         else:                      msg.adj_indent = msg.adj_indent+msg.adj_left_space+ ctrl_dist+msg.adj_right_space
#         ctrl_dist = 0

#         crs.jumpTo(qty=eval("cp."+ msg.ascii_type + "_Letters.height"), direction = cp.Move.UP)  # msg.ascii_type is the name of the type following the name

#     crs.jumpTo(qty=eval("cp."+ msg.ascii_type + "_Letters.height"), direction = cp.Move.DOWN)



# lista = [["AB"],["BC"],["DY"]]
# multi_art(lista)








import multi_art

data = [["AB"],["BC"],["DY"]]
msg = cp.Art()
msg.set_layout = "horizontal"
msg.set_bottom_line = True
msg.set_top_line    = True
msg.adj_indent = 2
msg.adj_left_space = 4
msg.adj_right_space = 6
msg.adj_middle_space = 2
msg.delay_ms = 100
msg.ascii_type = "Doh"

multi_art.multi_art(msg, data, [False,True,False], [87,90,11], [16,231,21])


































