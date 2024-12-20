'''
The extension can be omitted
'''
import source.source.custom_print as cp
pylo = cp.PyLO()
tbl = cp.FancyFormat()


file_info = pylo.read_csv_file("CSV_List")
tbl.print_fancy_format(file_info)


file_info = pylo.read_csv_file("file_1.csv")
tbl.print_fancy_format(file_info)