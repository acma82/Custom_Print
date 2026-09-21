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


```python
import custom_print as cp
msg = cp.FancyMessage()
msg.title_align = cp.Align.CENTER
msg.footnote_align = "right"   # msg.footnote_align = "r"
```
    Note: Although Align.NONE exist, it is only used with the FontStyle class using the method  print_style. For examples check their documentation.

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>


## Ascii_Letter
|    |                          |                  |
|----|--------------------------|------------------|
| id | Name                     | Value            |
|  1 | Alpha_Letter             | "Alpha"          |
|  2 | Ascii_Letter.ANSI_SHADOW | "ANSI_Shadow"    |
|  3 | Ascii_Letter.BIG         | "Big"            |
|  4 | Ascii_Letter.BLOCKS      | "Blocks"         |
|  5 | Ascii_Letter.BULBHEAD    | "Bulbhead"       |
|  6 | Ascii_Letter.CLASSY      | "Classy"         |
|  7 | Ascii_Letter.COLOSSAL    | "Colossal"       |
|  8 | Ascii_Letter.CRAZY       | "Crazy"          |
|  9 | Ascii_Letter.DOH         | "Doh"            |
| 10 | Ascii_Letter.DOOM        | "Doom"           |
| 11 | Ascii_Letter.EPIC        | "Epic"           |
| 12 | Ascii_Letter.GRACEFUL    | "Graceful"       |
| 13 | Ascii_Letter.LARRY       | "Larry"          |
| 14 | Ascii_Letter.MONEY_NE    | "Money_NE"       |
| 15 | Ascii_Letter.MONEY_NW    | "Money_NW"       |
| 16 | Ascii_Letter.MONEY_SE    | "Money_SE"       |
| 17 | Ascii_Letter.MONEY_SW    | "Money_SW"       |
| 18 | Ascii_Letter.MONO        | "Mono"           |
| 19 | Ascii_Letter.MOON        | "Moon"           |
| 20 | Ascii_Letter.MOON2       | "Moon2"          |
| 21 | Ascii_Letter.ROMAN       | "Roman"          |
| 22 | Ascii_Letter.STANDARD    | "Standard"       |
| 23 | Ascii_Letter.SWEET       | "Sweet"          |


