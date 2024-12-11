# PyLO Class
## Conversion
### <span style="color:purple"> <strong> Bool Type to List Type </strong> </span>

<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()
    
    variable = True
    result = pylo.bool_to_list(data=variable, convert_to_str=False)
    print(result)
    result = pylo.bool_to_list(data=variable, convert_to_str=True)
    print(result)
```


### <span style="color:purple"> <strong> Integer Type to List Type </strong> </span>
<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()
    
    variable = 10
    result = pylo.int_to_list(data=variable, convert_to_str=False)
    print(result)
    result = pylo.int_to_list(data=variable, convert_to_str=True)
    print(result)
```

### <span style="color:purple"> <strong> Float Type to List Type </strong> </span>
<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()
    
    variable = 5.5
    result = pylo.float_to_list(data=variable, convert_to_str=False)
    print(result)
    result = pylo.float_to_list(data=variable, convert_to_str=True)
    print(result)
```

### <span style="color:purple"> <strong> Complex Type to List Type </strong> </span>
<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    variable = 5+5j
    result = pylo.complex_to_list(variable, False)
    print(result)
    result = pylo.complex_to_list(variable, True)
    print(result)
```

### <span style="color:purple"> <strong> String Type to List Type </strong> </span>
<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    print(f"{cp.set_font(1,90,231)}  WORD_BY_WORD  {cp.reset_font()}")
    result = pylo.str_to_list(data=paragraph, option=pylo.Str_List_Option.WORD_BY_WORD, counter=False)
    print(result)

    cp.ins_newline(2)
    print(f"{cp.set_font(1,90,231)}  counter WORD_BY_WORD  {cp.reset_font()}")
    result = pylo.str_to_list(paragraph, pylo.Str_List_Option.WORD_BY_WORD, counter=True)
    print(result)
    
    cp.ins_newline(2)
    print(f"{cp.set_font(1,90,231)}  LINE_BY_LINE  {cp.reset_font()}")
    result = pylo.str_to_list(paragraph, pylo.Str_List_Option.LINE_BY_LINE, counter=False)
    print(result)
    
    cp.ins_newline(2)
    print(f"{cp.set_font(1,90,231)}  counter LINE_BY_LINE  {cp.reset_font()}")
    result = pylo.str_to_list(paragraph, pylo.Str_List_Option.LINE_BY_LINE, counter=True)
    print(result)
```

### <span style="color:purple"> <strong> Dictionary Type to List Type </strong> </span>
<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    mydict = {"Name":"Jose Alfredo","Last":"Jimenez","Country":"Mexico","Age":82, "Lista":[1,2,3]}

    print(f"{cp.set_font(1,90,231)}  Case 1  {cp.reset_font()}")
    result = pylo.dict_to_list(data=mydict, convert_to_str=False)
    for dato in result:
       print(dato)
    cp.ins_newline(2)

    print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
    result = pylo.dict_to_list(data=mydict, key_title="My Keys", value_title="My Values",convert_to_str=False)
    for dato in result:
       print(dato)
    cp.ins_newline(2)

    print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
    result = pylo.dict_to_list(data=mydict, key_title="none", value_title=None,convert_to_str=False)
    for dato in result:
       print(dato)
    cp.ins_newline(2)

    print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
    result = pylo.dict_to_list(data=mydict, key_title="My Keys", value_title="My Values",convert_to_str=True)
        for dato in result:
        print(dato)
```

> <span style="color:red">**Note:**</span> with one of then that is __"none"__ or __None__, it won't set the <span style="color:blue"> ***key_title*** </span> neither the <span style="color:blue"> ***value_title*** </span>.

### <span style="color:purple"> <strong> Range Type to List Type </strong> </span>

>   | Note: values for range            |                                               |
>   |-----------------------------------|-----------------------------------------------|
>   | convert_to_str = True/False       | layout="vertical"/"horizontal" or "h"/"v"     |
>   | header_title = ""                 | this will put Range Value(s) for header_title |
>   | header_title = None or "none"     | This won't set any header_title               |
>   | header_title = "Any Title Header" | This will set the header_title                | 

