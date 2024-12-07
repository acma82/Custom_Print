'''
custom_print module can handle any type of variable.
'''

#pylint: disable=bare-except
#pylint: disable=invalid-name
#pylint: disable=unused-import
#pylint: disable=line-too-long
#pylint: disable=too-many-lines
#pylint: disable=no-else-return
#pylint: disable=unused-variable
#pylint: disable=too-many-locals
#pylint: disable=protected-access
#pylint: disable=too-many-branches
#pylint: disable=consider-using-in
#pylint: disable=chained-comparison
#pylint: disable=too-many-arguments
#pylint: disable=too-many-statements
#pylint: disable=multiple-statements
#pylint: disable=consider-using-join
#pylint: disable=unspecified-encoding
#pylint: disable=unnecessary-negation
#pylint: disable=singleton-comparison
#pylint: disable=too-many-nested-blocks
#pylint: disable=too-many-public-methods
#pylint: disable=expression-not-assigned
#pylint: disable=consider-using-enumerate
#pylint: disable=unnecessary-comprehension
#pylint: disable=too-many-return-statements
#pylint: disable=unbalanced-tuple-unpacking
#pylint: disable=consider-using-max-builtin
#pylint: disable=too-many-instance-attributes
#pylint: disable=too-many-instance-attributes
#pylint: disable=too-many-instance-attributes
#pylint: disable=too-many-positional-arguments
#pylint: disable=inconsistent-return-statements
#pylint: disable=possibly-used-before-assignment


#-----------------------------------------------------------------------------------------------------------------------------------------------------
#12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
#        1         2         3         4         5         6         7         8         9         A         B         C         D         E         F
#-----------------------------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Required Modules                                                                                                                                   -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
import os
import sys
import enum
import platform
import csv          # PyLO class
import json         # PyLO class
import readline     # to use input and not cause problem with pylint

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Layout is used for the Range, Set, Frozenset.                                                                                                      -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#class Move(str, enum.Enum): # python3.9.18
class Move(enum.StrEnum):    # python3.12.1
# class Move():
    '''
    Move reference class
    '''
    UP    = "up"
    RIGHT = "right"
    DOWN  = "down"
    LEFT  = "left"


class Align(enum.StrEnum):
# class Align():
    '''
    Align reference class
    '''
    LEFT     = "left"
    CENTER   = "center"
    RIGHT    = "right"
    JUSTIFY  = "justify"


class Layout(enum.StrEnum):
# class Layout():
    '''
    Layout reference class
    '''
    HORIZONTAL = "horizontal"
    VERTICAL =   "vertical"


class Length_bg(enum.Enum):
# class Length_bg():
    '''
    Length reference class
    '''
    ALL_ROW   = 1
    ONLY_WORD = 2


class Line_Style(enum.StrEnum):
# class Line_Style():
    '''
    Line_Style reference class
    '''
    CUSTOMIZED   = "customized"
    SINGLE       = "single"
    SINGLE_BOLD  = "single_bold"
    SINGLE_HEAVY = "single_heavy"
    DOUBLE       = "double"
    DASH         = "dash"
    SQ_BRACKETS  = "sq_brackets"
    NONE         = "none"
    SPACE_COL_COLOR    = "space_col_color"
    NO_SPACE_COL_COLOR = "no_space_col_color"

#-----------------------------------------------------------------------------------------------------------------------------------------------------
class Unicode(enum.StrEnum):
# class Unicode():
    '''
    Unicode reference class
    '''
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Box Drawings                                                                                                                                   -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    BOX_DRAWINGS_LIGHT_HORIZONTAL          = "\N{BOX DRAWINGS LIGHT HORIZONTAL}"
    BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT  = "\N{BOX DRAWINGS LIGHT VERTICAL AND RIGHT}"
    BOX_DRAWINGS_LIGHT_VERTICAL_AND_LEFT   = "\N{BOX DRAWINGS LIGHT VERTICAL AND LEFT}"

    BOX_DRAWINGS_LIGHT_VERTICAL            = "\N{BOX DRAWINGS LIGHT VERTICAL}"
    BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL = "\N{BOX DRAWINGS LIGHT DOWN AND HORIZONTAL}"
    BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL   = "\N{BOX DRAWINGS LIGHT UP AND HORIZONTAL}"

    BOX_DRAWINGS_LIGHT_VERTICAL_AND_HORIZONTAL ="\N{BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL}"

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Triangle                                                                                                                                       -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    BLACK_UP_POINTING_TRIANGLE   = "\N{BLACK UP-POINTING TRIANGLE}"     # \u25B2  up fill arrow
    WHITE_UP_POINTING_TRIANGLE   = "\N{WHITE UP-POINTING TRIANGLE}"     # \u25B3  up empty arrow

    BLAKC_RIGHT_POINT_TRIANGLE   = "\N{BLACK RIGHT-POINTING TRIANGLE}"  # \u25B6  right fill  arrow
    WHITE_RIGHT_POINT_TRIANGLE   = "\N{WHITE RIGHT-POINTING TRIANGLE}"  # \u25B7  right empty arrow

    BLACK_DOWN_POINTING_TRIANGLE = "\N{BLACK DOWN-POINTING TRIANGLE}" # \u25BC  down fill  arrow
    WHITE_DOWN_POINTING_TRIANGLE = "\N{BLACK DOWN-POINTING TRIANGLE}" # \u25BD  down empty arrow

    BLACK_LEFT_POINTING_TRIANGLE = "\N{BLACK LEFT-POINTING TRIANGLE}" # \u25C0  left fill arrow
    WHITE_LEFT_POINTING_TRIANGLE = "\N{WHITE LEFT-POINTING TRIANGLE}" # \u25C1  left empty arrow

    EM_DASH = "\N{EM DASH}"
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Miscellaneous                                                                                                                                  -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    BLACK_DIAMOND = "\N{BLACK DIAMOND}"
    WHITE_DIAMOND = "\N{WHITE DIAMOND}"

    BLACK_CIRCLE  = "\N{BLACK CIRCLE}"
    WHITE_CIRCLE  = "\N{WHITE CIRCLE}"

    FACE = "(" + chr(0x25D5) + chr(0x25E1) + chr(0x25D5) + ")"



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Screen Functions Windows and Linux                                                                                                                 -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Clean the Terminal (Windows)                                                                                                                       -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def clean():

    ''' It cleans the terminal and returns the cursor to home. '''

    print("\033[2J",end="")  # clean the terminal
    print("\033[H",end="")   # return home the cursor


if os.name == 'nt' and (platform.release() == '10' or platform.release() == "11"):
    OS_Windows = True
    OS_Linux = False
    # Fix ANSI color in Windows 10 version 10.0.14393 (Windows Anniversary Update)
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Clear the Terminal (Windows)                                                                                                                   -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def clear():

        '''  It cleans the terminal and returns the cursor to home.  '''

        os.system("cls")

    # it may disable the scroll bar on the Command Prompt or the Windows PowerShell
    # to enable the scroll bar, got to Properties-> Layout-> Screen Buffer Size-> Set Height to 1000
    # use Command Prompt or Windows PowerShell
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Resize the Terminal (Windows)                                                                                                                  -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def resize(rows:int=25, cols:int=80)->None:

        '''  It resizes the terminal size.  '''

        #os.system(f"mode con:cols={cols} lines={rows}")
        os.system(f"mode {cols}, {rows}")


elif os.name == 'posix':
    OS_Windows = False
    OS_Linux = True
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Clear the Terminal (Linux)                                                                                                                     -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def clear():

        '''  It cleans the terminal and returns the cursor to home.  '''

        os.system("clear")

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Resize the Terminal (Linux)                                                                                                                    -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def resize(rows:int=25, cols:int=80)->None:

        '''  It resizes the terminal size.  '''

        os.system(f"resize -s {rows} {cols}")


