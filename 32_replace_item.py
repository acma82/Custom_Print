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
def exp_replace(data:list, ref_value="---", new_value="----")->list:
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

list_1 = [[1,[0,3],2,3],[4,5,3],[2,3,3]]
print("Original:",list_1)
resutl = pylo.replace(list_1,3,"A",True)
print("Result  :",resutl)
print("Original:",list_1)



 