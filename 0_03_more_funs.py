import custom_print as cp
crs = cp.Cursor()

#+-----------------------------------------------------------------------------------+
#|    ins_newline(n), set_font(*args), and reset_font(), ins_chr() Functions      |
#+-----------------------------------------------------------------------------------+
cp.ins_newline(2)
print(cp.set_font(1,11,21) + " Python is " + cp.set_font(0,1) + " Wonderful." + cp.reset_font())


color1 = cp.set_font(1,90,231)
color2 = cp.set_font(1,231,1)
color3 = cp.set_font(1,14,0)
cp.ins_newline(1)
print(f"{color1} Python {color2}{cp.ins_chr(12,".")}{color3} Amazing...! {cp.reset_font()}")
cp.ins_newline(2)


print("Hola",end=""); crs.jumpTo(2, cp.Move.LEFT)   
#+-----------------------------------------------------------------------------------+
#|    move_cursor_right Function                                                     |
#+-----------------------------------------------------------------------------------+
print(f"{cp.move_cursor_right(20)}Miguel Angel")   # This move the cursor only


cp.ins_newline(1)
print("Hola",end=""); crs.jumpTo(2, cp.Move.LEFT)  # This insert empty spaces to move the cursor
print(f"{cp.ins_chr(20," ")}Miguel Angel")
cp.ins_newline(2)


#+-----------------------------------------------------------------------------------+
#|    Subscript and SuperScript Function                                             |
#+-----------------------------------------------------------------------------------+
print(f"Water -> H{cp.subscript(2)}O    Power: X{cp.superscript("5+v")} + 5")


