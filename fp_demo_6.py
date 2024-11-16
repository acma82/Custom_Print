'''
Demo 6 very simple...!
'''

import fancyprint as fp

if __name__ == "__main__":
    tbl = fp.FancyFormat()

    
    # lst = [["Header 1"],
    #        ["Data 1"  ],
    #        ["Data 5"  ]]
    
    # lst = [["Header 1", "Header 2"],
    #        ["Data 1",   "Data 2"  ],
    #        ["Data 5",   "Data 6"  ]]

    # lst = [["Header 1", "Header 2", "Header 3"],
    #        ["Data 1",   "Data 2",   "Data 3"  ],
    #        ["Data 5",   "Data 6",   "Data 7"  ]]

    lst = [["Header 1", "Header 2", "Header 3", "Header 4"],
           ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
           ["Data 5",   "Data 6",   "Data 7",   "Data 8"  ]]
        
#     lst = [["Header 1", "Header 2", "Header 3", "Header 4", "Header 5"],
#            ["Data 1",   "Data 2",   "Data 3",   "Data 4",  "Data 5"],
#            ["Data 6",   "Data 6",   "Data 7",   "Data 8",  "Data 9"]]
    
#     lst = [["Header 1", "Header 2", "Header 3", "Header 4", "Header 5", "HEADER"],
#            ["Data 1",   "Data 2",   "Data 3",   "Data 4",  "Data 5",    "DATA"],
#            ["Data 6",   "Data 6",   "Data 7",   "Data 8",  "Data 9",    "DATA"]]

    tbl.print_fancy_format(data=lst, style=fp.Line_Style.NONE)
    
    # bg colors
    tbl.bg_horizontal_line = 1
    tbl.bg_corner_chr = 1
    tbl.bg_inner_corner_chr = 1
    tbl.bg_corner_under_line_header = 1
    tbl.bg_under_line_header = 1
    tbl.bg_vertical_header_line_chr = 1
    tbl.bg_vertical_line = 1
    tbl.bg_header = 23
    tbl.fg_header = 231
    tbl.bold_header = True
    tbl.bg_data = 231
    tbl.fg_data = 21
    tbl.bold_data = True
    tbl.adj_top_margin = 2

    # tbl.align_data = fp.Align.LEFT
    # tbl.align_header = fp.Align.RIGHT
    
    # tbl.horizontal_line_under_header_on = True
    # tbl.middle_horizontal_line_on = True
    # tbl.top_horizontal_line_on = False
    # tbl.bottom_horizontal_line_on = False
    
    tbl.adj_indent = 4
    tbl.adj_space  = 4

    # tbl.bg_all_cell_data = False
    # tbl.bg_all_cell_header = False

    tbl.print_fancy_format(data=lst, style=fp.Line_Style.NONE)
    tbl.print_fancy_format(data=lst, style=fp.Line_Style.DOUBLE_SPACE)
    tbl.print_fancy_format(data=lst, style=fp.Line_Style.NONE_SPACE)

    
    
    
    
    
    print(f"\n {fp.set_font(1,90,231)}  Manipulating the Space to obtain the same result....!  {fp.reset_font()}")
    
    tbl.top_left_corner_chr  = "  "
    tbl.top_right_corner_chr = "  "
    tbl.bottom_right_corner_chr = "  "
    tbl.bottom_left_corner_chr  = "  "
    tbl.left_vertical_line_chr  = "  "
    tbl.right_vertical_line_chr = "  "

    # tbl.top_horizontal_line_chr = " "
    # tbl.bottom_horizontal_line_chr = " "

    # Multiple Horizontal Data
    tbl.middle_top_corner_chr = "  "
    tbl.middle_vertical_line_chr = "  "
    tbl.middle_bottom_corner_chr = "  "

    # Multiple Vertical Data
    tbl.left_vertical_header_line_chr  = "  "
    tbl.right_vertical_header_line_chr = "  "
    tbl.left_corner_line_under_header_chr  = "  "
    tbl.right_corner_line_under_header_chr = "  "

    tbl.left_lateral_corner_chr  = "  "
    tbl.right_lateral_corner_chr = "  "

    # Matrix Data
    tbl.middle_vertical_header_line_chr = "  "
    tbl.middle_corner_line_under_header_chr = "  "
    tbl.middle_inner_corner_chr = "  "   
    tbl.print_fancy_format(data=lst, style=fp.Line_Style.CUSTOMIZED)

    

    tbl.middle_vertical_header_line_chr = ""
    tbl.middle_top_corner_chr = ""
    tbl.middle_vertical_line_chr = ""
    tbl.middle_bottom_corner_chr = ""
    tbl.print_fancy_format(data=lst, style=fp.Line_Style.CUSTOMIZED)



    tbl.top_horizontal_line_chr    = " "
    tbl.bottom_horizontal_line_chr = " "
    tbl.print_fancy_format(data=lst, style=fp.Line_Style.CUSTOMIZED)
