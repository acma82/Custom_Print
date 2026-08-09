#### [Back](README.md)

# AsciiArt

This class contains 4 [**methods**](#methods) and the attributes and their [**default values**](#Default_Values) are displays below.


## Methods
* [**print_ascii_art**](#print-ascii-art)
* [**print_multi_ascii_art**](#print_multi_ascii_art)
* [**print_ascii_logo_art**](#print_ascii_logo_art)
* [**print_reversed_ascii_logo_art**](#print_reversed_ascii_logo_art)




## Default Values

```python
    bold     = False;                bg = -1;                             fg = -1
    italic   = False;                underline = False;                   strike = False
    blinking = False;                dim = False;                         hidden = False
    inverse  = False;                ascii_type = Ascii_Letter.Standard
          
    adj_indent = 0;                  adj_space  = 0;                      delay_ms   = 0
    set_layout = Layout.VERTICAL;    set_top_line = True;                 set_bottom_line = True; 
    adj_left_space = 0;              adj_middle_space = 0;                adj_right_space = 0
        	   
```

<strong> Note </strong> → When using logo with your own colors the set_layout Horizontal will not work properly becuase it breaking into columns and that will cause problems unless you use the colors with the variables bg and fg then it will work properly.
you can use the HORIZONTAL set_layout and then you can use your own colors as shown below in the example.


# print ascii art
# print_multi_ascii_art
# print_ascii_logo_art
# print_reversed_ascii_logo_art