[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custom_print as cp
msg = cp.Art()
msg.ascii_type = cp.Ascii_Letter.MOON
```
> <span style="color:cyan" ><strong>  This class is used along AsciiArt. It contains 23 options. See the AsciiArt Class to visualize a complete example</strong>

## Bg

    This class is mainly used where background color is needed.
    See all the name available by calling the "bg_ansi_colors" function.

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>
```python
import custom_print as cp
print(f"{cp.Bg.SEA_BLUE} Hello There {cp.Bg.OFF} Bye ")
```
> <span style="color:cyan" ><strong>  This class is used where bg color is needed by its name. It contains 256 options.</strong>


## Divider_Style

    This class select the type of style for the divider to be used.

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
    This class is mainly used where foreground color is needed.
    See all the name available by calling the "fg_ansi_colors" function.

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>
```python
import custom_print as cp
print(f"{cp.Fg.SEA_BLUE} Hello There {cp.Fg.OFF} Bye ")

```
> <span style="color:cyan" ><strong>  This class is used where Fg color is needed by its name.  It contains 256 options.</strong>



## Layout
<!--- ## <span style="color:green"> <strong> Layout </strong> </span> --->
    This class is used where layout is needed. It contains 2 options.

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

      CUSTOMIZED        DESIGN_1
      DASH_LINE         DESIGN_2        PURPLE_WHITE
      SINGLE_LINE       DESIGN_3        WHITE_BLACK_1
      SINGLE_BOLD       DESIGN_4        WHITE_BLACK_2
      SINGLE_HEAVY      DESIGN_5        WHITE_PURPLE
      DOUBLE_LINE       DESIGN_6        TURQUOISE_BLACK
      SQ_BRACKETS       DESIGN_7        TURQUOISE_WHITE
      NONE              DESIGN_8        WHITE_BLACK_PURPLE
      SPACE_0           DESIGN_9        GRAY_TEAL_WHITE
      SPACE_1           DESIGN_10       BLUE_PURPLE_WHITE_1
      SPACE_2           RED_WHITE       BLUE_PURPLE_WHITE_2
      SPACE_3           BLUE_WHITE      GREEN_GREEN_BLACK
      SPACE_4           TEAL_WHITE      OLIVE_GREEN
      SPACE_5           SPACE_6


***Note that these options can be replaced for the original values.***

       CUSTOMIZED   = "customized"         DESIGN_1     = "design_1"
       DASH_LINE    = "dash_line"          DESIGN_2     = "design_2"
       SINGLE_LINE  = "single_line"        DESIGN_3     = "design_3"
       SINGLE_BOLD  = "single_bold"        DESIGN_4     = "design_4"
       SINGLE_HEAVY = "single_heavy"       DESIGN_5     = "design_5"
       DOUBLE_LINE  = "double_line"        DESIGN_6     = "design_6"
       SQ_BRACKETS  = "sq_brackets"        DESIGN_7     = "design_7"
       NONE         = "none"               DESIGN_8     = "design_8"
       SPACE_0      = "space_0"            DESIGN_9     = "design_9"
       SPACE_1      = "space_1"            DESIGN_10    = "design_10"
       SPACE_2      = "space_2"            RED_WHITE    = "red_white"
       SPACE_3      = "space_3"            BLUE_WHITE   = "blue_white"
       SPACE_4      = "space_4"            TEAL_WHITE   = "teal_white"
       SPACE_5      = "space_5"            PURPLE_WHITE = "purple_white"
       SPACE_6      = "space_6"            OLIVE_GREEN  = "olive_green"

       WHITE_BLACK_1       = "white_black_1"
       WHITE_BLACK_2       = "white_black_2"
       WHITE_PURPLE        = "white_purple"
       TURQUOISE_BLACK     = "turquoise_black"
       TURQUOISE_WHITE     = "turquoise_white"
       WHITE_BLACK_PURPLE  = "white_black_purple"
       GRAY_TEAL_WHITE     = "gray_teal_white"
       BLUE_PURPLE_WHITE_1 = "blue_purple_white_1"
       BLUE_PURPLE_WHITE_2 = "blue_purple_white_2"
       GREEN_GREEN_BLACK   = "green_green_black"


<br>

**Note:** Options SPACE_X, use colors to visualize the effect on the tables while NONE will ignore all the colors assigned to the table, See the example below.

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

```python
    lst = [["Header 1", "Header 2", "Header 3", "Header 4"],
           ["Data 1",   "Data 2",   "Data 3",   "Data 4"  ],
           ["Data 5",   "Data 6",   "Data 7",   "Data 8"  ]]
    tbl = cp.FancyFormat()
    tbl.header_bg   = 23;         tbl.data_bg   = 231
    tbl.header_fg   = 231;        tbl.data_fg   = 21
    tbl.header_bold = True;       tbl.data_bold = True
    tbl.horizontal_line_bg  = 1;  tbl.adj_top_margin = 1
    tbl.vertical_line_bg    = 1;  tbl.adj_top_space  = 1

    tbl.inner_corner_bg  = 1
    tbl.outer_corner_bg  = 1
    tbl.header_corner_bg = 1
    tbl.header_horizontal_line_on = True
    tbl.bottom_horizontal_line_on = True
    tbl.top_horizontal_line_on    = True
    tbl.header_horizontal_line_bg = 1
    tbl.header_vertical_line_bg   = 1

    tbl.title_bg    = 231;                tbl.title_fg  = 16;      tbl.title_bold = True
    tbl.title_align = cp.Align.CENTER;    tbl.title_msg = " NONE "

    tbl.header_horizontal_line_on = False
    tbl.print_fancy_format(data=lst, style=cp.Line_Style.NONE)
    tbl.title_msg = " SPACE_0"
    tbl.print_fancy_format(lst, cp.Line_Style.SPACE_0)
    tbl.title_msg = " SPACE_1"
    tbl.print_fancy_format(lst, cp.Line_Style.SPACE_1)
    tbl.title_msg = " SPACE_2"
    tbl.print_fancy_format(lst, cp.Line_Style.SPACE_2)
    tbl.title_msg = " SPACE_3 "
    tbl.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_3)
    tbl.title_msg = " SPACE_4 "
    tbl.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_4)
    tbl.title_msg = " SPACE_5 "
    tbl.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_5)
    tbl.title_msg = " SPACE_6 "
    tbl.print_fancy_format(data=lst, style=cp.Line_Style.SPACE_6)
```



## Logo

    Logo class has a few options.

|             |
|-------------|
| Logo_Centos |
| Logo_Debian |
| Logo_Linux  |
| Logo_RedHat |
| Logo_Unix   |
|             |


[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

```python
     import custom_print as cp
     art_logo = cp.AsciiArt()
     art_logo.ascii_type = cp.Logo_Centos
