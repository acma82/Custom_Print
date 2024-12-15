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
    shift(data, direction=Move.RIGHT, qty=0, update=False)
```

- This method shift the elements in a list to the left or right.

- update is used to save the actual list with the shift elements.

- If we set update to False, then we keep the original list as it is.


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
    swap(data, posi_1=0, posi_2=0, update=False)
```

This method swap two elements in a list.

- update is used to save the actual list with the swap elements.
        
- if update is set to False, then we keep the original list and save the new list into another variable.

- **posi_1** -> position 1 to be swap with position 2 <br>
- **posi_2** -> position 2 to be swap with position 1

- **Note:** If one of the position provided is out of range, the function will return the list as
            original and it will print a message out of range. 

<span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    print(f"{cp.set_font(1,23,231)}    Swap Items in a List    {cp.reset_font()}")
    lst = [[1,2],[3,4],[5,6],[7,8]]
    print("original: ", lst,end=""); print("   update=False,  pos1=0, pos2=2")
    newlist = pylo.swap(data=lst, update= False, posi_1= 0, posi_2=2)
    print("swaped_l: ",newlist)
    print("original: ", lst)

    print(f"{cp.ins_chr(n=80, unicode="-")}")

    print("original: ", lst,end=""); print(f"   {cp.set_font(1,1,231)} update=True, {cp.reset_font()} pos1=3, pos2=0")
    newlist = pylo.swap(data=lst, update=True, posi_1=3, posi_2=0)
    print("swaped_l: ",newlist)
    print("original: ", lst)
```

## Dimensions of a List

```python    
    dimensions(data)
```

This method returns the number of rows and cols in a list.
It will return the number of rows and cols in a list.

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
    autofill_data(data, fill_value="----", update=False)
```
This method will fill all the empty columns from the list.

- **fill_value** is the chr to be used to fill those columns. It can be str, int, float, or bool. 
  By default it's a str type (----). It only works for list in the form of table.


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
    transpose(data, autofill=True, fill_value="----", update=False)
```        
update is used to replace original list with the transpose list. update is set to False to keep
the original list and save the new list into another variable.

When the list is not square or rectangular, the list will be filled using
the fill_value. If the autofill is set to False, some data will be lost.


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
```

- This method converts all the elements of a list to string type

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
```
This method converts all items from a list to numbers where it is possible.
If it is not possible then it will take the **fill_value** provided to switch
the value where it was not possible to convert. If the **fill_value** provided is not
a number or it is not possible to convert it to a number then it will be
sustitute by zero, 0.

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
sort_by_col(self, data, ref_col=0, reverse_order=False, update=False)
```

**sort_by_col** will NOT sort the first row because it is considered the Header of the list.
If a column is mixed with string type and another type, like integer or float, it will
cause an <span style="color:red">***error***</span>. This method is intended to be used
with all cells filled with the same type per column except the header; any empty cells
will be filled automatically. If you want to fill those spots with a specific type, then
use the autofill_data method.

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

lst  = [["ID","Names",  "Last",    "Age","Department"],
        [  1, "Juan",   "Alegria",   30,  "EE"       ],
        [ 17, "Manuel", "Alvarez",   25,  "EC"       ],
        [  9, "Luis",   "Nanguse",   21,  "AD"       ],
        [  3, "Pancho", "Marlo",     41,  "BE"       ],
        [  2, "Felipe", "Cautizo",   15              ]] 

result = pylo.sort_by_col(data=lst, ref_col=0, reverse_order=False, update=False)
tbl.msg_title = "Sort_by Col 0"
tbl.print_fancy_format(result)

tbl.msg_title = "Original"
tbl.print_fancy_format(lst)

tbl.msg_title = "Sort_by Col 4"
result = pylo.sort_by_col(data=lst, ref_col=4, reverse_order=False, update=False)
tbl.print_fancy_format(result)

tbl.msg_title = "Sort_by Col 0. reverse_order=True, update=True"
result = pylo.sort_by_col(data=lst, ref_col=0, reverse_order=True, update=True)
tbl.print_fancy_format(result)

