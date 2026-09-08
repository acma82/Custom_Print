# import custom_print as cp
# cp.help_documentation()
#------------------------------------------------------------------------


# from custom_print import about_custom_print
# about_custom_print()


# from custom_print import help_documentation
# help_documentation()


# from custom_print import all_documentation
# all_documentation()



# from custom_print import screen_functions_info
# screen_functions_info()


# from custom_print import clean_info
# clean_info()


# from custom_print import clear_info
# clear_info()


# from custom_print import dimensions_info
# dimensions_info()


# from custom_print import erase_info
# erase_info()


# from custom_print import resize_info
# resize_info()


# from custom_print import ansi_colors_info
# ansi_colors_info()


# from custom_print import ins_chr_info
# ins_chr_info()


# from custom_print import ins_newline_info
# ins_newline_info()


# from custom_print import set_reset_font_info
# set_reset_font_info()


# from custom_print import terminal_bell_info
# terminal_bell_info()

import custom_print as cp

print(f"COFFEE: \u2615 \N{HOT BEVERAGE}")
print(f"Degree Celsius : \U00002103 \u267B \N{BLACK UNIVERSAL RECYCLING SYMBOL}")
print(f"Degree Fahrenheit : \u2109  ")
print(f"Black circle : \N{BLACK CIRCLE} \N{INVERSE WHITE CIRCLE}")
print(f"White circle : \N{Fisheye} ")
print(f"Inverse bullet : \N{INVERSE BULLET} ")
print(f"White heavy check mark:  \N{WHITE HEAVY CHECK MARK}  \u2713 \u2715 \u2714")
print(f"Curly loop:  \N{CURLY LOOP}")
print(f"Double curly loop : \N{DOUBLE CURLY LOOP} ")
print(f"Replacement Character: \N{REPLACEMENT CHARACTER}  ")  # No
print("enter : \u21B5 \u2BA0")
# from 21C4 to 21CA
print(f"double up arrow: \u2B85 \N{UPWARDS PAIRED ARROWS} \u2B87 \N{DOWNWARDS PAIRED ARROWS}")
print(f"double updown arrow: \u21C5 \N{UPWARDS ARROW LEFTWARDS OF DOWNWARDS ARROW}")
print("double arrows: \u2b81 \u2b83 \u2b82 \u2b80 \u2b86 \u2b84 \u2b85 \u2b87")

print(f"\N{PARENTHESIZED LATIN SMALL LETTER X}") # No
print(f"\N{Circled Latin Capital Letter I}")     # No
print(f"\N{MEDIUM WHITE CIRCLE} \N{MEDIUM BLACK CIRCLE} \N{BASEBALL} \N{SOCCER BALL}")
print(f"\N{BLACK FLORETTE} \N{CIRCLED WHITE STAR} Heavy_Asterisk: \u273d") # 
print(f"\N{BLACK QUESTION MARK ORNAMENT}  \N{WHITE QUESTION MARK ORNAMENT}")
print(f"\N{HEAVY EXCLAMATION MARK SYMBOL} \N{WHITE EXCLAMATION MARK ORNAMENT}")
print(f"\N{BLACK DIAMOND MINUS WHITE X}")
print(f"\N{CROSS MARK}")
print(f"\N{UPPER RIGHT SHADOWED WHITE SQUARE}")
print(f" \N{BLACK LARGE SQUARE}")
print(f" \N{WHITE LARGE SQUARE}")
print(f" \N{BLACK LARGE CIRCLE}") # No
print(f" \N{HEAVY LARGE CIRCLE}")
print(f" \N{HEAVY CIRCLED SALTIRE}") # No
print(f" UP DOWN TRIANGLEHEADED ARROW \u2B65")
print(f" LEFT RIGHT TRIANGLE HEADED ARROW \u2b64")

print(f" \N{BLACK UPWARDS EQUILATERAL ARROWHEAD}")
print(f" \N{BLACK RIGHTWARDS EQUILATERAL ARROWHEAD}")
print(f" \N{BLACK DOWNWARDS EQUILATERAL ARROWHEAD}")
print(f" \N{BLACK LEFTWARDS EQUILATERAL ARROWHEAD}")
print("ghost \U0001F47B poop \U0001F4A9 clown \U0001F921")
print("eyes \U0001F440 \U0001F441 \U0001F442")
print("python \U0001F40D \U0001F339 \U0001F388")
print(f"\u00A9  \u00AE \U000026AB Check here \U0001F7E1  \U0001F7E9 as check mark")
print(f"\U0001F537 Number One Option")

