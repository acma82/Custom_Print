#### [Back](README.md) 

# <span style="color:green"> <strong> Pen </strong> </span>

## Methods

    This class contains two methods:

    draw_line(size=0, layout=Layout.HORIZONTAL, tail="\N{BLACK DIAMOND}", body="-", head="\N{BLACK DIAMOND}")

    draw_rectangle(length=3, width=3, style=Line_Style.DASH)


| Rectangle Default Values      |                                   |                                 |
|-------------------------------|-----------------------------------|---------------------------------|
| top_left_corner_chr     = "+"	| top_horizontal_line_chr    = "-"  | right_vertical_line_chr = "|"   |
| top_right_corner_chr    = "+"	| bottom_horizontal_line_chr ="-"   | left_vertical_line_chr  = "|"   |
| bottom_right_corner_chr = "+"	| refill_bg_color = False           |                                 |
| bottom_left_corner_chr  = "+" |                                   |                                 |

| Line Default Values           | General Default Values            |
|-------------------------------|-----------------------------------|
|bold_draw_line = False         | adj_indent = 0                    |
bg_draw_line    = -1			|                                   |
fg_draw_line    = -1            |                                   |


<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pen = cp.Pen()
    pen.adj_indent = 8
    pen.draw_line(size=20, layout=cp.Layout.HORIZONTAL, tail=cp.Unicode.BLACK_LEFT_POINTING_TRIANGLE,
                  body=cp.Unicode.EM_DASH, head=cp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE)
    cp.ins_newline(2)
    pen.adj_indent = 14
    pen.draw_rectangle(length=8, width=4, style=cp.Line_Style.DOUBLE)
```

custom_print module is not a big thing, but I hope you find useful occasionally. **Python 3.12.1** or greater is required.						

Note: custom_print module has been tested on RedHat 9, Centos Stream 9, AlmaLinux 9, and Windows 10.


#### [Back](README.md)

https://github.com/acma82/custom_print

## Report bugs at	→	acma.mex@hotmail.com