tbl.msg_title = "New Original"
tbl.print_fancy_format(lst)

tbl.msg_title = ""
lst_2 = [5,1,9,5]
result2 = pylo.sort_by_col(data=lst_2, ref_col=10, reverse_order=False, update=False)
print("\n\nResult  : reverse_order=False, update=False")
tbl.print_fancy_format(result2)
print("Original:");  tbl.print_fancy_format(lst_2)

result2 = pylo.sort_by_col(data=lst_2, ref_col=0, reverse_order=True, update=True)
print("Result  : reverse_order=True, update=True ")
tbl.print_fancy_format(result2)
print("Original:");  tbl.print_fancy_format(lst_2)
```

## Write a List Into a CSV File

```python
write_csv_file(data, file_path="CSV_List")
```

It writes a list into a **CSV** file and it returns the path where the file was saved.
The path needs to be specified as it is. Do<span style="color:red"> <strong>NOT</strong> </span>
use tilda(~) or $HOME for quick access to the path, it could cause error. The extension can be
omitted or not. If the file_path is not provided then it will create the file in the current
path under the name **CSV_List.csv**. The file_path is assumed that it will contain the name of
the file as well.



<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()


classes_methods_fancyprint = [\
    ["Header 1","Header 2",    "Header 3",            "Header 4"        ,    "Header 5"      ],
    ["Cursor",  "FontStyle",   "FancyMessage",        "FancyFormat"        , "Pen"           ],
    ["jumpTo",  "start_style", "print_fancy_message", "print_fancy_format",  "draw_line"     ],
    ["jumpxy",  "stop_style",  "print_fancy_note",    "reset_fancy_format",  "draw_rectangle"],
    ["moveTo",  "print_style", "----             ",    "----             ",  "----"          ],
    ["movexy",  "reset_style", "----             ",    "----             ",  "----"          ]]

file_path = pylo.write_csv_file(classes_methods_fancyprint)
print(file_path)


list_1 = [10,[50],[250],["H"],100]
file_path = pylo.write_csv_file(list_1, "file_1")
print(file_path)
```

## Read a List From a CSV File

```python
read_csv_file(file_path:str="CSV_List")
```

It reads a **csv** file and save it into a list. The extension can be omitted.

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl = cp.FancyFormat()


file_info = pylo.read_csv_file("CSV_List")
tbl.print_fancy_format(file_info)


file_info = pylo.read_csv_file("file_1.csv")
tbl.print_fancy_format(file_info)
```

## Write a List Into a JSON File

```python
write_json_file(data, file_path="JSON_List")
```

It writes a list into a **JSON** file and it returns the path where the file was saved.
The path needs to be specified as it is. Do<span style="color:red"> <strong>NOT</strong> </span>
use tilda(~) or $HOME for quick access to the path, it could cause error. The extension can be
omitted or not. If the file_path is not provided then it will create the file in the current
path under the name **JSON_List.json**. The file_path is assumed that it will contain the name of
the file as well.

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

class_methods = [\
    ["Header 1","Header 2",    "Header 3",            "Header 4"        ,    "Header 5"      ],
    ["Cursor",  "FontStyle",   "FancyMessage",        "FancyFormat"        , "Pen"           ],
    ["jumpTo",  "start_style", "print_fancy_message", "print_fancy_format",  "draw_line"     ],
    ["jumpxy",  "stop_style",  "print_fancy_note",    "reset_fancy_format",  "draw_rectangle"],
    ["moveTo",  "print_style", "----             ",    "----             ",  "----"          ],
    ["movexy",  "reset_style", "----             ",    "----             ",  "----"          ]]

file_path = pylo.write_json_file(class_methods)
print(file_path)


list_1 = [10,[50],[250],["H"],100]
file_path = pylo.write_json_file(list_1, "file_1.json")
print(file_path)
```

## Read a List From a JSON File

```python
read_json_file(self, file_path:str="JSON_List")
```

It reads a **json** file and save it into a list. The extension can be omitted.

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl = cp.FancyFormat()


