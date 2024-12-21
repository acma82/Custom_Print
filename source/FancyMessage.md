#### [Back](README.md) 
## <span style="color:blue"> <strong> FancyMessage </strong> </span>
### [1. Methods](#methods)
### [2. Body Section](#body-default-values)
### [3. Note Section](#note-default-values)
### [4. Title Section](#title-default-values)
### [5. Footnote Section](#footnote-default-values)
### [6. Examples](#examples)


<!-- ---------------------------------- -->
<!-- General Section                    -->
<!-- ---------------------------------- -->
## Methods

This class contains 3 methods and the attributes and their default values are displays below.
+ print_fancy_message(msg_body="")

	→ This method works with Body Default Values, Title and Footnote Attributes.

+ print_fancy_note(msg_body="")

	→ This method works with Body Default Values, and Note Default Attributes.

+ get_message_attributes(msg_body="", print_attributes=True)

	→This method returns the attributes of the message in 2 variables. A list with all the attributes of the message and another list with all the words of the message. It has the option to print all the attributes at the same time.

[**Top**](#fancymessage)

## Body Default Values

```python
    bg_body     = 4            hidden_body  = False        strike_body    = False			
    fg_body     = 231	       italic_body = False         length         = Length_bg.ALL_ROW 
    dim_body    = False	       left_indent  = 2            inverse_body   = False			
    bold_body   = False        right_indent = 2            blinking_body  = False			
    msg_body    = "Body Msg	   top_lines    = 1            underline_body = False			
    help_lines  = False        bottom_lines = 1
```

    These two options work when length is Length_bg.ONLY_WORD. They don't do anything when length is Length_bg.All_ROW.

	adj_bg_lines_to_right_indent  = False

	adj_bg_msg_to_space_available = False

    Note: All the above variables are being used by both methods, print_fancy_message and print_fancy_note.

[**Top**](#fancymessage)

## Note Default Values

```python
    msg_note = " Note: "    align_note   = Align.JUSTIFY        blinking_note    = False
    bg_note    = 231        strike_note  = False                underline_note   = False
    fg_note     = 0         italic_note  = False                position_note    = 1 
    bold_note = False       inverse_note = False                right_space_note = 2
    dim_note  = False       hidden_note  = False                left_space_note	 = 2	
```

[**Top**](#fancymessage)

## Title Default Values

```python
    msg_title  = ""         align_title   = Align.LEFT          blinking_title		= False
    bg_title   = 4          strike_title  = False               underline_title	= False
    fg_title   = 231        italic_title  = False               title_indent		= 2
    bold_title = False      inverse_title = False               lines_title_body	= 1
    dim_title  = False      hidden_title  = False
```
[**Top**](#fancymessage)

## Footnote Default Values

```python
    msg_footnote  = ""      align_footnote   = Align.RIGHT      blinking_footnote   = False
    bg_footnote   = 4		strike_footnote  = False            underline_footnote  = False
    fg_footnote	  = 231     italic_footnote  = False            footnote_indent     = 2
    bold_footnote = False   inverse_footnote = False            lines_body_footnote = 1
    dim_footnote  = False   hidden_footnote  = False
```

## Examples
[**Top**](#fancymessage) <span style="color:red"> <strong> Example 1: </strong> </span>

```python
    import custom_print as cp
	msg = cp.FancyFormat()

	paragraph = '''
    Guido van Rossum, a Dutch programmer, created Python in the late 1980s
	as a hobby project. He started working on it in December 1989 at Cent-
	rum Wiskunde & Informatica (CWI) in the Netherlands.

    Python was first released on February 20, 1991. Python was named after
	the 1970s BBC comedy sketch series Monty Python's Flying Circus.'''

	msg.msg_title = "TITLE"
	msg.msg_footnote = "FOOTNOTE"

	msg.print_fancy_message(paragraph)		#  Method 1

	cp.ins_newline(2)

	msg.msg_note = “Python”
    msg.position_note = 4
	msg.print_fancy_note(paragraph)			#  Method 2
```

[**Top**](#fancymessage) <span style="color:red"> <strong> Example 2: </strong> </span>

```python
    import custom_print as cp
    paragraph3 = '''
    I should probably collect a list of the best
    romantic poems ever written, and maybe I will.
    This is not that. I mostly talk about writing
    books, but I noticed most of the other big
    writing sites actually get most of the their

    traffic from this keyword, because everybody
    is interested in romantic poetry! When you
    want to tell her how you feel, but do not
    have the words to express all that emotion...!
    '''
    fmsg = cp.FancyMessage()                       #  Method 3
    attributes, words = fmsg.get_message_attributes(msg_body=paragraph3, print_attributes=True)

    print(attributes)
    print()
    print(words)
```

**Note:** *words is a list that contains all the word of the paragraph.*

#### [Back](README.md)