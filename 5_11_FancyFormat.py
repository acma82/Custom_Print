import custom_print as cp


lst = [["Header 1", "Header 2", "Header 3", "Header 4"],
        ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
        ["Data 5",   "Data 6",   "Data 7",   "Data 8"  ]]


tbli = cp.FancyFormat()
tbli.header_bg   = 23;         tbli.data_bg   = 231
tbli.header_fg   = 231;        tbli.data_fg   = 21
tbli.header_bold = True;       tbli.data_bold = True
tbli.horizontal_line_bg  = 1;  tbli.adj_top_margin = 1
tbli.vertical_line_bg    = 1;  tbli.adj_top_space  = 1

tbli.inner_corner_bg  = 1
tbli.outer_corner_bg  = 1
tbli.header_corner_bg = 1
tbli.header_horizontal_line_on = True
tbli.bottom_horizontal_line_on = True
tbli.top_horizontal_line_on    = True
tbli.header_horizontal_line_bg = 1
tbli.header_vertical_line_bg   = 1



tbli.title_bg    = 231;                tbli.title_fg  = 16;      tbli.title_bold = True
tbli.title_align = cp.Align.CENTER;    tbli.title_msg = " NONE "

tbli.set_banded_row_on = True
tbli.banded_row_bg = 208
tbli.banded_row_fg = 231

tbli.header_horizontal_line_on = False
tbli.print_fancy_format(data=lst, style=cp.Line_Style.NONE)
tbli.title_msg = " SPACE_0"
tbli.print_fancy_format(lst, cp.Line_Style.SPACE_0)
tbli.title_msg = " SPACE_1"
tbli.print_fancy_format(lst, cp.Line_Style.SPACE_1)
tbli.title_msg = " SPACE_2"
tbli.print_fancy_format(lst, cp.Line_Style.SPACE_2)
tbli.title_msg = " SPACE_3 "
tbli.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_3)
tbli.title_msg = " SPACE_4 "
tbli.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_4)
tbli.title_msg = " SPACE_5 "
tbli.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_5)
tbli.title_msg = " SPACE_6 "
tbli.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_6)