```
**Note:** See AsciiArt Class for more options.










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
print("I am down")                       # direction = "down"
```

## No

    No class has 256 options. It represents the number of the color by its name.
    This class is used where a color needs to be assigned through the name rather than the number.

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

```python
      import custom_print as cp
      cp.bg_ansi_colors(bold=True, fg=0,  n_line=1)
      cp.fg_ansi_colors(bold=True, bg=-1, n_line=1)


      import custom_print as cp
      blue_msg = cp.FancyMessage()
      blue_msg.body_bg   = cp.No.VERY_LIGHT_BLUE
      blue_msg.body_fg   = cp.No.GO_GREEN
      blue_msg.print_fancy_message(" This is a DEMO...! ")

      # Note: These options can be replaced for the original values.

      import custom_print as cp
      blue_msg = cp.FancyMessage()
      blue_msg.body_bg   = 14
      blue_msg.body_fg   = 35
      blue_msg.print_fancy_message(" This is a DEMO...! ")
```



## Style
      The Style class allows you to customize the font style directly.
      The following are the available options:

|              |               |
|--------------|---------------|
| BOLD_ON      | BOLD_OFF      |
| DIM_ON       | DIM_OFF       |
| ITALIC_ON    | ITALIC_OFF    |
| UNDERLINE_ON | UNDERLINE_OFF |
| BLINKING_ON  | BLINKING_OFF  |
| INVERSE_ON   | INVERSE_OFF   |
| HIDDEN_ON    | HIDDEN_OFF    |
| STRIKE_ON    | STRIKE_OFF    |
| RESET_ALL    | OFF           |



