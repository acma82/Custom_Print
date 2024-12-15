import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()
tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True
tbl.align_title = cp.Align.LEFT

def reverse_order(data:list, update:list=False):
    headers = [];       body = []
    reversed_list = []; ctrl = 0
    tmp = []
    
    for row in data:
        if ctrl == 0:
            headers.append(row)
            ctrl = 1
        else:
            for col in row:
                tmp.append(col)
            body.append(tmp)
            tmp = []
    
    for row in reversed(body):
        reversed_list.append(row)
    reversed_list.insert(0,headers[0])

    if update == True:
        data.clear()
        for r in reversed_list:
            data.append(r)

    return reversed_list    

#---------------------------------------------------------------------
people = [\
      ["Names",  "Lasts",   "Age"],
      ["Pancho", "Melti",    50  ],
      ["Javier", "Nangy",    32  ],
      ["Melony", "Archi",    40  ],
      ["Jose",   "Valvimar", 18  ]]





reversed_list = pylo.reverse_order(people,False)
# reversed_list = pylo.reverse_order(people,True)

tbl.msg_title = " Reversed Order Of People "
tbl.print_fancy_format(reversed_list)

tbl.msg_title = " Original List People "
tbl.print_fancy_format(people)