<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    r = range(0,15,3)
    print(r)
    print(f"{cp.set_font(1,90,231)}  Case 1  {cp.reset_font()}")
    l = pylo.range_to_list(data=r, layout=cp.Layout.VERTICAL, convert_to_str=False)
    for n in l:
       print(n)
    cp.ins_newline(2)

    print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
    l = pylo.range_to_list(data=r, header_title="none", layout=cp.Layout.VERTICAL, convert_to_str=False)
    for n in l:
       print(n)
    cp.ins_newline(2)

    print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
    l = pylo.range_to_list(data=r, header_title="Header Title", layout=cp.Layout.VERTICAL, convert_to_str=False)
    for n in l:
       print(n)
    cp.ins_newline(2)

    print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
    l = pylo.range_to_list(data=r, header_title="Header Title", layout="h", convert_to_str=True)
    print(l)
    print(f"{cp.ins_chr(n=100, unicode="-")}")
    cp.ins_newline(2)
```


### <span style="color:purple"> <strong> Set|Frozenset Type to List Type </strong> </span>

>   | Note: values for set              |                                               |
>   |-----------------------------------|-----------------------------------------------|
>   | convert_to_str = True/False       | layout="vertical"/"horizontal" or "h"/"v"     |
>   | header_title = ""                 | this will put Set Value(s) for header_title   |
>   | header_title = None/"none"        | It won't set any header_title                 |
>   | header_title = "Any Title Header" | This will set the header_title                |

<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()


    set_1 = {1,3,5,7,9}
    print(f"{cp.set_font(1,90,231)}  Case 1  {cp.reset_font()}")
    result = pylo.set_to_list(data=set_1, header_title="None", layout=cp.Layout.VERTICAL, convert_to_str=False)
    print(result)
    print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
    result = pylo.set_to_list(data=set_1, header_title="", layout="vertical", convert_to_str=False)
    print(result)
    print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
    result = pylo.set_to_list(data=set_1, layout="v", convert_to_str=False)
    print(result)
    print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
    result = pylo.set_to_list(data=set_1, header_title="Hello_SET", layout="h", convert_to_str=True)
    print(result)
    print(f"{cp.ins_chr(n=100, unicode="-")}")
    cp.ins_newline(2)
```


>   | Note: values for frozenset        |                                                   |
>   |-----------------------------------|---------------------------------------------------|
>   | convert_to_str = True/False       | layout="vertical"/"horizontal" or "h"/"v"         |
>   | header_title = ""                 | this will put Frozenset Value(s) for header_title |
>   | header_title = None/"none"        | It won't set any header_title                     |
>   | header_title = "Any Title Header" | This will set the header_title                    |

<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    set_1 = {1,3,5,7,9}
    frozenset_1 = frozenset(set_1)
    print(f"{cp.set_font(1,90,231)}  Case 1  {cp.reset_font()}")
    result = pylo.set_to_list(data=frozenset_1, header_title="None", layout=cp.Layout.VERTICAL, convert_to_str=False)
    print(result)
    print(f"{cp.set_font(1,90,231)}  Case 2  {cp.reset_font()}")
    result = pylo.set_to_list(data=frozenset_1, header_title="", layout="vertical", convert_to_str=False)
    print(result)
    print(f"{cp.set_font(1,90,231)}  Case 3  {cp.reset_font()}")
    result = pylo.set_to_list(data=frozenset_1, layout="v", convert_to_str=False)
    print(result)
    print(f"{cp.set_font(1,90,231)}  Case 4  {cp.reset_font()}")
    result = pylo.set_to_list(data=frozenset_1, header_title="Hello_SET", layout="h", convert_to_str=True)
    print(result)
    print(f"{cp.ins_chr(n=100, unicode="-")}")
    cp.ins_newline(2)
