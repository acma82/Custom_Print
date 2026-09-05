import custom_print as cp

message = '''
Guido van Rossum, a Dutch programmer, created Python in the late 1980s
as a hobby project. He started working on it in December 1989 at Cent-
rum Wiskunde & Informatica (CWI) in the Netherlands.

Python was first released on February 20, 1991. Python was named after
the 1970s BBC comedy sketch series Monty Python's Flying Circus.
'''

paragraph3 = '''
 I should probably collect a list of the best romantic poems ever written, 
 and maybe I will. This is not that. I mostly talk about writing books, 
 but I noticed most of the other big writing sites actually get most of 
 ----
 the their traffic from this keyword, because everybody is interested in
 romantic poetry! When you   want to tell her how you feel, but do not
 have the words to express all that emotion...! '''

att = cp.FancyMessage()
att.length = cp.Length_Bg.ONLY_WORD

cp.ins_newline(2)
att.print_fancy_message(paragraph3)
attributes, words = att.get_message_attributes(paragraph3,True)

# print(attributes)
# print(words)