file_info = pylo.read_json_file("JSON_List.json")
tbl.print_fancy_format(file_info)


file_info = pylo.read_json_file("file_1.json")
tbl.print_fancy_format(file_info)
```


## Delete a Column from a List

```python
delete_col(data, col_ref=0, update=False)
```
It deletes a column from a list. If the col_ref is out of range, it will return a message,
**col_ref out of range in one or more columns from the list**, along with an empty list as
a result. This method was intended to be used with complete list as the example below.
**Notice:** that autofill_data method can be used if wished.

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl = cp.FancyFormat()

print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,23,231)} Case 5. Col_ref = 0, update=True {cp.reset_font()}")
lst_5 = [1,2,3,4,5,6]
print("Original    : ",lst_5)
result = pylo.delete_col(lst_5, 0, update=True)
print("Result      : ",result)
print("New Original: ",lst_5)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print(f"{cp.set_font(1,23,231)} Case 8. Col_ref = 0, update=False {cp.reset_font()}")
lst_8 = [[1,2,3,4,5,6]]
print("Original    : ",lst_8)
result = pylo.delete_col(lst_8, 1, update=False)
print("Result      : ",result)
print("New Original: ",lst_8)

print(f"{cp.ins_chr(n=80, unicode="-")}")

class_methods = [\
    ["Cursor",  "FontStyle",    "FancyMessage",          "FancyFormat"        ],
    ["jumpTo",  "start_style",  "print_fancy_message",   "print_fancy_format" ],
    ["jumpxy",  "stop_style",   "print_fancy_note",      "reset_fancy_format" ],
    ["moveTo",  "print_style",  "----             ",      "----             " ],
    ["movexy",  "reset_style",  "----             ",      "----             " ]]

tbl.bg_title = 90; tbl.align_title = cp.Align.CENTER
tbl.msg_title = " col_ref = 2, update=False "
tbl.print_fancy_format(class_methods)
tbl.msg_title = " Result After Deleting col 2"
new_list = pylo.delete_col(class_methods, 12)
tbl.print_fancy_format(new_list)
```

## make a list to a vector form list

