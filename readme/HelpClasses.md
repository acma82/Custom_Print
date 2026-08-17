#### [Back](README.md)

# Help Classes
* [**Align**](#align)
* [**Ascii_Letter**](#ascii_letter)
* [**Bg**](#bg)
* [**Divider_Style**](#divider_style)
* [**Fg**](#fg)
* [**Layout**](#layout)
* [**Length_bg**](#length_bg)
* [**Line_Style**](#line_style)
* [**Logo**](#logo)
* [**Move**](#move)
* [**No**](#no)
* [**Style**](#style)
* [**Unicode**](#unicode)



## Align
<!--- ## <span style="color:green"> <strong> Align </strong> </span> --->
> <span style="color:cyan" ><strong>  This class is used where alignment is needed. It contains 4 options. </strong>
- Align.RIGHT
- Align.LEFT
- Align.CENTER
- Align.JUSTIFY

**Note:** These options can be replaced for the original values as displays below:  

| Align.RIGHT | Align.LEFT | Align.CENTER | Align.JUSTIFY |
| :---------: | :--------: | :----------: | :-----------: |
| "right"     | "left"     |"center"      | "justify"     |
| "r"         | "l"        |"c"           | "j"           |

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>


```python
import custom_print as cp
msg = cp.FancyMessage()
msg.title_align = cp.Align.CENTER
msg.footnote_align = "right"   # msg.footnote_align = "r"
```

## Ascii_Letter
|                         |                  |
|-------------------------|------------------|
|Name                     | Value            |
|Alpha_Letter             | "Alpha"          |
|Ascii_Letter.ANSI_Shadow | "ANSI_Shadow"    |
|Ascii_Letter.Big         | "Big"            |
|Ascii_Letter.Blocks      | "Blocks"         |
|Ascii_Letter.Bulbhead    | "Bulbhead"       |
|Ascii_Letter.Classy      | "Classy"         |
|Ascii_Letter.Colossal    | "Colossal"       |
|Ascii_Letter.Crazy       | "Crazy"          |
|Ascii_Letter.Doh         | "Doh"            |
|Ascii_Letter.Doom        | "Doom"           |
|Ascii_Letter.Epic        | "Epic"           |
|Ascii_Letter.Graceful    | "Graceful"       |
|Ascii_Letter.Larry       | "Larry"          |
|Ascii_Letter.Money_NE    | "Money_NE"       |
|Ascii_Letter.Money_NW    | "Money_NW"       |
|Ascii_Letter.Money_SE    | "Money_SE"       |
|Ascii_Letter.Money_SW    | "Money_SW"       |
|Ascii_Letter.Mono        | "Mono"           |
|Ascii_Letter.Moon        | "Moon"           |
|Ascii_Letter.Moon2       | "Moon2"          |
|Ascii_Letter.Roman       | "Roman"          |
|Ascii_Letter.Standard    | "Standard"       |
|Ascii_Letter.Sweet       | "Sweet"          |


[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custom_print as cp                 
msg = cp.Art()
msg.ascii_type = cp.Ascii_Letter.Moon
```
> <span style="color:cyan" ><strong>  This class is used along AsciiArt. It contains 23 options.</strong>

## Bg

See all the name availables by using the "ansi_colors" function.

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>
```python
import custom_print as cp
print(f"{cp.Bg.SEA_BLUE} Hello There {cp.Bg.OFF} Bye ")
```
> <span style="color:cyan" ><strong>  This class is used where bg color is needed by its name. It contains 256 options.</strong>


## Divider_Style
|             |                 |
|-------------|-----------------|
|Name         | Value           |
|CUSTOMIZED   | "customized"    |
|SINGLE_LINE  | "single_line"   |
|SINGLE_BOLD  | "single_bold"   |
|SINGLE_HEAVY | "single_heavy"  |
|DOUBLE_LINE  | "double_line"   |
|DASH_1       | "dash_1"        |
|DASH_2       | "dash_2"        |
|SQ_BRACKETS  | "sq_brackets"   |
|BLUE_WHITE_1 | "blue_white_1"  |
|BLUE_WHITE_2 | "blue_white_2"  |

> <span style="color:cyan" ><strong>  This class is used where a divider is needed. It contains 10 options.</strong>

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custom_print as cp
div.print_fancy_divider(message=" Custom Print Divider", style=cp.Divider_Style.CUSTOMIZED)
div.print_fancy_divider(message=" Custom Print Divider", style=cp.Divider_Style.DASH_1)
# same as above
div.print_fancy_divider(message=" Custom Print Divider", style="customized")
div.print_fancy_divider(message=" Custom Print Divider", style="dash_1")
```

## Fg
See all the name availables by using the "ansi_colors" function

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>
```python
import custom_print as cp
print(f"{cp.Fg.SEA_BLUE} Hello There {cp.Fg.OFF} Bye ")

```
> <span style="color:cyan" ><strong>  This class is used where Fg color is needed by its name.  It contains 256 options.</strong>



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

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>
```python
import custom_print as cp
tbl  = cp.FancyFormat()

r = range(0,21,2)
tbl.print_fancy_format(r)
tbl.set_layout = cp.Layout.VERTICAL     # tbl.set_layout = "v" 
tbl.print_fancy_format(r)
```
## Length_Bg
<!--- ## <span style="color:green"> <strong> Length_bg </strong> </span> --->
    his class is used with FancyMessage class and contains 2 options.
+ ALL_ROW
+ ONLY_WORD

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custom_print as cp
msg = cp.FancyMessage()
path = " The new path: /mnt/home/user_name/Documents/ " # usually use with a paragra message type

msg.body_bg = 10
msg.body_fg = 0
msg.body_bold = True
msg.length = cp.Length_Bg.ONLY_WORD

msg.adj_bg_lines_to_right_indent =  False   # True make all the way to the space available
msg.adj_bg_msg_to_space_available = False   # True make all the way to the space available
# These two options are only available when using the msg.length = cp.Length_Bg.ONLY_WORD
# otherwise they will make it to the longest line

msg.print_fancy_message(path)
cp.ins_newline(3)
msg.length = cp.Length_Bg.ALL_ROW # all the width of the terminal
msg.print_fancy_message(path)
```





## Line_Style
<!--- ## <span style="color:green"> <strong> Line_Style </strong> </span> --->
	This class is used with FancyFormat class. There are some options available.

                    
      CUSTOMIZED     DESIGN_1    WHITE_PURPLE       
      DASH_LINE      DESIGN_2    WHITE_BLACK_PURPLE 
      SINGLE_LINE    DESIGN_3    WHITE_BLACK_1      
      DOUBLE_LINE    DESIGN_4    WHITE_BLACK_2      
      SINGLE_BOLD    DESIGN_5    PURPLE_WHITE       
      SINGLE_HEAVY   DESIGN_6    TURQUOISE_WHITE    
      SQ_BRACKETS    DESIGN_7    TEAL_WHITE         
      NONE           DESIGN_8    GRAY_TEAL_WHITE    
      NONE_SPACE_1   DESIGN_9    BLUE_PURPLE_WHITE_1
      NONE_SPACE_2   DESIGN_10   BLUE_PURPLE_WHITE_2
      SINGLE_SPACE   RED_WHITE   TURQUOISE_BLACK    
      DOUBLE_SPACE   BLUE_WHITE  GREEN_GREEN_BLACK  
                    

      Note: These options can be replaced for the original values.

      CUSTOMIZED   = "customized"        DESIGN_1   = "design_1"
      DASH_LINE    = "dash_line"         DESIGN_2   = "design_2"
      SINGLE_LINE  = "double_line"       DESIGN_3   = "design_3"
      DOUBLE_LINE  = "single_line"       DESIGN_4   = "design_4"
      SINGLE_BOLD  = "single_bold"       DESIGN_5   = "design_5"
      SINGLE_HEAVY = "single_heavy"      DESIGN_6   = "design_6"
      SQ_BRACKETS  = "sq_brackets"       DESIGN_7   = "design_7"
      NONE         = "none"              DESIGN_8   = "design_8"
      NONE_SPACE_1 = "none_space_1"      DESIGN_9   = "design_9"
      NONE_SPACE_2 = "none_space_2"      DESIGN_10  = "design_10"
      SINGLE_SPACE = "single_space"      RED_WHITE  = "red_white"
      DOUBLE_SPACE = "double_space"      BLUE_WHITE = "blue_white"

      WHITE_PURPLE        = "white_purple"
      WHITE_BLACK_PURPLE  = "white_black_purple"
      PURPLE_WHITE        = "purple_white"
      TURQUOISE_WHITE     = "turquoise_white"
      TEAL_WHITE          = "teal_white"
      GRAY_TEAL_WHITE     = "gray_teal_white"
      BLUE_PURPLE_WHITE_1 = "blue_purple_white_1"
      BLUE_PURPLE_WHITE_2 = "blue_purple_white_2"
      GREEN_GREEN_BLACK   = "green_green_black"
      WHITE_BLACK_1       = "white_black"
      WHITE_BLACK_2       = "white_black_2"
      TURQUOISE_BLACK     = "turquoise_black"


<br>


[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

```python
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

    tbli.title_bg    = 231
    tbli.title_fg    = 16
    tbli.title_bold  = True
    tbli.title_align = cp.Align.CENTER
    tbli.title_msg   = " NONE "
    tbli.print_fancy_format(data=lst, style=cp.Line_Style.NONE)

    tbli.title_msg = " NONE_SPACE_1"
    tbli.print_fancy_format(lst, cp.Line_Style.NONE_SPACE_1)

    tbli.title_msg = " NONE_SPACE_2"
    tbli.print_fancy_format(lst, cp.Line_Style.NONE_SPACE_2)

    tbli.title_msg = " SINGLE_SPACE "
    tbli.print_fancy_format(lst, cp.Line_Style.SINGLE_SPACE)

    tbli.title_msg = " DOUBLE_SPACE "
    tbli.print_fancy_format(lst, cp.Line_Style.DOUBLE_SPACE)

```





## Logo
[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>












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


[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custom_print as cp
crs = cp.Cursor()
clear()
# jumpTo method
crs.jumpTo(qty=2, direction = Move.DOWN) # direction = "d"
print("I am down")

```

## No
[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

## Style
[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

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

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custom_print as cp
print(f"{cp.ins_chr(20, cp.Unicode.BLACK_CIRCLE+" ")}")
```


#### [Back](README.md)