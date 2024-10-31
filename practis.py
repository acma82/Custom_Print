import fancyprint as fp
pen = fp.Pen()

tlb = fp.FancyFormat()
lst = [["Header 1","Header 2","Header 3","Header 4"],
       ["R2C1","R2C2","R2C3","R2C4"],
       ["R3C1","R3C2","R3C3","R3C4"],
       ["R4C1","R4C2"]]

tlb.msg_title = " Title "
tlb.bold_title = True
tlb.fg_title = 21
tlb.bg_title = 231
tlb.align_title = fp.Align.CENTER

tlb.bg_header = 90
tlb.fg_header = 231
tlb.horizontal_line_under_header_on = True

tlb.align_data = fp.Align.CENTER
tlb.fg_data = 14

tlb.msg_footnote = " Footnote "
tlb.align_footnote = fp.Align.RIGHT
tlb.bold_footnote = True
tlb.bg_footnote = 231
tlb.fg_footnote = 21

print("\n")

tlb.print_fancy_format(lst)

print("\n")
lst = [["Header"],["R2C1"],["R3C1"],["R4C1"]]
tlb.print_fancy_format(lst, fp.Line_Style.SINGLE)
fp.ins_newline(3)


pen.adj_indent = 8

pen.draw_line(size=20, layout=fp.Layout.HORIZONTAL, tail=fp.Unicode.BLACK_LEFT_POINTING_TRIANGLE,
              body=fp.Unicode.EM_DASH, head=fp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE)
print()
pen.adj_indent = 14
pen.bg_draw_line = 90; pen.fg_draw_line = 231
pen.refill_bg_color = True
pen.draw_rectangle(length=8, width=4, style=fp.Line_Style.DOUBLE)


paragraph = '''
 Guido van Rossum, a Dutch programmer, created Python in the late 1980s
as a hobby project. He started working on it in December 1989 at Cent-
rum Wiskunde & Informatica (CWI) in the Netherlands.

Python was first released on February 20, 1991. Python was named after
the 1970s BBC comedy sketch series Monty Python's Flying Circus.
'''

msg = fp.FancyMessage()
msg.msg_title = "TITLE"
msg.msg_footnote = "FOOTNOTE"
msg.print_fancy_message(paragraph)
fp.ins_newline(2)
msg.msg_note = "Python"
msg.print_fancy_note(paragraph)
