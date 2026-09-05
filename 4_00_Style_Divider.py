import custom_print as cp
'''
    It create a divider through the terminal screen.
'''
cp.ins_newline(1)

div = cp.Divider()
# +--------------------------------------------------------------------------------------------+
# | Printing the Divider                                                                       |
# +--------------------------------------------------------------------------------------------+
# Default Values (It does not that much)
div.print_fancy_divider(message=" Custom Print Divider", style=cp.Divider_Style.CUSTOMIZED)
cp.ins_newline(2)



# +--------------------------------------------------------------------------------------------+
# | Corner Settings                                                                            |
# +--------------------------------------------------------------------------------------------+
# Setting bg colors for corners              setting fg colors for corners
div.top_left_corner_bg     = 231;              div.top_left_corner_fg     = 16;
div.top_right_corner_bg    = 231;              div.top_right_corner_fg    = 16;
div.bottom_left_corner_bg  = 231;              div.bottom_left_corner_fg  = 16;
div.bottom_right_corner_bg = 231;              div.bottom_right_corner_fg = 16;

# Setting chr for corners                    Setting bold for corners
div.top_left_corner_chr     = "1";           div.all_corner_bold = True
div.top_right_corner_chr    = "2"
div.bottom_left_corner_chr  = "3"
div.bottom_right_corner_chr = "4"


# Setting bg colors for corners              setting fg colors for corners 
# div.all_fg_corner = -1;                    div.all_fg_corner = -1

# Setting chr for corners                    Setting bold for corners
# div.all_corner_chr  = "";                  div.all_corner_bold = True


# +--------------------------------------------------------------------------------------------+
# | Horizontal line Settings                                                                   |
# +--------------------------------------------------------------------------------------------+
# Setting chr for horizontal lines      Setting bg colors for horizontal lines     Setting fg colors for horizontal lines
div.top_horizontal_line_chr    = "*";   div.top_horizontal_line_bg    = 231;    div.top_horizontal_line_fg    = 16
div.bottom_horizontal_line_chr = "-";   div.bottom_horizontal_line_bg = 231;    div.bottom_horizontal_line_fg = 16

# div.top_horizontal_line_on     = True;  div.bottom_horizontal_line_on = True;  div.horizontal_line_bold      = True


# +--------------------------------------------------------------------------------------------+
# | Vertical line Settings                                                                     |
# +--------------------------------------------------------------------------------------------+
# Setting chr for horizontal lines   Setting bg colors for Vertical lines  Setting fg colors for Vertical lines
div.left_vertical_line_chr  = "5";   div.left_vertical_line_bg  = 231;      div.left_vertical_line_fg  = 16
div.right_vertical_line_chr = "6";   div.right_vertical_line_bg = 231;      div.right_vertical_line_fg = 16
div.vertical_line_bold      = True


# +--------------------------------------------------------------------------------------------+
# | Message Settings                                                                           |
# +--------------------------------------------------------------------------------------------+
# Message
div.msg_bg = 231;                   div.msg_fg = 234;                        div.msg_bold = True
div.adj_indent = 2;                 div.align = cp.Align.CENTER;             div.msg_italic = True

# Note: adj_indent only works when the align is set to JUSTIFY

# Fill blank
div.left_fill_bg = cp.No.GLADE_GREEN;              div.right_fill_bg = cp.No.BLAZE_ORANGE;                  # div.left_right_fill_bg = 11

# Note: all_fill_bg takes priority over the left_fill_bg and right_fill_bg

# +--------------------------------------------------------------------------------------------+
# | Printing the Divider                                                                       |
# +--------------------------------------------------------------------------------------------+
msg = "  My Divider Title Here...!  "
div.print_fancy_divider(message=msg, style=cp.Divider_Style.CUSTOMIZED)
cp.ins_newline(2)