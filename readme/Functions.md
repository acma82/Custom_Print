#### [Back](README.md)
# Functions
* <span style="color:blue"> <strong>Screen Fucntions </strong> </span>
  * [**clean**](#clean)
  * [**clear**](#clear)
  * [**erase**](#erase)
  * [**dimensions**](#dimensions)
  * [**resize**](#resize)

* <span style="color:blue"> <strong>  Internal Functions </strong> </span>
  * [**bg_ansi_colors**](#bg_ansi_colors)
  * [**fg_ansi_colors**](#fg_ansi_colors)
  * [**terminal_bell**](#terminal_bell)
  * [**ins_chr**](#ins_chr)
  * [**ins_newline**](#ins_newline)
  * [**reset_font**](#reset_font)
  * [**set_font**](#set_font)


## <span style="color:blue"><strong>  Screen Functions </span></strong>

## clean
It cleans the terminal and returns the cursor to home.

[**Top**](#functions) <span style="color:red"> <strong> Example: </strong> </span>

```python
import time
import custom_print as cp
print("Hello")
time.sleep(3)
cp.clean() # ansi code
```

## clear
It clears the terminal and returns the cursor to home.

[**Top**](#functions) <span style="color:red"> <strong> Example: </strong> </span>

```python
import time
import custom_print as cp
print("Hello")
time.sleep(3)
cp.clear() # operating system 
```

## erase
It erases the terminal and leaves the cursor in the current position.

[**Top**](#functions) <span style="color:red"> <strong> Example: </strong> </span>

```python
import time
import custom_print as cp
print("erase() function cleans the terminal and the cursor remain in the same position")
print("erase uses the ansi system")
time.sleep(3)
cp.erase()
print("Good Bye...!")
```

## dimensions
It returns the dimensions of the terminal, cols and rows.

[**Top**](#functions) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
cols, rows = cp.dimensions()
print("fp.dimensions() -> It returns the dimensions of the screen")
print("cols: ", cols, "  rows: ", rows)
```


## resize
***resize(row = 25, cols = 80)*** <br>
It resizes the terminal size.

[**Top**](#functions) <span style="color:red"> <strong> Example: </strong> </span>
```python   
    import custom_print as cp
    cp.clean()
    r, c = cp.dimensions()
    print(f"rows: {r}, cols: {c}")
    cp.resize(25, 120)
    print("Good Bye...!")    
```

## <span style="color:blue"><strong>  Internal Functions </span></strong>

## bg_ansi_colors
***bg_ansi_colors(bold = False, fg = -1, n_line = 0)*** <br>
This function displays all background colors available with ansi code. The following options are for a better visualization.

- The bold option for the font (True/False).
- The fg option to visualize the background colors with a specific foreground color.
- The n_line option to inset lines between the colors. 

[**Top**](#functions) <span style="color:red"> <strong> Example: </strong> </span>

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

[**Top**](#functions) <span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    cp.fg_ansi_colors(bold=True, bg=-1, n_line=1)
```

## ins_chr
***ins_chr(n = 1, unicode = " ")*** <br>
This function inserts **n** times the **unicode** provided, by default it is set to space.

[**Top**](#functions) <span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    print(f"{cp.ins_chr(n=80, unicode="-")}")
    print(f"{cp.ins_chr(n=80, unicode="\u25B6")}")
```

## ins_newline
***ins_newline(n=1)*** <br>
This function inserts **n** new lines.

[**Top**](#functions) <span style="color:red"> <strong> Example: </strong> </span>

```python
    import custon_print as cp
    print("Hello")
    cp.ins_newline(2)
    print("Bye")
```

## terminal_bell
This function makes the sound of the terminal bell.

[**Top**](#functions) <span style="color:red"> <strong> Example: </strong> </span>

```python
    import custon_print as cp
    input("Press Enter")
    cp.terminal_bell()
```

## move_cursor_right
move_cursor_right(n=0,option_space=False)
This function moves the cursor **n** times to the right. If the option space is set to True, it will print spaces rather than just move the cursor.

```python
    import custom_print as cp
    print(f"Hello{move_cursor_right(10)}Custom_Print...!")
```

## subscript and superscript Functions
These functions returns the argument as subscript or superscript respectively.
```python
    import custom_print as cp
    print(f"Water -> H{cp.subscript(2)}O    Power: X{cp.superscript('5+v')}+5")
```

## set_font
***set_font(bold=False, bg=-1, fg=-1, italic=False, underline=False, strike=False, blinking=False, dim=False, hidden=False, inverse=False)*** <br>
This function passes many attributes for the font. If passing all these arguments is a little annoying to you, you can use the **Bg, Fg, Style** Classes explained in the ***Font Color section*** or use **Font_Style** Class. The best way to use this function is to pass only the first 3 parameters like the example below. 

[**Top**](#functions) <span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
	print(cp.set_font(1,11,21) + " Python is " + cp.set_font(0,1) + " Wonderful."+cp.reset_font())           
	print(f"{cp.set_font(bold=0, bg=22, fg=0)} Python {cp.set_font(1,90,7)} Language.{cp.reset_font()}")

    Colors range goes from -1 to 256. To set the default color from the system use -1 or 256.
```

## reset_font
**reset_font()** &rarr; This function resets the font attruibutes when we use the **set_font()** function.

**Note:** These functions are being used by the **FancyFormat** Class. Feel free to ignore them if they are not useful to you

#### [Back](README.md)