else:
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Clean the Terminal (Other)                                                                                                                         -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
    def clear():

        '''  It cleans the terminal and returns the cursor to home.  '''

        print("\033[2J",end="")  # clean the terminal
        print("\033[H",end="")   # return home the cursor

    def resize(rows:int=25, cols:int=80)->None:

        '''  It resizes the terminal size.  '''

        os.system(f"resize -s {rows} {cols}")



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Returns the Terminal) Dimensions                                                                                                                   -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def dimensions():

    '''  It returns the dimensions of the terminal: cols, rows = dimensions()  '''

    cols, rows = os.get_terminal_size()
    return cols, rows



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Erase the Terminal                                                                                                                                 -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def erase():

    '''  It erases the terminal and leaves the cursor in the current position  '''

    print("\033[2J",end="")



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Linux Background Color Option List                                                                                                                 -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def bg_ansi_colors(bold=False, fg=-1, n_line=0):

    '''  This function displays all background colors available with ansi code  '''

    reset = "\033[0m"
    space = "   "
    ctrl  = 0
    msg   = " bg color number "

    if fg < 0 or fg > 256: fg_color = "-1"
    else:                  fg_color = str(fg)

    if bold == True: b = "1"
    else:            b = "0"

    for color in range(257):
        if color <= 9:                    space = "   "
        elif color <= 99 and color >=10:  space = "  "
        else:                             space = " "

        if ctrl <= 1:
            ctrl += 1
            if fg_color == "-1":
                print(f"\033[{b};48;5;{color}m {msg} {reset}{color}",end=space)
            else:
                print(f"\033[{b};48;5;{color};38;5;{fg_color}m {msg} {reset}{color}",end=space)
        else:
            ctrl = 0
            if fg_color == "-1":
                if n_line > 0:
                    print(f"\033[{b};48;5;{color}m {msg} {reset}{color}")
                    ins_newline(n_line)
                else:
                    print(f"\033[{b};48;5;{color}m {msg} {reset}{color}")

            else:
                if n_line > 0:
                    print(f"\033[{b};48;5;{color};38;5;{fg_color}m {msg} {reset}{color}")
                    ins_newline(n_line)
                else:
                    print(f"\033[{b};48;5;{color};38;5;{fg_color}m {msg} {reset}{color}")

    print("\x1B[0m  bg default color  -1")



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Linux Foreground Color Option List                                                                                                                 -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def fg_ansi_colors(bold=False, bg=-1, n_line=0):

    '''  This function displays all foreground colors available with ansi code  '''

    reset = "\033[0m"
    space = "   "
    ctrl  = 0
    msg   = " fg color number "

    if bg < 0 or bg > 256: bg_color = "-1"
    else:                  bg_color = str(bg)

    if bold == True: b = "1"
    else:            b = "0"

    for color in range(257):
        if color <= 9:
            space = "   "
        elif color <= 99 and color >=10:
            space = "  "
        else:
            space = " "

        if ctrl <= 1:
            ctrl += 1
            if bg_color == "-1":
                print(f"\033[{b};38;5;{color}m {msg} {reset}{color}",end=space)
            else:
                print(f"\033[{b};48;5;{bg_color};38;5;{color}m {msg} {reset}{color}",end=space)
        else:
            ctrl = 0
            if bg_color == "-1":
                if n_line > 0:
                    print(f"\033[{b};38;5;{color}m {msg} {reset}{color}")
                    ins_newline(n_line)
                else:
                    print(f"\033[{b};38;5;{color}m {msg} {reset}{color}")
            else:
                if n_line > 0:
                    print(f"\033[{b};48;5;{bg_color};38;5;{color}m {msg} {reset}{color}")
                    ins_newline(n_line)
                else:
                    print(f"\033[{b};48;5;{bg_color};38;5;{color}m {msg} {reset}{color}")

    print("\x1B[0m  fg default color  -1")



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Terminal Sounds                                                                                                                                    -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def terminal_bell():

    '''  This function makes sound of the terminal bell
         terminal_bell()
           '''

    print("\a")



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Insert A Unicode Character n Times                                                                                                                 -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def ins_chr(n=1, unicode=" "):

    '''  This function inserts n times the unicode provided
         ins_chr(n=x, unicode=" ")  '''

    sp = str(unicode)

    space = ""
    while n > 0:
        space += sp
        n -= 1
    return space



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Insert n Newlines                                                                                                                                  -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def ins_newline(n=1):

    '''  This function inserts n new lines
         ins_newline(n=1)  '''

    while n > 0:
        n -= 1
        print("")



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Move Cursor to the Right. This function is used as the indentation for the print                                                                   -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _move_right(n=0,option_space=False):

    '''  This function moves the cursor n spaces to the right.  '''

    if option_space == True:
        sp = ins_chr(n)
    else:
        if n == 0:
            sp = ""
        else:
            sp = f"\033[{str(n)}C"
    return sp



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Set Settings for the Font: Bold, Background, and Foreground                                                                                        -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def set_font(bold=False,bg=-1,fg=-1,italic=False,underline=False,strike=False,blinking=False,dim=False,hidden=False,inverse=False):

    '''  This function changes the attributes of the font (bold, bg, fg).

          set_font(bold=bool, bg=int, fg=int)

          Colors range from -1 to 256.
          To set the default color use -1 or 256.  '''

    # bg_color and fg_color, are int values but we convert then to str values
    reset = "\033[0m"

    if bg < 0 or bg > 255:  bgc = "reset"
    else:                   bgc = str(bg)

    if fg < 0 or fg > 255:  fgc = "reset"
    else:                   fgc = str(fg)


    if   bgc == "reset" and fgc == "reset":  settings = reset
    elif bgc == "reset" and fgc != "reset":  settings = reset+"\033[38;5;"+fgc+"m"
    elif bgc != "reset" and fgc == "reset":  settings = reset+"\033[48;5;"+bgc+"m"
    elif bgc != "reset" and fgc != "reset":  settings = reset+"\033[48;5;"+bgc+";38;5;"+fgc+"m"
    else:                                    settings = reset


    if   bold == True  and dim == False:  settings = settings + "\033[1m"
    elif bold == True  and dim == True:   settings = settings + "\033[1m"
    elif bold == False and dim == True:   settings = settings + "\033[2m"
    else:                                   pass  # (bold == False and dim == False):

    if italic == True:    settings = settings + "\033[3m"
    else:                 settings = settings + "\033[23m"

    if underline == True: settings = settings + "\033[4m"
    else:                 settings = settings + "\033[24m"

    if blinking == True:  settings = settings + "\033[5m"
    else:                 settings = settings + "\033[25m"

    if hidden == True:    settings = settings + "\033[8m"
    else:                 settings = settings + "\033[28m"

    if strike == True:    settings = settings + "\033[9m"
    else:                 settings = settings + "\033[29m"

    if inverse == True:   settings = settings + "\033[7m"
    else:                 settings = settings + "\033[27m"

    return settings



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Reset Settings for the Font: Bold, Background, and Foreground                                                                                      -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def reset_font():

    '''  This function resets the font attributes to the default ones.  '''

    return "\033[0m"



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Bool to List Type                                                                                                                     -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def bool2list(my_bool):

    '''  It Converts a Bool to a String List  '''

    tempo_list = []
    tempo_list.append(my_bool)
    return tempo_list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Integer to List Type                                                                                                                  -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def int2list(my_int):

    '''  It Converts a Integer Number to a String List n  '''

    tempo_list = []
    tempo_list.append(my_int)
    return tempo_list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Float to List Type                                                                                                                    -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def float2list(my_float):

    '''  It Converts a Float Number to a String List  '''

    tempo_list = []
    tempo_list.append(my_float)
    return tempo_list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Complex to List Type                                                                                                                  -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def complex2list(my_complex):

    '''  It Converts a Complex Number to a String List  '''

    tempo_list = []
    tempo_list.append(my_complex)
    return tempo_list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Convert From String to List Type                                                                                                                   -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def str2list(my_str):

    '''  It Converts a String to a String List  '''

    tempo_list = []
    tempo_list.append(my_str)
    return tempo_list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Dict to List Type                                                                                                                     -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def dict2list(my_dict, key_title="key", value_title="value"):

    '''  It Converts a Dictionay to a String List  '''

    my_key_list = []; my_data_list = []

    my_key_list  = list(my_dict.keys())
    my_data_list = list(my_dict.values())

    complete_list = [];  tempo_list = []
    if (key_title == "key") and (value_title == "value"):
        if (len(my_key_list)) > 1:   complete_list.append(["Keys","Values"])
        else:                        complete_list.append(["Key","Value"])

    elif (key_title == "none" and value_title == "none"):
        pass

    else:
        complete_list.append([key_title,value_title])

    for d in range(len(my_dict)):
        tempo_list.append(my_key_list[d])
        tempo_list.append(my_data_list[d])
        complete_list.append(tempo_list)
        tempo_list = []

    return complete_list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Set or Frozenset to List Type                                                                                                         -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def set2list(my_set:set, set_header = "none", layout:Layout=Layout.HORIZONTAL):

    '''  It Converts a Set or a Frozenset to a String List  '''

    # set and frozenset values are printed in aleatory order all the time
    tempo_list = []; cnt = 0; l = len(my_set)

    if layout.lower() == "v" or layout.lower() == Layout.VERTICAL:
        if "set" in set_header or "frozenset" in set_header:
            if len(my_set) > 1:
                tempo_list.append([set_header+" Values"])
            else:
                tempo_list.append([set_header+" Value"])

        elif set_header == "none":
            pass

        else:
            tempo_list.append([set_header])

        while l > 0:
            dato = list(my_set)[cnt]
            tempo_list.append([dato])
            cnt += 1
            l   -= 1

    if layout.lower() == "h" or layout.lower() == Layout.HORIZONTAL:
        if "set" in set_header or "frozenset" in set_header:
            if len(my_set) > 1:
                tempo_list.append("Set Values")
            else:
                tempo_list.append("Set Value")

        elif set_header == "none":
            pass

        else:
            tempo_list.append(set_header)

        while l > 0:
            dato = list(my_set)[cnt]
            tempo_list.append(dato)
            cnt += 1
            l   -= 1

    return tempo_list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Range to List Type                                                                                                                    -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def range2list(my_range:range, range_header = "none", layout:Layout=Layout.HORIZONTAL):

    '''  It Converts a Range to a String List  '''

    tempo_list = []

    if layout.lower() == "v" or layout.lower() == Layout.VERTICAL:
        if range_header   == "range": tempo_list = [["Range"]]
        elif range_header == "none":  pass
        else:                         tempo_list = [[range_header]]

        for n in my_range:
            tempo_list.append([n])

    if layout.lower() == "h" or layout.lower() == Layout.HORIZONTAL:
        if range_header   == "range": tempo_list = ["Range"]
        elif range_header == "none":  pass
        else:                         tempo_list = [range_header]

        for n in my_range:
            tempo_list.append(n)

    return tempo_list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Convert From Tuple to List Type                                                                                                                    -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def tuple2list(my_tuple):

    '''  It Converts a Tuple to a String List  '''

    tempo_list = []
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    if len(my_tuple) == 0:
        pass #return tempo_list

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    elif len(my_tuple) == 1:
                                                # string              ("")         -> Case 0   String
                                                # "empty_tuple"       ("",)        -> Case 1   Empty
        tempo_list.append(my_tuple[0])          # "one_item_no_row"   ("Apple",)   -> Case 2   Tuple
        #return tempo_list                       # "one_item_one_row"  (("Apple",)) -> Case 3   Tuple inside Tuple

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    #elif len(my_tuple) > 1:
    else:
        type_type = []; lengths = []
        l = len(my_tuple); tuple_tuple = 0; tuple_other = 0

        for n in range(len(my_tuple)):
            if isinstance(my_tuple[n], tuple):
                tuple_tuple = 1
                type_type.append("tuple")
                lengths.append(len(my_tuple[n]))

            else:
                tuple_other = 1
                type_type.append("other")
                lengths.append(1)

        # This is only for tuples inside the tuple ->
        # tupleData = (("hello","hello"),("hell",),("hi","bye","good"),([1,2],))        -> Case 4
        if (tuple_tuple == 1 and tuple_other == 0):
            tempo = []
            for col in my_tuple:
                for i in col:
                    tempo.append(i)
                tempo_list.append(tempo)
                tempo = []

        # This is only for other types inside a tuple
        # tupleData = ("hello","hell","hi",[1,2])                                       -> Case 5
        elif (tuple_tuple == 0 and tuple_other == 1):
            for n in my_tuple:
                tempo_list.append(n)     # for rows (Horizontal)
                #tempo_list.append([n])  # for cols (Vertical)

        # This is for combination tuple (tuple =1 and other = 1)                        -> Case 6
        # tupleData = (("hello","hello"),("hell",),("hi","bye","good"),[1,2], "hello")
        elif (tuple_tuple == 1 and tuple_other == 1):
            for n in range(l):
                if (lengths[n]) > 1:
                    tempo = []
                    for i in range(lengths[n]):
                        tempo.append(my_tuple[n][i])
                    tempo_list.append(tempo)

                else:
                    if type_type[n] == "other":
                        tempo_list.append([my_tuple[n]])
                    else:
                        tempo_list.append([my_tuple[n][0]])
        else:
            tempo_list = []

    return tempo_list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Get Data Type and Convert It to a List Type                                                                                                        -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def data2list(self,dato):

    '''  It Converts Any Type of Variable to a a String List Type  '''

    data_list = []
    # it is already a list type
    if isinstance(dato, list):
        return dato

    # bool type to list type
    elif isinstance(dato, bool):
        data_list = bool2list(dato)

    # int to list type
    elif isinstance(dato, int):
        data_list = int2list(dato)

    # float to list type
    elif isinstance(dato, float):
        data_list = float2list(dato)

    # string type
    elif isinstance(dato, str):
        data_list = str2list(dato)

    # complex type
    elif isinstance(dato, complex):
        if dato.imag < 0:
            data_list.append(str(dato.real)+"-"+str((dato.imag)*-1)+"j")
        else:
            data_list.append(str(dato.real)+"+"+str(dato.imag)+"j")

    # range type
    elif isinstance(dato, range):
        data_list = range2list(dato,"none",self.set_layout)

    # dictionary type
    elif isinstance(dato, dict):
        data_list = dict2list(dato)

    # set type
    elif isinstance(dato, set):
        data_list = set2list(dato,"none",self.set_layout)

    # frozenset type
    elif isinstance(dato, frozenset):
        data_list = set2list(dato,"none",self.set_layout)

    # tuple
    elif isinstance(dato, tuple):
        data_list = tuple2list(dato)

    else:
        data_list = "none"

    # none: bytes, bytearray, memoryview(bytes(5))

    return data_list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Get List Type                                                                                                                                      -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _get_list_type(my_list):
    if not isinstance(my_list, list):
        return "incorrect_variable_type"                # [Not a List] Case 0
    #-------------------------------------------------------------------------------------------------------------------------------------------------

    if len(my_list) == 0:
        return "empty_list"                             # []    Case 1

    #-------------------------------------------------------------------------------------------------------------------------------------------------

    if len(my_list) == 1:
        if isinstance(my_list[0], list):
            if len(my_list[0]) > 1:
                return "multiple_items_one_row"           # [[1,2,3]]   Case 5
            else:
                return "one_item_one_row"                 # [[1]]  Case 4
        else:
            return "one_item_no_row"                      # [1]   Case 2

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    if len(my_list) > 1:
        items = 0; rows = 0
        for n in my_list:
            if not isinstance(n, list):
                items = 1
            else:
                rows = 1

        if (items ==  1 and rows == 0):
            return "multiple_items_no_row"              #  [1,2,3]                      Case 3
        elif (items == 0 and rows == 1):
            return  "multiple_items_multiple_rows"      # [[1],[4],[7]]                 Case 6
                                                        # [[1,2,3],[4,5,6],[7,8,9]]     Case 6
                                                        # [[1],[1,2,3],[5,4,7,8]]       Case 6
                                                        # any combination of this is    Case 6
                                                        # [[1,2,3],[[2],3,4],[5,[6,7]]] Case 6
        else:
            return "mix_items"                          # [5,6,[1,2,3],[1,0,3]]         Case 7
                                                        # [[1,2],[1,2,[1]],[1,2,3]]     Case 7
                                                        # any combination of this is    Case 7



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Get Total Length of the Columns                                                                                                                    -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _get_total_length(self,my_list):
    my_length = 0
    list_dimensions = _get_list_type(my_list)
    if list_dimensions == "one_item_no_row":     # ["item"]
        # the *2 is because there are 2 adj_space one each size (left and right)
        # the +2 is because there are 2 vertical lines (left and right)
        my_length = len(my_list[0]) + (self.adj_space*2) + self.adj_indent + 2

    elif list_dimensions == "one_item_one_row":  # [[item]]
        # the *2 is because there are 2 adj_space one each size (left and right)
        # the adj_indent is because we have an indentation space at the begining
        # the +2 is because there are 2 vertical lines (left and right)
        my_length = len(my_list[0][0]) + (self.adj_space*2) + self.adj_indent + 2

    elif (list_dimensions == "multiple_items_one_row" or list_dimensions == "multiple_items_no_row"):
        # [1,2,3,4,5]  or [[1,2,3,4,5]]
        for item in my_list:
            my_length += len(item) + (self.adj_space*2) + 1  # this one is for the left vertical chr
        my_length += 1                                       # this one is for the right vertical chr, last one
        my_length += self.adj_indent                         # this is for the indentation space

    else:    # multiples rows
        one_item_per_row = True

        for row in my_list:             # checking if we a list like [[1],[2],[3]], only one column
            if  len(row) != 1:
                one_item_per_row = False
                break

        if one_item_per_row == True:    # finding the greatest column size in characters
            for row in my_list:
                for col in row:
                    if my_length < len(col):
                        my_length = len(col)

            # the adj_indent is because we have an indentation space at the begining
            # the *2 is because there are 2 adj_space one each size (left and right), self.adj_space
            # the +2 is because there are 2 vertical lines (left and right)
            my_length += self.adj_indent + (self.adj_space*2) + 2

        else:
            # we have a matrix list something like this [[10,20,30],[40,50,60],[70,80,90]]. awsome.
            max_rows, max_cols = _get_number_rows_cols_list(my_list)
            tempo_cols = []
            n_cols = []

            # we create the transpose of the list but we save their lens in the transpose rather than the data
            for c in range(max_cols):
                for r in range(max_rows):
                    tempo_cols.append(len(my_list[r][c]))
                n_cols.append(tempo_cols)
                tempo_cols = []

            longest_cols = []
            for col in n_cols:
                longest_cols.append(max(col)) # longest_cols keeps the size list of the longest columns in chr
                # making the complete sum of the all the length
                # the adj_indent is because we have an indentation space at the begining
                # sum(longest_cols) is suming all the longest cols in the list
                # the self.adj_space is multiply by 2 because we have to side, left and right, on each column then
                # we multiply by the number of columns in the list
                # the +1  is because there are 1 vertical lines no consiered in the list
                # of longest_cols (left, middles, and right)

            my_length = self.adj_indent + sum(longest_cols) + ((self.adj_space*2)*len(longest_cols)) + len(longest_cols) + 1

    return my_length



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Print Title On Terminal with Its Attributes: Bold, Bg and Fg Color (title)                                                                         -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _print_title(self,my_list):

    if self.msg_title == "":  return

    else:
        settings = set_font(self.bold_title,self.bg_title, self.fg_title,self.italic_title,self.underline_title,
                            self.strike_title,self.blinking_title,self.dim_title,self.hidden_title,self.inverse_title)

    total_length = _get_total_length(self,my_list)  # check for the length of the message

    if (self.align_title.lower() == "left") or (self.align_title.lower() == "l"):
        print(_move_right(self.adj_indent)+settings+self.msg_title+reset_font())

    elif (self.align_title.lower() == "center") or (self.align_title.lower() == "c"):
        difference = (int((total_length)/2)) - (int(((len(self.msg_title) + self.adj_indent))/2))
        if difference <= 0:
            print(_move_right(self.adj_indent)+settings+self.msg_title+reset_font()) # left align
        else:
            print(_move_right(self.adj_indent+difference)+settings+self.msg_title+reset_font())

    elif (self.align_title.lower() == "right") or (self.align_title.lower() == "r"):
        # the 1 is for the vertical line
        difference = total_length - (len(self.msg_title) + (self.adj_space) + self.adj_indent + 1)
        if difference <= 0:
            print(_move_right(self.adj_indent)+settings+self.msg_title+reset_font()) # left align
        else:
            print(_move_right(self.adj_indent+self.adj_space+1+difference)+settings+self.msg_title+reset_font())

    elif (self.align_title.lower() == "justify") or (self.align_title.lower() == "j"):
        difference = total_length - (len(self.msg_title) + (self.adj_space) + self.adj_indent + 1)
        if difference <= 0:
            print(_move_right(self.adj_indent)+settings+self.msg_title+reset_font()) # left align
        else:
            print(_move_right(self.adj_indent+self.adj_space+1)+settings+self.msg_title+reset_font())

    else:
        print(_move_right(self.adj_indent)+settings+self.msg_title+reset_font())   # left align

    ins_newline(self.adj_top_space)    # space between the the title and the top list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Print Footnote On Terminal with Its Attributes: Bold, Bg and Fg Color (footnote)                                                                   -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _print_notefoot(self,my_list):

    if self.msg_footnote == "": return

    else:
        settings = set_font(self.bold_footnote,self.bg_footnote, self.fg_footnote,self.italic_footnote,self.underline_footnote,\
                            self.strike_footnote,self.blinking_footnote,self.dim_footnote,self.hidden_footnote,self.inverse_footnote)

    total_length = _get_total_length(self,my_list)  # check for the length of the message

    ins_newline(self.adj_bottom_space)

    if (self.align_footnote.lower() == "left") or (self.align_footnote.lower() == "l"):
        print(_move_right(self.adj_indent)+settings+self.msg_footnote+reset_font())

    elif (self.align_footnote.lower() == "center") or (self.align_footnote.lower() == "c"):
        difference = (int((total_length)/2)) - (int(((len(self.msg_footnote) + self.adj_indent))/2))
        if difference <= 0:
            print(_move_right(self.adj_indent)+settings+self.msg_footnote+reset_font()) # left align
        else:
            print(_move_right(self.adj_indent+difference)+settings+self.msg_footnote+reset_font())

    elif (self.align_footnote.lower() == "right") or (self.align_footnote.lower() == "r"):
        difference = total_length - (len(self.msg_footnote) + (self.adj_space) + self.adj_indent + 1) # 1 is for the vertical line
        if difference <= 0:
            print(_move_right(self.adj_indent)+settings+self.msg_footnote+reset_font()) # left align
        else:
            print(_move_right(self.adj_indent+self.adj_space+1+difference)+settings+self.msg_footnote+reset_font())

    elif (self.align_footnote.lower() == "justify") or (self.align_footnote.lower() == "j"):
        difference = total_length - (len(self.msg_footnote) + (self.adj_space) + self.adj_indent + 1)
        if difference <= 0:
            print(_move_right(self.adj_indent)+settings+self.msg_footnote+reset_font()) # left align
        else:
            print(_move_right(self.adj_indent+self.adj_space+1)+settings+self.msg_footnote+reset_font())

    else:
        print(_move_right(self.adj_indent)+settings+self.msg_footnote+reset_font())   # left align



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Print Horizontal Line                                                                                                                              -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _print_horizontal_segment(self,start_chr,end_chr,times,indent,option):

    set_v   = set_font(self.bold_vertical_line, self.bg_vertical_line, self.fg_vertical_line)
    set_h   = set_font(self.bold_horizontal_line, self.bg_horizontal_line, self.fg_horizontal_line)
    set_c   = set_font(self.bold_corner_chr, self.bg_corner_chr, self.fg_corner_chr)
    set_hd  = set_font(self.bold_under_line_header, self.bg_under_line_header,self.fg_under_line_header)
    set_hdc = set_font(self.bold_corner_under_line_header, self.bg_corner_under_line_header,self.fg_corner_under_line_header)
    set_ic  = set_font(self.bold_inner_corner_chr, self.bg_inner_corner_chr,self.fg_inner_corner_chr)

    # indentation adds the space is set up for the indentation
    # we want the indentation space at the begining but not at the end of the line.

    if indent == 1:
        print(_move_right(self.adj_indent),end="")

    if option == "horizontal":
        print(set_v+start_chr+set_h,end="")

    elif option == "corner":
        print(set_c+start_chr+set_h,end="")

    elif option == "horizontal_header":
        print(set_hdc+start_chr+set_hd,end="")

    elif option == "inner_corner":
        print(set_ic+start_chr+set_h,end="")

    else:
        print(set_v+start_chr+set_h,end="")

    for n in range(times):
        print(end_chr,end="")

    print(reset_font(),end="")



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Print Single Element                                                                                                                               -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _print_single_element(self,my_list):

    if isinstance(my_list[0],list): item = my_list[0][0]
    else:                           item = my_list[0]

    ins_newline(self.adj_top_margin)
    # print title
    _print_title(self,my_list)

    # get all the settings for the list
    set_d = set_font(self.bold_data, self.bg_data, self.fg_data, self.italic_data, self.underline_data, self.strike_data,\
                     self.blinking_data, self.dim_data, self.hidden_data, self.inverse_data)
    set_v = set_font(self.bold_vertical_line, self.bg_vertical_line, self.fg_vertical_line)

    # print the top horizontal line
    if  self.top_horizontal_line_on == True:
        indent = 1  # to add the space at the beginning ()
        _print_horizontal_segment(self, self.top_left_corner_chr, self.top_horizontal_line_chr, ((len(item))+(2*self.adj_space)), indent, "corner")

        indent = 0  # to don't add this space at the end or the middle
        _print_horizontal_segment(self, self.top_right_corner_chr, self.top_horizontal_line_chr, 0, indent, "corner")
        print()
    else:
        pass

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # print data with adjustments. We are missing vertical line color and horizontal line color and data color
    if (self.align_data.lower() == "left") or (self.align_data.lower() == "l"):
        print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d + item + _move_right((self.adj_space*2),\
                          self.bg_all_cell_data) + set_v + self.right_vertical_line_chr + reset_font())

    elif (self.align_data.lower() == "right") or (self.align_data.lower() == "r"):
        print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d + _move_right((self.adj_space*2),\
                          self.bg_all_cell_data) + item + set_v + self.right_vertical_line_chr + reset_font())

    elif (self.align_data.lower() == "center") or (self.align_data.lower() == "c"):
        print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d + _move_right(self.adj_space, self.bg_all_cell_data) +\
                          item + _move_right(self.adj_space, self.bg_all_cell_data) + set_v + self.right_vertical_line_chr + reset_font())

    elif (self.align_data.lower() == "justify") or (self.align_data.lower() == "j"):
        print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d + _move_right(self.adj_space, self.bg_all_cell_data) +\
                          item + _move_right(self.adj_space, self.bg_all_cell_data) + set_v + self.right_vertical_line_chr + reset_font())

    else:
        print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d + _move_right(self.adj_space, self.bg_all_cell_data)+\
                          item + _move_right(self.adj_space, self.bg_all_cell_data) + set_v + self.right_vertical_line_chr + reset_font())

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # print the bottom horizontal line
    if  self.bottom_horizontal_line_on == 1:
        indent = 1  # to add the space at the beginning (vertical line chr)
        _print_horizontal_segment(self, self.bottom_left_corner_chr, self.bottom_horizontal_line_chr, ((len(item))+(2*self.adj_space)), indent, "corner")
        indent = 0  # to don't add this space at the end or the middle
        _print_horizontal_segment(self, self.bottom_right_corner_chr, self.bottom_horizontal_line_chr, 0, indent, "corner")
        print()

    else:  pass

    _print_notefoot(self,my_list)
    ins_newline(self.adj_bottom_margin)



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Print Multiple Horizontal Items (One Row OR No Row)                                                                                                -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _print_multiple_horizontal_items(self,my_list):
    ins_newline(self.adj_top_margin)
    # print title
    _print_title(self,my_list)

    # get all the settings for the list
    set_d = set_font(self.bold_data, self.bg_data, self.fg_data, self.italic_data, self.underline_data, self.strike_data,\
                     self.blinking_data, self.dim_data, self.hidden_data, self.inverse_data)

    set_v = set_font(self.bold_vertical_line, self.bg_vertical_line, self.fg_vertical_line)

    # drawing the top horizontal line
    if  self.top_horizontal_line_on == True:
        indent = 1  # to add the space at the beginning (indentation space)
        for item in my_list:
            if indent == 1:          # first segment
                _print_horizontal_segment(self, self.top_left_corner_chr, self.top_horizontal_line_chr, (len(item) +\
                                         (2*self.adj_space)), indent, "corner")
                indent = 0
            else:
                _print_horizontal_segment(self, self.middle_top_corner_chr, self.top_horizontal_line_chr,(len(item) +\
                                         (2*self.adj_space)), indent, "inner_corner")

                # corner or horizontal depends on what color to get if the corner colors or the horizontal_line
                # last segment, which is only the corner that's why it's 0 on value

        _print_horizontal_segment(self, self.top_right_corner_chr, self.top_horizontal_line_chr, 0, indent, "corner")
        print()  # done top line, jump to next line to print data

    else:  pass

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # print the data with their alignments
    indent = 1
    for item in my_list:
        if (self.align_data.lower() == "left") or (self.align_data.lower() == "l"):
            if indent == 1:
                print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d + item +\
                     _move_right((self.adj_space*2),self.bg_all_cell_data),end="")
                indent = 0
            else:
                print(set_v + self.middle_vertical_line_chr + set_d + item + _move_right((self.adj_space*2),self.bg_all_cell_data),end="")

        #---------------------------------------------------------------------------------------------------------------------------------------------
        elif (self.align_data.lower() == "right") or (self.align_data.lower() == "r"):
            if indent == 1:
                print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d+\
                     _move_right((self.adj_space*2),self.bg_all_cell_data) + item,end="")
                indent = 0
            else:
                print(set_v + self.middle_vertical_line_chr + set_d + _move_right((self.adj_space*2),self.bg_all_cell_data) + item,end="")

        #---------------------------------------------------------------------------------------------------------------------------------------------
        elif (self.align_data.lower() == "justify") or (self.align_data.lower() == "j")\
              or (self.align_data.lower() == "center") or (self.align_data.lower() == "c"):
            if indent == 1:
                print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d +\
                      _move_right(self.adj_space,self.bg_all_cell_data) + item + _move_right(self.adj_space,self.bg_all_cell_data),end="")
                indent = 0
            else:
                print(set_v + self.middle_vertical_line_chr + set_d+_move_right(self.adj_space,self.bg_all_cell_data) + item +\
                     _move_right(self.adj_space,self.bg_all_cell_data),end="")

        #---------------------------------------------------------------------------------------------------------------------------------------------
        else: # justify default one
            print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d + _move_right(self.adj_space,self.bg_all_cell_data) +\
                  item + _move_right(self.adj_space,self.bg_all_cell_data),end="")

    print(set_v + self.right_vertical_line_chr + reset_font())

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # print the bottom horizontal line
    if  self.bottom_horizontal_line_on == 1:
        indent = 1
        for item in my_list:
            if indent == 1:
                _print_horizontal_segment(self, self.bottom_left_corner_chr, self.bottom_horizontal_line_chr, (len(item) + (2*self.adj_space)),\
                                  indent, "corner") # first segment
                indent = 0

            else:  # middle segments. "corner"
                _print_horizontal_segment(self, self.middle_bottom_corner_chr, self.bottom_horizontal_line_chr, (len(item) + (2*self.adj_space)),\
                                    indent, "inner_corner")

                # corner or horizontal depends on what color to get if the corner colors or the horizontal_line
                # last segment, which is only the corner that's why it's 0 on value

        _print_horizontal_segment(self, self.bottom_right_corner_chr, self.bottom_horizontal_line_chr, 0, indent, "corner")
        print()

    _print_notefoot(self,my_list)
    ins_newline(self.adj_bottom_margin)



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Get Number of Rows and Cols of the List                                                                                                            -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _get_number_rows_cols_list(my_list):
    n_rows = len(my_list)
    n_cols = 0

    for n in my_list:
        if len(n) > n_cols:
            n_cols = len(n)

    return n_rows, n_cols



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Complete Information in the List, if need it                                                                                                       -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _complete_info_list(self,my_list):
    n_rows, n_cols = _get_number_rows_cols_list(my_list)
    row_tempo_list = []; matrix_update = []

    for row in range(n_rows):
        row_tempo_list = my_list[row]
        diff = n_cols - len(my_list[row])
        for col in range(diff):
            row_tempo_list.append(str(self.set_fill_chr))
        matrix_update.append(row_tempo_list)

    return matrix_update



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Get the Odd or Even Space Adjustment for the Word                                                                                                  -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _get_odd_even_space_adj(length,len_dato):
    sp_start = 0; sp_end=0
    odd_l = length%2
    odd_len_dato = len_dato%2

    if odd_l == 1:
        sp_start = (int(length/2))-(int(len_dato/2))       # if length word is odd
        if odd_len_dato == 1:  sp_end = sp_start           # if len_dato is odd
        else:                  sp_end = sp_start + 1       # if len_dato is even

    else:
        sp_start = (int(length/2))-(int(len_dato/2))       # if the length word is even
        if odd_len_dato == 1:  sp_end = sp_start - 1       # if len_dato is odd
        else:                  sp_end = sp_start           # if len_dato is even

    return sp_start, sp_end



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Print Matrix List                                                                                                                                  -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def _print_matrix_list(self,my_list):
    # d  :data,   v: vertical,   hcl: left_corner_header,   mch:middle_corner_header, rch:right_corner_header,   t:title(header)
    # get all the settings for the list

    set_d = set_font(self.bold_data, self.bg_data, self.fg_data,self.italic_data, self.underline_data, self.strike_data,\
                     self.blinking_data, self.dim_data, self.hidden_data, self.inverse_data)

    set_v = set_font(self.bold_vertical_line, self.bg_vertical_line, self.fg_vertical_line)

    set_hchr_v = set_font(self.bold_vertical_header_line_chr, self.bg_vertical_header_line_chr,self.fg_vertical_header_line_chr)

    set_t = set_font(self.bold_header, self.bg_header, self.fg_header,self.italic_header,self.underline_header,self.strike_header,\
                     self.blinking_header,self.dim_header,self.hidden_header,self.inverse_header)

    total_length = _get_total_length(self,my_list)

    ins_newline(self.adj_top_margin)
    # print title
    _print_title(self,my_list)
    # this is the last part and we need to start printing the matrix
    if len(my_list[0]) == 1:
        # we are dealing with only one column
        #---------------------------------------------------------------------------------------------------------------------------------------------
        #_print_horizontal_segment(self,start_chr,end_chr,times,indent,option)
        # item is the longest column
        length = total_length - (self.adj_indent + (self.adj_space*2) + 2) # length is the longest column length

        # print the top horizontal line
        if  self.top_horizontal_line_on == True:
            indent = 1  # to add the space at the beginning ()
            _print_horizontal_segment(self, self.top_left_corner_chr, self.top_horizontal_line_chr, length + (2*self.adj_space), indent, "corner")
            indent = 0  # to don't add this space at the end or the middle
            _print_horizontal_segment(self, self.top_right_corner_chr, self.top_horizontal_line_chr, 0, indent, "corner")
            print()

        else:  pass
            #-----------------------------------------------------------------------------------------------------------------------------------------
            # print data here
        ctrl_header = 0
        for row in my_list:
            for dato in row:
                if ctrl_header == 0:        # printing Header
                    ctrl_header += 1
                    if (self.align_header.lower() == "left") or (self.align_header.lower() == "l"):
                        print(_move_right(self.adj_indent) + set_hchr_v + self.left_vertical_header_line_chr + set_t + dato +\
                              _move_right((self.adj_space*2)+(length-len(dato)),self.bg_all_cell_header) + set_hchr_v +\
                              self.right_vertical_header_line_chr + reset_font(),end="")

                    elif (self.align_header.lower() == "right") or (self.align_header.lower() == "r"):
                        print(_move_right(self.adj_indent) + set_hchr_v + self.left_vertical_header_line_chr + set_t +\
                              _move_right((self.adj_space*2)+(length-len(dato)),self.bg_all_cell_header) + dato + set_hchr_v +\
                              self.right_vertical_header_line_chr + reset_font(),end="")

                    elif (self.align_header.lower() == "center") or (self.align_header.lower() == "c"):
                        # add the extra space for the word odd or even space adjustment for start and the end
                        oe_sp_start, oe_sp_end = _get_odd_even_space_adj(length,len(dato))
                        print(_move_right(self.adj_indent) + set_hchr_v + self.left_vertical_header_line_chr + set_t +\
                              _move_right(self.adj_space+oe_sp_start,self.bg_all_cell_header)+ dato +\
                              _move_right(self.adj_space+oe_sp_end,self.bg_all_cell_header) +\
                              set_hchr_v+self.right_vertical_header_line_chr+reset_font(),end="")

                    elif (self.align_header.lower() == "justify") or (self.align_header.lower() == "j"):
                        print(_move_right(self.adj_indent) + set_hchr_v + self.left_vertical_header_line_chr + set_t +\
                              _move_right(self.adj_space,self.bg_all_cell_header) + dato +\
                           _move_right(self.adj_space+(length-len(dato)),self.bg_all_cell_header) + set_hchr_v +\
                           self.right_vertical_header_line_chr+reset_font(),end="")
                    else:
                        print(_move_right(self.adj_indent) + set_hchr_v + self.left_vertical_header_line_chr + set_t +\
                              _move_right(self.adj_space,self.bg_all_cell_header) + dato +\
                              _move_right(self.adj_space+(length-len(dato)),self.bg_all_cell_header) + set_hchr_v +\
                              self.right_vertical_header_line_chr + reset_font(),end="")
                    print()
                    # the horizontal line between the headers and the first data row, only for matrix list
                    # if self.horizontal_line_under_header_on == True or self.middle_horizontal_line_on == 1:
                    # the horizontal line between the headers and the first data row, only for matrix list
                    if self.horizontal_line_under_header_on == True :
                        indent = 1; _print_horizontal_segment(self, self.left_corner_line_under_header_chr,\
                                 self.horizontal_line_under_header_chr, length + (2*self.adj_space), indent, "horizontal_header")
                        indent = 0; _print_horizontal_segment(self, self.right_corner_line_under_header_chr,\
                                                     self.horizontal_line_under_header_chr, 0, indent, "horizontal_header")
                        print()

                else:                        # printing Data
                    if (self.align_data.lower() == "left") or (self.align_data.lower() == "l"):
                        print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d + dato+\
                           _move_right((self.adj_space*2)+(length-len(dato)),self.bg_all_cell_data) +\
                           set_v + self.right_vertical_line_chr + reset_font(),end="")

                    elif (self.align_data.lower() == "right") or (self.align_data.lower() == "r"):
                        print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d +\
                              _move_right((self.adj_space*2)+(length-len(dato)),self.bg_all_cell_data) +\
                                 dato + set_v + self.right_vertical_line_chr + reset_font(),end="")

                    elif (self.align_data.lower() == "center") or (self.align_data.lower() == "c"):
                        # add the extra space for the word odd or even space adjustment for start and the end
                        oe_sp_start, oe_sp_end = _get_odd_even_space_adj(length,len(dato))
                        print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d +\
                              _move_right(self.adj_space+oe_sp_start,self.bg_all_cell_data)+ dato +\
                              _move_right(self.adj_space+oe_sp_end,self.bg_all_cell_data) + set_v +\
                              self.right_vertical_line_chr + reset_font(),end="")

                    elif (self.align_data.lower() == "justify") or (self.align_data.lower() == "j"):
                        print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d +\
                              _move_right(self.adj_space,self.bg_all_cell_data)+ dato +\
                              _move_right(self.adj_space+length-len(dato),self.bg_all_cell_data)+\
                              set_v + self.right_vertical_line_chr + reset_font(),end="")

                    else:
                        print(_move_right(self.adj_indent) + set_v + self.left_vertical_line_chr + set_d +\
                              _move_right(self.adj_space,self.bg_all_cell_data)+ dato +\
                              _move_right(self.adj_space+length-len(dato),self.bg_all_cell_data) + set_v +\
                              self.right_vertical_line_chr + reset_font(),end="")

                    print()
                    # the horizontal line for all the rows, only for matrix list. 1 shows it and 0 hides it
                    if self.middle_horizontal_line_on == 1:
                        ctrl_header += 1
                        if ctrl_header == len(my_list):  pass

                        else:
                            indent = 1; _print_horizontal_segment(self, self.left_lateral_corner_chr, self.middle_horizontal_line_chr,\
                                                                  length + (2*self.adj_space), indent, "inner_corner")

                            indent = 0; _print_horizontal_segment(self, self.right_lateral_corner_chr, self.middle_horizontal_line_chr,\
                                                                  0, indent, "inner_corner")
                            print()
        #---------------------------------------------------------------------------------------------------------------------------------------------

        # print the bottom horizontal line
        if  self.bottom_horizontal_line_on == 1:
            indent = 1  # to add the space at the beginning (vertical line chr)
            _print_horizontal_segment(self, self.bottom_left_corner_chr, self.bottom_horizontal_line_chr,\
                                      length + (2*self.adj_space), indent, "corner")
            indent = 0  # to don't add this space at the end or the middle
            _print_horizontal_segment(self, self.bottom_right_corner_chr, self.bottom_horizontal_line_chr,\
                                      0, indent, "corner")
            print()

        else:  pass

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # we are dealing with a matrix list something like this [[10,20,30],[40,50,60],[70,80,90]]                                                       -
    # Awsome...!                                                                                                                                     -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    else:
        max_rows, max_cols = _get_number_rows_cols_list(my_list)
        n_cols = []; tempo_cols = []

        # we create the transpose of the list but we save their lens in the transpose rather than the data
        for c in range(max_cols):
            for r in range(max_rows):
                tempo_cols.append(len(my_list[r][c]))
            n_cols.append(tempo_cols)
            tempo_cols = []

        longest_cols = []
        for col in n_cols:
            longest_cols.append(max(col)) # longest_cols keeps the size list of the longest columns in characters

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # drawing the top horizontal line
        if  self.top_horizontal_line_on == True:
            indent = 1  # to add the space at the beginning (indentation space)
            for item in longest_cols:
                if indent == 1:
                    _print_horizontal_segment(self, self.top_left_corner_chr, self.top_horizontal_line_chr, (item+(2*self.adj_space)),\
                                              indent, "corner")
                    indent = 0
                else:   # corner or horizontal affect the color bg fg which variable will take into action
                    _print_horizontal_segment(self, self.middle_top_corner_chr, self.top_horizontal_line_chr, (item+(2*self.adj_space)),\
                                              indent, "inner_corner")

            # last segment, which is only the corner that's why it's 0 on value
            _print_horizontal_segment(self, self.top_right_corner_chr, self.top_horizontal_line_chr, 0, indent, "corner")
            print() # done top line, jump to next line to print data

        else:  pass
        #---------------------------------------------------------------------------------------------------------------------------------------------
        # print header only
        ctrl_col = 0
        vertical = _move_right(self.adj_indent)+set_hchr_v+self.left_vertical_header_line_chr
        for dato in my_list[0]:

            if (self.align_header.lower() == "left") or (self.align_header.lower() == "l"):
                print(vertical + set_t + dato + _move_right((self.adj_space*2)+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_header) +\
                      reset_font(),end="")

            elif (self.align_header.lower() == "right") or (self.align_header.lower() == "r"):
                print(vertical + set_t + _move_right((self.adj_space*2)+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_header) +\
                      dato + reset_font(),end="")

            elif (self.align_header.lower() == "center") or (self.align_header.lower() == "c"):
                # add the extra space for the word odd or even space adjustment for start and the end
                oe_sp_start, oe_sp_end = _get_odd_even_space_adj(longest_cols[ctrl_col],len(dato))
                print(vertical + set_t + _move_right(self.adj_space+oe_sp_start,self.bg_all_cell_header) + dato +\
                      _move_right(self.adj_space+oe_sp_end,self.bg_all_cell_header) + reset_font(),end="")

            elif (self.align_header.lower() == "justify") or (self.align_header.lower() == "j"):
                print(vertical + set_t + _move_right(self.adj_space,self.bg_all_cell_header) + dato +\
                      _move_right(self.adj_space+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_header) + reset_font(),end="")

            else:
                print(vertical + set_t + _move_right(self.adj_space,self.bg_all_cell_header) + dato +\
                      _move_right(self.adj_space+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_header) + reset_font(),end="")

            vertical = set_hchr_v+self.middle_vertical_header_line_chr
            ctrl_col += 1
        print(set_hchr_v+self.right_vertical_header_line_chr+reset_font())

        #---------------------------------------------------------------------------------------------------------------------------------------------
        if self.horizontal_line_under_header_on == True :
            # the horizontal line between the headers and the firs data row, only for matrix list
            indent = 1  # to add the space at the beginning (indentation space)
            # drawing the bottom horizontal line
            for item in longest_cols:
                if indent == 1:
                    _print_horizontal_segment(self, self.left_corner_line_under_header_chr,\
                       self.horizontal_line_under_header_chr, (item+(2*self.adj_space)), indent,"horizontal_header") # first segment
                    indent = 0
                else:
                    _print_horizontal_segment(self, self.middle_corner_line_under_header_chr,\
                       self.horizontal_line_under_header_chr, (item+(2*self.adj_space)), indent,"horizontal_header") # middle segments

            # last segment, which is only the corner that's why it's 0 on value
            _print_horizontal_segment(self, self.right_corner_line_under_header_chr,\
                  self.horizontal_line_under_header_chr, 0, indent, "horizontal_header")

            print() # done top line, jump to next line to print data

        ctrl_sep = 1
        for datos in my_list[1:]:  # This skip the first one
            ctrl_col = 0
            vertical = _move_right(self.adj_indent)+set_v+self.left_vertical_line_chr
            for dato in datos:

                if (self.align_data.lower() == "left") or (self.align_data.lower() == "l"):
                    print(vertical + set_d + dato + _move_right((self.adj_space*2)+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_data) +\
                          reset_font(),end="")

                elif (self.align_data.lower() == "right") or (self.align_data.lower() == "r"):
                    print(vertical + set_d + _move_right((self.adj_space*2)+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_data) +\
                          dato + reset_font(),end="")

                elif (self.align_data.lower() == "center") or (self.align_data.lower() == "c"):
                    # add the extra space for the word odd or even space adjustment for start and the end
                    oe_sp_start, oe_sp_end = _get_odd_even_space_adj(longest_cols[ctrl_col],len(dato))
                    print(vertical + set_d + _move_right(self.adj_space+oe_sp_start,self.bg_all_cell_data) + dato +\
                          _move_right(self.adj_space+oe_sp_end,self.bg_all_cell_data) + reset_font(),end="")

                elif (self.align_data.lower() == "justify") or (self.align_data.lower() == "j"):
                    print(vertical + set_d + _move_right(self.adj_space,self.bg_all_cell_data) + dato +\
                          _move_right(self.adj_space+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_data) + reset_font(),end="")

                else:
                    print(vertical + set_d + _move_right(self.adj_space,self.bg_all_cell_data) + dato +\
                          _move_right(self.adj_space+(longest_cols[ctrl_col]-len(dato)),self.bg_all_cell_data) + reset_font(),end="")

                vertical = set_v+self.middle_vertical_line_chr
                ctrl_col += 1
            print(set_v+self.right_vertical_line_chr+reset_font())

            if self.middle_horizontal_line_on == 1:
                if ctrl_sep == len(my_list)-1:
                    # drawing the bottom horizontal line
                    if  self.bottom_horizontal_line_on == 1:
                        indent = 1  # to add the space at the beginning (indentation space)

                        for item in longest_cols:
                            if indent == 1:
                                # def _print_horizontal_segment(self,start_chr,end_chr,times,indent,option):
                                _print_horizontal_segment(self, self.bottom_left_corner_chr, self.bottom_horizontal_line_chr,\
                                   (item+(2*self.adj_space)), indent, "corner") # first segment
                                indent = 0

                            else:
                                # def _print_horizontal_segment(self,start_chr,end_chr,times,indent,option):
                                _print_horizontal_segment(self, self.middle_bottom_corner_chr, self.bottom_horizontal_line_chr,\
                                   (item+(2*self.adj_space)), indent, "inner_corner")
                                # last segment, which is only the corner that's why it's 0 on value
                        _print_horizontal_segment(self, self.bottom_right_corner_chr,\
                           self.bottom_horizontal_line_chr, 0, indent, "corner")

                    else:
                        pass
                else:
                    indent = 1  # to add the space at the beginning (indentation space)
                                # drawing the bottom horizontal line
                    for item in longest_cols:
                        if indent == 1:
                            # def _print_horizontal_segment(self,start_chr,end_chr,times,indent,option):
                            _print_horizontal_segment(self, self.left_lateral_corner_chr, self.middle_horizontal_line_chr,\
                                                     (item+(2*self.adj_space)), indent,"inner_corner")
                            indent = 0

                        else:
                            _print_horizontal_segment(self, self.middle_inner_corner_chr, self.middle_horizontal_line_chr,\
                                                     (item+(2*self.adj_space)), indent, "inner_corner")

                    _print_horizontal_segment(self, self.right_lateral_corner_chr, self.middle_horizontal_line_chr,\
                                              0, indent, "inner_corner")
                print()
            ctrl_sep += 1

        if self.middle_horizontal_line_on == 0:
            if  self.bottom_horizontal_line_on == 1:
                indent = 1  # to add the space at the beginning (indentation space)
                            # drawing the bottom horizontal line
                for item in longest_cols:
                    if indent == 1:
                        # first segment
                        _print_horizontal_segment(self, self.bottom_left_corner_chr, self.bottom_horizontal_line_chr,\
                                                 (item+(2*self.adj_space)), indent, "corner")
                        indent = 0
                    else:
                        #"horizontal")#"corner") # middle segments
                        _print_horizontal_segment(self, self.middle_bottom_corner_chr, self.bottom_horizontal_line_chr,\
                                                 (item+(2*self.adj_space)), indent, "inner_corner")

                        # last segment, which is only the corner that's why it's 0 on value
                _print_horizontal_segment(self, self.bottom_right_corner_chr, self.bottom_horizontal_line_chr,\
                                          0, indent, "corner")
                print() # done top line, jump to next line to print data

            else:  pass
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    _print_notefoot(self,my_list)
    ins_newline(self.adj_bottom_margin)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# End Printing Matrix                                                                                                                                -
