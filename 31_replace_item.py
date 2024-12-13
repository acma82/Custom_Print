'''  up to 2 brackets '''
def replace1(data:list, ref_value="---", new_value="----")->list:
    new_list = []
    for item in data:
        if isinstance(item, list):
            tempo = []
            for i in item:
                if ref_value == i:
                    tempo.append(new_value)
                else:
                    tempo.append(i)
            new_list.append(tempo)
            tempo = []
        else:
            if item == ref_value:
                new_list.append(new_value)
            else:
                new_list.append(item)
    return new_list
#-----------------------------------------------------------------------------------------
#                                                                                       --
#-----------------------------------------------------------------------------------------
import copy
'''  Up to 4 brackets  '''
def experiment_replace(data:list, ref_value="---", new_value="----")->list:
    x_tmp =copy.deepcopy(data)
    for inx in range(len(data)):
        if isinstance(data[inx], list):
            #----------------------------------------------------------------------------------------------------------------------------
            for it in range(len(data[inx])):
                if isinstance(data[inx][it], list):
                    #--------------------------------------------------------------------------------------------------------------------
                    for i in range(len(data[inx][it])):
                        if isinstance(data[inx][it], list):
                            #------------------------------------------------------------------------------------------------------------
                            for n in range(len(data[inx][it])):
                                if isinstance(data[inx][it][n], list):
                                    #----------------------------------------------------------------------------------------------------
                                    for m in range(len(data[inx][it][n])):
                                        if isinstance(data[inx][it][n][m], list):
                                            for l in range(len(data[inx][it][n][m])):
                                                #----------------------------------------------------------------------------------------
                                                if ref_value == data[inx][it][n][m][l]: x_tmp[inx][it][n][m][l] = new_value
                                                else:                                   pass
                                        else:
                                            if ref_value == data[inx][it][n][m]: x_tmp[inx][it][n][m] = new_value
                                            else:                                pass
                                else:
                                    if ref_value == data[inx][it][n]: x_tmp[inx][it][n] = new_value    
                                    else:                             pass
                        else:
                            if ref_value == data[inx][it][i]: x_tmp[inx][it][i] = new_value
                            else:                             pass
                else:
                    if data[inx][it] == ref_value: x_tmp[inx][it] = new_value
                    else:                          pass
        else:
            if data[inx] == ref_value: x_tmp[inx] = new_value
            else:                      pass
    return x_tmp
#-----------------------------------------------------------------------------------------
#                                                                                       --
#-----------------------------------------------------------------------------------------
import custom_print as cp
pylo = cp.PyLO()

print(f"{cp.set_font(1,1,15)} Replacing 3 for A {cp.reset_font()}")
list_1 = [[11,[10,3],12,3],[14,15,3],[12,3,3]]
print("Original:",list_1)
resutl = pylo.replace(data=list_1, old=3, new="A", update=True)
print("Result  :",resutl)
print("Original:",list_1)

list_2 = [["HeadeR 1", "HeadeR 2", "HeadeR 3",0],
          ["DatitO 1", "DatitO 2", "DatitO 3",1],
          ["DatitO 4", "DatitO 5", "DatitO 6",0],
          ["DatitO 1", "DatitO 2", "DatitO 1",3]]

resutl = pylo.replace(data=list_2, old=0, new="A", update=True)
print("Result  :",resutl)


 