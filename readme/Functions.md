#### [Back](README.md)
# Functions
* <span style="color:cyan"> <strong>Screen Fucntions </strong> </span>
  * [**clean**](#clean)
  * [**clear**](#clear)
  * [**erase**](#erase)
  * [**dimensions**](#dimensions)
  * [**resize**](#resize)

* <span style="color:cyan"> <strong>  Internal Functions </strong> </span>
  * [**bg_ansi_colors**](#bg_ansi_colors)
  * [**fg_ansi_colors**](#fg_ansi_colors)
  * [**ins_chr**](#ins_chr)
  * [**ins_newline**](#ins_newline)
  * [**reset_font**](#reset_font)
  * [**set_font**](#set_font)
  * [**terminal_bell**](#terminal_bell)


<!--  Screen Functions  -->

## <span style="color:cyan"><strong>  Screen Functions </span></strong>

## clean
It cleans the terminal and returns the cursor to home.

[**Top**](#functions) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import time
import custom_print as cp
print("Hello")
time.sleep(3)
cp.clean() # ansi code
print("Good Bye...!")
```

## clear
It clears the terminal and returns the cursor to home.

[**Top**](#functions) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import time
import custom_print as cp
print("Hello")
time.sleep(3)
cp.clear() # operating system
print("Good Bye...!")
```

## erase
It erases the terminal and leaves the cursor in the current position.

[**Top**](#functions) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import time
import custom_print as cp
print("This function cleans the terminal and the cursor remain in the same position, erase uses the ansi system")
time.sleep(3)
cp.erase()
print("Good Bye...!")
```

## dimensions
It returns the dimensions of the terminal, cols and rows.

[**Top**](#functions) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custom_print as cp
cols, rows = cp.dimensions()
print("cols: ", cols, "  rows: ", rows)
```


## resize
***resize(row = 25, cols = 80)*** <br>
It resizes the terminal size.

[**Top**](#functions) <span style="color:gray"> <strong> Example: </strong> </span>
```python   
import custom_print as cp
cp.clean()
r, c = cp.dimensions()
print(f"rows: {r}, cols: {c}")
cp.resize(25, 120)
print("Good Bye...!")    
```
    Note: This only works when we are using the gnome or Xfce terminal.
          Using konsole or another type of termial it may not work.





<!--  Internal Functions  -->



## <span style="color:cyan"><strong>  Internal Functions </span></strong>
    All these functions are used internally by the Custom_Print module. However,
    they are also exposed to the user. Feel free to use them if you find them
    useful, or simply ignore them if not needed.
## bg_ansi_colors
***bg_ansi_colors(bold = False, fg = -1, n_line = 0)*** <br>
This function displays all background colors available with ansi code. The following options are for a better visualization.

- The bold option for the font (True/False).
- The fg option to visualize the background colors with a specific foreground color.
- The n_line option to inset lines between the colors. 

[**Top**](#functions) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custom_print as cp
cp.bg_ansi_colors(bold=True, fg=0, n_line=1)
```


## fg_ansi_colors
***fg_ansi_colors(bold = False, bg = -1, n_line = 0)*** <br>
This function displays all the foreground colors available with ansi code. The following options are for a better visualization.
* The bold option for the font (True / False).
* The bg option to visualize the background colors with a specific foreground color.
* The n_line option to insert lines between the colors.

[**Top**](#functions) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custom_print as cp
cp.fg_ansi_colors(bold=True, bg=-1, n_line=1)
```


## ins_chr
***ins_chr(n = 1, unicode = " ")*** <br>
This function inserts **n** times the **unicode** provided, by default it is set to space.

[**Top**](#functions) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custom_print as cp
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="\u25B6")}")
```

## ins_newline
***ins_newline(n=1)*** <br>
This function inserts **n** new lines.

[**Top**](#functions) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custon_print as cp
print("Hello")
cp.ins_newline(2)
print("Bye")
```


## move_cursor_right
move_cursor_right(n=0,option_space=False)

option True, it will print **n** spaces. Option False, it won't print spaces it will only move the cursor. 

```python
import custom_print as cp
print(f"Hello{move_cursor_right(10)}Custom_Print...!")
```

## set_font
**set_font(bold=False, bg=-1, fg=-1, italic=False, underline=False, strike=False, blinking=False, dim=False, hidden=False, inverse=False)** <br>

    This function allows you to configure multiple font attributes. However,
    passing all these parameters can be cumbersome. For a more convenient
    approach, use the Bg, Fg, or Style classes described in the Font Color
    section, or use the Font_Style class instead.

    It is recommended to only pass the first three parameters, as shown in
    the example below.

[**Top**](#functions) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custom_print as cp
print(cp.set_font(1,11,21) + " Python is " + cp.set_font(0,1) + " Wonderful."+cp.reset_font())           
print(f"{cp.set_font(bold=0, bg=22, fg=0)} Python {cp.set_font(1,90,7)} Language.{cp.reset_font()}")

    Colors range goes from -1 to 256. To set the default color from the system use -1 or 256.
```


## reset_font
**reset_font()** &rarr; This function resets the font attruibutes when we use the **set_font()** function.

**Note:** These functions are being used by the **FancyFormat** Class. Feel free to ignore them if they are not useful to you


## subscript and superscript Functions
These functions returns the argument as subscript or superscript respectively.
```python
import custom_print as cp
print(f"Water -> H{cp.subscript(2)}O    Power: X{cp.superscript('5+v')}+5")
```
**Subscript**

    Note: If the symbol digit is not in the subscript_map, then it will set to ? which is the default value.

    subscript_map contains the following characters:
        a, e, h, i, j, k, l, m, n, o, p, r, s, t, u, v, x,
        0, 1, 2, 3, 4, 5, 6, 7, 8' 9, +, -, =, (, )


    subscript_map DOES NOT contains the following characters:
        b, c, d, f, g, q, w, y, z,
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T,
        U, V, W, X, Y, Z

**Superscript**

    Note: If the symbol digit is not in the superscript_map, then it will set to ? which is the default value.

    superscript_map contains the following characters:
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, r, s, t, u, v, w, x, y,
        A, B, D, E, G, H, I, J, K, L, M, N, O, P, R, T, U, V, W,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        +, -, =, (, )


    superscript_map DOES NOT contains the following characters:
        q, z,
        C, F, Q, S, X, Y,
        Z


## terminal_bell
This function makes the bell sound in the terminal.

[**Top**](#functions) <span style="color:gray"> <strong> Example: </strong> </span>

```python
import custon_print as cp
input("Press Enter")
cp.terminal_bell()
```

#### [Back](README.md)