```python
make_to_vector(data)
```
This function makes any list in a form as a vector. [1,2,3,4,5,etc.],up to 4 brackets. '''


<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

list_0 = [["A"],["B"]]
result = pylo.make_to_vector(list_0)
print(result)

list_1 = [5,6,[1,2,3],[1,0,3]]
result = pylo.make_to_vector(list_1)
print(result)

list_2 = [[5,6,9],[1,2,3],[1,0,3]]
result = pylo.make_to_vector(list_2)
print(result)

list_2 = [[1,2],["H",99],[[3,[5],[95,3],[5]],3],3,[5,6,7,8]]
result = pylo.make_to_vector(list_2)
print(result)
```


## Add a Column to a List

```python
add_col(data, new_col_data, col_posi=0)
```
This method adds a column into the list in a specific postion.
The original list has to be in the form of a matrix or table 
and the column to be added needs to be as a vector list.            


<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

tbl.bg_title = 90
tbl.align_title = cp.Align.LEFT

#------------------------------------------------------------------------------
# Adding list_2 as one col in list_1
tbl.msg_title = " List_1 "
list_1 = [["Header_1","Header_2"],["R1_C1","R1_C2"], ["R2_C1","R2_C2"]]
tbl.print_fancy_format(list_1)

tbl.msg_title = " List_2 to be added to List_1 as Col, pos=1 "
list_2 = ["New_Header",   "New_Row_Col",  "New_Row_Col"]
tbl.print_fancy_format(list_2)

tbl.msg_title = " New Complete List_1_2 "
list_1_2 = pylo.add_col(data=list_1, new_col_data=list_2, col_posi=1)
tbl.print_fancy_format(list_1_2)


#------------------------------------------------------------------------------
# Adding the list_4 as more Rows in list_3
list_3 = [["Header_1","Header_2","Header_3"],
          ["R1_C1","R1_C2","R1_C3"],
          ["R2_C1","R2_C2","R2_C3"]]

list_4 = [["R3_C1","R3_C2","R3_C3"],
          ["R4_C1","R4_C2","R4_C3"]]

for row in range(len(list_4)): list_3.append(list_4[row])

tbl.bg_title = 23; tbl.msg_title = " Adding list_4 as rows in list_3 "
tbl.print_fancy_format(list_3)


#------------------------------------------------------------------------------
# Adding list_6 as columns in list_5
tbl.bg_title = 1
tbl.msg_title = " Adding list_6 as cols in list_5 at the end "

list_5  = [["Header_1","Header_2","Header_3"],
          ["R1_C1","R1_C2","R1_C3"],
          ["R2_C1","R2_C2","R2_C3"]]

list_6 = [["R3_C1","R3_C2","R3_C3"],
          ["R4_C1","R4_C2","R4_C3"]]

for rows in range(len(list_6)):
    list_5_6 = pylo.add_col(data=list_5, new_col_data=list_6[rows], col_posi=len(list_5[0]))

tbl.print_fancy_format(list_5_6)
print(list_5_6)
```

## Replace an Item from a List

```python
replace(self, data:list, old:int|str, new:int|str, update=False)
```

It replaces a value for another value in a list
The list can be a vector [1,2,3,4] or a matrix (table) [[1,2],[3,1]]
or a combination of them [[1,2],[3,3,3],3,[5,6,7,8]]

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

print(f"{cp.set_font(1,1,15)} Replacing 3 for A {cp.reset_font()}")
list_1 = [[11,[10,3],12,3],[14,15,3],[12,3,3]]
print("Original:",list_1)
resutl = pylo.replace(data=list_1, old=3, new="A", update=True)
print("Result  :",resutl)
print("Original:",list_1)
```

## number a list
```python
number(data, start_number=0, id_txt="Id", renumber=False, update=False)
```

This method number the rows in a list by adding a column to the left side.
If the renumber is set to true then it will not add a new column but instead
it will renumerate the existen one.

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

tbl.bg_title = 90
tbl.align_title = cp.Align.LEFT
tbl.bg_title = 1
tbl.msg_title = " Adding list_6 as cols in list_5 at the end "

#-----------------------------------------------------------------------------------
list_5  = [["Header_1","Header_2","Header_3"],
          ["R1_C1","R1_C2","R1_C3"],
          ["R2_C1","R2_C2","R2_C3"]]

list_6 = [["R3_C1","R3_C2","R3_C3"],
          ["R4_C1","R4_C2","R4_C3"]]

for rows in range(len(list_6)):
    list_5_6 = pylo.add_col(data=list_5, new_col_data=list_6[rows], col_posi=len(list_5[0]))

tbl.print_fancy_format(list_5_6)
print(list_5_6)

#-----------------------------------------------------------------------------------
tbl.msg_title = " Adding the row numbers "
pylo.number(data=list_5_6, start_number=1, id_txt="ID", renumber=False, update=True)
tbl.print_fancy_format(list_5_6)

#-----------------------------------------------------------------------------------
tmp = [0,"RC","RRC","RRCC","RRRCC","RRRCCC"]
list_5_6.append(tmp)
tbl.msg_title = " Adding a new row "
tbl.print_fancy_format(list_5_6)

#-----------------------------------------------------------------------------------
pylo.number(data=list_5_6, start_number=1, id_txt="ID", renumber=True, update=True)
tbl.msg_title = " renumerating the rows "
tbl.print_fancy_format(list_5_6)
```

## Join 2 List as a Vector

```python
join_as_vector(data, list_to_join, col_posi=0)
```

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

list_1 = [[0,1],[2,3,4],5,[6,7,8]]
list_2 = [99,98,97]

print("List_1: ",list_1)
print("List_2: ",list_2)
print("\n")

for n in range(len(list_1)):
    join_list = pylo.join_as_vector(data=list_1, data2join=list_2, col_pos=n)
    print(f"Result:{n} {join_list}")

join_list = pylo.join_as_vector(data=list_1, data2join=list_2, col_pos=9)
print(f"Result:9 {join_list}")
```
## Find a Value in a List

```python
find_value(data:list, ref)
```
This method finds a value into a list and returns the location of the value.
Up to 4 brackets.

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

list_1 = [["Header 1", "Header 2", "Header 3",0],
          ["Datito 1", "Datito 2", "Datito 3",1],
          ["Datito 4", "Datito 5", "Datito 6",2],
          ["Datito 1", "Datito 2", "Datito 1",3]]

list_2 = [2,5,[2,7],8,8,9,"A",[8,2,2]]

list_3 = ["miGueL", "hellO",[7,8,"bB"]]

result = pylo.find_value(list_1, "DATITO 1")
print(result)

result = pylo.find_value(list_2, 8)
print(result)


result = pylo.find_value(list_3, "BB")
print(result)
```

## Conversion to Lower Case

```python
lower_case(data:list)
```

This method lower case all the items in a list.

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()


list_1 = [["HeadeR 1", "HeadeR 2", "HeadeR 3",0],
          ["DatitO 1", "DatitO 2", "DatitO 3",1],
          ["DatitO 4", "DatitO 5", "DatitO 6",2],
          ["DatitO 1", "DatitO 2", "DatitO 1",3]]

mylower = pylo.set_to_lower(list_1)
print(mylower)
```


## Conversion to Upper Case

```python
upper_case(self, data:list)
```

This method upper case all the items in a list.

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()


list_1 = [["HeadeR 1", "HeadeR 2", "HeadeR 3",0],
          ["DatitO 1", "DatitO 2", "DatitO 3",1],
          ["DatitO 4", "DatitO 5", "DatitO 6",2],
          ["DatitO 1", "DatitO 2", "DatitO 1",3]]

myupper = pylo.set_to_upper(list_1)
print(myupper)
```

## Conversion to Capitalize Case

```python
capitalize_case(data:list)
```

 This method capitalize all the items in a list.

<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

list_1 = [["HeadeR 1", "HeadeR 2", "HeadeR 3",0],
          ["DatitO 1", "DatitO 2", "DatitO 3",1],
          ["DatitO 4", "DatitO 5", "DatitO 6",2],
          ["DatitO 1", "DatitO 2", "DatitO 1",3]]

list_2 = ["miGueL", "hellO",[7,8,"bB"]]

mycapitalize = pylo.set_to_capitalize(list_1)
print(mycapitalize)

mycapitalize = pylo.set_to_capitalize(list_2)
print(mycapitalize)
```

## Merge 2 List
```python
merge(list_1, list_2, posi=0, merge_by=Appending.ROWS)
```

This method merge two list with two option of merge. It can be merge by ROWS
or by COLUMNS. It also, provides the option to pick the specific position
to start the merge on list_1. <br>
**Notice** that the rows in list_2 will be all the columns to be passed to the list_1.


<span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True

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

tbl.msg_title = " List 1: Methods "
tbl.print_fancy_format(methods)

tbl.msg_title = " List 2: People "
tbl.print_fancy_format(people)

tbl.msg_title = " Merge List 1 and List 2 as COLUMNS "
merge_list = pylo.merge(list_1=methods, list_2=people, posi=8, merge_by=pylo.Appending.COLUMNS) 
tbl.print_fancy_format(merge_list)

tbl.msg_title = " Merge List 1 and List 2 as ROWS "
merge_list = pylo.merge(list_1=methods, list_2=people, posi=8, merge_by=pylo.Appending.ROWS)
print(merge_list)
tbl.print_fancy_format(merge_list)


print(" Original ")
print(methods)
#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
cp.ins_newline(2)
print(people)
#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
cp.ins_newline(2)
print(merge_list)
#-------------------------------------------------------------------------------
print(cp.ins_chr(70,"-"))
#-------------------------------------------------------------------------------
```


> <span style="background-color:purple">
> <span style="color:yellow"><strong><i>
> Note: Although the main idea is to use list type, print_fancy_format(tbl) accepts any type of variable. Refer to Demo 1 and Demo 2. 
> </i></strong> </span> </span>