```

### <span style="color:purple"> <strong> Tuple Type to List Type </strong> </span>
<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    tupleData1 = (("Apple"));    print("case 0:",tupleData1)       # this is a string                     Case 0
    tupleData2 = ("",);          print("case 1:",tupleData2)       # this is a tuple                      Case 1
    tupleData3 = ("Apple",);     print("case 2:",tupleData3)       # this is a simple tuple               Case 2
    tupleData4 = (("Apple",));   print("case 3:",tupleData4)       # this is a tuple inside tuple         Case 3
    print()
    tupleData5 = (("hello",),("hell",),("hi",),([1,2],)) # this is a simple tuple w/ tuples     Case 4
    tupleData6 = (("hello","hello"),("hell",),("hi","bye","good"),([1,2],)) #                   Case 4

    print("Case 4:",tupleData5); print("Case 4:",tupleData6)
    print()

    tupleData7 = ("hello","hell","hi",[1,2])             # this is a simple tuple w/ string     Case 5
    tupleData8 = (("hello"),("hell"),("hi"),([1,2]))     # this is a simple tuples w/ string    Case 5
    print("Case 5:",tupleData7); print("Case 5:",tupleData8)
    print()

    # this is a tuple w/ combination other type of variables Case 6
    tupleData9 = (("hello","hello"),("hell",),("hi","bye","good"),[1,2], "hello")
    print("Case 6:",tupleData9)
    print()

    listData1 = pylo.tuple_to_list(tupleData1);   print("Case 0:",listData1)
    listData2 = pylo.tuple_to_list(tupleData2);   print("Case 1:",listData2)
    listData3 = pylo.tuple_to_list(tupleData3);   print("Case 2:",listData3)
    listData4 = pylo.tuple_to_list(tupleData4);   print("Case 3:",listData4)
    listData5 = pylo.tuple_to_list(tupleData5);   print("Case 4:",listData5)
    listData6 = pylo.tuple_to_list(tupleData6);   print("Case 4:",listData6)
    listData7 = pylo.tuple_to_list(tupleData7);   print("Case 5:",listData7)
    listData8 = pylo.tuple_to_list(tupleData8);   print("Case 5:",listData8)
    listData9 = pylo.tuple_to_list(tupleData9);   print("Case 6:",listData9)
    print(f"{cp.ins_chr(n=100, unicode="-")}")
    print()
```

## Shift an Element in a List
### <span style="color:purple"> <strong> Right Shift  and Left Shift </strong> </span>

```python
    shift(data:list, direction=Move.RIGHT, qty=0, update:bool=False)

   This function shift the elements in a list to the left or right.

   update is used to save the actual list with the shift elements.
   If we set update to False, then we keep the original list as it is.
```

<span style="color:red"> <strong> Example: </strong> </span>

```python
    lst = cp.PyLO()
   
    # Right Shift List
    list_1 = [[1],[4],[5,6]]
    print(f"{cp.ins_chr(n=80, unicode="-")}")
    print(f"{cp.set_font(1,23,231)}    Shift Item in a List    {cp.reset_font()}")
    print(f"{cp.ins_chr(n=80, unicode="-")}")
    cp.ins_newline(2)
    
    #---------------------------------------------------------------------------
    print("original_list:  ", list_1, end=""); print(f"   right_shift 2, {cp.set_font(1,21,231)} update=False {cp.reset_font()}")
    newlist = lst.shift(list_1, "r", 2, False)
    print("shifted _list:  ",newlist)
    print("original_list:  ", list_1)

    print(f"{cp.ins_chr(n=80, unicode="-")}")

    print("original_list:  ", list_1,end=""); print(f"   right_shift 2, {cp.set_font(1,1,231)} update=True {cp.reset_font()}")
    newlist = lst.shift(data=list_1, direction=cp.Move.RIGHT, qty= 2, update= True)
    print("shifted _list:  ",newlist)
    print("original_list:  ", list_1)

    cp.ins_newline(2)


    # Left Shift List
    list_1 = [[1,2,3,4,5,6]]
    #---------------------------------------------------------------------------
    print("original_list:  ", list_1, end=""); print(f"   left_shift 2, {cp.set_font(1,21,231)} update=False {cp.reset_font()}")
    newlist = lst.shift(list_1, "l", 2, False)
    print("shifted _list:  ",newlist)
    print("original_list:  ", list_1)

    print(f"{cp.ins_chr(n=80, unicode="-")}")

    print("original_list:  ", list_1,end=""); print(f"   left_shift 2, {cp.set_font(1,1,231)} update=True {cp.reset_font()}")
    newlist = lst.shift(data=list_1, direction=cp.Move.LEFT, qty= 2, update= True)
    print("shifted _list:  ",newlist)
    print("original_list:  ", list_1)
```

