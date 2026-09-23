import custom_print as cp

# create the class and set the settings
msg = cp.AsciiArt()
msg.set_layout = cp.Layout.HORIZONTAL
msg.set_layout = cp.Layout.VERTICAL
msg.set_bottom_line = True
msg.set_top_line    = True
msg.adj_indent = 2
msg.adj_left_space = 3
msg.adj_middle_space = 0
msg.adj_right_space = 1
msg.delay_ms = 100
msg.ascii_type = cp.Ascii_Letter.STANDARD

# Isometric 1
#       ___           ___           ___       ___       ___     1
#      /\__\         /\  \         /\__\     /\__\     /\  \    2
#     /:/  /        /::\  \       /:/  /    /:/  /    /::\  \   3
#    /:/__/        /:/\:\  \     /:/  /    /:/  /    /:/\:\  \  4
#   /::\  \ ___   /::\~\:\  \   /:/  /    /:/  /    /:/  \:\  \ 5
#  /:/\:\  /\__\ /:/\:\ \:\__\ /:/__/    /:/__/    /:/__/ \:\__\6
#  \/__\:\/:/  / \:\~\:\ \/__/ \:\  \    \:\  \    \:\  \ /:/  /7
#       \::/  /   \:\ \:\__\    \:\  \    \:\  \    \:\  /:/  / 8
#       /:/  /     \:\ \/__/     \:\  \    \:\  \    \:\/:/  /  9
#      /:/  /       \:\__\        \:\__\    \:\__\    \::/  /   10
#      \/__/         \/__/         \/__/     \/__/     \/__/    11

msg.adj_middle_space = 4

data = [["Py",  "th",  "on" ],         # 0.  Letters
        [True,  True,  True ],         # 1.  Bold
        [152,   115,   202  ],         # 2.  bg
        [16,    17,    23   ],         # 3.  Fg
        [False, False, False],         # 4.  italic
        [False, False, False],         # 5.  underline
        [False, False, False],         # 6.  strikes
        [False, False, False],         # 7.  blinking
        [False, False, False],         # 8.  dims
        [False, False, False],         # 9.  hiddends
        [False, False , False],         # 10. inverse
        [2,     3,     1    ],         # 11. left_space
        [0,     4,     0    ],         # 12. middle_space
        [2,     3,     2    ]]         # 13. right_space

msg.print_multi_ascii_art(data=data)

print()

msg.print_ascii_art("H")
print(msg.adj_middle_space)

