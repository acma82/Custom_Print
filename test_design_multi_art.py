import custom_print as cp
import design_ascii_art as daa



# daa.art_logo_1(dato="ABC@2~", option=cp.Ascii_Letter.Alpha)
cp.ins_newline(n=2)
print("    Type of Letters.")
print("    Python: Doom, IS: Graceful, PRETTY: Epic")
cp.ins_newline(n=2)

daa.art_logo_2([["Py"], ["th"], ["on"]], cp.Ascii_Letter.Doom,0)
daa.art_logo_2([[cp.ins_chr(n=15, unicode=" ")],["  Is   "],[cp.ins_chr(n=15, unicode=" ")]], cp.Ascii_Letter.Graceful, 1)
daa.art_logo_2([["Pr"], ["et"], ["ty"]], cp.Ascii_Letter.Epic,2)