#-----------------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Fancy Format Class, Defing the Class Without Initial Parameters                                                                                   --
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
class FancyFormat():
    '''
    It create the format for the fancy_print_format method
    '''
    def __init__(self):
        #---------------------------------------------------------------------------------------------------------------------------------------------
        # defining variable names                  # values to take                                                                                  -
        #---------------------------------------------------------------------------------------------------------------------------------------------
        # General Use
        self.adj_top_margin    = 0                 # lines to be add between the terminal and the title
        self.adj_bottom_margin = 0                 # lines to be add between the end of list or footnote and terminal
        self.adj_top_space     = 0                 # lines to be added between title and top list
        self.adj_bottom_space  = 0                 # lines to be added between bottom list and footnote
        self.adj_indent        = 2                 # space from the terminal to the box
        self.adj_space         = 2                 # space from left to right inside inside the box
        self.set_fill_chr      = "----"            # to fill the empty spots when the list is not complete
        self.set_layout        = Layout.HORIZONTAL # This is only for Range, Set, and Frozenset type data
        self.update_list       = False             # if we want to save the data as it's presented, but string each element in list

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Title Section
        self.msg_title       = ""                  # string value
        self.bold_title      = False               # two values False and True (0 and 1)
        self.bg_title        = -1                  # values -1 to 255
        self.fg_title        = -1                  # values -1 to 255
        self.align_title     = "justify"           # 4 values: justify(j),left(l), center(c), and right(r)
        self.italic_title    = False               # two values False and True (0 and 1)
        self.underline_title = False               # two values False and True (0 and 1)
        self.strike_title    = False               # two values False and True (0 and 1)
        self.blinking_title  = False               # two values False and True (0 and 1)
        self.dim_title       = False               # two values False and True (0 and 1)
        self.hidden_title    = False               # two values False and True (0 and 1)
        self.inverse_title   = False               # two values False and True (0 and 1)

        # Footnote Section
        self.msg_footnote       = ""               # string value
        self.bold_footnote      = False            # two values False and True (0 and 1)
        self.bg_footnote        = -1               # values -1 to 255
        self.fg_footnote        = -1               # values -1 to 255
        self.align_footnote     = "justify"        # 4 values: justify(j),left(l), center(c), and right(r)
        self.italic_footnote    = False            # two values False and True (0 and 1)
        self.underline_footnote = False            # two values False and True (0 and 1)
        self.strike_footnote    = False            # two values False and True (0 and 1)
        self.blinking_footnote  = False            # two values False and True (0 and 1)
        self.dim_footnote       = False            # two values False and True (0 and 1)
        self.hidden_footnote    = False            # two values False and True (0 and 1)
        self.inverse_footnote   = False            # two values False and True (0 and 1)

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Data Section
        self.bold_data        = False              # two values False and True (0 and 1)
        self.bg_data          = -1                 # values -1 to 255
        self.bg_all_cell_data = True               # how long will be the bg (all the cell or only the data)
        self.fg_data          = -1                 # values -1 to 255
        self.align_data       = "justify"          # 4 values: justify(j),left(l), center(c), and right(r)
        self.italic_data      = False              # two values False and True (0 and 1)
        self.underline_data   = False              # two values False and True (0 and 1)
        self.strike_data      = False              # two values False and True (0 and 1)
        self.blinking_data    = False              # two values False and True (0 and 1)
        self.dim_data         = False              # two values False and True (0 and 1)
        self.hidden_data      = False              # two values False and True (0 and 1)
        self.inverse_data     = False              # two values False and True (0 and 1)

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Horizontal Line Section
        self.top_horizontal_line_chr    = "-"      # chr used to print the horizontal segment for the top line
        self.top_horizontal_line_on     = True
        self.bottom_horizontal_line_chr ="-"       # chr used to print the horizontal segment for the bottom line
        self.bottom_horizontal_line_on  = True     # two values False and True (0 and 1)
        self.middle_horizontal_line_chr = "-"      # chr used to print the horizontal segment horizontal. Only matrix list
        self.middle_horizontal_line_on  = False    # horizontal line for all the rows, only for matrix list. 1 shows it and 0 hides it

        self.bold_horizontal_line = False          # two values False and True (0 and 1)
        self.bg_horizontal_line   = -1             # values -1 to 255
        self.fg_horizontal_line   = -1             # values -1 to 255
        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Vertical Line Section
        self.left_vertical_line_chr   = "|"        # used for the left vertical line only
        self.middle_vertical_line_chr = "|"        # all the vertical line in the middle between left and right. Only matrix
        self.right_vertical_line_chr  = "|"        # used for the right vertical line only

        self.bold_vertical_line = False            # two values False and True (0 and 1)
        self.bg_vertical_line   = -1               # values -1 to 255
        self.fg_vertical_line   = -1               # values -1 to 255

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # External Corner Section
        self.top_left_corner_chr     = "+"         # chr for the top left corner
        self.top_right_corner_chr    = "+"         # chr for the top right corner
        self.bottom_right_corner_chr = "+"         # chr for the bottom right corner
        self.bottom_left_corner_chr  = "+"         # chr for the bottom left corner

        self.bold_corner_chr = False               # two values False and True (0 and 1)
        self.bg_corner_chr   = -1                  # values -1 to 255
        self.fg_corner_chr   = -1                  # values -1 to 255

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Middle Corner Section
        self.middle_top_corner_chr    = "+"        # all the middle corners between top_left_corner_chr and top_right_corner_chr. Only matrix list
        self.middle_bottom_corner_chr = "+"        # all the middle corners between top_left_corner_chr and top_right_corner_chr. Only matrix list
        self.middle_inner_corner_chr  = "+"        # corner inside the matrix and sides but not top(left,right), or bottom(left, right). Only matrix list
        self.left_lateral_corner_chr  = "+"        # chr only for matrix list
        self.right_lateral_corner_chr = "+"        # chr only for matrix list

        self.bold_inner_corner_chr = False         # two values False and True (0 and 1)
        self.bg_inner_corner_chr   = -1            # values -1 to 255
        self.fg_inner_corner_chr   = -1            # values -1 to 255

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Header Section  Only for Matrix List
        self.bold_header        = False            # two values False and True (0 and 1)
        self.bg_header          = -1               # values -1 to 255
        self.bg_all_cell_header = True             # how long will be the bg (all the cell or only the header)
        self.fg_header          = -1               # values -1 to 255
        self.align_header       = "justify"        # 4 values: justify(j),left(l), center(c), and right(r)
        self.italic_header      = False            # two values False and True (0 and 1)
        self.underline_header   = False            # two values False and True (0 and 1)
        self.strike_header      = False            # two values False and True (0 and 1)
        self.blinking_header    = False            # two values False and True (0 and 1)
        self.dim_header         = False            # two values False and True (0 and 1)
        self.hidden_header      = False            # two values False and True (0 and 1)
        self.inverse_header     = False            # two values False and True (0 and 1)

        # Attributes for the header lines
        self.left_vertical_header_line_chr   = "|"     # small_bullet u'\u2022'
        self.right_vertical_header_line_chr  = "|"     # circle_bullet u'\u2B24'
        self.middle_vertical_header_line_chr = "|"     # matrix list only
        self.bold_vertical_header_line_chr   = False   # two values False and True (0 and 1)
        self.bg_vertical_header_line_chr     = -1      # values -1 to 255
        self.fg_vertical_header_line_chr     = -1      # values -1 to 255

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Under Line Header Section  Only for Matrix List
        # attributes for the line below the header text
        self.horizontal_line_under_header_on  = False    # horizontal line between headers and the firs data row. 1 shows it and 0 hides it
        self.horizontal_line_under_header_chr = "-"      # chr to be printed for theheader line

        self.bold_under_line_header = False              # values -1 to 255
        self.bg_under_line_header   = -1                 # values -1 to 255
        self.fg_under_line_header   = -1                 # values -1 to 255

        # attributes for the header corners (left, middles and right)
        self.left_corner_line_under_header_chr   = "+"   # only for header line
        self.right_corner_line_under_header_chr  = "+"   # only for header line
        self.middle_corner_line_under_header_chr = "+"   # only for header line
        self.bold_corner_under_line_header       = False # two values False and True (0 and 1)
        self.bg_corner_under_line_header         = -1    # values -1 to 255
        self.fg_corner_under_line_header         = -1    # values -1 to 255


    def reset_fancy_format(self):

        '''  It resets all the attributes of the class  '''

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # defining variable names                  # values to take                                                                                  -
        #---------------------------------------------------------------------------------------------------------------------------------------------
        # General Use
        self.adj_top_margin    = 0                 # lines to be add between the terminal and the title
        self.adj_bottom_margin = 0                 # lines to be add between the end of list or footnote and terminal
        self.adj_top_space     = 0                 # lines to be added between title and top list
        self.adj_bottom_space  = 0                 # lines to be added between bottom list and footnote
        self.adj_indent        = 2                 # space from the terminal to the box
        self.adj_space         = 2                 # space from left to right side inside the box
        self.set_fill_chr      = "----"            # to fill the empty spots when the list is not complete
        self.set_layout        = Layout.HORIZONTAL # This is only for Range, Set, and Frozenset type data
        self.update_list       = False             # if we want to save the data as it's presented, but string each element in list

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Title Section
        self.bg_title    = -1                      # values -1 to 255
        self.fg_title    = -1                      # values -1 to 255
        self.msg_title   = ""                      # string value
        self.bold_title  = False                   # two values False and True (0 and 1)
        self.align_title = "justify"               # 4 values: justify(j),left(l), center(c), and right(r)

        self.italic_title    = False               # two values False and True (0 and 1)
        self.underline_title = False               # two values False and True (0 and 1)
        self.strike_title    = False               # two values False and True (0 and 1)
        self.blinking_title  = False               # two values False and True (0 and 1)
        self.dim_title       = False               # two values False and True (0 and 1)
        self.hidden_title    = False               # two values False and True (0 and 1)
        self.inverse_title   = False               # two values False and True (0 and 1)

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Footnote Section
        self.msg_footnote   = ""                   # string value
        self.bold_footnote  = False                # two values False and True (0 and 1)
        self.bg_footnote    = -1                   # values -1 to 255
        self.fg_footnote    = -1                   # values -1 to 255
        self.align_footnote = "justify"            # 4 values: justify(j),left(l), center(c), and right(r)

        self.italic_footnote    = False            # two values False and True (0 and 1)
        self.underline_footnote = False            # two values False and True (0 and 1)
        self.strike_footnote    = False            # two values False and True (0 and 1)
        self.blinking_footnote  = False            # two values False and True (0 and 1)
        self.dim_footnote       = False            # two values False and True (0 and 1)
        self.hidden_footnote    = False            # two values False and True (0 and 1)
        self.inverse_footnote   = False            # two values False and True (0 and 1)


        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Data Section
        self.bold_data  = False                    # two values False and True (0 and 1)
        self.bg_data    = -1                       # values -1 to 255
        self.fg_data    = -1                       # values -1 to 255
        self.align_data = "justify"                # 4 values: justify(j),left(l), center(c), and right(r)

        self.middle_horizontal_line_on = False     # horizontal line for all the rows, only for matrix list. 1 shows it and 0 hides it
        self.bg_all_cell_data          = True      # how long will be the bg (all the cell or only the data)

        self.italic_data    = False                # two values False and True (0 and 1)
        self.underline_data = False                # two values False and True (0 and 1)
        self.strike_data    = False                # two values False and True (0 and 1)
        self.blinking_data  = False                # two values False and True (0 and 1)
        self.dim_data       = False                # two values False and True (0 and 1)
        self.hidden_data    = False                # two values False and True (0 and 1)
        self.inverse_data   = False                # two values False and True (0 and 1)

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Horizontal Line Section
        self.top_horizontal_line_chr    = "-"      # chr used to print the horizontal segment for the top line
        self.top_horizontal_line_on     = True
        self.bottom_horizontal_line_chr ="-"       # chr used to print the horizontal segment for the bottom line
        self.bottom_horizontal_line_on  = True     # two values False and True (0 and 1)
        self.middle_horizontal_line_chr = "-"      # chr used to print the horizontal segment horizontal. Only matrix list

        self.bold_horizontal_line = False          # two values False and True (0 and 1)
        self.bg_horizontal_line   = -1             # values -1 to 255
        self.fg_horizontal_line   = -1             # values -1 to 255
        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Vertical Line Section
        self.left_vertical_line_chr   = "|"        # used for the left vertical line only
        self.middle_vertical_line_chr = "|"        # all the vertical line in the middle between left and right. Only matrix
        self.right_vertical_line_chr  = "|"        # used for the right vertical line only

        self.bold_vertical_line = False            # two values False and True (0 and 1)
        self.bg_vertical_line   = -1               # values -1 to 255
        self.fg_vertical_line   = -1               # values -1 to 255

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Corner Section
        self.top_left_corner_chr     = "+"         # chr for the top left corner
        self.top_right_corner_chr    = "+"         # chr for the top right corner
        self.bottom_right_corner_chr = "+"         # chr for the bottom right corner
        self.bottom_left_corner_chr  = "+"         # chr for the bottom left corner

        self.bold_corner_chr = False               # two values False and True (0 and 1)
        self.bg_corner_chr   = -1                  # values -1 to 255
        self.fg_corner_chr   = -1                  # values -1 to 255

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Corner Section
        self.middle_top_corner_chr    =  "+"       # all the middle corners between top_left_corner_chr and top_right_corner_chr. Only matrix list
        self.middle_bottom_corner_chr = "+"        # all the middle corners between top_left_corner_chr and top_right_corner_chr. Only matrix list
        self.middle_inner_corner_chr  = "|"       # corner inside the matrix and sides but not top(left,right), or bottom(left, right). Only matrix list

        self.left_lateral_corner_chr  = "|"        # chr only for matrix list
        self.right_lateral_corner_chr = "|"        # chr only for matrix list

        self.bold_inner_corner_chr = False         # two values False and True (0 and 1)
        self.bg_inner_corner_chr   = -1            # values -1 to 255
        self.fg_inner_corner_chr   = -1            # values -1 to 255

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Header Section  Only for Matrix List
        # attributes for the header text
        self.bold_header  = False                  # two values False and True (0 and 1)
        self.bg_header    = -1                     # values -1 to 255
        self.fg_header    = -1                     # values -1 to 255
        self.align_header = "justify"              # 4 values: justify(j),left(l), center(c), and right(r)

        self.bg_all_cell_header = True             # how long will be the bg (all the cell or only the header)

        self.italic_header    = False              # two values False and True (0 and 1)
        self.underline_header = False              # two values False and True (0 and 1)
        self.strike_header    = False              # two values False and True (0 and 1)
        self.blinking_header  = False              # two values False and True (0 and 1)
        self.dim_header       = False              # two values False and True (0 and 1)
        self.hidden_header    = False              # two values False and True (0 and 1)
        self.inverse_header   = False              # two values False and True (0 and 1)

        self.left_vertical_header_line_chr   = "|" # small_bullet u'\u2022'
        self.right_vertical_header_line_chr  = "|" # circle_bullet u'\u2B24'
        self.middle_vertical_header_line_chr = "|" # matrix list only

        self.bold_vertical_header_line_chr = False # two values False and True (0 and 1)
        self.bg_vertical_header_line_chr   = -1    # values -1 to 255
        self.fg_vertical_header_line_chr   = -1    # values -1 to 255

        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Under Line Header Section  Only for Matrix List
        # attributes for the line below the header text
        self.horizontal_line_under_header_on  = False    # horizontal line between headers and the firs data row. 1 shows it and 0 hides it
        self.horizontal_line_under_header_chr = "-"      # chr to be printed for theheader line

        self.bold_under_line_header = False              # values -1 to 255
        self.bg_under_line_header   = -1                 # values -1 to 255
        self.fg_under_line_header   = -1                 # values -1 to 255

        # attributes for the header corners (left, middles and right)
        self.left_corner_line_under_header_chr   = "+"   # only for header line
        self.right_corner_line_under_header_chr  = "+"   # only for header line
        self.middle_corner_line_under_header_chr = "+"   # only for header line

        self.bold_corner_under_line_header = False       # two values False and True (0 and 1)
        self.bg_corner_under_line_header   = -1          # values -1 to 255
        self.fg_corner_under_line_header   = -1          # values -1 to 255



    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Defing a the main function to control the print of the list                                                                                    -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def print_fancy_format(self,data="none",style=Line_Style.CUSTOMIZED):

        '''  It prints any type of data in a fancy format

             print_fancy_format(data, style)  '''

        data_list = data2list(self, data)
        my_list = []
        # convert all elements in the list to strigs only because the int type will cause problems with len command
        list_type = _get_list_type(data_list)
        #---------------------------------------------------------------------------------------------------------------------------------------------

        if style.lower() == Line_Style.CUSTOMIZED: pass
        else:
            # backup all the default values
            # Horizontal Line Section
            thlc = self.top_horizontal_line_chr;    bhlc = self.bottom_horizontal_line_chr;     hlc = self.middle_horizontal_line_chr

            # Vertical Line Section
            lvlc = self.left_vertical_line_chr;     mvlc = self.middle_vertical_line_chr;       rvlc = self.right_vertical_line_chr

            # Corner Section
            tlcc = self.top_left_corner_chr;        trcc = self.top_right_corner_chr;           brcc = self.bottom_right_corner_chr
            blcc = self.bottom_left_corner_chr

            mtcc = self.middle_top_corner_chr;      mbcc = self.middle_bottom_corner_chr;       micc = self.middle_inner_corner_chr
            llcc = self.left_lateral_corner_chr;    rlcc = self.right_lateral_corner_chr

            # Header Section  Only for Matrix List
            lvhlc = self.left_vertical_header_line_chr
            rvhlc = self.right_vertical_header_line_chr
            mvhlc = self.middle_vertical_header_line_chr

            # Under Line Header Section  Only for Matrix List
            hluhc = self.horizontal_line_under_header_chr

            # attributes for the header corners (left, middles and right)
            lculhc = self.left_corner_line_under_header_chr
            rculhc = self.right_corner_line_under_header_chr
            mculhc = self.middle_corner_line_under_header_chr


            if style.lower() == Line_Style.SINGLE:
                # Horizontal Line Section
                self.top_horizontal_line_chr = "\u2500";   self.bottom_horizontal_line_chr = "\u2500";  self.middle_horizontal_line_chr = "\u2500"

                # Vertical Line Section
                self.left_vertical_line_chr  = "\u2502";   self.middle_vertical_line_chr = "\u2502";    self.right_vertical_line_chr = "\u2502"

                # Outside Corner Section
                self.top_left_corner_chr     = "\u250C";   self.top_right_corner_chr   = "\u2510"
                self.bottom_right_corner_chr = "\u2518";   self.bottom_left_corner_chr = "\u2514"

                # Middle Corner Section
                self.middle_top_corner_chr   = "\u252C";   self.middle_bottom_corner_chr = "\u2534";    self.middle_inner_corner_chr = "\u253C"
                self.left_lateral_corner_chr = "\u251C";   self.right_lateral_corner_chr = "\u2524"

                # Header Section  Only for Matrix List
                self.left_vertical_header_line_chr   = "\u2502"
                self.middle_vertical_header_line_chr = "\u2502"
                self.right_vertical_header_line_chr  = "\u2502"

                # Under Line Header Section  Only for Matrix List
                self.horizontal_line_under_header_chr   = "\u2500";          self.left_corner_line_under_header_chr   = "\u251C"
                self.right_corner_line_under_header_chr = "\u2524";          self.middle_corner_line_under_header_chr = "\u253C"


            elif style.lower() == Line_Style.SINGLE_BOLD:
                # Horizontal Line Section
                self.top_horizontal_line_chr = "\u2501";   self.bottom_horizontal_line_chr = "\u2501"; self.middle_horizontal_line_chr = "\u2501"

                # Vertical Line Section
                self.left_vertical_line_chr  = "\u2503";   self.middle_vertical_line_chr = "\u2503";   self.right_vertical_line_chr = "\u2503"

                # Outside Corner Section
                self.top_left_corner_chr     = "\u250F";   self.top_right_corner_chr   = "\u2513"
                self.bottom_right_corner_chr = "\u251B";   self.bottom_left_corner_chr = "\u2517"


                # Middle Corner Section
                self.middle_top_corner_chr   = "\u2533";   self.middle_bottom_corner_chr = "\u253B";   self.middle_inner_corner_chr = "\u254B"
                self.left_lateral_corner_chr = "\u2523";   self.right_lateral_corner_chr = "\u252B"

                # Header Section  Only for Matrix List
                self.left_vertical_header_line_chr   = "\u2503"
                self.right_vertical_header_line_chr  = "\u2503"
                self.middle_vertical_header_line_chr = "\u2503"

                # Under Line Header Section  Only for Matrix List
                self.horizontal_line_under_header_chr   = "\u2501";          self.left_corner_line_under_header_chr   = "\u2523"
                self.right_corner_line_under_header_chr = "\u252B";          self.middle_corner_line_under_header_chr = "\u254B"


            elif style.lower() == Line_Style.SINGLE_HEAVY:
                # Horizontal Line Section
                self.top_horizontal_line_chr = "\u2586";    self.bottom_horizontal_line_chr="\u2586";   self.middle_horizontal_line_chr = "\u2586"

                # Vertical Line Section
                self.left_vertical_line_chr  = "\u2588";    self.middle_vertical_line_chr = "\u2588";   self.right_vertical_line_chr = "\u2588"

                # Outside Corner Section
                self.top_left_corner_chr     = "\u2586";    self.top_right_corner_chr   = "\u2586"
                self.bottom_right_corner_chr = "\u2588";    self.bottom_left_corner_chr = "\u2588"

                # Middle Corner Section
                self.middle_top_corner_chr   = "\u2586";    self.middle_bottom_corner_chr = "\u2588";   self.middle_inner_corner_chr = "\u2588"
                self.left_lateral_corner_chr = "\u2588";    self.right_lateral_corner_chr = "\u2588"

                # Header Section  Only for Matrix List
                self.left_vertical_header_line_chr   = "\u2588"
                self.right_vertical_header_line_chr  = "\u2588"
                self.middle_vertical_header_line_chr = "\u2588"

                # Under Line Header Section  Only for Matrix List
                self.horizontal_line_under_header_chr   = "\u2586";          self.left_corner_line_under_header_chr   = "\u2588"
                self.right_corner_line_under_header_chr = "\u2588";          self.middle_corner_line_under_header_chr = "\u2586"


            elif style.lower() == Line_Style.DOUBLE:
                # Horizontal Line Section
                self.top_horizontal_line_chr = "\u2550";   self.bottom_horizontal_line_chr = "\u2550";   self.middle_horizontal_line_chr = "\u2550"

                # Vertical Line Section
                self.left_vertical_line_chr  = "\u2551";   self.middle_vertical_line_chr = "\u2551";     self.right_vertical_line_chr = "\u2551"

                # Outside Corner Section
                self.top_left_corner_chr     = "\u2554";   self.top_right_corner_chr   = "\u2557"
                self.bottom_right_corner_chr = "\u255D";   self.bottom_left_corner_chr = "\u255A"

                # Middle Corner Section
                self.middle_top_corner_chr   = "\u2566";   self.middle_bottom_corner_chr = "\u2569";     self.middle_inner_corner_chr = "\u256C"
                self.left_lateral_corner_chr = "\u2560";   self.right_lateral_corner_chr = "\u2563"

                # Header Section  Only for Matrix List
                self.left_vertical_header_line_chr   = "\u2551"
                self.right_vertical_header_line_chr  = "\u2551"
                self.middle_vertical_header_line_chr = "\u2551"

                # Under Line Header Section  Only for Matrix List
                self.horizontal_line_under_header_chr   = "\u2550";          self.left_corner_line_under_header_chr   = "\u2560"
                self.right_corner_line_under_header_chr = "\u2563";          self.middle_corner_line_under_header_chr = "\u256C"


            elif style.lower() == Line_Style.SQ_BRACKETS:
                # Horizontal Line Section
                self.top_horizontal_line_chr = " ";           self.bottom_horizontal_line_chr = " ";        self.middle_horizontal_line_chr = " "

                # Vertical Line Section
                self.left_vertical_line_chr  = "\u2502";      self.middle_vertical_line_chr = " ";          self.right_vertical_line_chr = "\u2502"

                # Outside Corner Section
                self.top_left_corner_chr     = "\u250C";      self.top_right_corner_chr   = "\u2510"
                self.bottom_right_corner_chr = "\u2518";      self.bottom_left_corner_chr = "\u2514"

                # Middle Corner Section
                self.middle_top_corner_chr   =  " ";          self.middle_bottom_corner_chr = " ";          self.middle_inner_corner_chr = " "
                self.left_lateral_corner_chr =  "\u2502";     self.right_lateral_corner_chr = "\u2502"

                # Header Section  Only for Matrix List
                self.left_vertical_header_line_chr   = "\u2502"
                self.right_vertical_header_line_chr  = "\u2502"
                self.middle_vertical_header_line_chr = " "

                # Under Line Header Section  Only for Matrix List
                self.horizontal_line_under_header_chr   = " ";               self.left_corner_line_under_header_chr   = "\u2502"
                self.right_corner_line_under_header_chr = "\u2502";          self.middle_corner_line_under_header_chr = " "


            elif style.lower() == Line_Style.DASH:
                # Horizontal Line Section
                self.top_horizontal_line_chr = "\u002D";   self.bottom_horizontal_line_chr = "\u002D";  self.middle_horizontal_line_chr = "\u002D"

                # Vertical Line Section
                self.left_vertical_line_chr  = "\u254E";   self.middle_vertical_line_chr = "\u254E";    self.right_vertical_line_chr = "\u254E"

                # Outside Corner Section
                self.top_left_corner_chr     = "\u002B";   self.top_right_corner_chr   = "\u002B"
                self.bottom_right_corner_chr = "\u002B";   self.bottom_left_corner_chr = "\u002B"

                # Middle Corner Section
                self.middle_top_corner_chr   =  "\u002B";  self.middle_bottom_corner_chr = "\u002B";    self.middle_inner_corner_chr = "\u002B"
                self.left_lateral_corner_chr =  "\u002B";  self.right_lateral_corner_chr = "\u002B"

                # Header Section  Only for Matrix List
                self.left_vertical_header_line_chr   = "\u254E"
                self.right_vertical_header_line_chr  = "\u254E"
                self.middle_vertical_header_line_chr = "\u254E"

                # Under Line Header Section  Only for Matrix List
                self.horizontal_line_under_header_chr   = "\u002D";          self.left_corner_line_under_header_chr   = "\u002B"
                self.right_corner_line_under_header_chr = "\u002B";          self.middle_corner_line_under_header_chr = "\u002B"


            elif style.lower() == Line_Style.SPACE_COL_COLOR:
                # Horizontal Line Section
                self.top_horizontal_line_chr = " ";         self.bottom_horizontal_line_chr = " ";      self.middle_horizontal_line_chr = " "

                # Vertical Line Section
                self.left_vertical_line_chr  = "  ";         self.middle_vertical_line_chr = "  ";      self.right_vertical_line_chr = "  "

                # Outside Corner Section
                self.top_left_corner_chr     = "  ";         self.top_right_corner_chr   = "  "
                self.bottom_right_corner_chr = "  ";         self.bottom_left_corner_chr = "  "

                # Middle Corner Section
                self.middle_top_corner_chr   = "  ";         self.middle_bottom_corner_chr = "  ";      self.middle_inner_corner_chr = "  "
                self.left_lateral_corner_chr = "  ";         self.right_lateral_corner_chr = "  "

                # Header Section  Only for Matrix List
                self.left_vertical_header_line_chr   = "  "
                self.right_vertical_header_line_chr  = "  "
                self.middle_vertical_header_line_chr = "  "

                # Under Line Header Section  Only for Matrix List
                self.horizontal_line_under_header_chr   = " ";      self.left_corner_line_under_header_chr   = "  "
                self.right_corner_line_under_header_chr = "  ";      self.middle_corner_line_under_header_chr = "  "


            elif style.lower() == Line_Style.NO_SPACE_COL_COLOR:
                # Horizontal Line Section
                self.top_horizontal_line_chr = " ";             self.bottom_horizontal_line_chr = " ";        self.middle_horizontal_line_chr = " "

                # Vertical Line Section
                self.left_vertical_line_chr  = "  ";             self.middle_vertical_line_chr = "";           self.right_vertical_line_chr = "  "

                # Outside Corner Section
                self.top_left_corner_chr     = "  ";             self.top_right_corner_chr   = "  "
                self.bottom_right_corner_chr = "  ";             self.bottom_left_corner_chr = "  "

                # Middle Corner Section
                self.middle_top_corner_chr   = "";               self.middle_bottom_corner_chr = ""
                self.left_lateral_corner_chr  = "  "
                self.middle_inner_corner_chr = ""
                self.right_lateral_corner_chr = "  "

                # Header Section  Only for Matrix List
                self.left_vertical_header_line_chr   = "  "
                self.right_vertical_header_line_chr  = "  "
                self.middle_vertical_header_line_chr = ""

                self.right_corner_line_under_header_chr  = "  "
                self.left_corner_line_under_header_chr   = "  "
                self.horizontal_line_under_header_chr    = " "

                # Under Line Header Section  Only for Matrix List
                n_rows = 0; n_cols = 0

                if list_type == "incorrect_variable_type" or list_type == "empty_list":  pass

                elif list_type == "one_item_no_row":
                    n_cols = 1; n_rows = 1                  # Done  ["dato"]


                elif list_type == "one_item_one_row":
                    n_cols = 1; n_rows = 1                  # Done [["dato"]]


                elif list_type == "multiple_items_no_row":
                    n_rows = 1                              # Done ["Hello","bye","good"]
                    n_cols = sum(1 for num in data_list)

                elif list_type == "multiple_items_one_row": # Done [["Hello","bye","good"]]
                    n_rows = 1

                    for n in data_list[0]:
                        n_cols += 1

                # Done [["Hello"],["bye"],["good"]] or [["Hello","mio"],["bye"],["good","hh"]]
                elif list_type == "multiple_items_multiple_rows":
                    n_rows = len(data_list); n_cols = 0; lengths = []

                    for r in data_list:
                        lengths.append(len(r))
                    n_cols = max(lengths)

                if (n_cols == 0 or n_cols == 1):
                    self.middle_corner_line_under_header_chr = "  "

                else:
                    self.middle_corner_line_under_header_chr = ""


            elif style.lower() == Line_Style.NONE:
                # Horizontal Line Section
                self.top_horizontal_line_chr = " ";         self.bottom_horizontal_line_chr = " ";      self.middle_horizontal_line_chr = " "

                # Vertical Line Section
                self.left_vertical_line_chr  = " ";         self.middle_vertical_line_chr = " ";        self.right_vertical_line_chr = " "

                # Outside Corner Section
                self.top_left_corner_chr     = " ";         self.top_right_corner_chr   = " "
                self.bottom_right_corner_chr = " ";         self.bottom_left_corner_chr = " "

                # Middle Corner Section
                self.middle_top_corner_chr   = " ";         self.middle_bottom_corner_chr = " ";         self.middle_inner_corner_chr = " "
                self.left_lateral_corner_chr = " ";         self.right_lateral_corner_chr = " "

                # Header Section  Only for Matrix List
                self.left_vertical_header_line_chr   = " "
                self.right_vertical_header_line_chr  = " "
                self.middle_vertical_header_line_chr = " "

                # Under Line Header Section  Only for Matrix List
                self.horizontal_line_under_header_chr   = " ";      self.left_corner_line_under_header_chr   = " "
                self.right_corner_line_under_header_chr = " ";      self.middle_corner_line_under_header_chr = " "

            else: pass


        #---------------------------------------------------------------------------------------------------------------------------------------------
        # Checking the list_type                                                                                                                     -
        #---------------------------------------------------------------------------------------------------------------------------------------------
        if list_type == "empty_list":                   # []
            data_list.append(" ")
            _print_single_element(self,data_list)


        #---------------------------------------------------------------------------------------------------------------------------------------------
        elif list_type == "one_item_no_row":              # ["one"]
            my_list = [str(data_list[0])]
            _print_single_element(self,my_list)

            if self.update_list == True and (isinstance (data, list)):     #  updte the list
                data_list[0] = str(data_list[0][0])

        #---------------------------------------------------------------------------------------------------------------------------------------------
        elif list_type == "one_item_one_row":             # [["one"]]
            my_list = [str(data_list[0][0])]
            _print_single_element(self,my_list)

            if self.update_list == True and (isinstance (data, list)):     #  updte the list
                data_list[0] = str(data_list[0][0])

        #---------------------------------------------------------------------------------------------------------------------------------------------
        elif list_type == "multiple_items_one_row":       # [[1,2,3,4]]
            # we need to convert from one row many cols to many cols and no row
            # also convert the elements in my_list to string. all of them
            for row in data_list:
                for n in row:
                    my_list.append(str(n))

            _print_multiple_horizontal_items(self,my_list)

            # if we want to save the new list to into the old one as string
            if self.update_list == True and (isinstance (data, list)):
                data_list.clear()
                for n in my_list:
                    data_list.append(n)

        #---------------------------------------------------------------------------------------------------------------------------------------------
        elif list_type == "multiple_items_no_row":        # [1,2,3,4]
            # also convert the elements in my_list to string. all of them
            for n in (data_list):
                my_list.append(str(n))

            _print_multiple_horizontal_items(self,my_list)

            # if we want to save the new list to into the old one as string
            if self.update_list == True and (isinstance (data, list)):
                data_list.clear()
                for n in my_list:
                    data_list.append(n)

        #---------------------------------------------------------------------------------------------------------------------------------------------
        elif list_type == "mix_items":                    # [10,[50],[250],["H"],100]
                                                          # "C",["H","K","P","o"]]
           # also convert the elements in my_list to string. all of them
            for n in (data_list):
                my_list.append(str(n))

            _print_multiple_horizontal_items(self,my_list)

            # if we want to save the new list to into the old one as string
            if self.update_list == True and (isinstance (data, list)):
                data_list.clear()
                for n in my_list:
                    data_list.append(n)

        #---------------------------------------------------------------------------------------------------------------------------------------------
        elif list_type == "multiple_items_multiple_rows":  # [[7,6],[5,4],[1,2,3]] or [[2],[3],[5]]
            # converting the data_list to string any single element into my_list
            # save the new matrix my_list and now we need to complete the matrix if necessary
            tempo_list1 = []; tempo_list2 = []
            for row in data_list:
                for col in row:
                    tempo_list1.append(str(col))
                tempo_list2.append(tempo_list1)
                tempo_list1 = []

            my_list = _complete_info_list(self,tempo_list2)  # make the list complete
            _print_matrix_list(self,my_list)

              # if we want to save the new list to into the old one as string
            if self.update_list == True and (isinstance (data, list)):
                data_list.clear()
                for n in my_list:
                    data_list.append(n)

        #---------------------------------------------------------------------------------------------------------------------------------------------
        else:
            print(list_type+": ",data_list)

        if style == Line_Style.CUSTOMIZED: pass
        else:
            # putting back all the default values
            # Horizontal Line Section
            self.top_horizontal_line_chr    = thlc
            self.bottom_horizontal_line_chr = bhlc
            self.middle_horizontal_line_chr = hlc

            # Vertical Line Section
            self.left_vertical_line_chr   = lvlc
            self.middle_vertical_line_chr = mvlc
            self.right_vertical_line_chr  = rvlc

            # Corner Section
            self.top_left_corner_chr  = tlcc;          self.bottom_right_corner_chr = brcc
            self.top_right_corner_chr = trcc;          self.bottom_left_corner_chr  = blcc

            self.middle_top_corner_chr    = mtcc;      self.right_lateral_corner_chr = rlcc
            self.middle_bottom_corner_chr = mbcc;      self.left_lateral_corner_chr  = llcc
            self.middle_inner_corner_chr  = micc

            # Header Section  Only for Matrix List
            self.left_vertical_header_line_chr   = lvhlc
            self.right_vertical_header_line_chr  = rvhlc
            self.middle_vertical_header_line_chr = mvhlc

            # Under Line Header Section  Only for Matrix List
            self.horizontal_line_under_header_chr = hluhc

            # attributes for the header corners (left, middles and right)
            self.left_corner_line_under_header_chr   = lculhc
            self.right_corner_line_under_header_chr  = rculhc
            self.middle_corner_line_under_header_chr = mculhc



