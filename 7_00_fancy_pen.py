import custom_print as cp

pen = cp.Pen()

pen.draw_line_fg = cp.No.ORANGE
pen.draw_line(15)
pen.draw_line_bg = cp.No.AVOCADO_GREEN
cp.ins_newline(2)
pen.fill_color = True
pen.draw_rectangle(15,5, cp.Line_Style.SINGLE_HEAVY)