#### [Back](README.md)

# Aid Classes
* [**Align**](#align)
* [**Divider_Style**](#divider)
* [**Layout**](#layout)
* [**Length_bg**](#length_bg)
* [**Line_Style**](#line_style)
* [**Move**](#move)
* [**Unicode**](#unicode)



## Align
<!--- ## <span style="color:green"> <strong> Align </strong> </span> --->
> <span style="color:blue" ><strong>  This class is used where alignment is needed. It contains 4 options. </strong>
- Align.RIGHT
- Align.LEFT
- Align.CENTER
- Align.JUSTIFY

**Note:** These options can be replaced for the original values as displays below:  

| Align.RIGHT | Align.LEFT | Align.CENTER | Align.JUSTIFY |
| :---------: | :--------: | :----------: | :-----------: |
| "right"     | "left"     |"center"      | "justify"     |
| "r"         | "l"        |"c"           | "j"           |

[**Top**](#aid-classes) <span style="color:red"> <strong> Example: </strong> </span>


```python
import custom_print as cp
msg = cp.FancyMessage()
msg.title_align = cp.Align.CENTER
msg.footnote_align = "right"   # msg.footnote_align = "r"
```

## Divider

> <span style="color:blue" ><strong>  This class is used where a divider is needed. It contains 10 options.</strong>

|                  |                |
|------------------|----------------|
| **CUSTOMIZED**   | "customized"   |
| **SINGLE_LINE**  | "single_line"  |
| **SINGLE_BOLD**  | "single_bold"  |
| **SINGLE_HEAVY** | "single_heavy" |
| **DOUBLE_LINE**  | "double_line"  |
| **DASH_1**       | "dash_1"       |
| **DASH_2**       | "dash_2"       |
| **SQ_BRACKETS**  | "sq_brackets"  |
| **BLUE_WHITE_1** | "blue_white_1" |
| **BLUE_WHITE_2** | "blue_white_2" |

[**Top**](#aid-classes) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
div.print_fancy_divider(message=" Custom Print Divider", style=cp.Divider_Style.CUSTOMIZED)
div.print_fancy_divider(message=" Custom Print Divider", style=cp.Divider_Style.DASH_1)
# same as above
div.print_fancy_divider(message=" Custom Print Divider", style="customized")
div.print_fancy_divider(message=" Custom Print Divider", style="dash_1")
```

## Layout
<!--- ## <span style="color:green"> <strong> Layout </strong> </span> --->
    This class is used with FancyFormat class and Pen class. It contains 2 options.

* Layout.HORIZONTAL
* Layout.VERTICAL

**Note:** These options can be replaced for the original values as displays below:

| Layout.HORIZONTAL | Layout.VERTICAL |
| :---------------: | :-------------: |
| "horizontal"      | "vertical"      |
| "h"               | "v"             |

[**Top**](#aid-classes) <span style="color:red"> <strong> Example: </strong> </span>
```python
import custom_print as cp
tbl  = cp.FancyFormat()

r = range(0,21,2)
tbl.print_fancy_format(r)
tbl.set_layout = cp.Layout.VERTICAL     # tbl.set_layout = "v" 
tbl.print_fancy_format(r)
```
## Length_bg
<!--- ## <span style="color:green"> <strong> Length_bg </strong> </span> --->
    his class is used with FancyMessage class and contains 2 options.
+ ALL_ROW
+ ONLY_WORD

[**Top**](#aid-classes) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
msg = cp.FancyMessage()
path = " The new path: /mnt/home/user_name/Documents/ " # usually use with a paragra message type

msg.body_bg = 10
msg.body_fg = 0
msg.body_bold = True
msg.length = cp.Length_bg.ONLY_WORD

msg.adj_bg_lines_to_right_indent =  False   # True make all the way to the space available
msg.adj_bg_msg_to_space_available = False   # True make all the way to the space available
# These two options are only available when using the msg.length = cp.Length_bg.ONLY_WORD
# otherwise they will make it to the longest line

msg.print_fancy_message(path)
cp.ins_newline(3)
msg.length = cp.Length_bg.ALL_ROW # all the width of the terminal
msg.print_fancy_message(path)
```





## Line_Style
<!--- ## <span style="color:green"> <strong> Line_Style </strong> </span> --->
	This class is used with FancyFormat class. There are some options available.

            CUSTOMIZED         DESIGN_1       WHITE_PURPLE             GREEN_GREEN_BLACK 
            DASH               DESIGN_2       WHITE_BLACK_PURPLE       WHITE_BLACK_1  
            SINGLE_LINE        DESIGN_3       RED_WHITE                WHITE_BLACK_2
            DOUBLE_LINE        DESIGN_4       PURPLE_WHITE             TURQUOISE_BLACK
            SINGLE_BOLD        DESIGN_5       BLUE_WHITE          
            SINGLE_HEAVY       DESIGN_6       TURQUOISE_WHITE     
            SQR_BRACKETS       DESIGN_7       TEAL_WHITE      
            NONE               DESIGN_8       GRAY_TEAL_WHITE 
                               DESIGN_9       BLUE_PURPLE_WHITE_1
                               DESIGN_10      BLUE_PURPLE_WHITE_2



<br>

**Note:** These options can be replaced for the original values as displays below:

|                    |                |                 |               |                  |                |
|--------------------|----------------|-----------------|---------------|------------------|----------------|
|	**CUSTOMIZED**   | "customized"   | **SINGLE_LINE** | "single_line" | **SINGLE_SPACE** | "single_space" |
|	**SINGLE_BOLD**  | "single_bold"  | **DASH**        | "dash"        | **DOUBLE_SPACE** | "double_space" |
|	**SINGLE_HEAVY** | "single_heavy" | **DOUBLE_LINE** | "double_line" |                  |                |
|	**SQ_BRACKETS**  | "sq_brackets"  | **NONE**        | "none"        |                  |                |

<br>
<br>

|              |            |               |             |
|--------------|------------|---------------|------------ |
| **DESIGN_1** | "design_1" | **DESIGN_2**  | "design_2"  |
| **DESIGN_3** | "design_3" | **DESIGN_4**  | "design_4"  |
| **DESIGN_5** | "design_5" | **DESIGN_6**  | "design_6"  |
| **DESIGN_7** | "design_7" | **DESIGN_8**  | "design_8"  |
| **DESIGN_9** | "design_9" | **DESIGN_10** | "design_10" |


**Note:** These DESIGN options work with the ***design_color*** along with **header**_bg_fg and **data**_bg_fg variables.

<br>
<br>

|                         |                       |                    |                      |
|-------------------------|-----------------------|--------------------|----------------------|
| **WHITE_PURPLE**        | "white_purple"        | WHITE_BLACK_PURPLE | "white_black_purple" |
| **RED_WHITE**           | "red_white"           | PURPLE_WHITE       | "purple_white"       |
| **BLUE_WHITE**          | "blue_white"          | TURQUOISE_WHITE    | "turquoise_white"    |
| **TEAL_WHITE**          | "teal_white"          | GRAY_TEAL_WHITE    | "gray_teal_white"    |
| **BLUE_PURPLE_WHITE_1** | "blue_purple_white_1" | WHITE_BLACK_1      | "white_black"        |
| **BLUE_PURPLE_WHITE_2** | "blue_purple_white_2" | WHITE_BLACK_2      | "white_black_v2"     |
| **GREEN_GREEN_BLACK**   | "green_green_black"   | TURQUOISE_BLACK    | "turquoise_black"    |

<br>    
<br>    

These are the variables to visualize when using **SINGLE_SPACE** or **DOUBLE_SPACE**.
|                               |                                    |                                       |
|-------------------------------|------------------------------------|---------------------------------------| 
|horizontal_line_bg        = 21 | header_bg                   = 90   | data_bg                   = 231       |
|vertical_line_bg          = 21 | header_fg                   = 231  | data_fg                   = 0         |
|bg_corner_chr             = 21 | header_bold                 = True | data_bold                 = True      |
|inner_corner_bg_chr       = 21 | header_corner_bg            = 21   | middle_horizontal_line_on = True      |
|header_horizontal_line_bg = 21 | header_vertical_line_bg_chr = 21	 | header_horizontal_line_on = True      |

**Note:** Play with the colors and see your creation. Use the No.Name_Color if you prefer rather than the number.


[**Top**](#aid-classes) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
div = cp.Divider()
my_color = cp.No.EARLY_NIGHT_BLUE        # cp.No.INDIGO

div.all_corner_bg             = my_color
div.top_horizontal_line_bg    = my_color
div.bottom_horizontal_line_bg = my_color
div.left_vertical_line_bg     = cp.No.WHITE
div.right_vertical_line_bg    = cp.No.WHITE

div.all_fill_bg  = cp.No.WHITE

div.msg_align = cp.Align.JUSTIFY
div.adj_indent = 20
div.msg_bold = True


# +--------------------------------------------------------------------------------------------+
# | Printing the Divider                                                                       |
# +--------------------------------------------------------------------------------------------+
div.print_fancy_divider(message=" SQ BRACKET OPTION ", style=cp.Divider_Style.SQ_BRACKETS)

```





















## Move
<!--- ## <span style="color:green"> <strong> Move </strong> </span> --->
    This class is used with the Cursor class and it contains 4 options.

+ Move.RIGHT
+ Move.LEFT
+ Move.UP
+ Move.DOWN

**Note:** These options can be replaced for the original values as displays below:

| Move.RIGHT | Move.LEFT | Move.UP   | Move.DOWN  |
| :--------: | :--------:| :--------:| :--------: |
| "right"    | "left"    |"up"       | "down"     |
| "r"        | "l"       |"u"        | "d"        |


[**Top**](#aid-classes) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
crs = cp.Cursor()
clear()
# jumpTo method
crs.jumpTo(qty=2, direction = Move.DOWN) # direction = "d"
print("I am down")

```
## Unicode
<!--- ## <span style="color:green"> <strong> Unicode </strong> </span> --->
    This class is to insert some unicode characters.

#### Unicode Names
|Lines and Circles                           | Shapes                       |
|--------------------------------------------|------------------------------|
| BOX_DRAWINGS_LIGHT_HORIZONTAL              | BLACK_UP_POINTING_TRIANGLE   |
| BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT      | WHITE_UP_POINTING_TRIANGLE   |
| BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT       | BLACK_RIGHT_POINT_TRIANGLE   |
| BOX_DRAWINGS_LIGHT_VERTICAL                | WHITE_RIGHT_POINT_TRIANGLE   |
| BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL     | BLACK_DOWN_POINTING_TRIANGLE |
| BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL       | WHITE_DOWN_POINTING_TRIANGLE |
| BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL | BLACK_LEFT_POINTING_TRIANGLE |
| EM_DASH                                    | WHITE_LEFT_POINTING_TRIANGLE |
| BLACK_CIRCLE                               | BLACK_DIAMOND                |
| WHITE_CIRCLE                               | WHITE_DIAMOND                |
| FACE                                       | Reference → https://www.unicode.org/charts/nameslist/ |

[**Top**](#aid-classes) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
print(f"{cp.ins_chr(20, cp.Unicode.BLACK_CIRCLE+" ")}")
```


#### [Back](README.md)