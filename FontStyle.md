#### [Back](README.md) 
# <span style="color:blue"> <strong> FontStyle </strong> </span>
* [**Methods**](#methods)
* [**Default Values**](#default-values)
* [**Examples**](#examples)


## Methods

This class contains 4 methods and the attributes and their default values are displays below.

+ **style_on() and style_off()** 

    These methods are used if we will be continuing using the style in many rows.

+ **reset_style()** 

    This method will reset the style to the default values.

+ **print_style(msg=message)**

    This method will print the style with the defined attributes.

[**Top**](#fontstyle)

## Default Values

```python
	bg     = -1           hidden   = False        force_align     = False 
    fg     = -1           indent   = 0            blinking        = False
    dim    = False        strike   = False        underline       = False
	bold   = False        italic   = False        bg_top_lines    = 0
    align  = "j"          inverse  = False	      bg_bottom_lines = 0
        	   

	indent → this defines how far we want to start to print the message from the left, it works with style_on and print_style.

	bg_top_lines  and bg_bottom_lines → these are lines above and below the message with the bg specified.
```

## Examples

[**Top**](#fontstyle) <span style="color:red"> <strong> Example 1: <span style="color:purple"> style_on() and style_off() </span> </strong> </span>

```python
	import custom_print as cp
	fs = cp.FontStyle()
	fs.bg = 21
	fs.fg = 231
	print(f”{fs.style_on()}Font Style Line 1 ”)
	print(f” Font Style Line 2 ”)
	print(f” Font Style Line 3 {fs.style_off()}”)
	fs.reset_style()
	print(f”{fs.style_on()} Default Style {fs.style_off()}”)	
```

[**Top**](#fontstyle) <span style="color:red"> <strong> Example 2: <span style="color:purple"> print_style(msg) </span> </strong> </span>

```python
    import custom_print as cp
    fs = cp.FontStyle()

    fs.fg = 231
    fs.bg = 23
    fs.bold = True
    fs.bg_top_lines = 1
    fs.bg_bottom_lines = 1

    #-------------------------------------------
    msg = f'''
    Full Name Author Here...!
    Align.OPTION
    force_align = False
    Python3.12
    '''

    fs.align = cp.Align.LEFT
    fs.print_style(msg)

    fs.align = cp.Align.CENTER
    fs.print_style(msg)

    fs.align = cp.Align.RIGHT
    fs.print_style(msg)

    fs.align = cp.Align.JUSTIFY
    fs.indent = 7
    fs.print_style(msg)
    cp.ins_newline(2)

    fs.align = "none"
    fs.print_style(msg)
    cp.ins_newline(2)

    #-------------------------------------------
    print(f"{cp.ins_chr(90,"-")}")
    #-------------------------------------------

    msg = f'''
    Full Name Author Here...!
    Align.OPTION
    force_align = True
    Python3.12
    '''

    cp.ins_newline(2)
    fs.force_align = True
    fs.align = cp.Align.LEFT
    fs.print_style(msg)

    fs.align = cp.Align.CENTER
    fs.print_style(msg)

    fs.align = cp.Align.RIGHT
    fs.print_style(msg)

    fs.align = cp.Align.JUSTIFY
    fs.indent = 12
    fs.print_style(msg)

    cp.ins_newline(2)
    fs.align = "none"
    fs.print_style(msg)
```

[**Top**](#fontstyle) <span style="color:red"> <strong> Example 3: <span style="color:purple"> print_style(msg) </span> </strong> </span>

```python
    import custom_print as cp
    fs = cp.FontStyle()
    fs.fg = 231
    fs.bg = 90

    paragraph = '''
	This is the Module Docstrings
	Trailing WhiteSpace refers to any whitespace characters 
	at the end of a line of code or string.
	missing-final-newline refers to set
	the last empty line at the end of the code
	pylint practis.py
	'''

    cp.ins_newline(2)

	fs.align = cp.Align.CENTER
	fs.force_align = False
	fs.bg_top_lines = 1
	fs.bg_bottom_lines = 1
	fs.print_style(paragraph)

	cp.ins_newline(2)

	fs.align = cp.Align.CENTER
	fs.force_align = True
	fs.bg_top_lines = 2
	fst.bg_bottom_lines = 2
	fs.print_style(paragraph)
```
#### [Back](README.md)