## Swap 2 Items in a List
```python    
    swap(data:list, pos1=0, pos2=0, update:bool=False)

    This function swap two elements in a list.

    update is used to save the actual list with the swap elements.
        
    if update is set to False, then we keep the original list and save
    the new list into another variable.

    pos1 -> position 1 to be swap with position 2
    pos2 -> position 2 to be swap with position 1

    Note: If one of the position provided is out of range, the function
          will return the list as original and it will print a message
          out of range. 
```

<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    print(f"{cp.set_font(1,23,231)}    Swap Items in a List    {cp.reset_font()}")
    lst = [[1,2],[3,4],[5,6],[7,8]]
    print("original: ", lst,end=""); print("   update=False,  pos1=0, pos2=2")
    newlist = pylo.swap(data=lst, update= False, pos1= 0, pos2=2)
    print("swaped_l: ",newlist)
    print("original: ", lst)

    print(f"{cp.ins_chr(n=80, unicode="-")}")

    print("original: ", lst,end=""); print(f"   {cp.set_font(1,1,231)} update=True, {cp.reset_font()} pos1=3, pos2=0")
    newlist = pylo.swap(data=lst, update=True, pos1=3, pos2=0)
    print("swaped_l: ",newlist)
    print("original: ", lst)
```

## Dimensions of a List

```python    
    dimensions(data:list)

    This function return the number of rows and cols in a list.
    It will return the number of rows and cols in a list.
```

<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    print(f"{cp.ins_chr(n=80, unicode="-")}")
    list_1 = [1,2,3,4,5,6]
    lst_dimension = pylo.dimensions(data=list_1)
    print(f"Case 5 \u279C {lst_dimension}")

    list_1 = [[1,2],[3,4],[5,6]]
    lst_dimension = pylo.dimensions(data=list_1)
    print(f"Case 6 Max \u279C {lst_dimension}")
```


## Autofill Data in a List

```python
    autofill_data(data:list, fill_value:str="----", update:bool=False)

    This function will fill all the empty columns from the list.
    fill_value is the chr to be used to fill those columns. It can be str,
    int, float, or bool. By default it's a str type (----).
    It only works for list in the form of table.
```

<span style="color:red"> <strong> Example: </strong> </span>

```python  
    import custom_print as cp
    pylo = cp.PyLO()

    lst = [[9,8,7],[4],[5,6]]

    print("Original:",lst)
    result = pylo.autofill_data(lst, fill_value=9.8, update=False)
    print("mylist=lst, fill_value=9.8, update=False")
    print("Result  :",result)
    print("Original:",lst)

    print(f"{cp.ins_chr(n=80, unicode="-")}")
    print(f"{cp.ins_chr(n=80, unicode="-")}")

    print("Original:",lst)
    result = pylo.autofill_data(data=lst, fill_value=99, update=True)
    print("mylist=lst, fill_value=99, update=True")
    print("Result  :",result)
    print("Original:",lst)
```

## Transpose

```python
    transpose(data:list, autofill=True, fill_value="----", update:bool=False)
        
    update is used to replace original list with the transpose list.
    update is set to False to keep the original list and save
    the new list into another variable.

    When the list is not square or rectangular, the list will be filled using
    the fill_value. If the autofill is set to False, some data will be lost.
```

