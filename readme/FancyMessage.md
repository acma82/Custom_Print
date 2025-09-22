#### [Back](README.md)
# FancyMessage
<!--- # <span style="color:green"> <strong> FancyMessage </strong> </span> --->

* [**Body Section**](#body-default-values)
* [**Note Section**](#note-default-values)
* [**Title Section**](#title-default-values)
* [**Footnote Section**](#footnote-default-values)
* [**Fancy Message Examples**](#fancy-message-examples)


<!-- ---------------------------------- -->
<!-- General Section                    -->
<!-- ---------------------------------- -->
## Methods

This class contains 3 methods and the attributes and their default values are displays below.
+ **print_fancy_message(body_msg="")**

	→ This method works with Body Default Values, Title and Footnote Attributes.

+ **print_fancy_note(body_msg="")**

	→ This method works with Body Default Values, and Note Default Attributes.

+ **get_message_attributes(body_msg="", print_attributes=True)**

	→This method returns the attributes of the message in 2 variables. A list with all the attributes of the message and another list with all the words of the message. It has the option to print all the attributes at the same time.

## Body Default Values

```python
    body_bg     = 4            body_hidden  = False        body_strike    = False
    body_fg     = 231          body_italic  = False        length         = Length_bg.ALL_ROW
    body_dim    = False        left_indent  = 2            body_inverse   = False
    body_bold   = False        right_indent = 2            body_blinking  = False
    body_msg    = "Body Msg"   top_lines    = 1            body_underline = False
    help_lines  = False        bottom_lines = 1
```


    The following options work when length is set to Length_bg.ONLY_WORD.

    They don't do anything when length is set to Length_bg.All_ROW.

	adj_bg_lines_to_right_indent  = False

	adj_bg_msg_to_space_available = False

    Note: All the above variables are being used by both methods, print_fancy_message and print_fancy_note.


[**Top**](#fancymessage)

## Note Default Values

```python
    note_msg  = " Note: "   note_align   = Align.JUSTIFY        note_blinking    = False
    note_bg   = 231         note_strike  = False                note_underline #-----------------------------------------------------------------------------------------------------+
#  Vertical line Variables                                                                            |
#-----------------------------------------------------------------------------------------------------+   
  = False
    note_fg   = 0           note_italic  = False                note_position    = 1
    note_bold = False       note_inverse = False                note_right_space = 2
    note_dim  = False       note_hidden  = False                note_left_space  = 2
```

## Title Default Values

```python
    title_msg  = ""         title_align   = Align.LEFT          title_blinking      = False
    title_bg   = 4          title_strike  = False               title_underline     = False
    title_fg   = 231        title_italic  = False               title_indent        = 2
    title_bold = False      title_inverse = False               lines_title_body    = 1
    title_dim  = False      title_hidden  = False
```

## Footnote Default Values

```python
    footnote_msg  = ""      footnote_align   = Align.RIGHT      footnote_blinking   = False
    footnote_bg   = 4       footnote_strike  = False            footnote_underline  = False
    footnote_fg	  = 231     footnote_italic  = False            footnote_indent     = 2
    footnote_bold = False   footnote_inverse = False            footnote_lines_body = 1
    footnote_dim  = False   footnote_hidden  = False
```

## Fancy Message Examples
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

	msg.title_msg = "TITLE"
	msg.footnote_msg = "FOOTNOTE"

	msg.print_fancy_message(paragraph)		#  Method 1

	cp.ins_newline(2)

	msg.note_msg = “Python”
    msg.note_position = 4
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
    attributes, words = fmsg.get_message_attributes(body_msg=paragraph3, print_attributes=True)

    print(attributes)
    print()
    print(words)
```

**Note:** *words is a list that contains all the word of the paragraph.*

#### [Back](README.md)