print(cp.Unicode.FIRE) 


pylo = cp.PyLO()
tbl = cp.FancyFormat()
all_topics = [
    "Screen_Functions",  "clean", "clear","dimensions", "erase", "resize",

    "Internal_Functions", "ansi_colors", "get_list_type", "ins_chr", "ins_newline", "move_cursor_right", "set_reset_font", "subscript", "superscript", "terminal_bell",

    "Help_Classes",  "Align", "Ascii_Letter", "Bg", "Divider_Style", "Fg", "Layout", "Length_Bg", "Line_Style", "Logo", "Move",  "No",  "Style",  "Unicode",

    "Cursor",  "jumpTo", "jumpxy", "moveTo", "movexy",

    "Fontstyle",  "style_on_off", "reset_style", "print_style",

    "FancyMessage",  "print_fancy_message", "print_fancy_note", "get_message_attributes",

    "Pen",  "draw_line", "draw_rectangle",

    "Divider",  "print_fancy_divider",

    "FancyFormat",  "print_fancy_format", "reset_fancy_format",

     "AsciiArt", "print_ascii_art", "print_multi_ascii_art", "print_ascii_logo_art", "print_reversed_ascii_logo_art"]

# transpose_topics = pylo.transpose(all_topics)
# result = pylo.number(data=transpose_topics, start_number=1, id_txt="No.")

# tbl.print_fancy_format(result) 


# lista_type = cp.get_list_type([1,2,3])#(result)
# print(lista_type)


# print(f"{cp.move_cursor_right(n=12, option_space=True)} Hello")
# print(f"{cp.move_cursor_right(n=12, option_space=False)} Hello") 

# lst = [["H1","H2"],[5,4],[3]]
# tbl.print_fancy_format(None)

# lst = ["bool","str","list","set","range", "complex","int","float", "dict", "tuple","frozenset","None"]
# ordered_letters = sorted(lst)
# print(ordered_letters)



# message = f'''
# A{cp.Unicode.SUPERSCRIPT_ALPHA  }  B{cp.Unicode.SUBSCRIPT_ALPHA  }
# A{cp.Unicode.SUPERSCRIPT_BETA   }  B{cp.Unicode.SUBSCRIPT_BETA   }
# A{cp.Unicode.SUPERSCRIPT_GAMMA  }  B{cp.Unicode.SUBSCRIPT_GAMMA  }
# A{cp.Unicode.SUPERSCRIPT_DELTA  }  B{cp.Unicode.SUBSCRIPT_DELTA  }
# A{cp.Unicode.SUPERSCRIPT_EPSILON}  B{cp.Unicode.SUBSCRIPT_EPSILON}
# A{cp.Unicode.SUPERSCRIPT_THETA  }  B{cp.Unicode.SUBSCRIPT_THETA  }
# A{cp.Unicode.SUPERSCRIPT_IOTA   }  B{cp.Unicode.SUBSCRIPT_IOTA   }
# A{cp.Unicode.SUPERSCRIPT_PHO    }  B{cp.Unicode.SUBSCRIPT_PHO    }
# A{cp.Unicode.SUPERSCRIPT_PHI    }  B{cp.Unicode.SUBSCRIPT_PHI    }
# A{cp.Unicode.SUPERSCRIPT_PSI    }  B{cp.Unicode.SUBSCRIPT_PSI    }
# A{cp.Unicode.SUPERSCRIPT_CHI    }  B{cp.Unicode.SUBSCRIPT_CHI    }
# '''
# print(message)
pen = cp.Pen()
crs = cp.Cursor()
ex_fst = cp.FontStyle()

pen.adj_indent = 35

pen.draw_line(size=5, layout=cp.Layout.VERTICAL, tail=ex_fst.style_on()+cp.Unicode.BOX_DRAWINGS_LIGHT_DOWN_AND_HORIZONTAL,\
                body=cp.Unicode.BOX_DRAWINGS_LIGHT_VERTICAL, head=ex_fst.style_on()+cp.Unicode.BOX_DRAWINGS_LIGHT_UP_AND_HORIZONTAL)