import custom_print as cp
div = cp.Divider()


# +---------------------------------------------------------------------------------------+
# +       bg                                                                              +
# +---------------------------------------------------------------------------------------+
# corners
div.top_left_corner_bg    = 4;          div.top_right_corner_bg    = 11
div.bottom_left_corner_bg = 11;         div.bottom_right_corner_bg = 4


# horizontal lines                      fill
div.top_horizontal_line_bg    = 22;     div.left_fill_bg  = 231
div.bottom_horizontal_line_bg = 21;     div.right_fill_bg = 228


# vertical lines                        msg
div.left_vertical_line_bg  = 54;        div.msg_bg = 54
div.right_vertical_line_bg = 54


# +---------------------------------------------------------------------------------------+
# +       fg                                                                              + 
# +---------------------------------------------------------------------------------------+
# colors fg
div.top_left_corner_fg    = 5;          div.top_right_corner_fg    = 6
div.bottom_left_corner_fg = 6;          div.bottom_right_corner_fg = 5


# msg
div.top_horizontal_line_fg    = 12;     div.left_vertical_line_fg  = 11
div.bottom_horizontal_line_fg = 11;     div.right_vertical_line_fg = 226

div.msg_fg = 231;
# +---------------------------------------------------------------------------------------+
# +       Bold                                                                            + 
# +---------------------------------------------------------------------------------------+
# bold
div.msg_bold    = True;                 div.vertical_line_bold   = True
div.all_corner_bold = True;             div.horizontal_line_bold = True
 

# +---------------------------------------------------------------------------------------+
# +       Chr                                                                             + 
# +---------------------------------------------------------------------------------------+
div.top_left_corner_chr  = " 1 ";      div.bottom_left_corner_chr  =" 3 "
div.top_right_corner_chr = " 2 ";      div.bottom_right_corner_chr = " 4 "

div.left_vertical_line_chr = " |!| ";  div.right_vertical_line_chr = " |!| "

div.top_horizontal_line_chr = "-";     div.bottom_horizontal_line_chr = "-"
# uncomment the line below to practice a little bit and comment the above line
div.top_horizontal_line_chr = "-|**|-";     div.bottom_horizontal_line_chr = "*-|-*"

# +---------------------------------------------------------------------------------------+
# +       Align                                                                           + 
# +---------------------------------------------------------------------------------------+
# div.align = cp.Align.CENTER # Default
# div.align = cp.Align.LEFT
# div.align = cp.Align.RIGHT
# div.msg_align = cp.Align.JUSTIFY;          div.adj_indent = 8


# +---------------------------------------------------------------------------------------+
# +       On/Off Top/Bottom                                                               + 
# +---------------------------------------------------------------------------------------+
# div.top_horizontal_line_on    = False      # by default is set to True
# div.bottom_horizontal_line_on = False      # by default is set to True

# +---------------------------------------------------------------------------------------+
# +       Priorities over the others                                                      +
# +---------------------------------------------------------------------------------------+
# uncomment the below line to practice a little bit
# div.all_corner_chr  = " |6| ";         div.all_corner_bg = 7;       div.all_corner_fg = 234
# div.all_fill_bg = 0

title = " Your Title Here...! "

# +---------------------------------------------------------------------------------------+
# +       Customize works with default variables                                          +
# +---------------------------------------------------------------------------------------+
div.print_fancy_divider(title, cp.Divider_Style.CUSTOMIZED);   cp.ins_newline(2)
# +---------------------------------------------------------------------------------------+
# +       These Templates respect only the colors but not the chr variables               +
# +---------------------------------------------------------------------------------------+
div.msg_align = cp.Align.RIGHT
div.print_fancy_divider(title, cp.Divider_Style.DASH_1);       cp.ins_newline(2)
div.print_fancy_divider(title, cp.Divider_Style.DASH_2);       cp.ins_newline(2)
div.print_fancy_divider(title, cp.Divider_Style.BLUE_WHITE_1);    cp.ins_newline(2)
div.print_fancy_divider(title, cp.Divider_Style.BLUE_WHITE_2);    cp.ins_newline(2)
div.print_fancy_divider(title, cp.Divider_Style.SINGLE_LINE);  cp.ins_newline(2)

div.msg_align = cp.Align.JUSTIFY;          div.adj_indent = 20
div.print_fancy_divider(title, cp.Divider_Style.SINGLE_BOLD);  cp.ins_newline(2)
div.print_fancy_divider(title, cp.Divider_Style.SINGLE_HEAVY); cp.ins_newline(2)
div.print_fancy_divider(title, cp.Divider_Style.DOUBLE_LINE);  cp.ins_newline(2)
div.print_fancy_divider(title, cp.Divider_Style.SQ_BRACKETS);  cp.ins_newline(2)



div2 = cp.Divider()
div2.msg_align = cp.Align.LEFT
div2.print_fancy_divider(title, cp.Divider_Style.CUSTOMIZED);   cp.ins_newline(2)
div2.print_fancy_divider(title, cp.Divider_Style.DASH_1);       cp.ins_newline(2)
div2.print_fancy_divider(title, cp.Divider_Style.DASH_2);       cp.ins_newline(2)
div2.print_fancy_divider(title, cp.Divider_Style.BLUE_WHITE_1);    cp.ins_newline(2)
div2.print_fancy_divider(title, cp.Divider_Style.BLUE_WHITE_2);    cp.ins_newline(2)

div2.msg_align = cp.Align.CENTER
div2.print_fancy_divider(title, cp.Divider_Style.SINGLE_LINE);  cp.ins_newline(2)
div2.print_fancy_divider(title, cp.Divider_Style.SINGLE_BOLD);  cp.ins_newline(2)
div2.print_fancy_divider(title, cp.Divider_Style.SINGLE_HEAVY); cp.ins_newline(2)
div2.print_fancy_divider(title, cp.Divider_Style.DOUBLE_LINE);  cp.ins_newline(2)
div2.print_fancy_divider(title, cp.Divider_Style.SQ_BRACKETS);  cp.ins_newline(2)



div2.all_fill_bg = 231
div2.msg_bg = 234
div2.msg_fg = 11
div2.print_fancy_divider(title, cp.Divider_Style.DOUBLE_LINE);  cp.ins_newline(2)