#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Cursor Class. Manipulate Cursor Around The Terminal                                                                                               --
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
class Cursor():
    '''
    Cursor class helps to move the cursor around the terminal
    '''
    def jumpTo(self,qty=0, direction=Move.DOWN):

        '''  Moves the cursor n position to the Direction Specified  '''

        print(Cursor.moveTo(self, qty, direction),end="")


    def moveTo(self,qty=0, direction=Move.DOWN):

        '''  Moves the cursor n position to the Direction Specified  '''

        if direction.lower() == Move.UP or direction.lower() == "u":
            if qty == 0: movement = ""
            else:        movement = f"\033[{str(qty)}A"

        elif direction.lower() == Move.DOWN  or direction.lower() == "d":
            if qty == 0: movement = ""
            else:        movement = f"\033[{str(qty)}B"

        elif direction.lower() == Move.RIGHT or direction.lower() == "r":
            if qty == 0: movement = ""
            else:        movement = f"\033[{str(qty)}C"

        elif direction.lower() == Move.LEFT or direction.lower() == "l":
            if qty == 0: movement = ""
            else:        movement = f"\033[{str(qty)}D"

        else:  movement = ""
        return movement


    def jumpxy(self,x=0,y=0):

        '''  This function moves the cursor to specific position (x,y)  '''

        print(Cursor.movexy(self, y, x),end="")


    def movexy(self,x=0, y=0):

        '''  Moves the cursor to specific position (x, y)  '''

        if (y<=-1 or x<=-1):
            posi = ""
        else:
            posi = f"\033[{str(y)};{str(x)}H"

        return posi



