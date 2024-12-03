'''
The extension can be omitted
'''
import custom_print as cp
pylo = cp.PyLO()
tbl = cp.FancyFormat()


file_info = pylo.read_json_file("JSON_List.json")
tbl.print_fancy_format(file_info)


file_info = pylo.read_json_file("file_1.json")
tbl.print_fancy_format(file_info)

# file_info = pylo.read_json_file("/home/user_name/Documents/file_1.json")
# tbl.print_fancy_format(file_info)