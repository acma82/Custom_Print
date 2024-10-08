import fancyprint as fp
lista = fp.FancyFormat()

# lista.bg_header = 99
# lista.fg_header = 231
# lista.bg_data   = 22
# lista.fg_data   = 231

lista.bg_title    = 11
lista.fg_title    = 21
lista.bold_title  = True
lista.msg_title   = " Welcome...! "
lista.align_title = fp.Align.RIGHT

#lista.align_footnote = "r"; 
lista.bg_footnote    = 6
lista.fg_footnote    = 0
lista.bold_footnote  = True
lista.msg_footnote   = " GoodBye...! "
lista.align_footnote = fp.Align.LEFT

lista.align_header = fp.Align.CENTER
lista.align_data = fp.Align.CENTER

lista.horizontal_line_under_header_on = True
lista.horizontal_separator_line_on = True

# my_data = ["Miguel Angel Aguilar Cuesta"]
# my_data = [["Miguel","Angel","Aguilar","Cuesta"]]
# my_data = ["Miguel","Angel","Aguilar","Cuesta"]
# my_data = [["Miguel"],["Amgel"],["Aguilar"],["Cuesta"],["ACMA_1982_07_18"]]
my_data = [["Name",  "Last",   "Age", "Key"],\
           ["Miguel","Aguilar", 42, "ACMA_1982_07_18"],\
           ["Hello", "Bye",     99, "012345"]]


# lista.print_fancy_format(my_data,fp.Line_Style.DASH)

print()


#----------------------------------------------------------------------------------------------------------------------------------------------------
# lines
# indent, tail, body, head, length=1
def print_horizontal_line(lst):   
   print(fp.ins_space(lst[0]) + lst[1],end="")   
   for n in range(lst[4]): print(lst[2],end="")
   print(lst[3])


def print_vertical_line(lst):
   print(fp.ins_space(lst[0])+lst[1])
   for n in range(lst[4]): print(fp.ins_space(lst[0]) + lst[2])
   print(fp.ins_space(lst[0]) + lst[3])

print("\033[1;48;5;90;38;5;231m")
# indent, tail, body, head, length=1
chars_lines = [[2,"-","-","-",10],
               [2,"\u2015","\u2015","\u2015",10],
               [2,"\u25C0","-","\u25B6",10],
               [2,"\u25C0","\u2015","\u25B6",10],

               [2,"\u2731","\u2015","\u273D",10],               

               [2,"\u273D","-","\u25B6",10],
               [2,"\u25C0","-","\u25CF",10],
               [2,"\u273D","\u2015","\u25B6",10]] 

for ch in chars_lines:
   print_horizontal_line(ch)



# indent, tail, body, head, length=1
chars_lines = [[2,"|","|","|",5],
               [4,"\u25B2","\u254E","\u25BC",5],
               [6,"\u273D","\u254E","\u25BC",5],
               [8,"\u25B2","\u254E","\u25BC",5],
               [10,"\u25B2","\u2503","\u253B",5],
               [12,"\u25B2","\u2502","\u2534",5]] 

for ch in chars_lines:   
   print_vertical_line(ch)



