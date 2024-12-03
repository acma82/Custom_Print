'''
The path needs to be specified as it is.
Do NOT use tilda(~) or $HOME for quick access
to the path.
The extension can be omitted
'''
import custom_print as cp
pylo = cp.PyLO()


classes_methods_fancyprint = [["Header 1","Header 2",     "Header 3",              "Header 4"        ,     "Header 5"],
                              ["Cursor",  "FontStyle",    "FancyMessage",          "FancyFormat"        ,  "Pen"],
                              ["jumpTo",  "start_style",  "print_fancy_message",   "print_fancy_format",   "draw_line"],
                              ["jumpxy",  "stop_style",   "print_fancy_note",      "reset_fancy_format",   "draw_rectangle"],
                              ["moveTo",  "print_style",  "----             ",      "----             ",   "----"],
                              ["movexy",  "reset_style",  "----             ",      "----             "   ]]

file_path = pylo.write_csv_file(classes_methods_fancyprint)
print(file_path)


list_1 = [10,[50],[250],["H"],100]
file_path = pylo.write_csv_file(list_1, "file_1")
print(file_path)


# list_1 = [10,[50],[250],["H"],100]
# file_path = pylo.write_csv_file(list_1, "/home/user_name_here/Documents/file_1")
# print(file_path)
