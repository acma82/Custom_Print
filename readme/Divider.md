#### [Back](README.md)
# Divider
  
## Default Variables
```python
#-----------------------------------------------------------------------------------------------------+
#  corner variables                                                                                   |
#-----------------------------------------------------------------------------------------------------+
self.top_left_corner_chr     = " ";       self.bg_top_left_corner     = -1;       self.fg_top_left_corner     = -1
self.top_right_corner_chr    = " ";       self.bg_top_right_corner    = -1;       self.fg_top_right_corner    = -1
self.bottom_left_corner_chr  = " ";       self.bg_bottom_left_corner  = -1;       self.fg_bottom_left_corner  = -1
self.bottom_right_corner_chr = " ";       self.bg_bottom_right_corner = -1;       self.fg_bottom_right_corner = -1

self.all_corner_chr  = "";                self.all_bg_corner = -1;                self.all_fg_corner = -1
self.all_corner_bold = False

#-----------------------------------------------------------------------------------------------------+
#  Horizontal line Variables                                                                          |
#-----------------------------------------------------------------------------------------------------+   
self.top_horizontal_line_chr    = " ";  self.bg_top_horizontal_line    = -1;   self.fg_top_horizontal_line    = -1
self.bottom_horizontal_line_chr = " ";  self.bg_bottom_horizontal_line = -1;   self.fg_bottom_horizontal_line = -1
self.top_horizontal_line_on     = True; self.bottom_horizontal_line_on = True; self.horizontal_line_bold      = False

#-----------------------------------------------------------------------------------------------------+
#  Vertical line Variables                                                                            |
#-----------------------------------------------------------------------------------------------------+
self.left_vertical_line_chr  = " ";      self.bg_left_vertical_line  = -1;        self.fg_left_vertical_line  = -1
self.right_vertical_line_chr = " ";      self.bg_right_vertical_line = -1;        self.fg_right_vertical_line = -1
self.vertical_line_bold      = False

#-----------------------------------------------------------------------------------------------------+
#  Message Variables                                                                                  |
#-----------------------------------------------------------------------------------------------------+
self.msg_bg = -1;                        self.msg_fg = -1;                        self.msg_bold = False
self.adj_indent = 2;                     self.align = Align.CENTER
# Fill blank
self.left_fill_bg = -1;                  self.right_fill_bg = -1;                  self.all_fill_bg = -1
```

## Example
```python
import custom_print as cp
'''
    It create a divider through the terminal screen.
'''
cp.ins_newline(1)

div = cp.Divider()


# +--------------------------------------------------------------------------------------------+
# | Divider Settings                                                                           |
# +--------------------------------------------------------------------------------------------+
my_color = cp.No.EARLY_NIGHT_BLUE         # cp.No.INDIGO

div.all_corner_bg = my_color
div.top_horizontal_line_bg    = my_color
div.bottom_horizontal_line_bg = my_color

div.left_vertical_line_bg  = cp.No.WHITE
div.right_vertical_line_bg = cp.No.WHITE

div.all_fill_bg  = cp.No.WHITE

div.msg_align = cp.Align.JUSTIFY
div.adj_indent = 20
div.msg_bold = True


# +--------------------------------------------------------------------------------------------+
# | Printing the Divider                                                                       |
# +--------------------------------------------------------------------------------------------+
div.print_fancy_divider(message=" SQ BRACKET OPTION ", style=cp.Divider_Style.SQ_BRACKETS)

cp.ins_newline(2)
div.msg_bg = 231
div.msg_fg = 234

div.print_fancy_divider(message=" SQ BRACKET OPTION ", style=cp.Divider_Style.SQ_BRACKETS)

```

![Alt text](Divider_1.png)

#### [Back](README.md)