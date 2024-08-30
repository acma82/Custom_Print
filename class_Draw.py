import fancyprint as fp
drw = fp.Draw()
crs = fp.Cursor()

# single line box
drw.body = '\u2502'
drw.body     = '\u2500'       # 9,  line
drw.line(20, 4, 20,layout=fp.Layout.HORIZONTAL)
print()

drw.tail     = '\u250C'       # 13, left top corner
drw.head     = '\u2510'       # 14, right top corner
drw.body     = '\u2500'       # 9,  line

drw.line(-1,-1,25)             # horizontal
# drw.arrow(-1,1,10)
print()
drw.body = '\u2502'
drw.line(-1,-1,10,"vertical")

# rv = 10
# crs.jump(qty=9, direction="right")
# print("*")

drw.tail  = '\u2514'          # 16, left bottom corner
drw.head  = '\u2518'          # 15, right bottom corner
drw.body     = '\u2500'       # 9,  line
drw.line(-1,-1,25)             # Horizontal
#drw.arrow(-1,1,10)
print("\n")


# print("\u23FB")