#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Font Style Class. Manipulate Font In The Terminal                                                                                                 --
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# ansi codes
# reset_all : "\033[0m"         Terminal_Bell : "\a"
# bold_on   : "\033[1m"         underline_on  : "\033[4m"         hidden_on    : "\033[8m"
# bold_off  : "\033[22m"        underline_off : "\033[24m"        hidden_off   : "\033[28m"
# dim_on    : "\033[2m"         blinking_on   : "\033[5m"         strike_on    : "\033[9m"
# dim_off   : "\033[22m"        blinking_off  : "\033[25m"        strike_off   : "\033[29m"
# italic_on : "\033[3m"         reverse_on    : "\033[7m"         background   : "\033[48;5;{str(bg)}m"
# italic_off: "\033[23m"        reverse_off   : "\033[27m"        foreground   : "\033[38;5;{str(fg)}m"
# backspace : "\b"              horizontal tab: "\t"              vertical tab : "\v"
class FontStyle():
    '''
    FontStyle class print fancy text
    '''
    def __init__(self):
        # General Use
        self.bg  = -1;       self.bold      = False;    self.hidden    = False;    self.italic    = False
        self.fg  = -1;       self.underline = False;    self.strike    = False;    self.inverse   = False
        self.dim = False;    self.blinking  = False

        # Print_Style
        self.align = Align.JUSTIFY;    self.bg_top_lines    = 0
        self.force_align = False;      self.bg_bottom_lines = 0

        # self.indent is used for style_on and for print_style when using justify
        self.indent    = 0

    def _set_font(self)->str:

        '''  This function changes the attributes of the font (bold=bool, bg=int, fg=int).
       
        Colors range from -1 to 256, where -1 or 256 is the defualt one.  '''


        # bg_color and fg_color, are int values but we convert then to str values
        reset = "\033[0m"
        if self.bg < 0 or self.bg > 255:  bgc = "reset"
        else:                             bgc = str(self.bg)

        if self.fg < 0 or self.fg > 255:  fgc = "reset"
        else:                             fgc = str(self.fg)


        if (bgc == "reset" and fgc == "reset"):  settings = reset
        elif bgc == "reset" and fgc != "reset":  settings = reset+"\033[38;5;"+fgc+"m"
        elif bgc != "reset" and fgc == "reset":  settings = reset+"\033[48;5;"+bgc+"m"
        elif bgc != "reset" and fgc != "reset":  settings = reset+"\033[48;5;"+bgc+";38;5;"+fgc+"m"
        else:                                    settings = reset


        if   (self.bold == True and self.dim  == False): settings = settings + "\033[1m"
        elif (self.bold == True and self.dim  == True):  settings = settings + "\033[1m"
        elif (self.bold == False and self.dim == True):  settings = settings + "\033[2m"
        else:                                            pass   # (bold == False and dim == False):


        if self.italic == True:      settings = settings + "\033[3m"
        else:                        settings =  settings + "\033[23m"

        if self.underline == True:   settings = settings + "\033[4m"
        else:                        settings = settings + "\033[24m"

        if self.blinking == True:    settings = settings + "\033[5m"
        else:                        settings = settings + "\033[25m"

        if self.inverse == True:     settings = settings + "\033[7m"
        else:                        settings = settings + "\033[27m"

        if self.hidden == True:      settings = settings + "\033[8m"
        else:                        settings = settings + "\033[28m"

        if self.strike == True:      settings = settings + "\033[9m"
        else:                        settings = settings + "\033[29m"

        return settings



    def reset_style(self):
        '''
        Reset the FontStyle class
        '''
        # General Use
        self.bg  = -1;       self.bold      = False;    self.hidden    = False;    self.italic    = False
        self.fg  = -1;       self.underline = False;    self.strike    = False;    self.inverse   = False
        self.dim = False;    self.indent    = 0;        self.blinking  = False

        # print_style
        self.align = Align.JUSTIFY;    self.bg_top_lines    = 0
        self.force_align = False;      self.bg_bottom_lines = 0



    def style_on(self)->str:
        '''
        Activate the style
        '''
        if self.indent <= 0:
            settings = self._set_font()# + f"\033[0C"
        else:                 settings = self._set_font() + f"\033[{str(self.indent)}C"
        return settings



    def style_off(self)->str:
        '''
        Deactivate the style
        '''
        return "\033[0m"



    def print_style(self, msg)->None:
        '''
        print_style will help to print a fancy statement on the terminal
        '''
        #---------------------------------------------------------------------------------------------------------------------------------
        def _print_bg_lines(move_crs, insert_sp, settings, lines):
            if lines == 0:
                pass

            else:
                n = lines
                while n>0:
                    print(f"{move_crs}{settings}{insert_sp}\033[0m")
                    n -= 1

        #---------------------------------------------------------------------------------------------------------------------------------
        def _terminal_cols_smaller_than_biggest_line():
            message_lst = msg.split()
            print(f"{settings}",end="")
            for l in range(len(message_lst)):
                for n in message_lst[l]:
                    print(f"{n}",end="")
                print(" ", end="")

            suma = 0
            for w in message_lst:
                suma += len(w) + 1

            if tncols > suma:
                diff = tncols - suma
                print(_move_right(diff, True),end="")

            else:
                done = True
                while done:
                    suma = suma - tncols
                    if suma < 0:
                        done = False

                diff = suma * (-1)
                print(_move_right(diff, True),end="")
            print(f"{reset_font()}",end="")


        #---------------------------------------------------------------------------------------------------------------------------------
        reset = "\033[0m"
        fm = FancyMessage()
        fm.left_indent = 0; fm.right_indent = 0
        tnrows, tncols, space_available, number_letter_line_list, adj_diff_space, new_msg, n_lines = fm._get_msg_attributes(msg,True)
        settings = self._set_font()

        cnt_l = 0     # counting the number of letter in the new message
        cnt_p = 0     # counting the position of the list containing the letters
        wd_line = ""  # keeps the line info
        wd_list = []  # keep the text of the lines as list

        for l in range(len(new_msg)):
            wd_line += new_msg[l]
            cnt_l += 1
            if cnt_l == number_letter_line_list[cnt_p]:
                cnt_l  = 0
                cnt_p += 1
                wd_list.append(wd_line)
                wd_line = ""

        biggets_line  = max(number_letter_line_list)
        bg_space_line = _move_right(biggets_line,option_space=True)

        if biggets_line < tncols:
            #-----------------------------------------------------------------------------------------------------------------------------------------
            if self.align.lower() == Align.CENTER or self.align.lower() == "c":
            #-----------------------------------------------------------------------------------------------------------------------------------------
                move_cursor  = _move_right(n=(int((tncols - biggets_line)/2)),option_space=False)
                _print_bg_lines(move_cursor, bg_space_line , settings,self.bg_top_lines)
                if self.force_align == True:
                    #---------------------------------------------------------------------------------------------------------------------------------
                    for l in wd_list:
                        l2 = int((biggets_line - len(l))/2)
                        r = int((biggets_line - len(l))%2)
                        print(f"{move_cursor}{settings}{_move_right(n=l2,option_space=True)}{l}{_move_right(n=l2+r,option_space=True)}{reset}")

                else:   # Center (force = False)
                    #---------------------------------------------------------------------------------------------------------------------------------
                    for l in wd_list:
                        adj = biggets_line - len(l)
                        print(f"{move_cursor}{settings}{l}{_move_right(n=adj,option_space=True)}{reset}")
                _print_bg_lines(move_cursor, bg_space_line , settings,self.bg_bottom_lines)


            #-----------------------------------------------------------------------------------------------------------------------------------------
            elif self.align.lower() == Align.RIGHT or self.align.lower() == "r":
            #-----------------------------------------------------------------------------------------------------------------------------------------
                move_cursor = _move_right(n=(int(tncols - biggets_line)), option_space=False)
                _print_bg_lines(move_cursor, bg_space_line , settings, self.bg_top_lines)
                if self.force_align == True:
                    #---------------------------------------------------------------------------------------------------------------------------------
                    for l in wd_list:
                        l2 = int(tncols - biggets_line)
                        ll = biggets_line - len(l)
                        print(f"{_move_right(n=l2,option_space=False)}{settings}{_move_right(n=ll,option_space=True)}{l}{reset}")

                else:   # Right (forced = False)
                    #---------------------------------------------------------------------------------------------------------------------------------
                    for l in wd_list:
                        l2 = int(tncols - biggets_line)
                        ll = biggets_line - len(l)
                        print(f"{_move_right(n=l2,option_space=False)}{settings}{l}{_move_right(n=ll,option_space=True)}{reset}")

                _print_bg_lines(move_cursor, bg_space_line , settings,self.bg_bottom_lines)


            #-----------------------------------------------------------------------------------------------------------------------------------------
            elif self.align.lower() == Align.LEFT or self.align.lower() == "l":
            #-----------------------------------------------------------------------------------------------------------------------------------------
                move_cursor = _move_right(n=0, option_space=False)
                _print_bg_lines(move_cursor, bg_space_line , settings, self.bg_top_lines)
                if self.force_align == True:
                    for l in wd_list:
                        ll = biggets_line - len(l)
                        print(f"{settings}{l}{_move_right(n=ll,option_space=True)}{reset}")

                else:   # Left (forced = False)
                    for l in wd_list:
                        ll = biggets_line - len(l)
                        print(f"{settings}{_move_right(n=ll,option_space=True)}{l}{reset}")

                _print_bg_lines(move_cursor, bg_space_line , settings, self.bg_bottom_lines)


            #-----------------------------------------------------------------------------------------------------------------------------------------
            elif self.align.lower() == Align.JUSTIFY or self.align.lower() == "j":
            #-----------------------------------------------------------------------------------------------------------------------------------------
                move_cursor = _move_right(n=self.indent, option_space=False)
                _print_bg_lines(move_cursor, bg_space_line , settings, self.bg_top_lines)

                if self.force_align == True:
                    for l in wd_list:
                        ll = biggets_line - len(l)
                        print(f"{_move_right(n=self.indent,option_space=False)}{settings}{l}{_move_right(n=ll,option_space=True)}{reset}")

                else:   # Justify (forced = False)
                    for l in wd_list:
                        ll = biggets_line - len(l)
                        print(f"{_move_right(n=self.indent,option_space=False)}{settings}{_move_right(n=ll,option_space=True)}{l}{reset}")

                _print_bg_lines(move_cursor, bg_space_line , settings, self.bg_bottom_lines)

            #-----------------------------------------------------------------------------------------------------------------------------------------
            else:
            #-----------------------------------------------------------------------------------------------------------------------------------------
                carry = 0
                if self.force_align == True:
                    for l in range(len(number_letter_line_list)):
                        print(f"{_move_right(self.indent,False)}{settings}",end="")
                        for n in range(number_letter_line_list[l]):
                            print(f"{new_msg[n+carry]}",end="")
                        carry += number_letter_line_list[l]
                        print(reset)
                else:
                    bg_space_line = _move_right(tncols,option_space=True)
                    move_cursor = ""
                    _print_bg_lines(move_cursor, bg_space_line , settings, self.bg_bottom_lines)
                    _terminal_cols_smaller_than_biggest_line()
                    _print_bg_lines(move_cursor, bg_space_line , settings, self.bg_bottom_lines)

        else:
            # It will come in only if the condition is = if biggets_line < tncols:
            bg_space_line = _move_right(tncols,option_space=True)
            move_cursor = ""
            _print_bg_lines(move_cursor, bg_space_line , settings, self.bg_bottom_lines)
            _terminal_cols_smaller_than_biggest_line()
            _print_bg_lines(move_cursor, bg_space_line , settings, self.bg_bottom_lines)