[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>
```python
    import custom_print as cp

    message = f'''
    {cp.set_font(1,231,90)} \u25CF Output: {cp.reset_font()}
    {cp.ins_chr(11)} Normal {cp.Style.BOLD_ON}{cp.Style.ITALIC_ON}{cp.Style.UNDERLINE_ON} I am Bold,Italic and Underline. {cp.Style.OFF} Normal

    {cp.ins_chr(11)} {cp.Bg.SEA_BLUE}{cp.Style.BOLD_ON}{cp.Style.ITALIC_ON} Hello There {cp.Style.OFF} Bye {cp.Bg.OFF}

    {cp.ins_chr(11)} {cp.Bg.SEA_BLUE}{cp.Fg.GREEN_YELLOW}{cp.Style.BOLD_ON}{cp.Style.UNDERLINE_ON} Hello There {cp.Style.RESET_ALL} Bye

    {cp.ins_chr(11)} {cp.Bg.SEA_BLUE}{cp.Fg.GREEN_YELLOW}{cp.Style.BOLD_ON}{cp.Style.UNDERLINE_ON} Hello There {cp.reset_font()} Bye

    {cp.set_font(1,196,231)} Note {cp.reset_font()} Style.OFF only resets the style options and does not affect the
    '''
    print(message)
```

    background (bg) or foreground (fg) colors. To fully reset the
    font colors, use the reset_font() function or Style.RESET_ALL.

    Be aware that Bg.OFF only disables the background color, while
    Fg.OFF only disables the foreground color (and vice versa).


## Unicode
<!--- ## <span style="color:green"> <strong> Unicode </strong> </span> --->
    This class is to insert some unicode characters.

#### Unicode Names

    The Unicode class provides several predefined options

       • BOX_DRAWINGS_LIGHT_HORIZONTAL  ─
       • BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT  ├
       • BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT  ┤
       • BOX_DRAWINGS_LIGHT_VERTICAL            │
       • BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL  ┬
       • BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL   ┴
       • BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL ┼

       • BLACK_UP_POINTING_TRIANGLE    ▲
       • WHITE_UP_POINTING_TRIANGLE    △
       • BLAKC_RIGHT_POINTING_TRIANGLE ▶
       • WHITE_RIGHT_POINTING_TRIANGLE ▷
       • BLACK_DOWN_POINTING_TRIANGLE  ▼
       • WHITE_DOWN_POINTING_TRIANGLE  ▼
       • BLACK_LEFT_POINTING_TRIANGLE  ◀
       • WHITE_LEFT_POINTING_TRIANGLE  ◁

       • RIGHT_ARROW                →
       • LEFT_ARROW                 ←
       • UP_ARROW                   ↑
       • DOWN_ARROW                 ↓
       • UP_DOWN_ARROW              ↕
       • UPWARDS_PAIRED_ARROWS      ⇈
       • DOWNWARDS_PAIRED_ARROWS    ⇊
       • LEFTWARDS_PAIRED_ARROWS    ⇇
       • RIGHTWARDS_PAIRED_ARROWS   ⇉
       • BLACK_RIGHTWARDS_ARROWHEAD ➤

       • FIRE 🔥
       • EYES  👀
       • POOP  💩
       • FACE (◕◡◕)
       • GHOST  👻
       • CLOWN  🤡
       • BALLON  🎈
       • BULLET •
       • COFFEE  ☕
       • EM_DASH —
       • LOWERCASE_N_TILDE   ñ
       • UPPERCASE_N_TILDE   Ñ
       • LEFT_CURLY_BRACKET  {
       • RIGHT_CURLY_BRACKET }

       • SUBSCRIPT_ALPHA   ?          • SUPERSCRIPT_ALPHA   ᵅ
       • SUBSCRIPT_BETA    ᵦ          • SUPERSCRIPT_BETA    ᵝ
       • SUBSCRIPT_GAMMA   ᵧ          • SUPERSCRIPT_GAMMA   ᵞ
       • SUBSCRIPT_DELTA   ?          • SUPERSCRIPT_DELTA   ᵟ
       • SUBSCRIPT_EPSILON ?          • SUPERSCRIPT_EPSILON ᵋ
       • SUBSCRIPT_THETA   ?          • SUPERSCRIPT_THETA   ᶿ
       • SUBSCRIPT_IOTA    ?          • SUPERSCRIPT_IOTA    ᶥ
       • SUBSCRIPT_PHO     ᵨ          • SUPERSCRIPT_PHO     ?
       • SUBSCRIPT_PHI     ?          • SUPERSCRIPT_PHI     ᶲ
       • SUBSCRIPT_PSI     ᵩ          • SUPERSCRIPT_PSI     ᵠ
       • SUBSCRIPT_CHI     ᵪ          • SUPERSCRIPT_CHI     ᵡ

       • BLACK_DIAMOND ◆              • WHITE_DIAMOND   ◇
       • BLACK_DIAMOND_MINUS ❖        • WHITE_DIAMOND   ◈
       • LARGE_BLUE_DIAMON 🔷         • LARGE_ORANGE_DIAMON 🔶

       • RED_SQUARE          🟥       • RED_CIRCLE    🔴
       • BLUE_SQUARE         🟦       • BLUE_CIRCLE   🔵
       • ORANGE_SQUARE       🟧       • ORANGE_CIRCLE 🟠
       • YELLOW_SQUARE       🟨       • YELLOW_CIRCLE 🟡
       • GREEN_SQUARE        🟩       • GREEN_CIRCLE  🟢
       • PURPLE_SQUARE       🟪       • PURPLE_CIRCLE 🟣
       • BROWN_SQUARE        🟫       • BROWN_CIRCLE  🟤
       • BLACK_SQUARE        ⬛       • BLACK_CIRCLE  ⚫
       • WHITE_SQUARE        ⬜       • WHITE_CIRCLE  ⚪
       • BLACK_SQUARE_BUTTON 🔲       • WHITE_START_CIRCLE ✪
       • WHITE_SQUARE_BUTTON 🔳       • HEAVY_CIRCLE ⭕

[**Top**](#help-classes) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custom_print as cp
print(f"{cp.ins_chr(20, cp.Unicode.BLACK_CIRCLE+" ")}")
print(cp.Unicode.FIRE)
print(cp.Unicode.POOP)
```
    How Unicode Characters Work...!

    print Unicode value with 2 digits,  Use \x + number of character.
        1. print("\x65")

    print Unicode value from 2 to 4 digits, Use \u + number of the character.
        2. print("\u0065")
        3. print("\u2757")

    print Unicode value with 5 to 8 digits, Use \U + number of the character.
        4. print("\U00000065")
        5. print("\U00002757")
        6. print("\U0001F525 Fuego Code\")



    Print Unicode by Name: import unicodedata,  It may be necessary.
        7. print("\N{{FIRE}}   Fuego Name")
        8. print("\N{{LATIN SMALL LETTER A}}")
        9. print("\N{{NEGATIVE SQUARED CROSS MARK}}")
        10.print("\N{Eyes})

    Note: The U+2724 Unicode value is in Hexadecimal
        A. print("\u2724")         {cp.Unicode.RIGHT_ARROW}
        B. print("\U00002724")     {cp.Unicode.RIGHT_ARROW}
        C. print(chr(0x2724))      {cp.Unicode.RIGHT_ARROW}
        D. print("\N{{HEAVY FOUR BALLOON-SPOKED ASTERISK}}")

#### [Back](README.md)