### Cases
| Original_list                         |      Transpose_list                           |
|---------------------------------------|-----------------------------------------------|
| 0.- pass not a list variable          | returns a empty list
| 1.- pass empty list                   | returns a empty list
|                                       | 
| 2.- [10]                              | [[10]]
| 3.- [[10]]                            | [10]
|                                       |
| 4.- [10, 20, 30]                      | [[10], [20], [30]]
| 5.- [[10, 20, 30]]                    | [10, 20, 30]
| 6.- [[10], [20], [30]]                | [[10, 20, 30]]
|                                       |
| 7.- [[1,2,3],  [4,5,6],   [7,8,9]]    | [[1,4,7], [2,5,8], [3,6,9]]
| 8.- [[1,2,3],  [4,5,6],   [7,8,9,10]] | [[1,4,7], [2,5,8], [3,6,9]]
| 9.- [[1,2,3],  [4,5,6,7], [7,8,9,10]] | [[1,4,7], [2,5,8], [3,6,9]]
| A.-[[1,2,3,4], [4,5,6],   [7,8,9]]    | [[1,4,7], [2,5,8], [3,6,9]]
|                                       |
| B.-[5, 6, [4,5], 45]                  | [[5], [6], [[4,5]], [45]]

<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    lst = [[9,8,7,1],[4,2],[5,6,0]]
    print(f"{cp.ins_chr(n=80, unicode="-")}")

    print(f"{cp.set_font(1,90,231)}autofill=True    fill_value=15    update=False  {cp.reset_font()}")
    print(f"original : {lst}")
    trans_lst = pylo.transpose(data=lst, autofill=True, fill_value=15, update=False)
    print("Transpose:",trans_lst)
    print("original :", lst)

    print(f"{cp.ins_chr(n=80, unicode="-")}")
    print(f"{cp.ins_chr(n=80, unicode="-")}")

    print(f"{cp.set_font(1,23,231)}autofill=True    fill_value=15    update=True    {cp.reset_font()}")
    print("original :", lst)
    trans_lst = pylo.transpose(data=lst, autofill=True, fill_value=15, update=True)
    print("Transpose:",trans_lst)
    print("original :", lst)
    print(f"{cp.ins_chr(n=80, unicode="-")}")


    print(f"{cp.ins_chr(n=80, unicode="-")}")
    lst = [[9,8,7,1],[4,2],[5,6,0]]

    print(f"{cp.set_font(1,21,231)}autofill=False    fill_value=15    update=False  {cp.reset_font()}")
    print(f"original : {lst}")
    trans_lst = pylo.transpose(data=lst, autofill=False, fill_value=15, update=False)
    print("Transpose:",trans_lst)
    print("original :", lst)

    print(f"{cp.ins_chr(n=80, unicode="-")}")
    print(f"{cp.ins_chr(n=80, unicode="-")}")

    print(f"{cp.set_font(1,1,231)}autofill=False    fill_value=15    update=True    {cp.reset_font()}")
    print("original :", lst)
    trans_lst = pylo.transpose(data=lst, autofill=False, fill_value=15, update=True)
    print("Transpose:",trans_lst)
    print("original :", lst)
    print(f"{cp.ins_chr(n=80, unicode="-")}")

    lst = [5, 6, [4,5], 45]
    result = pylo.transpose(lst)
    print(result)
```

## Data to String

```python
    data_to_str(data:list, update=False)

    Converts all the elements of a list to string type
```

<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    print(f"{cp.ins_chr(n=80, unicode="-")}")
    lst = [1,2,3,4,5,6]
    print(f"Original: {lst}  {cp.set_font(1,21,231)} update = False {cp.reset_font()}")
    result = pylo.data_to_str(data=lst)
    print("Result  :",result)
    print("Original:", lst)

    print(f"{cp.ins_chr(n=80, unicode="-")}")
    lst = [[1],[2],[3],[4],[5],[6]]
    print(f"Original: {lst}  {cp.set_font(1,1,231)} update = True {cp.reset_font()}")
    result = pylo.data_to_str(data=lst, update=True)
    print("Result  :",result)
    print("Original:",lst)
```

