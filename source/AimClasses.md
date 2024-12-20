#### [Back](README.md)

## <span style="color:blue"> <strong> Aim Classes </strong> </span>
* [Align](#align)
* []

## <span style="color:purple"> <strong> Align </strong> </span>
    This class is used with the FancyFormat class and FancyMessage class. It contains 4 options.    

- Align.RIGHT
- Align.LEFT
- Align.CENTER
- Align.JUSTIFY

**Note:** These options can be replaced for the original values as displays below:

| Align.RIGHT | Align.LEFT | Align.CENTER | Align.JUSTIFY |
| :---------: | :--------: | :----------: | :-----------: |
| "right"     | "left"     |"center"      | "justify"     |
| "r"         | "l"        |"c"           | "j"           |

## <span style="color:purple"> <strong> Color </strong> </span>
    
```
This class will help to select a color when using the set_font() function or the FancyStyle class or you can use the number for the color as well.
```
| List of Color | Available in  | Custom Print | Module      |
|:-------------:|:-------------:|:------------:|:-----------:|
| BLACK    | RED        | BLUE          | GREEN        |             |


## <span style="color:purple"> <strong> Layout </strong> </span>
    This class is used with FancyFormat class and Pen class. It contains 2 options.

* Layout.HORIZONTAL
* Layout.VERTICAL

**Note:** These options can be replaced for the original values as displays below:

| Layout.HORIZONTAL | Layout.VERTICAL |
| :---------------: | :-------------: |
| "horizontal"      | "vertical"      |
| "h"               | "v"             |

## <span style="color:purple"> <strong> Length_bg </strong> </span>
    his class is used with FancyMessage class and contains 2 options.
+ ALL_ROW
+ ONLY_WORD

## <span style="color:purple"> <strong> Line_Style </strong> </span>
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
|	SINGLE_BOLD  | single_bold"         | DASH       | "dash"   | NO_SPACE_COL_COLOR | "no_space_col_color" |
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


<span style="color:red"> <strong> Example: </strong> </span> Check Demo_6.


## <span style="color:purple"> <strong> Move </strong> </span>
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


## <span style="color:purple"> <strong> Unicode </strong> </span>
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

#### [Back](README.md)