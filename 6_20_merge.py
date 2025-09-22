import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

tbl.title_bg  = 90
tbl.title_bold = True
tbl.title_italic = True
tbl.title_align  = cp.Align.LEFT

#-----------------------------------------------------------------------------------------
methods = [\
    ["Cursor",  "FontStyle"  ,    "FancyMessage"       ,    "FancyFormat"        ],
    ["jumpTo",  "start_style",    "print_fancy_message",    "print_fancy_format" ],
    ["jumpxy",  "stop_style" ,    "print_fancy_note"   ,    "reset_fancy_format" ],
    ["moveTo",  "print_style"],
    ["movexy"]]

people = [\
      ["Names",  "Lasts",   "Age"],
      ["Pancho", "Melti",    50  ],
      ["Javier", "Nangy",    32  ],
      ["Melony", "Archi",    40  ],
      ["Jose",   "Valvimar", 18  ]]

tbl.title_msg = " List 1: Methods "
tbl.print_fancy_format(methods)

tbl.title_msg = " List 2: People "
tbl.print_fancy_format(people)

tbl.title_msg = " Merge List people to List methods as COLUMNS "
merge_cols = pylo.merge(list_1=methods, list_2=people, posi=8, merge_by=pylo.Appending.COLUMNS) 
tbl.print_fancy_format(merge_cols)

tbl.title_msg = " Merge List 1 and List 2 as ROWS "
merge_rows = pylo.merge(list_1=methods, list_2=people, posi=8, merge_by=pylo.Appending.ROWS)
tbl.print_fancy_format(merge_rows)

cp.ins_newline(2)
print(f"{cp.set_font(1,23,231)} Methods {cp.reset_font()} ")
print(methods)
#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
cp.ins_newline(2)
print(f"{cp.set_font(1,23,231)} People {cp.reset_font()} ")
print(people)
#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
cp.ins_newline(2)
print(f"{cp.set_font(1,23,231)} Merge ROWS {cp.reset_font()} ")
print(merge_rows)
#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
cp.ins_newline(2)
print(f"{cp.set_font(1,23,231)} Merge COLUMNS {cp.reset_font()} ")
print(merge_cols)
#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
