import custom_print as cp

message = '''
Guido van Rossum, a Dutch programmer, created Python in the late 1980s
as a hobby project. He started working on it in December 1989 at Cent-
rum Wiskunde & Informatica (CWI) in the Netherlands.

Python was first released on February 20, 1991. Python was named after
the 1970s BBC comedy sketch series Monty Python's Flying Circus.
'''

att = cp.FancyMessage()
att.length = cp.Length_bg.ONLY_WORD

cp.ins_newline(2)
att.print_fancy_message(message)
attributes, words = att.get_message_attributes(message,True)
