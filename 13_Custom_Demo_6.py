'''
Demo 6 very simple...!
'''

import source.source.custom_print as cp

if __name__ == "__main__":
    tbl = cp.FancyFormat()

    
    lst0 = [["Header 1"],
           ["Data 1"  ],
           ["Data 5"  ]]
    
    lst1 = [["Header 1", "Header 2"],
            ["Data 1",   "Data 2"  ],
            ["Data 5",   "Data 6"  ]]

    lst2 = [["Header 1", "Header 2", "Header 3"],
            ["Data 1",   "Data 2",   "Data 3"  ],
            ["Data 4",   "Data 5",   "Data 6"  ]]

    lst3 = [["Header 1", "Header 2", "Header 3", "Header 4"],
           ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
           ["Data 5",   "Data 6",   "Data 7",   "Data 8"  ]]
        
    lst4 = [["Header 1", "Header 2", "Header 3", "Header 4", "Header 5"],
            ["Data 1",   "Data 2",   "Data 3",   "Data 4",  "Data 5"],
            ["Data 6",   "Data 6",   "Data 7",   "Data 8",  "Data 9"]]
    
    lst5 = [["Header 1", "Header 2", "Header 3", "Header 4", "Header 5", "HEADER"],
            ["Data 1",   "Data 2",   "Data 3",   "Data 4",  "Data 5",    "DATA"],
            ["Data 6",   "Data 6",   "Data 7",   "Data 8",  "Data 9",    "DATA"]]

    # tbl.print_fancy_format(data=lst, style=cp.Line_Style.NONE)
    #-----------------------------------------------------------------------------------
    # Red                                                                              -
    #-----------------------------------------------------------------------------------
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

    # tbl.align_data = cp.Align.LEFT
    # tbl.align_header = cp.Align.RIGHT
    
    # tbl.horizontal_line_under_header_on = True
    # tbl.middle_horizontal_line_on = True
    # tbl.top_horizontal_line_on = False
    # tbl.bottom_horizontal_line_on = False
    
    tbl.adj_indent = 4
    tbl.adj_space  = 4

    tbl.top_left_corner_chr  = "  "
    tbl.top_right_corner_chr = "  "
    tbl.bottom_right_corner_chr = "  "
    tbl.bottom_left_corner_chr  = "  "
    tbl.left_vertical_line_chr  = "  "
    tbl.right_vertical_line_chr = "  "

    # tbl.top_horizontal_line_chr = " "
    tbl.bottom_horizontal_line_chr = " "

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
    tbl.middle_corner_line_under_header_chr = "  "  # when more than one column headers
    tbl.middle_inner_corner_chr = "  "
    tbl.print_fancy_format(data=lst3, style=cp.Line_Style.CUSTOMIZED)

    tbl.horizontal_line_under_header_on = True
    tbl.middle_horizontal_line_on = True
    
    tbl.print_fancy_format(data=lst3, style=cp.Line_Style.CUSTOMIZED)  
    
    tbl.top_horizontal_line_chr    = " "
    tbl.middle_horizontal_line_chr = " "
    tbl.print_fancy_format(data=lst3, style=cp.Line_Style.CUSTOMIZED)
    tbl.horizontal_line_under_header_on = False
    tbl.middle_horizontal_line_on = False

            
      
    # Vertical Line Section
    tbl.middle_vertical_line_chr = ""
    
    # Middle Corner Section
    tbl.middle_top_corner_chr   = ""
    tbl.middle_bottom_corner_chr = ""
    tbl.middle_inner_corner_chr = ""
        
    # Header Section  Only for Matrix List
    tbl.middle_vertical_header_line_chr = ""  
    tbl.print_fancy_format(data=lst3, style=cp.Line_Style.CUSTOMIZED)



    tbl.horizontal_line_under_header_on = True
    tbl.middle_horizontal_line_on = True
    tbl.horizontal_line_under_header_chr = " "  # When number of cols >= 2 and horizontal_line_under_header_on = True


    # when horizontal_line_under_header_on = True. With NONESPACE
    tbl.middle_corner_line_under_header_chr = ""
    tbl.print_fancy_format(data=lst3, style=cp.Line_Style.CUSTOMIZED)

    lst = [["Header 1"], ["Header 2"], ["Header 3"], ["Header 4"]]
    tbl.print_fancy_format(data=lst, style=cp.Line_Style.CUSTOMIZED)

    tbl.horizontal_line_under_header_on = False
    tbl.middle_horizontal_line_on = False
    tbl.print_fancy_format(data=lst, style=cp.Line_Style.CUSTOMIZED)

    #-----------------------------------------------------------------------------------
    # Blue                                                                             -
    #-----------------------------------------------------------------------------------
    tbl1 = cp.FancyFormat()
    # bg colors
    tbl1.bg_horizontal_line = 21
    tbl1.bg_vertical_line   = 21
    tbl1.bg_corner_chr      = 21

    tbl1.bg_inner_corner_chr  = 21
    tbl1.bg_under_line_header = 21

    tbl1.bg_corner_under_line_header = 21
    tbl1.bg_vertical_header_line_chr = 21
    
    tbl1.bg_header = 90
    tbl1.fg_header = 231
    tbl1.bold_header = True
    
    tbl1.bg_data = 231
    tbl1.fg_data = 0
    tbl1.bold_data = True
    
    
    tbl1.adj_top_margin = 2
    tbl1.adj_indent = 4
    tbl1.adj_space  = 4

    # tbl.bg_all_cell_data = False              NO_SPACE_COLOR_COL  DOUBLE_SPACE_COLOR_COL
    # tbl.bg_all_cell_header = False

    tbl1.print_fancy_format(data=lst, style=cp.Line_Style.NONE)
    tbl1.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_COL_COLOR)
    tbl1.print_fancy_format(data=lst, style=cp.Line_Style.NO_SPACE_COL_COLOR)
    tbl1.print_fancy_format(data=lst, style=cp.Line_Style.DOUBLE)

    tbl1.print_fancy_format(data=lst2, style=cp.Line_Style.NONE)
    tbl1.print_fancy_format(data=lst2, style=cp.Line_Style.SPACE_COL_COLOR)
    tbl1.print_fancy_format(data=lst2, style=cp.Line_Style.NO_SPACE_COL_COLOR)
    tbl1.print_fancy_format(data=lst4, style=cp.Line_Style.DOUBLE)


    tbl1.horizontal_line_under_header_on = True
    tbl1.middle_horizontal_line_on = True
    tbl1.print_fancy_format(data=lst, style=cp.Line_Style.NONE)
    tbl1.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_COL_COLOR)
    tbl1.print_fancy_format(data=lst, style=cp.Line_Style.NO_SPACE_COL_COLOR)
    tbl1.print_fancy_format(data=lst, style=cp.Line_Style.DOUBLE)

    tbl1.print_fancy_format(data=lst2, style=cp.Line_Style.NONE)
    tbl1.print_fancy_format(data=lst2, style=cp.Line_Style.SPACE_COL_COLOR)
    tbl1.print_fancy_format(data=lst2, style=cp.Line_Style.NO_SPACE_COL_COLOR)
    tbl1.print_fancy_format(data=lst4, style=cp.Line_Style.DOUBLE)
