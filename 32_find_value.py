import copy
import custom_print as cp

tbl = cp.FancyFormat()
pylo = cp.PyLO()

#-----------------------------------------------------------------------------------------
# grep                                                                                  --
#-----------------------------------------------------------------------------------------
def experiment_grep(data:list, value:int|str)->list:
    grep_list = [] 
    ctrl = 0
    try:
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == value:
                    grep_list.append([row, col, value])
        if len(grep_list) > 0:
            grep_list.insert(0, ["Row","Col","value"])
        else: pass
    except:
        grep_list = []
        print("inside")
        def find_value(data:list):
            new_list = []
            for value in range(len(data)):
                if isinstance(data[value], list):
                    new_list.append(find_value(data[value]))
                else:
                    if data[value] == value:
                        tempo = ["Positon",value]
                        grep_list.append(tempo)
                
        find_value(data)

    return grep_list



list_1 = [["Header 1", "Header 2", "Header 3",0],
          ["Datito 1", "Datito 2", "Datito 3",1],
          ["Datito 4", "Datito 5", "Datito 6",2],
          ["DaTitO 1", "Datito 2", "datito 1",3]]

list_2 = [2,5,[2,7],8,8,9,"A",[8,2,2]]

list_3 = ["miGueL", "hellO",["BB",7,8,"bB"]]

result = pylo.find_value(data=list_1, value="DATITO 1", case_sensitive=False)
tbl.print_fancy_format(result)
tbl.print_fancy_format(list_1)


result = pylo.find_value(list_2, 8, True) # Number are NOT Case Sensitive
print("Case_Sensitive=False: ",result)


result = pylo.find_value(list_3, "BB", True)
print("Case_Sensitive=True:  ",result)