#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Fancy Message Class (Single line or a Paragraph Text in the Terminal)                                                                             --
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
class FancyMessage(Cursor):
    '''
    FancyMessage class
    '''
    def __init__(self):
        super().__init__()       # Super Class to use all (vars and funs) from Cursor Class
                                    # with the Initialization Draw Class(self), ex. self.gotoxy(x,y)
        self.bg_body        = 4;          self.underline_body = False     # 4         False
        self.fg_body        = 231;        self.blinking_body  = False     # 231       False
        self.bold_body      = False;      self.inverse_body   = False     # False     False
        self.dim_body       = False;      self.hidden_body    = False     # False     False
        self.italic_body    = False;      self.strike_body    = False     # False     False

        self.msg_body = "Body Msg";       self.help_lines = False

        self.left_indent = 2;             self.right_indent = 2
        self.top_lines = 1;               self.bottom_lines = 1

        self.length = Length_bg.ALL_ROW
        # These two options don't do anything when length = Length_bg.All_ROW
        self.adj_bg_lines_to_right_indent = False     # True or False
        self.adj_bg_msg_to_space_available = False    # True or False



        #--------------------------------------------------------------------
        # Note Settings Here, print_fancy_note
        self.msg_note = " Note: "
        self.align_note = Align.JUSTIFY;    self.position_note = 1
        self.bg_note = 231;                 self.fg_note = 0;                 self.bold_note  = False
        self.dim_note = False;              self.italic_note = False;         self.underline_note = False
        self.blinking_note = False;         self.inverse_note = False;        self.hidden_note = False
        self.strike_note = False;           self.left_space_note = 2;         self.right_space_note = 2

        # Title Settings Here, print_fancy_message
        self.align_title = Align.LEFT;      self.title_indent = 2;            self.msg_title = "" # title_indent works with Align.JUSTIFY
        self.lines_title_body = 1;          self.strike_title = False
        self.bg_title = 4;                  self.fg_title = 231;              self.bold_title  = False
        self.dim_title = False;             self.italic_title = False;        self.underline_title = False
        self.blinking_title = False;        self.inverse_title = False;       self.hidden_title = False

        # Footnote Settings Here, print_fancy_message
        self.align_footnote = Align.RIGHT;  self.footnote_indent = 2;         self.msg_footnote = "" # footnote_indent works with Align.JUSTIFY
        self.lines_body_footnote = 1;       self.strike_footnote = False
        self.bg_footnote = 4;               self.fg_footnote = 231;           self.bold_footnote  = False
        self.dim_footnote = False;          self.italic_footnote = False;     self.underline_footnote = False
        self.blinking_footnote = False;     self.inverse_footnote = False;    self.hidden_footnote = False


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Get Message Attributes                                                                                                                         -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def _get_msg_attributes(self,data:str="Message",all_attribute:bool=False):
        msg = str(data)
        tncols, tnrows = os.get_terminal_size()

        space_available = tncols - self.left_indent - self.right_indent

        longest_line   = 0;                       quotient = 0
        letter_counter = 0;                       residue  = 0
        msg_type       = "single_line";           new_msg  = ""


        quotient_number_letter_line_list = [];    fit_number_letter_line_list   = []
        residue_number_letter_line_list  = [];    carry_number_letter_line_list = []

        adj_diff_space     = [];                  number_letter_line_list = []
        result_multi_lines = []


        for l in msg:
            if l=="\n":
                number_letter_line_list.append(letter_counter)
                letter_counter = 0
                msg_type="multiple_lines"

            else:
                new_msg += l
                letter_counter += 1


        if msg_type == "single_line":
            quotient = int(letter_counter/space_available)
            residue  = letter_counter%space_available
            while quotient>0:
                number_letter_line_list.append(space_available)
                quotient -= 1
            number_letter_line_list.append(residue)

            for n in number_letter_line_list:
                adj_diff_space.append(space_available - n)


        else:   # multiple lines
            number_letter_line_list.append(letter_counter) # the last one not added
            longest_line = max(number_letter_line_list)
            # first item when only enter it's deleted
            if number_letter_line_list[0] == 0:  number_letter_line_list.pop(0)
            # last item when only enter it's deleted
            if number_letter_line_list[(len(number_letter_line_list))-1] == 0:
                number_letter_line_list.pop((len(number_letter_line_list))-1)

            if space_available > longest_line:
                for n in number_letter_line_list:
                    adj_diff_space.append(space_available-n)

            else:
                for line in range(len(number_letter_line_list)):
                    if number_letter_line_list[line] <= space_available:
                        fit_number_letter_line_list.append(number_letter_line_list[line])

                    else:
                        quotient = int(number_letter_line_list[line]/space_available)
                        residue  = number_letter_line_list[line]%space_available
                        n = quotient

                        while n > 0:
                            quotient_number_letter_line_list.append(space_available)
                            n -= 1

                        residue_number_letter_line_list.append(residue)
                        carry_number_letter_line_list.append(quotient+1)

                ctrl = 0
                for r in number_letter_line_list:
                    if r > space_available:
                        last_one = carry_number_letter_line_list[ctrl] - 1

                        for n in range(carry_number_letter_line_list[ctrl]):
                            if last_one == n:
                                result_multi_lines.append(residue_number_letter_line_list[ctrl])
                                ctrl += 1
                            else:
                                result_multi_lines.append(space_available)
                    else:
                        result_multi_lines.append(r)


                number_letter_line_list = result_multi_lines

                for n in number_letter_line_list:
                    adj_diff_space.append(space_available - n)

        if all_attribute == True:
            return tnrows, tncols, space_available, number_letter_line_list, adj_diff_space, new_msg, len(number_letter_line_list)

        else:
            return len(number_letter_line_list), space_available, tncols


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Send the Data To the Terminal                                                                                                                  -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def _send_msg_terminal(self,data="Message"):
        def _print_bg_lines(lines, bg_format_line_color="\033[0m"):
            if lines == 0:
                print("\033[0m",end="")
            else:
                n = lines
                while n>0:
                    print(bg_format_line_color)
                    n -= 1

        tnrows, tncols, space_available, number_letter_line_list, adj_diff_space, new_msg, n_lines = FancyMessage._get_msg_attributes(self,data,True)

        color = set_font(self.bold_body, self.bg_body, self.fg_body, self.italic_body, self.underline_body, self.strike_body,
                         self.blinking_body, self.dim_body, self.hidden_body, self.inverse_body)
        color2= set_font(bg=self.bg_body, fg=self.fg_body, inverse=self.inverse_body)

        # from here we need: tncols, space_available, number_letter_line_list, adj_diff_space, new_msg
        longest_line = max(number_letter_line_list)

        # self.adj_bg_lines_to_right_indent by default  = False
        # self.adj_bg_msg_to_space_available by default = False

        if self.length == Length_bg.ALL_ROW:
            bg_format_line_color = f"{color2}{ins_chr(tncols)}{reset_font()}"
            # change color for color2 to delete at the beginning the strike, and/or underline option(s)
            start_line = f"{color2}{ins_chr(self.left_indent)}"

        elif self.length == Length_bg.ONLY_WORD:
            if self.adj_bg_lines_to_right_indent == True:
                bg_format_line_color = f"{color2}{_move_right(self.left_indent)}{ins_chr(space_available)}{reset_font()}"  # change color for color2

            else:  # elif (self.adj_bg_lines_to_right_indent == False):
                bg_format_line_color = f"{_move_right(self.left_indent)}{color2}{ins_chr(longest_line)}{reset_font()}"     # change color for color2

            start_line = f"{_move_right(self.left_indent)}{color2}"                                                        # change color for color2

        else: pass

        carry = 0; last_one = n_lines - 1
        _print_bg_lines(self.top_lines, bg_format_line_color)       # bg_line

        print(start_line,end="")

        # start printing the message
        for nl in range(n_lines):
            for n in range(number_letter_line_list[nl]):
                print(f"{color}{new_msg[carry+n]}",end="")          # added color because the color2 can be slightly different

            carry += number_letter_line_list[nl]

            if self.length == Length_bg.ALL_ROW:
                for n in range(adj_diff_space[nl]+self.right_indent):
                    print(color2+" ",end="")                        # to delete at the end the strike, and/or underline option(s)

            elif self.length == Length_bg.ONLY_WORD:
                if self.adj_bg_msg_to_space_available == True:
                    for n in range(space_available -  number_letter_line_list[nl]):
                        print(color2+" ",end="")                    # to delete the strike we add color2
                else:                                               # elif (self.adj_bg_msg_to_space_available == False):
                    for n in range(longest_line-number_letter_line_list[nl]):
                        print(color2+" ",end="")

                print(f"{reset_font()}",end="")

            else:  pass

            print()
            if last_one == nl: pass
            else:                print(start_line,end="")

        # end printing the message
        _print_bg_lines(self.bottom_lines, bg_format_line_color)    # bg_line


    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Print Fancy Note                                                                                                                                 -
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def print_fancy_note(self, msg_body:str="")->None:

        '''  It prints the fancy note with the attributes defined  '''

        if msg_body == "":  msg_body = self.msg_body

        # save original values
        li_obj = self.left_indent

        # settings for the msg_body
        if self.msg_note == "":  len_msg_note = 0
        else:                      len_msg_note = len(self.msg_note)

        self.left_indent = self.left_space_note + len_msg_note + self.right_space_note
        n_lines, space_available, tncols = self._get_msg_attributes(msg_body, False)

        total_back_lines = self.top_lines + n_lines + self.bottom_lines
        if   self.position_note >= (total_back_lines): lines_back = 0
        elif self.position_note <= 0:                  lines_back = total_back_lines
        else:                                          lines_back = total_back_lines - self.position_note

        self._send_msg_terminal(msg_body)

        # settings for the note
        settings_note = set_font(bold=self.bold_note, bg=self.bg_note, fg=self.fg_note, italic=self.italic_note,\
                                 underline=self.underline_note, strike=self.strike_note, blinking=self.blinking_note,\
                                 dim=self.dim_note, hidden=self.hidden_note, inverse=self.inverse_note)

        if self.align_note == Align.LEFT or self.align_note == "l":
            print(f"{self.moveTo(qty=lines_back, direction=Move.UP)}{settings_note}{self.msg_note}",end="")

        elif self.align_note == Align.CENTER or self.align_note == "c":
            myq = int((self.left_space_note+self.right_space_note)/2)
            print(f"{self.moveTo(qty=lines_back, direction=Move.UP)}{self.moveTo(myq, Move.RIGHT)}{settings_note}{self.msg_note}",end="")

        elif self.align_note == Align.RIGHT or self.align_note == "r":
            myq = self.left_space_note + self.right_space_note
            print(f"{self.moveTo(lines_back, Move.UP)}{self.moveTo(myq, Move.RIGHT)}{settings_note}{self.msg_note}",end="")

        else:  # JUSTIFY
            print(f"{self.moveTo(lines_back, Move.UP)}{self.moveTo(self.left_space_note, Move.RIGHT)}{settings_note}{self.msg_note}")

        self.jumpTo(qty=lines_back-1, direction=Move.DOWN)
        print(f"{reset_font()}",end="")

        # putting back original values
        self.left_indent = li_obj
        # n_lines, space_available, tncols are variables for reference to calculate the message
        if self.help_lines == True:
            print(f"{ins_chr(self.left_indent)}Body_Lines:{n_lines}  Space_Available:{space_available}  N.Cols: {tncols}N.Lines:{total_back_lines}")


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Print Fancy Message                                                                                                                            -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def print_fancy_message(self, msg_body:str="")->None:

        '''  It prints the fancy message with the attributes defined  '''

        if msg_body == "":  msg_body = self.msg_body

        # save original values
        li_obj = self.left_indent;      bold_obj    = self.bold_body;            blinking_obj  = self.blinking_body
        tl_obj = self.top_lines;        italic_obj  = self.italic_body;          underline_ojb = self.underline_body
        bg_obj = self.bg_body;          strike_obj  = self.strike_body;          fnm_obj       = self.msg_footnote
        fg_obj = self.fg_body;          hidden_obj  = self.hidden_body;          dim_obj       = self.dim_body
        bl_obj = self.bottom_lines;     inverse_obj = self.inverse_body
        ti_obj = self.msg_title

        n_lines, space_available, tncols = self._get_msg_attributes(msg_body)  # settings for title

        #---------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------------------------------------------------------------
        if not self.msg_title == "": #!= None:
            # working with the font color
            self.bg_body     = self.bg_title;          self.underline_body = self.underline_title
            self.fg_body     = self.fg_title;          self.blinking_body  = self.blinking_title
            self.bold_body   = self.bold_title;        self.inverse_body   = self.inverse_title
            self.dim_body    = self.dim_title;         self.hidden_body    = self.hidden_title
            self.italic_body = self.italic_title;      self.strike_body    = self.strike_title

            if   self.align_title == Align.LEFT or self.align_title == "l":  pass

            elif self.align_title == Align.CENTER or self.align_title == "c":
                sp = int((space_available - len(self.msg_title))/2)
                self.msg_title = ins_chr(sp) + self.msg_title

            elif self.align_title == Align.RIGHT or self.align_title == "r":
                sp = space_available - len(self.msg_title) # 1 for not jumping line and finished
                self.msg_title = ins_chr(sp) + self.msg_title

            else:                                         # Align.JUSTIFY
                self.msg_title = ins_chr(self.title_indent) + self.msg_title

            self.bottom_lines = self.lines_title_body
            self._send_msg_terminal(self.msg_title)

            # This is necessary because when is right alignment, it jumps automatically to the next row
            if (self.align_title == Align.RIGHT and self.msg_title != ""):
                print("\033[1A",end="")
                print(f"{ins_chr(tncols)}")
                print("\033[1A",end="")

            # settings for body (we recovered left_indent, and change bottom_lines and change top_lines)
            if not self.msg_footnote == "":  self.bottom_lines = 0
            else:                            self.bottom_lines = bl_obj

            self.left_indent = li_obj
            self.bg_body     = bg_obj;          self.underline_body = underline_ojb
            self.fg_body     = fg_obj;          self.blinking_body  = blinking_obj
            self.bold_body   = bold_obj;        self.inverse_body   = inverse_obj
            self.dim_body    = dim_obj;         self.hidden_body    = hidden_obj
            self.italic_body = italic_obj;      self.strike_body    = strike_obj

            if not self.msg_title == "":  self.top_lines = 0
            else:                         self.top_lines = tl_obj

            self.fg_body = fg_obj  # returning the color for the body
            self._send_msg_terminal(msg_body)

        else:
            if not self.msg_footnote == "":   self.bottom_lines = self.lines_body_footnote
            else:                             self.bottom_lines = bl_obj

            self._send_msg_terminal(msg_body)

        #---------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------------------------------------------------------------
        if not self.msg_footnote == "":
            if   self.align_footnote == Align.LEFT or self.align_footnote == "l":  pass

            elif self.align_footnote == Align.CENTER or self.align_footnote == "c":
                sp = int((space_available - len(self.msg_footnote))/2)
                self.msg_footnote = ins_chr(sp) + self.msg_footnote

            elif self.align_footnote == Align.RIGHT or self.align_footnote == "r":
                sp = space_available - len(self.msg_footnote) # 1 for not jumping line and finished
                self.msg_footnote = ins_chr(sp) + self.msg_footnote

            else:
                self.msg_footnote = ins_chr(self.footnote_indent) + self.msg_footnote # JUSTIFY

            self.top_lines    = self.lines_body_footnote;    self.bottom_lines   = bl_obj
            self.bg_body      = self.bg_footnote;            self.underline_body = self.underline_footnote
            self.fg_body      = self.fg_footnote;            self.blinking_body  = self.blinking_footnote
            self.bold_body    = self.bold_footnote;          self.inverse_body   = self.inverse_footnote
            self.dim_body     = self.dim_footnote;           self.hidden_body    = self.hidden_footnote
            self.italic_body  = self.italic_footnote;        self.strike_body    = self.strike_footnote

            self._send_msg_terminal(self.msg_footnote)

            # This is necessary because when is right alignment, it jumps automatically to the next row
            if self.align_footnote == Align.RIGHT and self.msg_footnote != "":
                print("\033[1A",end="")
                print(f"{ins_chr(tncols)}")
                print("\033[1A",end="")

        else:  pass

        # putting back original values
        self.top_lines    = tl_obj;            self.left_indent    = li_obj            #  self.bottom_lines = bl_obj
        self.bg_body      = bg_obj;            self.underline_body = underline_ojb
        self.fg_body      = fg_obj;            self.blinking_body  = blinking_obj
        self.bold_body    = bold_obj;          self.inverse_body   = inverse_obj
        self.dim_body     = dim_obj;           self.hidden_body    = hidden_obj
        self.italic_body  = italic_obj;        self.strike_body    = strike_obj
        self.msg_footnote = fnm_obj;           self.msg_title      = ti_obj

        # n_lines, space_available, tncols are variables for reference to calculate the message
        if self.help_lines == True:
            total_lines = n_lines + self.top_lines + self.bottom_lines

            if self.msg_title != "":     total_lines += 1 + self.lines_title_body

            if self.msg_footnote != "":  total_lines += 1 + self.lines_body_footnote

            print(f"{ins_chr(self.left_indent)}Body_Lines:{n_lines}  Space_Available:{space_available}  N.Cols: {tncols}  N.Lines:{total_lines}")


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Get Message Attributes                                                                                                                         -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def get_message_attributes(self, msg_body:str="", print_attributes=True)->list:
        '''
        It returns the attributes of the message
        '''
        tnrows, tncols, space_available, number_letter_line_list, adj_diff_space, new_msg_list, n_lines =\
                                                                                                FancyMessage._get_msg_attributes(self,msg_body,True)

        if msg_body == "":  msg_body = self.msg_body

        smallest_line = min(number_letter_line_list)
        longest_line  = max(number_letter_line_list)
        words = msg_body.split()
        counter_words = len(words)
        total_characters = sum(number_letter_line_list)
        screen_size_xy = [tncols,tnrows]

        result_lst  =  [["Attributes",                    "Values"],
                        ["Screen Size_xy",                screen_size_xy],
                        ["Left Indent",                   self.left_indent],
                        ["Right Indent",                  self.right_indent],
                        ["Space Available",               space_available],
                        ["Longest Line",                  longest_line],
                        ["Smallest Line",                 smallest_line],
                        ["List Line Lengths",             number_letter_line_list],
                        ["List Line Spaces",              adj_diff_space],
                        ["Words Into a List",             "\'words\'"],
                        ["Total Number of Lines",         n_lines],
                        ["Total Number of Words",         counter_words],
                        ["Total Number of Characters",    total_characters]]


        new_msg_list = [["Position","Word"]]
        cnt = 0
        for n in words:
            new_msg_list.append([cnt, n])
            cnt += 1

        if print_attributes == True:
            tbl = FancyFormat()
            # Title
            tbl.msg_title = "  get_message_attributes(message, True)  "
            tbl.align_title = Align.LEFT
            tbl.bold_title   = True;   tbl.bg_title = 231
            tbl.italic_title = True;   tbl.fg_title = 21
               # bg colors
            tbl.bg_horizontal_line = 21
            tbl.bg_vertical_line   = 21
            tbl.bg_corner_chr      = 21

            tbl.bg_inner_corner_chr  = 21
            tbl.bg_under_line_header = 21

            tbl.bg_corner_under_line_header = 21
            tbl.bg_vertical_header_line_chr = 21

            tbl.bg_header = 90
            tbl.fg_header = 231
            tbl.bold_header = True

            tbl.bg_data = 231
            tbl.fg_data = 0
            tbl.bold_data = True

            tbl.adj_top_margin = 2
            tbl.adj_indent = 4
            tbl.adj_space  = 4

            tbl.horizontal_line_under_header_on = True
            tbl.adj_bottom_margin = 1
            tbl.print_fancy_format(data=result_lst, style=Line_Style.SPACE_COL_COLOR)
            tbl.adj_top_margin = 1
            tbl.msg_title = "  Words of The Message Into a List  "
            tbl.print_fancy_format(new_msg_list)

        return result_lst, new_msg_list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Class Draw Pictures Around The Terminal                                                                                                           --
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
class Pen(Cursor):                      # Inheritance the Cursor Class here.
    '''
    Pen class will draw lines nad squares
    '''
    def __init__(self):                  # Initializing Draw Class as self
        super().__init__()                # Super Class to use all (vars and funs) from Cursor Class
                                          # with the Initialization Draw Class(self), ex. self.gotoxy(x,y)
        # General Section
        self.adj_indent = 0               # space from the terminal to the box
        self.bold_draw_line = False
        self.bg_draw_line = -1
        self.fg_draw_line = -1
        self.refill_bg_color = False

        # Rectangle Section
        # Horizontal Line Section
        self.top_horizontal_line_chr = "-";      self.bottom_horizontal_line_chr = "-"
        # Vertical Line Section
        self.left_vertical_line_chr  = "|";      self.right_vertical_line_chr = "|"
        # Corner Section
        self.top_left_corner_chr     = "+";      self.top_right_corner_chr   = "+"
        self.bottom_right_corner_chr = "+";      self.bottom_left_corner_chr = "+"


    def draw_line(self, size=0, layout=Layout.HORIZONTAL, tail="\N{BLACK DIAMOND}", body="-", head="\N{BLACK DIAMOND}"):

        '''  It draws a line with the parameters specified

             draw_line(size=0, layout=Layout.HORIZONTAL,
             tail="\N{BLACK DIAMOND}", body="-", head="\N{BLACK DIAMOND}"  '''

        settings = set_font(self.bold_draw_line, self.bg_draw_line, self.fg_draw_line)

        if layout.lower() == "h" or layout.lower() == Layout.HORIZONTAL:
            self.jumpTo(qty = self.adj_indent, direction = Move.RIGHT)
            print(f"{settings}{tail}",end="")
            for n in range(size-2): print(body,end="")
            print(head,end="")
            reset_font()


        elif layout.lower() == "v" or layout.lower() == Layout.VERTICAL:
            self.jumpTo(qty = self.adj_indent, direction = Move.RIGHT)
            print(f"{settings}{tail}")
            for n in range(size-2): print(f"{self.moveTo(qty = self.adj_indent, direction = Move.RIGHT)}{body}")
            print(f"{self.moveTo(qty=self.adj_indent, direction=Move.RIGHT)}{head}")
            reset_font()

        else:  pass


    def draw_rectangle(self,length=3, width=3, style=Line_Style.DASH):

        '''  It draws a rectangle with the parameters specified
             draw_rectangle(self,length=3, width=3, style=Line_Style.DASH)  '''

        if length <= 2: length = 3   # length = largo, width = alto
        if width  <= 2: width  = 3

        #---------------------------------------------------------------------------------------------------------------
        # Refill bg Option For The Rectangle                                                                           -
        #---------------------------------------------------------------------------------------------------------------
        if self.refill_bg_color == True:
            square = []

            sq_in = FancyFormat()
            # General
            sq_in.adj_indent = self.adj_indent
            sq_in.adj_space  = 0

            # Data section
            sq_in.bg_data = self.bg_draw_line
            sq_in.fg_data = self.fg_draw_line
            sq_in.bg_all_cell_data   = True

            # Horizontal Line Section
            sq_in.top_horizontal_line_chr    = self.top_horizontal_line_chr
            sq_in.bottom_horizontal_line_chr = self.bottom_horizontal_line_chr
            sq_in.top_horizontal_line_on     = True
            sq_in.bottom_horizontal_line_on  = True


            sq_in.bold_horizontal_line = self.bold_draw_line           # two values False and True (0 and 1)
            sq_in.bg_horizontal_line   = self.bg_draw_line             # values -1 to 255
            sq_in.fg_horizontal_line   = self.fg_draw_line             # values -1 to 255

            # Vertical Line Section
            sq_in.bold_vertical_line = self.bold_draw_line             # two values False and True (0 and 1)
            sq_in.bg_vertical_line   = self.bg_draw_line               # values -1 to 255
            sq_in.fg_vertical_line   = self.fg_draw_line               # values -1 to 255

            sq_in.left_vertical_line_chr  = self.left_vertical_line_chr
            sq_in.right_vertical_line_chr = self.right_vertical_line_chr

            # Corner Section
            sq_in.top_left_corner_chr     = self.top_left_corner_chr
            sq_in.top_right_corner_chr    = self.top_right_corner_chr
            sq_in.bottom_right_corner_chr = self.bottom_right_corner_chr
            sq_in.bottom_left_corner_chr  = self.bottom_left_corner_chr
            sq_in.bold_corner_chr = self.bold_draw_line       # two values False and True (0 and 1)
            sq_in.bg_corner_chr   = self.bg_draw_line         # values -1 to 255
            sq_in.fg_corner_chr   = self.fg_draw_line         # values -1 to 255

            # Line Under Header and Header Section
            sq_in.bg_header = self.bg_draw_line
            sq_in.fg_header = self.fg_draw_line

            sq_in.horizontal_line_under_header_on = False

            sq_in.bg_all_cell_header = True

            sq_in.bg_vertical_header_line_chr = self.bg_draw_line
            sq_in.fg_vertical_header_line_chr = self.fg_draw_line

            for n in range(width-2):
                square.append([ins_chr(length-2)])

            sq_in.print_fancy_format(square, style)

        #---------------------------------------------------------------------------------------------------------------
        # NO Refill bg Option For The Rectangle                                                                        -
        #---------------------------------------------------------------------------------------------------------------
        else:
            def _print_horiz_sq_line(settings, indent, size, tail, body, head):
                self.jumpTo(qty = indent, direction = Move.RIGHT)
                print(f"{settings}{tail}",end="")
                for n in range(size-2): print(body,end="")
                print(head)
                reset_font()

            def _print_vert_sq_line(settings, indent, size, tail, body, head):
                self.jumpTo(qty = indent, direction = Move.RIGHT)
                print(f"{settings}{tail}")
                for n in range(size-2): print(f"{self.moveTo(qty = indent, direction = Move.RIGHT)}{body}")
                print(f"{self.moveTo(qty=indent, direction=Move.RIGHT)}{head}")
                reset_font()


            if style.lower() == Line_Style.CUSTOMIZED: pass
            else:                                      # Backup all the default values
                # Horizontal Line Section
                thlc = self.top_horizontal_line_chr;    bhlc = self.bottom_horizontal_line_chr

                # Vertical Line Section
                lvlc = self.left_vertical_line_chr;     rvlc = self.right_vertical_line_chr

                # Corner Section
                tlcc = self.top_left_corner_chr;        trcc = self.top_right_corner_chr
                brcc = self.bottom_right_corner_chr;    blcc = self.bottom_left_corner_chr

                #---------------------------------------------------------------------------------------------------------------
                # start drwaing the rectangle                                                                                  -
                #---------------------------------------------------------------------------------------------------------------
                if style.lower() == Line_Style.SINGLE:

                    # Horizontal Line Section
                    self.top_horizontal_line_chr = "\u2500";      self.bottom_horizontal_line_chr="\u2500"

                    # Vertical Line Section
                    self.left_vertical_line_chr  = "\u2502";      self.right_vertical_line_chr = "\u2502"

                    # Outside Corner Section
                    self.top_left_corner_chr = "\u250C";          self.top_right_corner_chr = "\u2510"
                    self.bottom_right_corner_chr="\u2518";        self.bottom_left_corner_chr="\u2514"


                elif style.lower() == Line_Style.SINGLE_BOLD:

                    # Horizontal Line Section
                    self.top_horizontal_line_chr = "\u2501";      self.bottom_horizontal_line_chr="\u2501"

                    # Vertical Line Section
                    self.left_vertical_line_chr  = "\u2503";      self.right_vertical_line_chr = "\u2503"

                    # Outside Corner Section
                    self.top_left_corner_chr = "\u250F";          self.top_right_corner_chr = "\u2513"
                    self.bottom_right_corner_chr="\u251B";        self.bottom_left_corner_chr="\u2517"


                elif style.lower() == Line_Style.SINGLE_HEAVY:
                    # Horizontal Line Section
                    self.top_horizontal_line_chr = "\u2586";      self.bottom_horizontal_line_chr="\u2586"

                    # Vertical Line Section
                    self.left_vertical_line_chr  = "\u2588";      self.right_vertical_line_chr = "\u2588"

                    # Outside Corner Section
                    self.top_left_corner_chr = "\u2586";          self.top_right_corner_chr = "\u2586"
                    self.bottom_right_corner_chr="\u2588";        self.bottom_left_corner_chr="\u2588"


                elif style.lower() == Line_Style.DOUBLE:
                    # Horizontal Line Section
                    self.top_horizontal_line_chr = "\u2550";      self.bottom_horizontal_line_chr="\u2550"

                    # Vertical Line Section
                    self.left_vertical_line_chr  = "\u2551";      self.right_vertical_line_chr = "\u2551"

                    # Outside Corner Section
                    self.top_left_corner_chr = "\u2554";          self.top_right_corner_chr = "\u2557"
                    self.bottom_right_corner_chr="\u255D";        self.bottom_left_corner_chr="\u255A"


                elif style.lower() == Line_Style.SQ_BRACKETS:
                    # Horizontal Line Section
                    self.top_horizontal_line_chr = " ";           self.bottom_horizontal_line_chr=" "

                    # Vertical Line Section
                    self.left_vertical_line_chr  = "\u2502";      self.right_vertical_line_chr = "\u2502"

                    # Outside Corner Section
                    self.top_left_corner_chr = "\u250C";          self.top_right_corner_chr = "\u2510"
                    self.bottom_right_corner_chr="\u2518";        self.bottom_left_corner_chr="\u2514"


                elif style.lower() == Line_Style.DASH:
                    # Horizontal Line Section
                    self.top_horizontal_line_chr = "\u002D";      self.bottom_horizontal_line_chr="\u002D"

                    # Vertical Line Section
                    self.left_vertical_line_chr  = "\u254E";      self.right_vertical_line_chr = "\u254E"

                    # Outside Corner Section
                    self.top_left_corner_chr = "\u002B";          self.top_right_corner_chr = "\u002B"
                    self.bottom_right_corner_chr="\u002B";        self.bottom_left_corner_chr="\u002B"


                elif style.lower() == Line_Style.NONE:
                    # Horizontal Line Section
                    self.top_horizontal_line_chr = " ";           self.bottom_horizontal_line_chr=" "

                    # Vertical Line Section
                    self.left_vertical_line_chr  = " ";           self.right_vertical_line_chr = " "

                    # Outside Corner Section
                    self.top_left_corner_chr = " ";               self.top_right_corner_chr = " "
                    self.bottom_right_corner_chr=" ";             self.bottom_left_corner_chr=" "

                else: pass
            #-------------------------------------------------------------------------------------------------------------------
            # def draw_rectangle(self,length=3, width=3, style=Line_Style.DASH):
            # def set_font(bold=False,bg=-1,fg=-1,italic=False,underline=False,strike=False,blinking=False,dim=False,hidden=False,inverse=False):
            settings = set_font(self.bold_draw_line, self.bg_draw_line, self.fg_draw_line)

            # top horizontal line
            tail = self.top_left_corner_chr
            body = self.top_horizontal_line_chr
            head = self.top_right_corner_chr
            _print_horiz_sq_line(settings, self.adj_indent, length, tail, body, head)


            # left vertical line
            self.jumpTo(qty=1, direction=Move.UP)
            tail = self.top_left_corner_chr
            body = self.left_vertical_line_chr
            head = self.bottom_left_corner_chr
            _print_vert_sq_line(settings, self.adj_indent, width, tail, body, head)


            # bottom horizontal line
            self.jumpTo(qty=1, direction=Move.UP)
            tail = self.bottom_left_corner_chr
            body = self.bottom_horizontal_line_chr
            head = self.bottom_right_corner_chr
            _print_horiz_sq_line(settings, self.adj_indent, length, tail, body, head)


            # right vertical line
            self.jumpTo(qty=width,  direction=Move.UP)
            tail = self.top_right_corner_chr
            body = self.right_vertical_line_chr
            head = self.bottom_right_corner_chr
            _print_vert_sq_line(settings, (length+self.adj_indent-1), width, tail, body, head)


            if style == Line_Style.CUSTOMIZED: pass
            else:
                # putting back all the default values
                # Horizontal Line Section
                self.top_horizontal_line_chr = thlc;    self.bottom_horizontal_line_chr = bhlc

                # Vertical Line Section
                self.left_vertical_line_chr = lvlc;     self.right_vertical_line_chr = rvlc

                # Corner Section
                self.top_left_corner_chr = tlcc;        self.top_right_corner_chr = trcc
                self.bottom_right_corner_chr = brcc;    self.bottom_left_corner_chr = blcc
            #---------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Class PyLO. Operation With List Personal                                                                                                          --
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
class PyLO():
    '''
    PyLO class helps to make some quit operations with list in python
    '''
    class Str_List_Option(enum.StrEnum):
        '''  How the string is converted to list  '''
        WORD_BY_WORD = "word_by_word"
        LINE_BY_LINE = "line_by_line"


    class Fill_Type(enum.StrEnum):
        '''  How to fill the empty cells when we are trying to sort a list  '''
        STRING = "string"
        NUMBER = "number"


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Conversion to List                                                                                                                             -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def _bifc_to_list(self,data, convert_to_str=False):
        '''  It converts bool, int, float, and complex type to list type  '''
        tempo_list = []
        if convert_to_str == True:
            tempo_list.append(str(data))
        else:
            tempo_list.append(data)
        return tempo_list


    def bool_to_list(self,data:bool, convert_to_str=False):
        '''  It sets a bool variable into list as a bool or as string type  '''
        new_list = PyLO._bifc_to_list(self, data, convert_to_str)
        return new_list


    def int_to_list(self,data:int, convert_to_str=False):
        '''  It sets a int variable into list as an integer or as string type  '''
        new_list = PyLO._bifc_to_list(self, data, convert_to_str)
        return new_list


    def float_to_list(self,data:float, convert_to_str=False):
        '''  It sets a float variable into list as a float or as string type  '''
        new_list = PyLO._bifc_to_list(self, data, convert_to_str)
        return new_list


    def complex_to_list(self,data:complex, convert_to_str=False):
        '''  It sets a complex variable into a list as a complex or as string type   '''
        new_list = PyLO._bifc_to_list(self, data, convert_to_str)
        return new_list

    #---------------------------------------------------------------------------------------------------------------------------------------------
    def str_to_list(self,data:str, option:Str_List_Option=Str_List_Option.WORD_BY_WORD, counter=False):
        '''  It sets a string variable into a list as word by word or line by line  '''
        if option == "word_by_word" and counter == False:
            tempo_list = data.split()

        elif option == "word_by_word" and counter == True:
            cnt = 0
            tempo_list = []
            tempo = data.split()
            for w in tempo:
                tempo_list.append([cnt,w])
                cnt += 1

        elif option == "line_by_line":
            cnt = -1
            line_word = ""
            tempo_list = []
            for l in data:
                if l != "\n":
                    line_word += l
                else:
                    if cnt == -1:
                        cnt = 0
                    else:
                        if counter == True:
                            tempo_list.append([cnt,line_word])
                            cnt += 1
                            line_word = ""
                        else:
                            tempo_list.append(line_word)
                            cnt += 1
                            line_word = ""
        else:
            tempo_list = []

        return tempo_list


    #---------------------------------------------------------------------------------------------------------------------------------------------
    def dict_to_list(self,data:dict, key_title="key", value_title="value", convert_to_str=False):
        '''  It sets a dictionary variable into a list with its original values or as string values   '''

        my_key_list = []; my_data_list = []

        my_key_list  = list(data.keys())
        my_data_list = list(data.values())

        complete_list = [];  tempo_list = []
        if (key_title == "key") and (value_title == "value"):
            if (len(my_key_list)) > 1:   complete_list.append(["Keys","Values"])
            else:                        complete_list.append(["Key","Value"])

        elif (key_title == None or value_title == None or \
                key_title.lower() == "none" or value_title.lower() == "none"):
            pass

        else:
            complete_list.append([key_title,value_title])

        for d in range(len(data)):
            if convert_to_str == True:
                tempo_list.append(str(my_key_list[d]))
                tempo_list.append(str(my_data_list[d]))
                complete_list.append(tempo_list)
                tempo_list = []
            else:
                tempo_list.append(my_key_list[d])
                tempo_list.append(my_data_list[d])
                complete_list.append(tempo_list)
                tempo_list = []

        return complete_list


    #---------------------------------------------------------------------------------------------------------------------------------------------
    def range_to_list(self, data:range, header_title = "", layout:Layout=Layout.HORIZONTAL, convert_to_str=False):
        '''  It sets a range variable into a list with its original values or as string values   '''

        tempo_list = []

        def range_to_list_get_header(layout):
            header = "Range"
            if header_title == "":
                if len(data) > 1:
                    if layout == "vertical": tempo_list.append([header + " Values"])
                    else:                    tempo_list.append(header  + " Values")

                else:
                    if layout == "vertical": tempo_list.append([header + " Value"])
                    else:                    tempo_list.append(header  + " Value")

            elif (header_title == None or header_title.lower() == "none"):
                pass
            else:
                if layout == "vertical":  tempo_list.append([header_title])
                else:                     tempo_list.append(header_title)

        #for n in data:
        if (layout.lower() == "v" or layout == Layout.VERTICAL):
            range_to_list_get_header("vertical")
            for n in data:
                if convert_to_str == False:  tempo_list.append([n])
                else:                        tempo_list.append([str(n)])

        elif (layout.lower() == "h" or layout == Layout.HORIZONTAL):
            range_to_list_get_header("horizontal")
            for n in data:
                if convert_to_str == False:  tempo_list.append(n)
                else:                        tempo_list.append(str(n))

        else: pass

        return tempo_list


    #---------------------------------------------------------------------------------------------------------------------------------------------
    # set and frozenset values are printed in aleatory order all the time
    def set_to_list(self, data:set|frozenset, header_title:str="",layout:Layout=Layout.VERTICAL, convert_to_str=False):
        '''  It sets a set or a frozenset variable into a list with its original values or as string values   '''

        tempo_list = []

        #----------------------------------------------------------------------------------
        def _set_to_list_get_header(layout):
            if isinstance(data, set):       header = "Set"
            if isinstance(data, frozenset): header = "Frozenset"

            if header_title == "":
                if len(data) > 1:
                    if layout == "vertical": tempo_list.append([header + " Values"])
                    else:                    tempo_list.append(header  + " Values")

                else:
                    if layout == "vertical": tempo_list.append([header + " Value"])
                    else:                    tempo_list.append(header  + " Value")

            elif (header_title == None or header_title.lower() == "none"):
                pass
            else:
                if layout == "vertical":  tempo_list.append([header_title])
                else:                     tempo_list.append(header_title)

        #----------------------------------------------------------------------------------
        def _set_to_list_layout_vertical():
            _set_to_list_get_header("vertical")

            for d in data:
                if convert_to_str == False:  tempo_list.append([d])
                else:                        tempo_list.append([str(d)])


        def _set_to_list_layout_horizontal():
            _set_to_list_get_header("horizontal")

            for d in data:
                if convert_to_str == False:  tempo_list.append(d)
                else:                        tempo_list.append(str(d))

        #----------------------------------------------------------------------------------
        if (layout.lower() == "v"   or layout.lower() == Layout.VERTICAL):
            _set_to_list_layout_vertical()

        elif (layout.lower() == "h" or layout.lower() == Layout.HORIZONTAL):
            _set_to_list_layout_horizontal()

        else: pass

        return tempo_list



    #---------------------------------------------------------------------------------------------------------------------------------------------
    def tuple_to_list(self, data:tuple):
        '''  This function converts a tuple into a list keeping its original values '''
        tempo_list = []
        #-----------------------------------------------------------------------------------------------
        if len(data) == 0:
            return tempo_list

        #-----------------------------------------------------------------------------------------------
        elif len(data) == 1:
                                        # string              ("")         -> Case 0   String
                                        # "empty_tuple"       ("",)        -> Case 1   Empty
            tempo_list.append(data[0])  # "one_item_no_row"   ("Apple",)   -> Case 2   Tuple
            return tempo_list           # "one_item_one_row"  (("Apple",)) -> Case 3   Tuple inside Tuple

        #-----------------------------------------------------------------------------------------------
        #elif len(data) > 1:
        else:
            type_type = []; lengths = []
            l = len(data); tuple_tuple = 0; tuple_other = 0

            for n in range(len(data)):
                if isinstance(data[n], tuple):
                    tuple_tuple = 1
                    type_type.append("tuple")
                    lengths.append(len(data[n]))

                else:
                    tuple_other = 1
                    type_type.append("other")
                    lengths.append(1)

            # This is only for tuples inside the tuple ->
            # tupleData = (("hello","hello"),("hell",),("hi","bye","good"),([1,2],))        -> Case 4
            if (tuple_tuple == 1 and tuple_other == 0):
                tempo = []
                for col in data:
                    for i in col:
                        tempo.append(i)
                        tempo_list.append(tempo)
                        tempo = []

            # This is only for other types inside a tuple
            # tupleData = ("hello","hell","hi",[1,2])                                       -> Case 5
            elif (tuple_tuple == 0 and tuple_other == 1):
                for n in data:
                    tempo_list.append(n)     # for rows (Horizontal)
                    #tempo_list.append([n])  # for cols (Vertical)


            # This is for combination tuple (tuple =1 and other = 1)                        -> Case 6
            # tupleData = (("hello","hello"),("hell",),("hi","bye","good"),[1,2], "hello")
            elif (tuple_tuple == 1 and tuple_other == 1):
                for n in range(l):
                    if (lengths[n]) > 1:
                        tempo = []
                        for i in range(lengths[n]):
                            tempo.append(data[n][i])
                        tempo_list.append(tempo)

                    else:
                        if type_type[n] == "other":
                            tempo_list.append([data[n]])
                        else:
                            tempo_list.append([data[n][0]])
            else:
                tempo_list = []

        return tempo_list


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Shift An Element Inside A List, RIGHT or LEFT                                                                                                  -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def _right_shift(self,my_list:list, qty:int=0, update:bool=False)->list:
        '''
        This function shift the elements in a list to the right.

        update is used to save the actual list with the shift elements.
        update is set to False is we wish to keep the original list and save
        the new list into another variable.
        '''
        list_type = _get_list_type(my_list)

        # list_type = incorrect_variable_type: [Not a list type variable]
        if list_type == "incorrect_variable_type":
            return my_list
        # list_type = empty_list: []
        elif list_type == "empty_list":
            return my_list

        # list_type = one_item_no_row: ["one"]
        elif list_type == "one_item_no_row":
            return my_list

        # list_type = one_item_one_row: [["one"]]
        elif list_type == "one_item_one_row":
            return my_list

        # list_type == "multiple_items_no_row"          [1,2,3,4]
        # list_type == "multiple_items_multiple_rows"   [[7,6],[5,4],[1,2,3]] or [[2],[3],[5]]
        # list_type == "mix_items"                      [10,[50],[250],["H"],100]
        elif list_type == "multiple_items_no_row" or list_type == "mix_items"\
            or list_type == "multiple_items_multiple_rows":

            result = []; result = my_list; tempo = []

            length = len(result)-1
            for rot in range(qty):
                tempo.append(result[length])
                for n in range(length):
                    tempo.append(result[n])
                result = tempo
                tempo = []

            if update == True:
                my_list.clear()
                for n in result: my_list.append(n)
                return my_list
            else:
                return result

        # list_type = multiple_items_one_row: [[1,2,3,4]]
        elif list_type == "multiple_items_one_row":
            tempo = []; result = []; result = my_list[0]; length = len(result)-1

            for rot in range(qty):
                tempo.append(result[length])
                for n in range(length):
                    tempo.append(result[n])
                result = tempo
                tempo = []

            if update == True:
                my_list.clear()
                for n in result: tempo.append(n)
                my_list.append(tempo)
                return my_list

            else:
                return [result]

        # A different case will just return the same list
        else:
            return my_list

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def _left_shift(self, my_list:list, qty=0, update:bool=False)->list:
        '''
        This function shift the elements in a list to the left.

        update is used to save the actual list with the shift elements.
        update is set to False is we wish to keep the original list and save
        the new list into another variable.'''

        list_type = _get_list_type(my_list)

        # list_type = incorrect_variable_type: [Not a list type variable]
        if list_type == "incorrect_variable_type":
            return my_list

        # list_type = empty_list: []
        elif list_type == "empty_list":
            return my_list

        # list_type = one_item_no_row: ["one"]
        elif list_type == "one_item_no_row":
            return my_list

        # list_type = one_item_one_row: [["one"]]
        elif list_type == "one_item_one_row":
            return my_list

        # list_type == "multiple_items_no_row"          [1,2,3,4]
        # list_type == "multiple_items_multiple_rows"   [[7,6],[5,4],[1,2,3]] or [[2],[3],[5]]
        # list_type == "mix_items"                      [10,[50],[250],["H"],100]
        elif list_type == "multiple_items_no_row" or list_type == "mix_items"\
            or list_type == "multiple_items_multiple_rows":

            result = []; result = my_list; tempo = []; length = len(result)-2
            for rot in range(qty):
                tempo.append(result[1])
                for n in range(length):
                    idx = n + 2
                    tempo.append(result[idx])
                tempo.append(result[0])
                result = tempo
                tempo = []
            if update == 1:
                my_list.clear()
                for n in result: my_list.append(n)
                return my_list
            else:
                return result

        # list_type = multiple_items_one_row: [[1,2,3,4]]
        elif list_type == "multiple_items_one_row":
            tempo = []; result = []; result = my_list[0]; length = len(result)-2
            for rot in range(qty):
                tempo.append(result[1])
                for n in range(length):
                    idx = n + 2
                    tempo.append(result[idx])
                tempo.append(result[0])
                result = tempo
                tempo = []

            if update == 1:
                my_list.clear()
                for n in result: tempo.append(n)
                my_list.append(tempo)
                return my_list
            else:
                return [result]

        # A different case will just return the same list
        else:
            return my_list

    def shift(self, data:list, direction=Move.RIGHT, qty=0, update:bool=False)->list:
        '''
        This function shift the elements in a list to the left or right.

        update is used to save the actual list with the shift elements.
        If we set update to False, then we keep the original list and save
        the new list into another variable.'''

        if direction == "r" or direction == Move.RIGHT:
            tempo = PyLO._right_shift(self, my_list=data, qty=qty, update=update)
        elif direction == "l" or direction == Move.LEFT:
            tempo = PyLO._left_shift(self, my_list=data,  qty=qty, update=update)
        else:
            tempo = data
        return tempo


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Swap Two Items Into A List                                                                                                                     -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def swap(self, my_list:list, pos1=0, pos2=0, update:bool=False)->list:
        '''
        This function swap two elements in a list.

        update is used to save the actual list with the swap elements.

        If update is set to False, then we keep the original list and save
        the new list into another variable.

        pos1 -> position 1 to be swap with position 2
        pos2 -> position 2 to be swap with position 1

        Note: If one of the position provided is out of range, the function
              will return the list as original and it will print a message
              out of range.'''

        if pos1 == pos2:
            return my_list

        else:
            list_type = _get_list_type(my_list)

            # list_type = incorrect_variable_type: [Not a list type variable]
            if list_type == "incorrect_variable_type":
                return my_list

            # list_type = empty_list: []
            elif list_type == "empty_list":
                return my_list

            # list_type = one_item_no_row: ["one"]
            elif list_type == "one_item_no_row":
                return my_list

            # list_type = one_item_one_row: [["one"]]
            elif list_type == "one_item_one_row":
                return my_list

            # list_type == "multiple_items_no_row"          [1,2,3,4]
            # list_type == "multiple_items_multiple_rows"   [[7,6],[5,4],[1,2,3]] or [[2],[3],[5]]
            # list_type == "mix_items"                      [10,[50],[250],["H"],100]
            elif list_type == "multiple_items_no_row" or list_type == "mix_items"\
                or list_type == "multiple_items_multiple_rows":
                result = []; length = len(my_list) - 1

                if length < pos1:
                    print(f" pos1 = {pos1} is out of range...! ")
                    return my_list
                if length < pos2:
                    print(f" pos2 = {pos2} is out of range...! ")
                    return my_list

                for n in range(len(my_list)):
                    if n == pos1:
                        result.append(my_list[pos2])
                    elif n == pos2:
                        result.append(my_list[pos1])
                    else:
                        result.append(my_list[n])

                if update == 1:
                    my_list.clear()
                    [my_list.append(n) for n in result]
                    return my_list
                else:
                    return result

            # list_type = multiple_items_one_row: [[1,2,3,4]]
            elif list_type == "multiple_items_one_row":
                result = []; length = len(my_list[0]) - 1
                if length < pos1:
                    print(f" pos1 = {pos1} is out of range...! ")
                    return my_list
                if length < pos2:
                    print(f" pos2 = {pos2} is out of range...! ")
                    return my_list

                for n in range(len(my_list[0])):
                    if n == pos1:
                        result.append(my_list[0][pos2])
                    elif n == pos2:
                        result.append(my_list[0][pos1])
                    else:
                        result.append(my_list[0][n])

                if update == 1:
                    my_list.clear()
                    [my_list.append(n) for n in result]
                    return [my_list]
                else:
                    return result

            else:
                return [my_list]

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Get Dimensions of a List                                                                                                                       -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def dimensions(self, data:list)->list[int]:
        '''
        dimensions(self, data:list=[])->list[int]

        This function return the number of rows and cols in a list.
        If the list is not square, then it will pick the longest col unless 
        otherwise specified in the length_col.
        '''
        n_rows = 0
        n_cols = 0
        n_cols_max = 0
        n_cols_min = 0
        row_col_list = []

        list_type = _get_list_type(data)

        if list_type == "incorrect_variable_type" or list_type == "empty_list":
            pass

        elif list_type == "one_item_no_row": # Done  ["dato"]
            n_rows = 1
            n_cols_max = 1
            n_cols_min = 1

        elif list_type == "one_item_one_row": # Done [["dato"]]
            n_rows = 1
            n_cols_max = 1
            n_cols_min = 1

        elif list_type == "multiple_items_no_row": # Done ["Hello","bye","good"]
            n_rows = 1
            for num in range(len(data)):
                n_cols += 1
            n_cols_max = n_cols
            n_cols_min = n_cols

        elif list_type == "multiple_items_one_row": # Done [["Hello","bye","good"]]
            n_rows = 1
            for n in data[0]:
                n_cols += 1
            n_cols_max = n_cols
            n_cols_min = n_cols

        # Done [["Hello"],["bye"],["good"]] or [["Hello","mio"],["bye"],["good","hh"]]
        elif list_type == "multiple_items_multiple_rows":
            n_rows = len(data); n_cols = 0; lengths = []

            for r in data:
                lengths.append(len(r))

            n_cols_max = max(lengths)
            n_cols_min = min(lengths)

        else:       # "mix_items"
            n_rows = 1
            n_cols_max = len(data)
            n_cols_min = len(data)

        row_col_list.append(["All_rows",n_rows])
        row_col_list.append(["max_cols",n_cols_max])
        row_col_list.append(["min_cols",n_cols_min])

        return row_col_list


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Autofill Data. It Completes Data List to Make   it Rectangular List (Rows, Cols)                                                               -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def autofill_data(self, data:list, fill_value:str="----", update:bool=False)->list:
        '''
        autofill_data(list, str/int/float, boolean)

        This function will fill all the empty columns from the list.
        fill_value is the chr to be used to fill those columns. It can be str,
        int, float, or bool. By default it's a str type (----). '''

        list_type = _get_list_type(data)
        if list_type == "multiple_items_multiple_rows":

            n_rows_n_cols_list = PyLO.dimensions(self, data)
            n_rows = n_rows_n_cols_list[0][1]
            n_cols = n_rows_n_cols_list[1][1]

            tempo = []; matrix_update = []

            for row in range(n_rows):
                for col in range(n_cols):
                    try:
                        tempo.append(data[row][col])
                    except:
                        tempo.append(fill_value)

                matrix_update.append(tempo)
                tempo = []

            if update == True:
                data.clear()
                [data.append(n) for n in matrix_update]
            return matrix_update

        else:
            return data


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Transpose List (Converting The Rows Into Cols AND Cols Into Rows)                                                                              -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def transpose(self, data:list, autofill=True, fill_value="----", update:bool=False)->list:
        '''
        transpose(data:list, autofill:bool, fill_value:int|float|str, update:bool)

        update is used to replace original list with the transpose list.
        update is set to False to keep the original list and save
        the new list into another variable.

        When the list is not square or rectangular, the list will be filled using
        the fill_value. If the autofill is set to False, some data will be lost. '''

        transpose_list = []
        list_type = _get_list_type(data)
        print(list_type)

        if list_type == "incorrect_variable_type":  # [Not a List]  Done...! Case 0
            pass #return "incorrect variable type"

        elif list_type == "empty_list":             # []  Done...! Case 1
            pass #return "empty list"

        elif list_type == "multiple_items_one_row": # input: [[10,20,30]] output: [10,20,30] Done...! Case 5
            for row in data:
                for col in row:
                    transpose_list.append(col)
            #return transpose_list

        elif list_type == "one_item_one_row":       # input: [[10]] output: [10] Done...! Case 4
            transpose_list.append(data[0][0])
            #return transpose_list

        elif list_type == "one_item_no_row":        # input :[10]  output: [[10]] Done...! Case 2
            transpose_list = [[data[0]]]
            #return transpose_list

        elif list_type == "multiple_items_no_row":  # input: [10,20,30] output: [[10],[20],[30]] Done...! Case 3
            for col in range(len(data)):
                transpose_list.append([data[col]])
            #return transpose_list

        elif list_type == "mix_items":
            for n in data:
                transpose_list.append([n])
                #return transpose_list                # input: [5,[50],45] or [5,[50,40],45] or [[5],6,40,[45]] Case 9

        else:   # input: [[1],[2],[3]] output: [[1,2,3]] Done...! Case 6
                # input: [[1,2,3],[4,5,6],[7,8,9]] output: [[1,4,7],[2,5,8],[3,6,9]] Done...!  Case 7
                # input: [[1,2,3],[4,5,6,6],[7,8,9,9]] output: [[1,4,7],[2,5,8],[3,6,9]] Done...! Case 8
                # input: [[1,2,3],[4,5],[7,8,9]] output: Error_data_dimension Done...! Case 9
                # note: the element 0 needs to be greater than the rest.

            #--------------------------------------------------------------
            if autofill == True:
                fill_list = PyLO.autofill_data(self, data=data, fill_value=fill_value)
            else:
                fill_list = data
            #--------------------------------------------------------------

            lengths = []
            for l in fill_list:           # finding the smallest
                lengths.append(len(l))

            smaller = min(lengths)

            for item in fill_list:
                if len(item) != smaller:
                    break

            for i in range(smaller):
                row =[]
                for item in fill_list:
                    # appending to new list with values and index positions
                    # i contains index position and item contains values
                    row.append(item[i])
                transpose_list.append(row)

        if update == False:
            pass
        else:
            data.clear()
            for n in transpose_list:
                data.append(n)

        return transpose_list


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Convert a List From Any Type to String                                                                                                         -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def num_to_str(self, data:list, update=False)->list:

        '''  Converts elements of a list type to string type  '''
        new_list = []
        for value in data:
            if isinstance(value, list):
                new_list.append(PyLO.num_to_str(self, value))
            else:
                new_list.append(str(value))


        if update == True:
            data.clear()
            for n in new_list: data.append(n)

        return new_list


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Convert a List From String to Number                                                                                                           -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def str_to_num(self, data:list, fill_value=0, update=False)->list:

        '''  Converts all items into the list to number type  '''

        def convert_to_number(value, alternative):
            new_value = 0
            try:
                new_value = int(value)                # the number is integer or a string integer
            except:
                try:
                    new_value = float(value)          # the number is float or a string float
                except:
                    try:
                        new_value = complex(value)    # the number is complex or a string complex
                    except:
                        new_value = alternative
            return new_value


        new_refill = convert_to_number(fill_value, 0)

        new_list = []
        for value in data:
            if isinstance(value, list):
                new_list.append(PyLO.str_to_num(self, value, new_refill))
            else:
                new_list.append(convert_to_number(value, new_refill))


        if update == True:
            data.clear()
            for n in new_list: data.append(n)

        return new_list


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Sort a List by Column                                                                                                                          -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def sort_by_col(self, data:list, ref_col=0, fill_value="----", fill_type:Fill_Type=Fill_Type.STRING, reverse_order:bool=False, update:bool=False)->list:

        '''  Sort a list by col. It won't sort the first row because it is consider the Header of the list '''

        def _get_order_only_horizontal(in_list):
            tempo_list = []
            #print("starting: ", in_list)
            if fill_type.lower()   == "string":  [tempo_list.append(str(n)) for n in in_list]
            elif fill_type.lower() == "number":  tempo_list = PyLO.str_to_num(self, data=in_list, fill_value=fill_value, update=False)
            else:                           [tempo_list.append(str(n)) for n in in_list]

            sorted_list = sorted(tempo_list)
            if reverse_order == False:
                pass
            elif reverse_order == True:
                list.reverse(sorted_list)
            #print("result: ",sorted_list)
            return sorted_list

        list_type = _get_list_type(data)

        if list_type == "incorrect_variable_type":
            return []

        elif list_type == "empty_list":
            return []

        elif list_type == "one_item_no_row": # Done  ["dato"]
            return data

        elif list_type == "one_item_one_row": # Done [["dato"]]
            return data

        elif list_type == "multiple_items_no_row": # multiple_items_no_row -> ["Hello","bye","good"]
            sorted_list = _get_order_only_horizontal(data)

            if update == True:
                data.clear()
                [data.append(n) for n in sorted_list]
            return sorted_list

        elif list_type == "multiple_items_one_row": # Done [["Hello","bye","good"]]
            tempo = []
            [tempo.append(n) for n in data[0]]
            sorted_list = _get_order_only_horizontal(tempo)

            if update == True:
                data.clear()
                [data.append(n) for n in sorted_list]

            return [sorted_list]

            # Done [["Hello"],["bye"],["good"]] or [["Hello","mio"],["bye"],["good","hh"]]
        elif list_type == "multiple_items_multiple_rows":
            complete_list = PyLO.autofill_data(self, data=data, fill_value=fill_value, update=False)
            n_rows_n_cols_list = PyLO.dimensions(self, complete_list)
            n_rows = n_rows_n_cols_list[0][1]
            n_cols = n_rows_n_cols_list[1][1]

            if ref_col >= n_cols:
                print()
                print(" ref_col out of range...! ")
                print()
                return data

            else:
                if fill_type == "string":
                    new_list = PyLO.num_to_str(self, data=complete_list, update=False)
                    sorted_list = [new_list[0]] + sorted(new_list[1:], key=lambda x: x[ref_col])
                    if reverse_order == False:
                        pass
                    else:
                        header_row = sorted_list.pop(0)
                        list.reverse(sorted_list)
                        sorted_list.insert(0,header_row)

                    #sorted_list = [my_list[0]] + sorted(complete_list[1:], key=lambda x: str(x[ref_col]))
                elif fill_type == "number":
                    header_row = complete_list.pop(0)
                    new_list = PyLO.str_to_num(self, data=complete_list, update=False)
                    new_list.insert(0,header_row)
                    sorted_list = [new_list[0]] + sorted(new_list[1:], key=lambda x: x[ref_col])
                    if reverse_order == False:
                        pass
                    else:
                        header_row = sorted_list.pop(0)
                        list.reverse(sorted_list)
                        sorted_list.insert(0,header_row)

                else:
                    new_list = PyLO.num_to_str(self, data=data, update=False)
                    sorted_list = [new_list[0]] + sorted(complete_list[1:], key=lambda x: x[ref_col])


                if update == True:
                    data.clear()
                    [data.append(n) for n in sorted_list]

                return sorted_list

        else:
            print()
            print(msg=" Not supported between instances of int and list ")
            print()
            return data


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Write a CSV File                                                                                                                               -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def write_csv_file(self, data:list, file_path:str="CSV_List")->str:

        '''  It writes a list into a CSV file  '''

        current_path = os.getcwd()
        ext = ""
        for l in file_path[-4:]:
            ext += l

        if ext == ".csv": file_name = file_path
        else:             file_name = file_path + ".csv"

        list_type = _get_list_type(data)

        #with open(file_path + ".csv", "w", newline="") as file:
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            if (list_type == "one_item_one_row" or list_type == "multiple_items_one_row" or\
                list_type == "multiple_items_multiple_rows"):
                for row in range(len(data)):
                    writer.writerow([col for col in data[row]])
            else:
                writer.writerow([col for col in data])

        if "/" in file_name: file = file_name
        else:                  file = current_path+"/"+file_name

        return file



    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Read a CSV File                                                                                                                                -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def read_csv_file(self, file_path:str="CSV_List")->list:

        '''  It reads a CSV file and returns a list of the contains of the file '''

        rows = []; ext = ""
        for l in file_path[-4:]:
            ext += l

        if ext == ".csv": file_name = file_path
        else:             file_name = file_path + ".csv"

        #with open(file_path + ".csv", "r", newline="") as file:
        try:
            with open(file_name, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    rows.append(row)
        except:
            rows = ["No Data or Not File"]

        list_type = _get_list_type(rows)
        csv_list = []
        if (list_type == "one_item_one_row" or list_type == "multiple_items_one_row"):
            for n in rows:
                for m in n:
                    csv_list.append(m)
        else:
            csv_list = rows
        return csv_list


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Write a List into JSON File                                                                                                                    -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def write_json_file(self, data:list, file_path:str="JSON_List")->str:

        '''  It writes a list into a json file  '''

        current_path = os.getcwd()
        ext = ""
        for l in file_path[-5:]:
            ext += l

        if ext == ".json": file_name = file_path
        else:             file_name = file_path + ".json"

        with open(file_name, "w") as data_file:
            json.dump(data, data_file, indent=4)

        if "/" in file_name: file = file_name
        else:                  file = current_path+"/"+file_name

        return file


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Read a JSON File and Return it as a List                                                                                                       -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def read_json_file(self, file_path:str="JSON_List")->list:

        '''  It reads a json file and returns a list of the contains of the file  '''

        ext = ""
        for l in file_path[-5:]:
            ext += l

        if ext == ".json": file_name = file_path
        else:             file_name = file_path + ".json"

        try:
            with open(file_name, "r") as data_file:
                data = json.load(data_file)
        except:
            data = ["No Data or Not File"]

        return data


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Delete a Column in a List                                                                                                                      -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def delete_col(self, data:list, col_ref:int=0, update:bool=False)->list:

        '''  It deletes a specific column in a list  '''

        n_rows_n_cols_list = PyLO.dimensions(self, data)
        n_cmax = n_rows_n_cols_list[1][1];      new_list = [];      tempo_rows = [];        tempo = data

        list_type = _get_list_type(data)

        if list_type == "incorrect_variable_type"   or list_type == "empty_list":  pass

        else:
            if col_ref > n_cmax-1 or col_ref < 0:
                print("col_ref is out of range in one or more columns in the list")
                # new_list = data
            else:
                #                 Done  ["dato"]                    Done [["dato"]]
                if list_type == "one_item_no_row" or list_type == "one_item_one_row":
                    if update == True: data.pop(0)
                    else: pass

                # multiple_items_no_row -> ["Hello","bye","good"]          mix_items -> [10,[50],[250],["H"],100]
                elif list_type == "multiple_items_no_row" or list_type == "mix_items":
                    value = tempo.pop(col_ref)
                    for n in tempo:
                        new_list.append(n)

                    if update == True: pass
                    else: data.insert(col_ref,value)

                elif list_type == "multiple_items_one_row":       # Done [["Hello","bye","good"]]
                    if col_ref > 0:
                        print("col_ref is out of range in one or more columns in the list")
                    else:
                        value = tempo.pop(col_ref)

                        for n in tempo:
                            new_list.append(n)

                        if update == True: pass
                        else: data.insert(col_ref,value)

                # Done [["Hello"],["bye"],["good"]] or [["Hello","mio"],["bye"],["good","hh"]]
                elif list_type == "multiple_items_multiple_rows":
                    for row in data:
                        for col in range(len(row)):
                            if col == col_ref:  pass
                            else:               tempo_rows.append(row[col])

                        if len(row) == 1 and col_ref == col: pass
                        else:             new_list.append(tempo_rows)

                        tempo_rows = []

                    if update == False: pass
                    else:
                        data.clear()
                        for row in new_list:
                            for col in row:
                                tempo_rows.append(col)
                            data.append(tempo_rows)
                            tempo_rows = []
                else:
                    pass
        return new_list


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Number a List                                                                                                                                  -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def number(self, data:list, start_number=0, id_txt="Id", renumber:bool=False, update:bool=False)->list:

        '''  Enumerate a list by adding a column to the left side  '''

        def set_counter(data, start_number, id_txt):
            result = []
            list_type = _get_list_type(data)
            if list_type == "multiple_items_multiple_rows":

                tempo = []
                header = data.pop(0)
                header.insert(0,id_txt)
                for row in data:
                    tempo = row
                    tempo.insert(0,start_number)
                    start_number += 1
                    result.append(tempo)
                    tempo = []
                result.insert(0,header)
            else:
                result = data
            return result

        if renumber == False:
            result = set_counter(data, start_number, id_txt)
        else:
            original = PyLO.delete_col(self, data=data, col_ref=0, update=False)
            result = set_counter(original, start_number, id_txt)

        if update == False: pass
        else:
            tempo_rows = []
            data.clear()
            for row in result:
                for col in row:
                    tempo_rows.append(col)
                data.append(tempo_rows)
                tempo_rows = []
        return result


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Table List To Vector List                                                                                                                      -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def make_to_vector(self, data:list)->list:

        '''  This function makes any list in a form as a vector. [1,2,3,4,5,etc.] '''

        vector_lista = []
        for item in data:
            if isinstance(item, list):
                for i in item:
                    if isinstance(i, list):
                        for n in i:
                            if isinstance(n, list):
                                for m in n:
                                    vector_lista.append(m)
                            else:
                                vector_lista.append(n)
                    else:
                        vector_lista.append(i)
            else:
                vector_lista.append(item)
        return vector_lista


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Join Two List as a Vector                                                                                                                      -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def join_as_vector(self, data:list, data2join:list, col_ref:int=0)->list:

        '''  It joins two list as a vector, join_list = [1,2,3,4,5,etc.]  '''

        join_list = []
        if data == [] or data == [[]] or data == [[[]]]:
            type_list_data = "empty_list"
        else:
            type_list_data = _get_list_type(data)
            if   type_list_data == "one_item_one_row": type_list_data = "multiple_items_one_row"
            elif type_list_data == "one_item_no_row":  type_list_data = "multiple_items_no_row"
            else: pass

        if data2join == [] or data2join == [[]] or data2join == [[[]]]:
            type_list2join = "empty_list"
        else:
            type_list2join = _get_list_type(data2join)
            if   type_list2join == "one_item_one_row": type_list2join = "multiple_items_one_row"
            elif type_list2join == "one_item_no_row":  type_list2join = "multiple_items_no_row"
            else: pass


        if type_list_data == "incorrect_variable_type" or type_list2join == "incorrect_variable_type":  pass  # case 0

        elif type_list_data == "empty_list" and type_list2join == "empty_list":  pass                         # case 1

        else:
            if type_list_data != "empty_list" and type_list2join == "empty_list":     # case 1 with all cases
                join_list = PyLO.make_to_vector(self, data)

            elif type_list_data == "empty_list" and type_list2join != "empty_list":   # all cases with case 1
                join_list = PyLO.make_to_vector(self, data2join)

            else:
                tempo_jl = PyLO.make_to_vector(self, data2join)
                tempo_dl = PyLO.make_to_vector(self, data)

                if col_ref <= 0:
                    join_list = tempo_jl
                    for i in tempo_dl:
                        join_list.append(i)

                else:
                    if type_list_data == "multiple_items_no_row":

                        if col_ref >= len(data):
                            join_list = tempo_dl
                            for i in tempo_jl: join_list.append(i)
                        else:
                            cnt = 0
                            for cold in data:
                                if col_ref == cnt:
                                    for coljl in tempo_jl:
                                        join_list.append(coljl)
                                    join_list.append(cold)
                                else:
                                    join_list.append(cold)
                                cnt += 1

                    elif type_list_data == "multiple_items_one_row":

                        if col_ref >= len(data[0]):
                            join_list = tempo_dl
                            for i in tempo_jl: join_list.append(i)
                        else:
                            cnt = 0
                            for cold in data[0]:
                                if col_ref == cnt:
                                    for coljl in tempo_jl:
                                        join_list.append(coljl)
                                    join_list.append(cold)
                                else:
                                    join_list.append(cold)
                                cnt += 1


                    elif type_list_data == "multiple_items_multiple_rows":
                        if col_ref >= len(data):
                            join_list = tempo_dl
                            for i in tempo_jl: join_list.append(i)
                        else:
                            cnt = 0
                            for cold in data:
                                for rowd in cold:
                                    if col_ref == cnt:
                                        for n in tempo_jl:
                                            join_list.append(n)
                                        join_list.append(rowd)
                                        cnt += 1
                                    else:
                                        join_list.append(rowd)
                                cnt += 1

                    else:  # "mix_items"
                        cnt = 0
                        for item in data:
                            if isinstance(item, list):
                                result = PyLO.make_to_vector(self, item)
                                if col_ref == cnt:
                                    for n in tempo_jl: join_list.append(n)
                                    cnt += 1
                                    for n in result: join_list.append(n)
                                else:
                                    for n in result: join_list.append(n)
                            else:
                                join_list.append(item)
                            cnt += 1

        return join_list


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Add a New Column in a List                                                                                                                     -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def add_col(self, data:list, new_col_data:list, col_ref:int=0)->list:

        '''  It adds a column in a list that is in a form of a matrix or table
             list     = [["H1","H2"],        ["R1C1","R2C1],           ["R2C1","R2C2"]]
             new_list = [["H1","H2","New_H"],["R1C1","R1C2","NewR1C3"],["R2C1","R2C2","NewR2C3"]]  '''

        if new_col_data == [] or new_col_data == [[]] or new_col_data == [[[]]]:  pass
        else:
            if isinstance(data, list) and isinstance(new_col_data, list):
                list_type = _get_list_type(data)
                if list_type == "multiple_items_one_row" or list_type == "multiple_items_multiple_rows" or list_type == "one_item_one_row":
                    new_list = data
                    col_info = PyLO.make_to_vector(self, new_col_data)

                    length_c = len(col_info)
                    length_d = len(data)

                    diff = length_c - length_d
                    if diff < 0:
                        miss_col = diff * -1
                        for n in range(miss_col):
                            col_info.append(" ")
                    else: pass

                    cnt = 0
                    ctrl = 0
                    for row in data:
                        if col_ref <= 0:
                            new_list[ctrl].insert(0, col_info[ctrl])
                            # ctrl += 1

                        elif col_ref >= len(row):
                            new_list[ctrl].append(col_info[ctrl])
                            # ctrl += 1

                        else:
                            for n in range(len(row)):
                                if n == col_ref:
                                    new_list[ctrl].insert(n, col_info[cnt])
                                    cnt += 1
                                else: pass
                            # ctrl += 1
                        ctrl += 1
                else:
                    new_list = PyLO.join_as_vector(self, new_col_data,data, 0)
            else:
                new_list =[]

        return new_list


    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Replace a Value in the List                                                                                                                    -
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    def replace(self, data:list, old:int|str, new:int|str, update=False)->list:

        '''  It replaces a value for another in a list
             The list can be a vector [1,2,3,4] or a matrix (table) [[1,2],[3,1]]
             or a combination of them [[1,2],[3,3,3],3,[5,6,7,8]]  '''

        new_list = []
        for value in data:
            if isinstance(value, list):
                new_list.append(PyLO.replace(self, value, old, new))
            elif value == old:
                new_list.append(new)
            else:
                new_list.append(value)

        if update == True:
            data.clear()
            for n in new_list: data.append(n)
        
        return new_list




# Planning to use this script as help of the Module custom_print.
if __name__ == "__main__":
    print("Working on The Documentation Here")
    cmdl_argv = []
    for argv in sys.argv:
        cmdl_argv.append(argv.lower())

    table = FancyFormat()
    table.print_fancy_format(cmdl_argv)