## Data to Number

```python
    data_to_num(self, data:list, fill_value=0, update=False)

    Converts all items from a list to numbers where it is possible.
    If it is not possible then it will take the fill_value provided to switch
    the value was not possible to convert. If the fill value provided is not
    a number or it is not possible to convert it to a number then it will be
    sustitute by zero, 0.
```

<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    print(f"{cp.ins_chr(n=80, unicode="-")}")

    print(f"{cp.set_font(1,90,231)}  Case 7  {cp.reset_font()}")
    lst = ["-10.5","-40",["50"],[250],["a","H"],"10"]
    print("original: ", lst)
    result = pylo.data_to_num(data=lst, fill_value=10, update=False)
    print("result  : ",result)
    print("original: ", lst)

    print(f"{cp.ins_chr(n=80, unicode="-")}")

    print("original: ", lst)
    result = pylo.data_to_num(data=lst, fill_value='A', update=True)
    print("result  : ",result)
    print("original: ", lst)
```

## Sort a List by Column

```python
sort_by_col(self, data:list, ref_col=0, sort_type:Sort_By=Sort_By.STRING, reverse_order:bool=False, update:bool=False):
```

**sort_by_col** won't sort the first row because it is considered the Header of the list.
The **sort_type** option refers to the column sort order. When the **Sort_By** is set
to STRING, it will convert all the items of the list to string type. If a column is mixed with
string type and another type, like integer or float, it will cause an <span style="color:red">***error***</span>. This method is
intended to be used with all cells filled; any empty cells will be filled automatically.

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()
tbl.msg_title = "Original"

lst  = [["ID","Names",  "Last",    "Age","Department"],
        [1,   "Juan",   "Alegria",   30,  "EE"       ],
        [17,  "Manuel", "Alvarez",   25,  "EC"       ],
        [9,   "Luis",   "Naguse",    21,  "AD"       ],
        [3,   "Pancho", "Marlo",     41,  "BE"       ],
        [2,   "Felipe", "Cautizo",   15              ]] 

tbl.print_fancy_format(lst)

result = pylo.sort_by_col(data=lst, ref_col=0, sort_type="number", reverse_order=False, update=False)
tbl.msg_title = "Sort_by Col 0. Number"
tbl.print_fancy_format(result)

tbl.msg_title = "Sort_by Col 0. String"
result = pylo.sort_by_col(data=lst, ref_col=0, sort_type="string", reverse_order=False, update=False)
tbl.print_fancy_format(result)

tbl.msg_title = "Sort_by Col 0. Number, rever_order=True, update=True"
result = pylo.sort_by_col(data=lst, ref_col=0, sort_type="number", reverse_order=True, update=True)
tbl.print_fancy_format(result)

tbl.msg_title = "New Original"
tbl.print_fancy_format(lst)


tbl.msg_title = ""
lst_2 = [10,1,5,3]
result2 = pylo.sort_by_col(data=lst_2, ref_col=0, sort_type=pylo.Sort_By.STRING, reverse_order=False)
tbl.print_fancy_format(lst_2)
tbl.print_fancy_format(result2)

result2 = pylo.sort_by_col(data=lst_2, ref_col=0, sort_type=pylo.Sort_By.NUMBER, reverse_order=True)
tbl.print_fancy_format(lst_2)
tbl.print_fancy_format(result2)
```

## Write a List Into a CSV File

write_csv_file

## Read a List From a CSV File

## Write a List Into a JSON File

## Read a List From a JSON File

> <span style="background-color:purple">
> <span style="color:yellow"><strong><i>
> Note: Although the main idea is to use list type, print_fancy_format(tbl) accepts any type of variable. Refer to Demo 1 and Demo 2. 
> </i></strong> </span> </span>


