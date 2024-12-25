#### [Back](README.md)

# Aid Classes
* [**Align**](#align)
* [**Layout**](#layout)
* [**Length_bg**](#length_bg)
* [**Line_Style**](#line_style)
* [**Move**](#move)
* [**Unicode**](#unicode)


## <span style="color:green"> <strong> Align </strong> </span>
<!-- >> <span style="color:blue" ><strong>  This class is used where alignment is needed. It contains 4 options.   -->

> This class is used where alignment is needed. It contains 4 options.

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
msg.align_title = cp.Align.CENTER
msg.align_footnote = "right"   # msg.align_footnote = "r"
```

## <span style="color:green"> <strong> Layout </strong> </span>
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

## <span style="color:green"> <strong> Length_bg </strong> </span>
    his class is used with FancyMessage class and contains 2 options.
+ ALL_ROW
+ ONLY_WORD

[**Top**](#aid-classes) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
msg = cp.FancyMessage()
path = " The new path: /mnt/home/user_name/Documents/ " # usually use with a paragra message type

msg.bg_body = 10
msg.fg_body = 0
msg.bold_body = True
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


## <span style="color:green"> <strong> Line_Style </strong> </span>
	This class is used with FancyFormat class and Pen class. There are some options available.

            CUSTOMIZED          SINGLE          SPACE_COL_COLOR
            SINGLE_BOLD         DASH            NO_SPACE_COL_COLOR
            SINGLE_HEAVY        DOUBLE
            SQR_BRACKETS        NONE


    Note: SPACE_COL_COLOR and NO_SPACE_COL_COLOR are not included in Pen class.

**Note:** These options can be replaced for the original values as displays below:

|                |                      |            |          |                                           |
|----------------|----------------------|------------|----------|-------------------------------------------|
|	CUSTOMIZED   | "customized"         | SINGLE     | "single" | SPACE_COL_COLOR    | "space_col_color"    |
|	SINGLE_BOLD  | "single_bold"        | DASH       | "dash"   | NO_SPACE_COL_COLOR | "no_space_col_color" |
|	SINGLE_HEAVY | "single_heavy"       | DOUBLE     | "double" |                    |                      |
|	SQ_BRACKETS  | "sq_brackets"        | NONE       | "none"   |                    |                      |


    Variables to visualize the effect on options SPACE_COL_COLOR and NO_SPACE_COL_COLOR with FancyFormat.

|                         |                                  |                                       |
|-------------------------|----------------------------------|---------------------------------------| 
|bg_horizontal_line  = 21 | bg_header                  = 90  | bg_data = 231                         |
|bg_vertical_line    = 21 | fg_header                  = 231 | fg_data  = 0                          |
|bg_corner_chr       = 21 | bold_header                = True| bold_data = True                      |
|bg_inner_corner_chr = 21 | bg_corner_under_line_header= 21  | middle_horizontal_line_on = True      |
|bg_under_line_header= 21 | bg_vertical_header_line_chr= 21	 | horizontal_line_under_header_on = True|


[**Top**](#aid-classes) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
tbl  = cp.FancyFormat()

r = range(0,21,2)
tbl.print_fancy_format(r, cp.Line_Style.DOUBLE)
tbl.set_layout = cp.Layout.VERTICAL
tbl.print_fancy_format(r, cp.Line_Style.SQ_BRACKETS)

```

## <span style="color:green"> <strong> Move </strong> </span>
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

## <span style="color:green"> <strong> Unicode </strong> </span>
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