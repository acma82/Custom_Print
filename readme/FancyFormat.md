#### [Back](README.md)
# FancyFormat
<!--- # <span style="color:green"> <strong> FancyFormat </strong> </span> --->
* [**General Section**](#general-section)
* [**Title Section**](#title-section)
* [**Footnote Section**](#footnote-section)
* [**Data Section**](#data-section)
* [**Horizontal Line Section**](#horizontal-line-section)
* [**Vertical Line Section**](#vertical-line-section)
* [**External Corner Section**](#external-corner-section)
* [**Middle Corner Section**](#middle-corner-section)
* [**Header Section**](#header-section)
* [**Header Under Line Section**](#header-under-line-section)
* [**Sumarize**](#sumarize)
* [**Demo**](#demo-1)
* [**Banded Row**](#banded-row)
* [**Multi Colors**](#multi-color)


<!-- ---------------------------------- -->
<!-- Methods                            -->
<!-- ---------------------------------- -->
## Methods
This class contains two methods:
+ ***print_fancy_format(data, style)*** <br>
    by default is set up to customized option. This method take two parameters, **data** and **line style**. <br>
    **data:** can be bool, int, float, complex, str, dictionary, range, set, frozenset, or tuple. <br>
    **style:** use the class Line_Style for more option. Check demos for more reference.

+ ***reset_fancy_format()*** <br>
    Any modification on the section variables will be affected on the customized line style. This method will reset all
    section variables to their default values at once.

<!-- ---------------------------------- -->
<!-- General Section                    -->
<!-- ---------------------------------- -->
## General Section
**adj → adjust**
    
```python    
    adj_top_margin = 0        adj_bottom_margin = 0        adj_indent = 2        set_fill_chr = "----"
    
    adj_top_space  = 0        adj_bottom_space  = 0        adj_space  = 2        updata_list  = False 

    design_color   = 4        bg_line_colors    = -1       fg_line_colors = -1   bold_lines   = False

    set_layout     = Layout.HORIZONTAL

```

|                      |                                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| **adj_top_margin**   | Lines to be added between the terminal ($) and the title.                       |
| **adj_top_space**    | Lines to be added between title and top list.                                   |
| **adj_bottom_margin**| Lines to be added between the end of the list or footnote to the terminal ($).  |
| **adj_bottom_space** | Lines to be added between the bottom of the list and the footnote.              |
| **adj_indent**       | Space from the left terminal to the first character in the list to be printed.  | 
| **adj_space**        | Space from the left of the box to the first character in the list to be printed.| 
| **design_color**     | This color is used for the designs (1 through 10).                              |
| **bg_line_colors**   | Set all the bg_line colors, if it's set to default (-1, 256) then It will be    |
|                      | used the default variables.                                                     |
| **fg_line_colors**   | Set all the fg_line colors, if it's set to default (-1, 256) then It'll be used |
|                      | the default variables.                                                          |
| **bold_lines**       | It will set all the lines to regular and it will respect every single variable  |
|                      | assigned to the bold lines. For True, it will take priority over the others vars| 

>  <span style="color:red"> <strong> Note: </strong> </span> These variables only accept integer(int) values. 

|                 |                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
|**set_fill_chr** | When a list is not complete in the data, it will be filled out with some characters. fill_chr will be converted to string.|
|**set_layout**   |	This option only works with set, frozenset, range or dictionary type of variables.                                        |
|**update_list**  | update the list being pass as is displayed on the terminal.                                                               |

Notice that every single element in the list being passed will be converted to string in a temporary internal list. 
If you want to save this conversion to your original list then set to True the update_list option. It only works with the list type of variable.

**Note:** adj_top_space won’t work if the title is not set up. Also adj_bottom_space won’t work if the footnote is not set up.
	  Use adj_top_margin or adj_bottom_margin or ins_newline(n), or print(“\n”) if you need more space.

[**Top**](#fancyformat)

<!-- ---------------------------------- -->
<!-- Title Section                      -->
<!-- ---------------------------------- -->
## Title Section

```python
    title_msg	= ""        title_align  = "justify"         title_hidden    = False
    title_bold	= False     title_italic = False             title_inverse   = False
    title_bg	= -1        title_strike = False             title_blinking  = False
    title_fg	= -1        title_dim    = False             title_underline = False
```

**title_msg** is the title name for the list. It only accepts string values, by defaults is empty.

<!-- --------------------------------- -->
<!-- Footnote Section                  -->
<!-- --------------------------------- -->
## Footnote Section

```python
    footnote_msg  = ""      footnote_align  = "justify"     footnote_hidden    = False
    footnote_bold = False   footnote_italic = False         footnote_inverse   = False
    footnote_bg	  = -1      footnote_strike = False         footnote_blinking  = False
    footnote_fg	  = -1      footnote_dim    = False         footnote_underline = False
```

**footnote_msg** The title name for the list. It only accepts string values, by default is empty.

<!-- ---------------------------------- -->
<!-- Data Section                       -->
<!-- ---------------------------------- -->
## Data Section

```python
    data_align = "justify"  data_hidden = False             data_inverse     = False
    data_bold  = False      data_italic = False             data_blinking    = False
    data_bg    = -1         data_strike = False             data_underline   = False
    data_fg    = -1         data_dim    = False             data_all_cell_bg = True
```

**data_all_cell_bg** The bg color will affect the entire cell or just the data.

<!-- ---------------------------------- -->
<!-- Horizontal Line Section            -->
<!-- ---------------------------------- -->
## Horizontal Line Section

```python
    top_horizontal_line_chr    = "-"        bottom_horizontal_line_chr ="-"    
    middle_horizontal_line_chr = "-"        top_horizontal_line_on     = True
    bottom_horizontal_line_on  = True       middle_horizontal_line_on  = False
    horizontal_line_bold       = False      horizontal_line_bg         = -1
    horizontal_line_fg         = -1
```
For more reference check **Figure 1**.

[**Top**](#fancyformat)

<!-- ---------------------------------- -->
<!-- Vertical Line Section              -->
<!-- ---------------------------------- -->
## Vertical Line Section

```python
    vertical_line_bold = False              left_vertical_line_chr   = "|"
    vertical_line_bg   = -1                 middle_vertical_line_chr = "|"
    vertical_line_fg   = -1                 right_vertical_line_chr  = "|"
    left_vertical_line_on   = True          right_vertical_line_on   = True
    middle_vertical_line_on = True 
```    

For more reference check **Figure 1 and Figure 2**.

<!-- ---------------------------------- -->
<!-- External Corner Section            -->
<!-- ---------------------------------- -->
## External Corner Section

```python
    top_left_corner_chr  = "+"        bottom_right_corner_chr = "+"       outer_corner_bg = -1
    top_right_corner_chr = "+"        bottom_left_corner_chr  = "+"       outer_corner_fg = -1
    outer_corner_bold = False
```

For more reference check **Figure 1**.

<!-- ---------------------------------- -->
<!-- Middle Corner Section              -->
<!-- ---------------------------------- -->
## Middle Corner Section

```python
    inner_corner_bold_chr = False   middle_top_corner_chr    = "+"      middle_right_corner_chr = "+"
    inner_corner_bg_chr	  = -1      middle_inner_corner_chr  = "+"      middle_left_corner_chr  = "+"
    inner_corner_fg_chr   = -1      middle_bottom_corner_chr = "+"
```

For reference check **Figure 3 and 4**.

[**Top**](#fancyformat)

<!-- ---------------------------------- -->
<!-- Header Section                     -->
<!-- ---------------------------------- -->
## Header Section

```python
    header_align = "justify"        header_hidden = False               header_inverse      = False
    header_bold  = False            header_italic = False               header_blinking     = False
    header_bg    = -1               header_strike = False               header_underline    = False
    header_fg    = -1               header_dim    = False               header_all_cell_bg  = True
```

**data_all_cell_bg** The bg color will affect the entire cell or just the header.

#### <span style="color:cyan"> Attributes for the Header Lines</span> 

```python
    header_vertical_line_bold_chr = False       header_right_vertical_line_chr  = "|"
    header_vertical_line_bg_chr   = -1          header_left_vertical_line_chr   = "|"
    header_vertical_line_fg_chr   = -1          header_middle_vertical_line_chr	= "|"
```

For reference check **Figure 3 and 4**.

[**Top**](#fancyformat)


<!-- ---------------------------------- -->
<!-- Header Under Line Section          -->
<!-- ---------------------------------- -->
## Header Line Section
#### <span style="color:cyan"> Attributes for the line below the header text</span>

```python

    header_horizontal_line_bold = False              header_horizontal_line_on	 = False
    header_horizontal_line_bg   = -1                 header_horizontal_line_chr = "-" 
    header_horizontal_line_fg   = -1
```    
    header_horizontal_line_on	            Horizontal lines between headers and the first data row.


#### <span style="color:cyan"> Attributes for the header corners (left, middles and right)</span>

```python

    header_corner_bold = False       header_left_corner_chr   = "+"
    header_corner_bg   = -1          header_right_corner_chr  = "+"
    header_corner_fg   = -1          header_middle_corner_chr = "+"
```

For more reference check [**figure 3**](#figure-3).

[**Top**](#fancyformat)


<!-- ---------------------------------- -->
<!-- Figure 3 and 4                     -->
<!-- ---------------------------------- -->
## Figure 3
![Alt text](Figure_3.png)
[**Top**](#fancyformat)
## Figure 4
![Alt text](Figure_4.png)
[**Top**](#fancyformat)

# Sumarize
<!-- ---------------------------------- -->
<!-- Sumarize, Figure 1, 2, and 5       -->
<!-- Alignment and Colors Section       -->
<!-- ---------------------------------- -->
**Note:** All the **bg** and **fg** values accept int values from -1 to 256. Default values from the system are -1 and 256. Set the number of the color by name using Use the class Color as shown on Aid class Section.

**Note:** All the **align** options accept 4 values, left (l), justify (j), center (c), and right (r).

<span style="background-color:purple">
<span style="color:yellow"><strong><i>
Note: Although the main idea is to use list type, print_fancy_format(tbl) accepts any type of variable. Refer to Demo 1 and Demo 2. 
</i></strong> </span> </span>

## Figure 1
![Alt text](Figure_1.png)
[**Top**](#fancyformat)
## Figure 2
![Alt text](Figure_2.png)
[**Top**](#fancyformat)
## Figure 5
![Alt text](Figure_5.png)
[**Top**](#fancyformat)

|                                         |                                      |                                  |
|-----------------------------------------|--------------------------------------|----------------------------------|
| 1.- adj_top_margin                      | 2.- top_space                        | 3.- adj_indent                   |
| 4.- adj_space                           | 5.- bottom_space                     | 6.- title_msg                    |
| 7.- footnote_msg                        | 8.- data                             | 9.- top_horizontal_line_chr      |
| 10.- bottom_horizontal_line_chr         | 11.- left_vertical_line_chr          | 12.- right_vertical_line_chr     |
| 13.- top_left_corner_chr                | 14.- top_right_corner_chr            | 15.- bottom_right_corner_chr     |
| 16.- bottom_left_corner_chr             | 17.- middle_top_corner_chr           | 18.- middle_vertical_line_chr    |
| 19.- middle_bottom_corner_chr           | 20.- header                          | 21.- header_horizontal_line_chr  |
| 22.- header_left_vertical_line_chr      | 23.- header_right_vertical_line_chr  | 24.- header_left_corner_chr      |
| 25.- header_right_corner_chr            | 26.- middle_horizontal_line_chr      | 27.- middle_left_corner_chr     |
| 28.- middle_right_corner_chr           | 29.- header_middle_vertical_line_chr | 30.- header_middle_corner_chr    |
| 31.- middle_inner_corner_chr            | 32.- set_fill_chr                    | 33.- adj_bottom_margin           |
|                                         |                                      |                                  |


***Reference Values:***
|                                      |                                    |                                       |
|--------------------------------------|------------------------------------|---------------------------------------|
|                                      |                                    |                                       |
| top_horizontal_line_on    &rarr; 9   | header_horizontal_line_on &rarr; 21| middle_horizontal_line_on &rarr; 26   |
| bottom_horizontal_line_on &rarr; 10  | left_vertical_line_on &rarr; 11    | right_vertical_line_on &rarr; 12      |
| middle_vertical_line_on &rarr; 18    |                                    |                                       |
|                                      |                                    |                                       |



<!-- ---------------------------------- -->
<!-- Demo 1                             -->
<!-- ---------------------------------- -->

## Example 1 
[**Top**](#fancyformat)
   
```python
'''  Demo  '''
import custom_print

list1 = custom_print.FancyFormat()

# title
list1.title_bg    = 11
list1.title_fg    = 0
list1.title_bold  = 1
list1.title_align = "r"
list1.title_msg   = " Title List "

# footnote
list1.footnote_align = "l"
list1.footnote_msg   = " Footnote "
list1.footnote_fg    = 226
list1.footnote_bg    = 6
list1.footnote_bold  = 1

list1.header_horizontal_line_on = 1
list1.middle_horizontal_line_on = 1
list1.header_bg = 6
list1.header_fg = 0
list1.header_bold = 1
list1.data_align = "left"
list1.data_bg = 55
list1.data_fg = 256

list1.adj_top_margin = 2

my_list = [["Header 1","Header 2","Header 3","Header 4"],["R2C1","R2C2","R2C3","R2C4"],
           ["R3C1","R3C2","R3C3","R3C4"],["R4C1","R4C2","R4C3","R4C4"]]

list1.print_fancy_format(my_list, custom_print.Line_Style.SINGLE_LINE)

list1.top_horizontal_line_on = 0
list1.header_horizontal_line_on = 0
list1.middle_horizontal_line_on = 0
list1.bottom_horizontal_line_on = 0
list1.print_fancy_format(my_list)
```

![Alt text](Demo.png)


## Example 2
```python

import custom_print as cp

lst = [["Header 0",    "Header 1",    "Header 2",    "Header 3"   ],
       ["Col 0 Row 1", "Col 1 Row 1", "Col 2 Row 1", "Col 3 Row 1"],
       ["Col 0 Row 2", "Col 1 Row 2", "Col 2 Row 2", "Col 3 Row 2"],
       ["Col 0 Row 3", "Col 1 Row 3", "Col 2 Row 3", "Col 3 Row 3"]]

tbl = cp.FancyFormat()

# Header settings                       Data settings
tbl.header_bg = cp.No.INDIGO;           tbl.data_bg = cp.No.SUMMER_GREEN
tbl.header_fg = cp.No.WHITE;            tbl.data_fg = cp.No.LIGHT_WHITE
tbl.header_bold = True;                 tbl.data_bold  = False
tbl.header_align = cp.Align.CENTER;     tbl.data_align = cp.Align.LEFT

# table settings
tbl.adj_top_margin = 4;                 tbl.adj_bottom_margin = 4 
tbl.adj_indent = 8;                     tbl.adj_space = 4        
tbl.design_color = cp.No.YELLOW_GREEN


# +--------------------------------------------------------------------------------------------+
# | Printing Fancy Format                                                                      |
# +--------------------------------------------------------------------------------------------+
tbl.print_fancy_format(data=lst, style=cp.Line_Style.DESIGN_5)

```

![Alt text](Demo2.png)
[**Top**](#fancyformat)
<!-- ---------------------------------- -->
<!-- Banded_Row                      -->
<!-- ---------------------------------- -->
## Banded Row
**set_banded_row_on** was created to apply alternating background colors to the table rows.
When **set_banded_row_on** is set to True, banded_row_bg and banded_row_fg control the 
banded row behavior. See the example below.

```python
    import custom_print as cp
    tbl = cp.FancyFormat()
    crs = cp.Cursor()

    lst = [["set_banded_row_on = False"],["Data 1"],
            ["Data 2"],["Data 3"],["Data 4"]]

    tbl.adj_indent = 40
    tbl.title_msg = "Banded Row Inactive"
    tbl.header_bg = 4;          tbl.header_fg = 231
    tbl.data_bg = 231;          tbl.data_fg = 16
    tbl.header_horizontal_line_on = True

    tbl.print_fancy_format(lst)

    lst = [["set_banded_row_on = True"],["Data 1"],
            ["Data 2"],["Data 3"],["Data 4"]]

    tbl.adj_indent = 6
    tbl.title_msg = "Banded Row Active"
    tbl.set_banded_row_on = True
    tbl.banded_row_bg = 208;    tbl.banded_row_fg = 16
    crs.jumpTo(qty=8, direction=cp.Move.UP)

    tbl.print_fancy_format(lst)

```
![Alt text](banded_row_01.png)

**bande_row_step**  variable is set to 1 by default. It can be changed to a different value for more convenience for the visualization.

![Alt text](banded_row_02.png)

[**Top**](#fancyformat)

## Multi Color

                                                                               
          Multi Color Section                                                   
                                                                                
          self.set_multi_bg_fg_on = False   |                                   
                                            |                                   
          self.data_multi_bg_step  = 1      |    self.data_multi_fg_step  = 1   
          self.data_multi_bg_stop  = 255    |    self.data_multi_fg_stop  = 255 
                                            |                                   
                                                                                

      This option was created to apply alternating background colors to the
      table rows. When  set_multi_bg_fg_on  is set to True, the following
      variables control the color behavior:

      data_multi_bg acts as a range variable in the format (start, stop, step).
      The start value is taken from the data_bg variable (see Data Section for
      details). The stop value is defined by  data_multi_bg_stop.  The step
      value is defined by  data_multi_bg_step. 

      For example, if a table has 5 data rows, data_bg is set to 9 (PASTEL_RED),
      and  data_multi_bg_stop  is set to 21, the background colors will be
      applied as shown in the table below.


      Rows        Start                 Color           check color name
        1          data_bg = 9          PASTEL_RED            (9)
        2          data_bg += step(10)  ELECTRIC_LIGHT_GREEN  (10)
        3          data_bg += step(11)  DARKISH_YELLOW        (11)
        4          data_bg += step(12)  LIGHT_BLUE            (12)
        5          data_bg += step(13)  LIGHT_PURPLE          (13)

       Note  In this example,  data_multi_bg_stop is set to 21. Since the table
             only contains 5 rows, the stop value is not reached. Now assume
              data_multi_bg_step  is set to 4. In this case,
             the background colors will be applied as shown in the table below.

       Rows        Start                Color
        1          data_bg = 9          PASTEL_RED            (9)
        2          data_bg += _step     LIGHT_PURPLE          (13)
        3          data_bg += step(17)  DARK_BLUE             (17)
        4          data_bg += step(21)  PASTEL_RED            (21) Restar (9)
        5          data_bg += step(13)  LIGHT_PURPLE          (13)


       Note  The fourth row reaches the defined limit  (data_multi_bg_stop). 
             Once the limit is reached, the color sequence restarts from the
             beginning — using the  data_bg  color, which is 9 (PASTEL_RED).
             The variable  data_multi_fg  works exactly the same way as
              data_multi_bg. 

In the following example, the background color step is set to 0
(static background) to make the foreground color progression easier to
see. Please also note that the header colors are not affected by these
settings.


```python
    import custom_print as cp
    tbl = cp.FancyFormat()

    lst   = [["Header 1", "Header 2", "Header 3", "Header 4"],
            ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
            ["Data 2",   "Data 6",   "Data 7",   "Data 8"  ],
            ["Data 3",   "Data 2",   "Data 3",   "Data 4"  ],
            ["Data 4",   "Data 2",   "Data 3",   "Data 4"  ],
            ["Data 5",   "Data 2",   "Data 3",   "Data 4"  ]]

    tbl.header_bg = cp.No.VERY_DARK_MAGENTA
    tbl.header_fg = cp.No.WHITE

    tbl.data_bg   = cp.No.WHITE # 15
    tbl.data_multi_bg_step = 0


    tbl.set_multi_bg_fg_on = True
    tbl.data_bold = True
    tbl.data_fg = 9               # start
    tbl.data_multi_fg_stop = 21

    tbl.data_multi_fg_step = 1
    tbl.print_fancy_format(data=my_list,
                            style=cp.Line_Style.DASH_LINE)

    tbl.data_multi_fg_step = 4
    tbl.print_fancy_format(data=my_list,
                            style=cp.Line_Style.DASH_LINE)

```    
![Alt text](multi_color_01.png)


```python
    import custom_print as cp
    tbl = cp.FancyFormat()

    lst = [["Header 1", "Header 2", "Header 3", "Header 4"],
            ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
            ["Data 2",   "Data 6",   "Data 7",   "Data 8"  ],
            ["Data 3",   "Data 2",   "Data 3",   "Data 4"  ],
            ["Data 4",   "Data 2",   "Data 3",   "Data 4"  ],
            ["Data 5",   "Data 2",   "Data 3",   "Data 4"  ]]

    tbl.title_msg = " Line_Style.TEAL_WHITE "
    tbl.title_align = cp.Align.CENTER
    tbl.title_bg = cp.No.DARK_WHITE
    tbl.title_fg = 22

    tbl.header_bg = cp.No.VERY_DARK_MAGENTA
    tbl.header_fg = cp.No.WHITE

    tbl.data_align = cp.Align.CENTER
    tbl.data_bold  = True
    tbl.data_bg    = cp.No.WHITE # 15 (start)
    tbl.data_fg    = 9           #    (start)

    tbl.set_multi_bg_fg_on = True

    tbl.data_multi_bg_step = 2
    tbl.data_multi_bg_stop = 255  # This is the default value
                                # just to undertand better.
                                # Not necessary.
    tbl.data_multi_fg_step = 4
    tbl.data_multi_fg_stop = 121

    tbl.print_fancy_format(data=lst,
                        style=cp.Line_Style.TEAL_WHITE)
    # TEAL_WHITE -> data_bg=231  data_fg=21
    # How the design is done with the colors internally.
```
![Alt text](multi_color_02.png)


#### [Back](README.md)