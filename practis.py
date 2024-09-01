import fancyprint as fp
lista = fp.FancyFormat()

lista.bg_header = 99
lista.fg_header = 231
lista.bg_data   = 22
lista.fg_data   = 231

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

lista.align_header = fp.Align.LEFT
lista.align_data = fp.Align.LEFT

# my_data = ["Miguel Angel Aguilar Cuesta"]
# my_data = [["Miguel","Angel","Aguilar","Cuesta"]]
# my_data = ["Miguel","Angel","Aguilar","Cuesta"]
# my_data = [["Miguel"],["Amgel"],["Aguilar"],["Cuesta"],["ACMA_1982_07_18"]]
my_data = [["Name",  "Last",   "Age", "Key"],\
           ["Miguel","Aguilar", 42, "ACMA_1982_07_18"],\
           ["Hello", "Bye",     99, "012345"]]


lista.bg_all_cell_data = True    # default
lista.bg_all_cell_header = True  # default
lista.print_fancy_format(my_data)

print("\n")

lista.bg_all_cell_data = False
lista.bg_all_cell_header = False
lista.print_fancy_format(my_data)
