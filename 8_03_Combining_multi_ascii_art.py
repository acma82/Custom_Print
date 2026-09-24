import custom_print as cp


cp.ins_newline(n=2)
print("    Type of Letters.")
print("    Python: Doom, IS: Mono, PRETTY: Epic")
cp.ins_newline(n=2)

row_1 = ["Py    ",  "th      ",  "on  " ] # 0.  Letters
row_2 = [f"{cp.ins_chr(n=18)}", "IS    ", f"{cp.ins_chr(n=10)}"]
row_3 = ["PR", "ET", "TY"]

data =  [[True,  True,  True],         # 1.  Bold
        [152,   115,   202  ],         # 2.  bg
        [16,    17,    23   ],         # 3.  Fg
        [False, False, False],         # 4.  italic
        [False, False, False],         # 5.  underline
        [False, False, False],         # 6.  strikes
        [False, False, False],         # 7.  blinking
        [False, False, False],         # 8.  dims
        [False, False, False],         # 9.  hiddends
        [False, False, False],         # 10. inverse
        [2,     2,     2    ],         # 11. left_space
        [1,     1,     1    ],         # 12. middle_space
        [2,     2,     2    ]]         # 13. right_space



multi_msg = cp.AsciiArt()
multi_msg.delay_ms = 40
multi_msg.set_layout = "h" # cp.Layout.HORIZONTAL #VERTICAL

data.insert(0, row_1)
multi_msg.ascii_type = cp.Ascii_Letter.DOOM
multi_msg.print_multi_ascii_art(data=data)


multi_msg.ascii_type = cp.Ascii_Letter.MONO
data[0] = row_2
multi_msg.print_multi_ascii_art(data=data)

multi_msg.ascii_type = cp.Ascii_Letter.EPIC
data[0] = row_3
multi_msg.print_multi_ascii_art(data=data)




