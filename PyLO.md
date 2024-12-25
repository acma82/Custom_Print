#### [Back](README.md)
# PyLO Class 
1. **Aid Classes**
    
    * [**Appending**](#appending)
        * ROWS
        * COLUMNS

    * [**Case**](#case)
        * UPPER
        * LOWER
        * CAPITALIZE
        * NONE

    * [**Order**](#order)
        * ASCENDING
        * DESCENDING
    
    * [**Str_List_Option**](#str_list_option)
        * WORD_BY_WORD
        * LINE_BY_LINE


2. **Conversion Methods**
    * [**bool_to_list**](#bool-type-to-list-type)
    * [**int_to_list**](#integer-type-to-list-type)
    * [**float_to_list**](#float-type-to-list-type)
    * [**complex_to_list**](#complex-type-to-list-type)
    * [**str_to_list**](#string-type-to-list-type)
    * [**dict_to_list**](#dictionary-type-to-list-type)
    * [**range_to_list**](#range-type-to-list-type)
    * [**set_to_list**](#set-or-frozenset-type-to-list-type)
    * [**tuple_to_list**](#tuple-type-to-list-type)
    * [**data_to_str**](#data-to-string)
    * [**data_to_num**](#data-to-number)

3.  **File Methods**
    * [**write_csv_file**](#write-a-list-into-a-csv-file)
    * [**read_csv_file**](#read-a-list-from-a-csv-file)
    * [**write_json_file**](#write-a-list-into-a-json-file)
    * [**read_json_file**](#read-a-list-from-a-json-file)

4. **Case Methods**
    * [**lower_case**](#lower-case)
    * [**upper_case**](#upper-case)
    * [**capitalize_case**](#capitalize-case)
    * [**update_case**](#update-case)
    * [**update_case_col**](#update-case-col)

5. **Table Methods**
    * [**autofill_data**](#autofill-data)
    * [**dimensions**](#list-dimensions)

    * [**find_value**](#find-value)
    * [**replace_value**](#replace-value)
    * [**delete_value**](#delete-value)

    * [**add_col**](#add-a-new-column-to-a-list)
    * [**delete_col**](#delete-a-column)

    * [**make_to_vector**](#make-a-list-into-a-vector-list)
    * [**join_as_vector**](#join-tow-list-as-a-vector)

    * [**shift**](#shift)
    * [**swap**](#swap)

    * [**number**](#add-number-of-rows-to-a-list)
    * [**transpose**](#transpose)
    * [**merge**](#merge)
    * [**reversed_row_order**](#reversed-row-order)
    * [**sort_rows_by_cols**](#sort-rows-by-columns)
    * [**sort_cols**](#sort-columns)
 
<!-- ---------------------------------- -->
<!-- Appending                          -->
<!-- ---------------------------------- -->
## Appending
[**Top**](#pylo-class)
This class is used with ***merge*** method. There are two options.
* Appending.ROWS
* Appending.COLUMNS


<!-- ---------------------------------- -->
<!-- Case                               -->
<!-- ---------------------------------- -->
## Case
This class is used with the methods ***update_case*** and ***update_case_col***. There are four options.
* Case.LOWER
* Case.UPPER
* Case.CAPITALIZE
* Case.NONE


<!-- ---------------------------------- -->
<!-- Order                              -->
<!-- ---------------------------------- -->
## Order
[**Top**](#pylo-class)
This class is used with ***sort_cols*** method. There are two options.
* Order.ASCENDING
* Order.DESCENDING


<!-- ---------------------------------- -->
<!-- String to List Option              -->
<!-- ---------------------------------- -->
## Str_List_Option
This class is used with ***str_to_list*** method. There are two options.
* WORD_BY_WORD
* LINE_BY_LINE


<!-- ---------------------------------- -->
<!-- All Conversion Methods             -->
<!-- ---------------------------------- -->
# Conversions

## <span style="color:purple"> <strong> Bool Type to List Type </strong> </span> 

```python
bool_to_list(data, convert_to_str=False)
```
This method sets a bool variable into a list where ***data*** is the bool type. It contains a parameter, ***convert_to_str***, with two options:

1. False: It sets the bool inside the list as a bool type.
2. True: It sets the bool inside the list as a str type.

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()
    
    variable = True
    result = pylo.bool_to_list(data=variable, convert_to_str=False)
    print(result)
    result = pylo.bool_to_list(data=variable, convert_to_str=True)
    print(result) 
```


## <span style="color:purple"> <strong> Integer Type to List Type </strong> </span>

```python
int_to_list(data, convert_to_str=False)
```
This method sets an int variable into a list where ***data*** is the int type. It contains a parameter, ***convert_to_str***, with two options:

1. False: It sets the int inside the list as a int type.
2. True: It sets the  int inside the list as a str type.

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()
    
    variable = 10
    result = pylo.int_to_list(data=variable, convert_to_str=False)
    print(result)
    result = pylo.int_to_list(data=variable, convert_to_str=True)
    print(result)
```


## <span style="color:purple"> <strong> Float Type to List Type </strong> </span>

```python
float_to_list(data, convert_to_str=False)
```
This method sets an int variable into a list where ***data*** is the float type. It contains a parameter, ***convert_to_str***, with two options:

1. False: It sets the float inside the list as a float type.
2. True:  It sets the float inside the list as a str type.

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span> 


```python
    import custom_print as cp
    pylo = cp.PyLO()
    
    variable = 5.5
    result = pylo.float_to_list(data=variable, convert_to_str=False)
    print(result)
    result = pylo.float_to_list(data=variable, convert_to_str=True)
    print(result)
```


## <span style="color:purple"> <strong> Complex Type to List Type </strong> </span>
[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
    import custom_print as cp
    pylo = cp.PyLO()

    variable = 5+5j
    result = pylo.complex_to_list(variable, False)
    print(result)
    result = pylo.complex_to_list(variable, True)
    print(result)
```

## <span style="color:purple"> <strong> String Type to List Type </strong> </span>

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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

## <span style="color:purple"> <strong> Dictionary Type to List Type </strong> </span>

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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

## <span style="color:purple"> <strong> Range Type to List Type </strong> </span>

>   | Note: values for range            |                                               |
>   |-----------------------------------|-----------------------------------------------|
>   | convert_to_str = True/False       | layout="vertical"/"horizontal" or "h"/"v"     |
>   | header_title = ""                 | this will put Range Value(s) for header_title |
>   | header_title = None or "none"     | This won't set any header_title               |
>   | header_title = "Any Title Header" | This will set the header_title                | 

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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


## <span style="color:purple"> <strong> Set or Frozenset Type to List Type </strong> </span>

>   | Note: values for set              |                                               |
>   |-----------------------------------|-----------------------------------------------|
>   | convert_to_str = True/False       | layout="vertical"/"horizontal" or "h"/"v"     |
>   | header_title = ""                 | this will put Set Value(s) for header_title   |
>   | header_title = None/"none"        | It won't set any header_title                 |
>   | header_title = "Any Title Header" | This will set the header_title                |

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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

## <span style="color:purple"> <strong> Tuple Type to List Type </strong> </span>

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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


<!-- ---------------------------------- -->
<!-- data to string                     -->
<!-- ---------------------------------- -->
## Data to String

```python
    data_to_str(data, update=False)
```

- This method converts all the elements of a list to string type

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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

<!-- ---------------------------------- -->
<!-- data to number                     -->
<!-- ---------------------------------- -->
## Data to Number

```python
    data_to_num(self, data, fill_value=0, update=False)
```
This method converts all items from a list to numbers where it is possible.
If it is not possible then it will take the **fill_value** provided to switch
the value where it was not possible to convert. If the **fill_value** provided is not
a number or it is not possible to convert it to a number then it will be
sustitute by zero, 0.

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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




<!-- ---------------------------------- -->
<!-- File Methods                       -->
<!-- ---------------------------------- -->
## Write a List Into a CSV File

```python
write_csv_file(data, file_path="CSV_List")
```

It writes a list into a **CSV** file and it returns the path where the file was saved.
The path needs to be specified as it is. Do<span style="color:red"> <strong>NOT</strong> </span>
use tilda(~) or $HOME for quick access to the path, it could cause error. The extension can be
omitted. If the file_path is not provided then it will create the file in the current
path under the name **CSV_List.csv**. The file_path is assumed that it will contain the name of
the file as well.



[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl = cp.FancyFormat()


file_info = pylo.read_json_file("JSON_List.json")
tbl.print_fancy_format(file_info)


file_info = pylo.read_json_file("file_1.json")
tbl.print_fancy_format(file_info)
```

<!-- ---------------------------------- -->
<!-- Lower Case Method                  -->
<!-- ---------------------------------- -->
## Lower Case
 This method lower case all the items in a list.

```python
lower_case(data)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

list_1 = [["HeadeR 1", "HeadeR 2", "HeadeR 3",0],
          ["DatitO 1", "DatitO 2", "DatitO 3",1],
          ["DatitO 4", "DatitO 5", "DatitO 6",0],
          ["DatitO 1", "DatitO 2", "DatitO 1",3]]

list_2 = ["miGUEL", "heLLO",[7,8,"bBBB"]]


lowerl1 = pylo.lower_case(list_1)
print(lowerl1)
cp.ins_newline(3)
lowerl2 = pylo.lower_case(list_2)
print(lowerl2)
```


<!-- ---------------------------------- -->
<!-- Upper Case Method                  -->
<!-- ---------------------------------- -->
## Upper Case
This method upper case all the items in a list.

```python
upper_case(data)
```
[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()


list_1 = [["HeadeR 1", "HeadeR 2", "HeadeR 3",0],
          ["DatitO 1", "DatitO 2", "DatitO 3",1],
          ["DatitO 4", "DatitO 5", "DatitO 6",0],
          ["DatitO 1", "DatitO 2", "DatitO 1",3]]

list_2 = ["miGUEL", "heLLO",[7,8,"bBBB"]]


upperl1 = pylo.upper_case(list_1)
print(upperl1)
cp.ins_newline(3)
upperl2 = pylo.upper_case(list_2)
print(upperl2)
```


<!-- ---------------------------------- -->
<!-- Capitalize Case Method             -->
<!-- ---------------------------------- -->
## Capitalize Case
This method capitalize all the items in a list.

```python
upper_capitalize(data)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()


list_1 = [["HeadeR 1", "HeadeR 2", "HeadeR 3",0],
          ["DatitO 1", "DatitO 2", "DatitO 3",1],
          ["DatitO 4", "DatitO 5", "DatitO 6",0],
          ["DatitO 1", "DatitO 2", "DatitO 1",3]]

list_2 = ["miGUEL", "heLLO",[7,8,"bBBB"]]


capitalizel1 = pylo.capitalize_case(list_1)
print(capitalizel1)
cp.ins_newline(3)
capitalizel2 = pylo.capitalize_case(list_2)
print(capitalizel2)
```


<!-- ---------------------------------- -->
<!-- Update Case Method                 -->
<!-- ---------------------------------- -->
## Update Case
This method updates the case to the headers and the data.

```python
update_case(data, header_case=Case.CAPITALIZE, data_case=Case.LOWER, update=False)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

tbl  = cp.FancyFormat()
tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True
tbl.align_title = cp.Align.CENTER

#         0           1          2            3         4
l1 = [["NaMeS",    "LaStS",    "AgeS",  "DeparTmenT", "AWeB"    ],
      ["MigueL",   "AC",       40,         "EE",      "UnO"     ],
      ["TyleR",    "HiG",      35,         "ECE",     "DoS"     ],
      ["AleX",     "CalL",     38,         "EE",      "TreS"    ],
      ["MatT",     "ArmacI",   40,         "CS",      "CuatrO"  ]]

#l1 = [["NaMeS",    "LaStS",    "AgeS",  "DeparTmenT", "AWeB"]]

result = pylo.update_case(l1, pylo.Case.UPPER, pylo.Case.LOWER, False)
tbl.msg_title = " Headers Upper, Data Lower "; tbl.print_fancy_format(result)
tbl.msg_title = " Original List ";             tbl.print_fancy_format(l1)

result = pylo.update_case(data=l1, header_case=pylo.Case.CAPITALIZE, data_case=pylo.Case.LOWER, update=False)
tbl.msg_title = " Headers Capitalize, Data Lower "; tbl.print_fancy_format(result)
tbl.msg_title = " Original List ";                  tbl.print_fancy_format(l1)

result = pylo.update_case(data=l1, header_case=pylo.Case.LOWER, data_case=pylo.Case.UPPER, update=True)
tbl.msg_title = " Headers Lower, Data Upper. update=True "; tbl.print_fancy_format(result)
tbl.msg_title = " Original List ";             tbl.print_fancy_format(l1)
```


<!-- ---------------------------------- -->
<!-- Update Case Col Method             -->
<!-- ---------------------------------- -->
## Update Case Col
This method updates the case for a specific column, header and data.
Notice that the list has to be a mxn list, otherwise it will consider only the data case.

```python
update_case_col(data, header_case=Case.CAPITALIZE, data_case=Case.LOWER, col_ref=0, update=False)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

tbl  = cp.FancyFormat()
tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True
tbl.align_title = cp.Align.CENTER

#         0           1          2            3         4
l1 = [["NaMeS",    "LaStS",    "AgeS",  "DeparTmenT", "AWeB"    ],
      ["MigueL",   "AC",       40,         "EE",      "UnO"     ],
      ["TyleR",    "HiG",      35,         "ECE",     "DoS"     ],
      ["AleX",     "CalL",     38,         "EE",      "TreS"    ],
      ["MatT",     "ArmacI",   40,         "CS",      "CuatrO"  ]]


result = pylo.update_case_col(data=l1, header_case="capitalize", data_case="LOWER", col_ref=4, update=False)
tbl.msg_title = " Header=Capitalize, Data=Lower, col_ref=4, Update=False"
tbl.print_fancy_format(result)

cp.ins_newline(2)

result = pylo.update_case_col(data=l1, header_case=pylo.Case.LOWER, data_case=pylo.Case.UPPER, col_ref=4, update=True)
tbl.msg_title = " Header=Lower, Data=Upper, col_ref=4, Update=True"
tbl.print_fancy_format(result)
tbl.msg_title = " Original"
tbl.print_fancy_format(l1)
```


<!-- ---------------------------------- -->
<!-- Autofill Data Method               -->
<!-- ---------------------------------- -->
## Autofill Data

```python
autofill_data(data, fill_value="----", update=False)
autofill_data(list, str/int/float, boolean)
```

This function will fill all the empty columns from the list.
fill_value is the chr to be used to fill those columns. It can be str,
int, float, or bool. By default it's a str type (----).

**Notice** that the list has to be a mxn list, otherwise it will return the same list.

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

lst = [[9,8,7],[4],[5,6]]

print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")

print("Original:",lst)
result = pylo.autofill_data(lst)
print("Using default values")
print("Result  :",result)
print("Original:",lst)


print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")


print("Original:",lst)
result = pylo.autofill_data(lst, fill_value=9.8, update=False)
print("mylist=lst, fill_value=9.8, update=False")
print("Result  :",result)
print("Original:",lst)


print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")


print("Original:",lst)
result = pylo.autofill_data(data=lst, fill_value=99, update=False)
print("mylist=lst, fill_value=99, update=False")
print("Result  :",result)
print("Original:",lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")

print("Original:",lst)
result = pylo.autofill_data(data=lst, fill_value="AB", update=True)
print("mylist=lst, fill_value=\"AB\", update=True")
print("Result  :",result)
print("Original:",lst)
```


<!-- ---------------------------------- -->
<!-- List Dimensions Method             -->
<!-- ---------------------------------- -->
## List Dimensions
This function return the number of rows and cols in a list.

```python
lst_dimension = dimensions(data)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

msg = f'''
   Options                             Results                           Cases
   list_1 = "hello"                    incorrect_variable_type             1
   list_1 = []                         empty_list                          2
   list_1 = [5]                        one_item_no_row                     3
   list_1 = [[1]]                      one_item_one_row                    4
   list_1 = [1,2,3,4,5,6]              multiple_items_no_row               5
   list_1 = [[1,2],[3,4],[5,6]]        multiple_items_multiple_rows        6
   list_1 = [[1],[4],[5,6,7]]
   list_1 = [10,[50],[250],["H"],100]  mix_items                           7
   list_1 = [[1,2,3,4,5,6]]            multiple_items_one_row              8 
   '''
print(msg)

print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = "Hello"
lst_dimension = pylo.dimensions(data=list_1)
print(f"Case 1 \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = []
lst_dimension = pylo.dimensions(data=list_1)
print(f"Case 2 \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = [5]
lst_dimension = pylo.dimensions(data=list_1)
print(f"Case 3 \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = [[1]]
lst_dimension = pylo.dimensions(data=list_1)
print(f"Case 4 \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = [1,2,3,4,5,6]
lst_dimension = pylo.dimensions(data=list_1)
print(f"Case 5 \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = [[1,2],[3,4],[5,6]]
lst_dimension = pylo.dimensions(data=list_1)
print(f"Case 6 Max \u279C {lst_dimension}")


list_1 = [[1],[4],[5,6,7]]
lst_dimension = pylo.dimensions(data=list_1)
print(f"Case 6 Min \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = [[10],[50],[250],["H"],100]
lst_dimension = pylo.dimensions(data=list_1)
print(f"Case 7 \u279C {lst_dimension}")


print(f"{cp.ins_chr(n=80, unicode="-")}")

print(f"{cp.ins_chr(n=80, unicode="-")}")
list_1 = [[1,2,3,4,5,6]]
lst_dimension = pylo.dimensions(data=list_1)
print(f"Case 8 \u279C {lst_dimension}")
```

<!-- ---------------------------------- -->
<!-- Find Value Method                  -->
<!-- ---------------------------------- -->
## Find Value
This method finds a value into a list and returns the location of the value in a list.
Up to 4 brackets. <br>
**Notice** that Numbers are ***NOT*** Case Sensitive

```python
result = find_value(data, ref, case_sensitive=False)       
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import copy
import custom_print as cp

tbl = cp.FancyFormat()
pylo = cp.PyLO()

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
```


<!-- ---------------------------------- -->
<!-- Replace Value Method               -->
<!-- ---------------------------------- -->
## Replace Value
It replaces an item value for another in a list
The list can be a vector [1,2,3,4] or a matrix (table) [[1,2],[3,1]]
or a combination of them [[1,2],[3,3,3],3,[5,6,7,8]] <br>
**Notice** that Numbers are ***NOT*** Case Sensitive

```python
new_lst = replace_value(data, old, new, case_sensitive=True, update=False)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

print(f"{cp.set_font(1,1,15)} old=3, new=\"NEW\", case_sensitive=True, update=False {cp.reset_font()}")
list_1 = [[11,[10,3],12,3],[14,15,3],[12,3,3]]
print("Original:",list_1)
new_lst = pylo.replace_value(list_1, old=3, new="NEW", case_sensitive=True, update=False)
print("Result  :",new_lst)
print("Original:",list_1)

cp.ins_newline(2)

list_2 = [["HeadeR 1", "HeadeR 2", "HeadeR 3",0],
          ["DatitO 1", "DatitO 2", "DatitO 3",1],
          ["DatitO 4", "DatitO 5", "DatitO 6",0],
          ["DatitO 1", "DatitO 2", "DatitO 1",3]]


print(f"{cp.set_font(1,1,15)} old=\"datito 1\", new=\"NEW\", case_sensitive=False, update=True {cp.reset_font()}")
new_lst = pylo.replace_value(data=list_2, old="datito 1", new="NEW", case_sensitive=False, update=True)
print("Result  :",new_lst)
cp.ins_newline(2)
print(list_2)
```

<!-- ---------------------------------- -->
<!-- Delete Value Method                -->
<!-- ---------------------------------- -->
## Delete Value
This method delete an item from the list. <br>
**Notice** that Numbers are ***NOT*** Case Sensitive

```python
new_lst = delete_item(data, ref="", case_sensitive=True, update=False)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

people = [\
      ["Names",  "Lasts",   "Age"],
      ["Pancho", "Melti",    50  ],
      ["Javier", "Nangy",    32  ],
      ["Melony", "Archi",    40  ],
      ["Jose",   "Valvimar", 18  ]]
tbl.msg_title = " Original People List "
tbl.print_fancy_format(people)

print(f"{cp.set_font(1,23,231)} Delete age item on header with case_sensitive=False, update=True. {cp.reset_font()}")
new_people = pylo.delete_value(data=people, value="age", case_sensitive=False, update=True)
print(new_people)
print(f"{cp.set_font(1,23,231)} Original {cp.reset_font()}")
print(people)

cp.ins_newline(2)


print(f"{cp.set_font(1,23,231)} Delete 3 case_sensitive=False, update=False. {cp.reset_font()}")
numbers = [[11,[10,3],12,3],[14,15,3],[12,3,3]]
new_numbers = pylo.delete_value(numbers, 3, False, False)
print("3 is gone: ",new_numbers)
print("Original : ",numbers)
```



<!-- ---------------------------------- -->
<!--  Add a New Column to a List Method -->
<!-- ---------------------------------- -->
## Add a New Column to a List
This method adds a column into the list in a specific postion.
The original list has to be in the form of a matrix or table 
and the column to be added needs to be as a vector list.

Notice that if you want to add more than one column at same time, use the merge method.
Otherwise use a for loop as the example below will solve the problem.

Ex.
   data = [["H1","H2"],["R1C1","R1C2"], ["R2C1","R2C2"]]
   new_col_data = ["New_Header",   "New_Row_Col",  "New_Row_Col"]
   result = add_col(data, new_col_data, 1)

```python
new_list = add_col(data, col_data, posi=0)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

tbl.bg_title = 90
tbl.align_title = cp.Align.LEFT

#------------------------------------------------------------------------------
# Adding list_2 as one col in list_1
tbl.msg_title = " List_1 "
list_1 = [["Header_1", "Header_2"],
          ["R1_C1",    "R1_C2"],
          ["R2_C1",    "R2_C2"]]

tbl.print_fancy_format(list_1)

tbl.msg_title = " List_2 to be added to List_1 as Col, pos=1 "
list_2 = ["New_Header",   "New_Row_Col",  "New_Row_Col"]
tbl.print_fancy_format(list_2)

tbl.msg_title = " New Complete List_1_2 "
tbl.msg_footnote = " data=list_1, col_data=list_2, posi=1 "
list_1_2 = pylo.add_col(data=list_1, col_data=list_2, posi=1)
tbl.print_fancy_format(list_1_2)
tbl.msg_footnote = ""


# Adding list_4 as columns in list_3
cp.ins_newline(2)
tbl.msg_title = ""
tbl.bg_title = 1

tbl.msg_title = " List 3 "
list_3  = [["Header_1","Header_2","Header_3"],
           ["R1_C1",   "R1_C2",   "R1_C3"],
           ["R2_C1",   "R2_C2",   "R2_C3"]]
tbl.print_fancy_format(list_3)

tbl.msg_title = " List 4 "
list_4 = [["R3_C1","R3_C2","R3_C3"],
          ["R4_C1","R4_C2","R4_C3"]]
tbl.print_fancy_format(list_4)

# add cols into another list merge in horizontal
tmp = list_3
for rows in range(len(list_4)):
    tmp = pylo.add_col(data=tmp, col_data=list_4[rows], posi=len(tmp)+1)
tbl.print_fancy_format(tmp, cp.Line_Style.DOUBLE)

tmp = list_3
for rows in range(len(list_4)):
    tmp = pylo.add_col(data=tmp, col_data=list_4[rows], posi=len(tmp))
tbl.print_fancy_format(tmp, cp.Line_Style.DOUBLE)

```


<!-- ---------------------------------- -->
<!-- Delete a Column In a List Method   -->
<!-- ---------------------------------- -->
## Delete a Column

It deletes a specific column from the list

```python
new_list = delete_col(data, index=0, update=False)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl = cp.FancyFormat()

methods = [\
    ["Cursor",  "FontStyle"  ,  "FancyMessage"       ,  "Pen"           ],
    ["jumpTo",  "start_style",  "print_fancy_message",  "draw_line"     ],
    ["jumpxy",  "stop_style" ,  "print_fancy_note"   ,  "draw_rectangle"],
    ["moveTo",  "print_style",  "----"               ,  "----"          ],
    ["movexy",  "reset_style",  "----"               ,  "----"          ]]

tbl.bg_title = 90; tbl.align_title = cp.Align.CENTER
tbl.msg_title = " Original, index = 2, update=False "
tbl.print_fancy_format(methods)

tbl.msg_title = " Result After Deleting col 2 "
new_list = pylo.delete_col(methods, 2)
tbl.print_fancy_format(new_list)
```


<!-- ---------------------------------- -->
<!-- Make a List to Avector Method      -->
<!-- ---------------------------------- -->
## Make a List into a Vector List
This function makes any list in a form as a vector. [1,2,3,4,5,etc.],
up to 4 brackets.

```python
new_list = make_to_vector(data)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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

list_2 = [[1,2],["Hello",99],[[3,[5],[95,3],[5]],3],3,[5,6,7,8]]
result = pylo.make_to_vector(list_2)
print(result)

list_2 = [10,"MiGueL", "HellO",7]
result = pylo.make_to_vector(list_2)
print(result)
```


<!-- ---------------------------------- -->
<!-- Join 2 List as Vector Method       -->
<!-- ---------------------------------- -->
## Join Tow List as a Vector

It joins two list as a vector, join_list = [1,2,3,4,5,etc.]

```python
new_list = join_as_vector(data, list_to_join, col_posi=0)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

list_1 = [[0,1],[2,3,4],5,[6,7,8]]
list_2 = [99,98,97]

print("List_1: ",list_1)
print("List_2: ",list_2)
print("\n")

for n in range(len(list_1)):
    join_list = pylo.join_as_vector(data=list_1, list_to_join=list_2, col_posi=n)
    print(f"Result:{n} {join_list}")

join_list = pylo.join_as_vector(data=list_1, list_to_join=list_2, col_posi=9)
print(f"Result:9 {join_list}")
```


<!-- ---------------------------------- -->
<!-- Shift an Item in a List Method     -->
<!-- ---------------------------------- -->
## Shift
This function ***shift*** two elements in a list. It can be to the left or to the right. <br>
update is used to save the actual list with the shift elements.
If we set update to False, then we keep the original list and save
the new list into another variable.

```python
shift(data, direction=Move.RIGHT, qty=0, update=False)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

list_1 = [[1],[4],[5,6]]

# Right Shift List
print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,23,231)}    Shift Item in a List    {cp.reset_font()}")
print(f"{cp.ins_chr(n=80, unicode="-")}")
cp.ins_newline(2)
#---------------------------------------------------------------------------
print("original_list:  ", list_1, end=""); print(f"   right_shift 2, {cp.set_font(1,21,231)} update=False {cp.reset_font()}")
newlist = pylo.shift(list_1, "r", 2, False)
print("shifted _list:  ",newlist)
print("original_list:  ", list_1)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original_list:  ", list_1,end=""); print(f"   right_shift 2, {cp.set_font(1,1,231)} update=True {cp.reset_font()}")
newlist = pylo.shift(data=list_1, direction=cp.Move.RIGHT, qty= 2, update= True)
print("shifted _list:  ",newlist)
print("original_list:  ", list_1)

cp.ins_newline(2)

# Left Shift List
list_1 = [[1,2,3,4,5,6]]
#---------------------------------------------------------------------------
print("original_list:  ", list_1, end=""); print(f"   left_shift 2, {cp.set_font(1,21,231)} update=False {cp.reset_font()}")
newlist = pylo.shift(list_1, "l", 2, False)
print("shifted _list:  ",newlist)
print("original_list:  ", list_1)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original_list:  ", list_1,end=""); print(f"   left_shift 2, {cp.set_font(1,1,231)} update=True {cp.reset_font()}")
newlist = pylo.shift(data=list_1, direction=cp.Move.LEFT, qty= 2, update= True)
print("shifted _list:  ",newlist)
print("original_list:  ", list_1)
```


<!-- ---------------------------------- -->
<!-- Swap 2 items in a List Method      -->
<!-- ---------------------------------- -->
## Swap
This function swap two elements in a list. <br>
update is used to save the actual list with the swap elements. <br>
If update is set to False, then we keep the original list and save
the new list into another variable. <br>
posi_1 -> position 1 to be swap with position 2 <br>
posi_2 -> position 2 to be swap with position 1 <br>

**Note:** If one of the position provided is out of range, the function
        will return the list as original and it will print a message
        out of range.'''

```python
new_list = swap(data, posi_1=0, posi_2=0, update=False)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.set_font(1,23,231)}    Swap Items in a List    {cp.reset_font()}")
lst = [[1,2],[3,4],[5,6],[7,8]]
print("original: ", lst,end=""); print("   update=False,  posi_1=0, posi_2=2")
new_list = pylo.swap(data=lst, update= False, posi_1= 0, posi_2=2)
print("swaped_l: ",new_list)
print("original: ", lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original: ", lst,end=""); print(f"   {cp.set_font(1,1,231)} update=True, {cp.reset_font()} posi_1=3, posi_2=0")
new_list = pylo.swap(data=lst, update=True, posi_1=3, posi_2=10)
print("swaped_l: ",new_list)
print("original: ", lst)
```

<!-- ---------------------------------- -->
<!-- Number a List Method               -->
<!-- ---------------------------------- -->
## Add Number of Rows to a List
This method set the number of rows by adding a column to the left side.

```python
new_list = number(data, start_number=0, id_txt="Id", renumber=False, update=False)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp

pylo = cp.PyLO()
tbl  = cp.FancyFormat()
tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True

people = [\
      ["Names",  "Lasts",   "Age"],
      ["Pancho", "Melti",    50  ],
      ["Javier", "Nangy",    32  ],
      ["Melony", "Archi",    40  ],
      ["Jose",   "Valvimar", 18  ]]

print(f"{cp.ins_chr(20, cp.Unicode.BLAKC_RIGHT_POINT_TRIANGLE+cp.Unicode.BLACK_LEFT_POINTING_TRIANGLE+" ")}")

tbl.msg_title = " People "
tbl.print_fancy_format(people)

number_people = pylo.number(people, 1, "Num", False, False)
tbl.msg_title = " New People "
tbl.print_fancy_format(number_people)

tbl.msg_title = " Adding a New Person "
number_people.insert(2,[999, "KAYLA", "ACBD",  12])
tbl.print_fancy_format(number_people)

tbl.msg_title = " Numbering Again "
pylo.number(data=number_people, start_number=1, id_txt="No.", renumber=True, update=True)
tbl.print_fancy_format(number_people)
```

<!-- ---------------------------------- -->
<!-- Transpose of a List Method         -->
<!-- ---------------------------------- -->
## Transpose
update is used to replace original list with the transpose list. <br>
update is set to False to keep the original list and save
the new list into another variable. <br>
When the list is not square or rectangular, the list will be filled using
the fill_value. If the autofill is set to False, some data will be lost.

```python
transpose_list = transpose(data, autofill=True, fill_value="----", update=False)
```
### Cases
| Original_list                         |      Transpose_list                           |
|---------------------------------------|-----------------------------------------------|
| 0.- pass not a list variable          | returns a empty list                          |
| 1.- pass empty list                   | returns a empty list                          |
|                                       |                                               |
| 2.- [10]                              | [[10]]                                        |
| 3.- [[10]]                            | [10]                                          |
|                                       |                                               |
| 4.- [10, 20, 30]                      | [[10], [20], [30]]                            |
| 5.- [[10, 20, 30]]                    | [10, 20, 30]                                  |
| 6.- [[10], [20], [30]]                | [[10, 20, 30]]                                |
|                                       |                                               |
| 7.- [[1,2,3],  [4,5,6],   [7,8,9]]    | [[1,4,7], [2,5,8], [3,6,9]]                   |
| 8.- [[1,2,3],  [4,5,6],   [7,8,9,10]] | [[1,4,7], [2,5,8], [3,6,9]]                   |
| 9.- [[1,2,3],  [4,5,6,7], [7,8,9,10]] | [[1,4,7], [2,5,8], [3,6,9]]                   |
| A.-[[1,2,3,4], [4,5,6],   [7,8,9]]    | [[1,4,7], [2,5,8], [3,6,9]]                   |
|                                       |                                               |
| B.-[5, 6, [4,5], 45]                  | [[5], [6], [[4,5]], [45]]                     |
|                                       |                                               |

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

msg = f'''
            Inputs                     Outputs                                       Cases
   list_1 = "hello"                    []                                              1
   list_1 = []                         []                                              2
   list_1 = [5]                        [[5]]                                           3
   list_1 = [[1]]                      [1]                                             4
   list_1 = [1,2,3,4,5,6]              [[1],[2],[3],[4],[5],[6]]                       5
   list_1 = [[1,2],[3,4],[5,6]]        [[1,3,5],[2,4,6]           ]                    6
   list_1 = [[1],[4],[5,6]]            [[1,4,5],[fill_value,fill_value,6]]
                                       [[1,4,5]] -> autofill = False
                                       [[1,4,5]] -> autofill = False, type=\'string\'
   list_1 = [10,[50],[250],["H"],100]  [[10],[[50]],[[250]],[["H"]],[100]]             7

   list_1 = [[1,2,3,4,5,6]]            [1, 2, 3, 4, 5, 6]                              8 
   list_1 = [1, 2, 3, 4, 5, 6]         [[1], [2], [3], [4], [5], [6]]
   list_1 = [[1],[2],[3],[4],[5],[6]]  [[1,2,3,4,5,6]]
   '''

print(f"{cp.ins_chr(n=80, unicode="-")}")

print(msg)
a = 6+2j
print(a)
lst1 = "hello"
lst2 = []
lst3 = [5]
lst4 = [[1]]
lst5 = [1,2,3,4,5,6]
lst61 = [[1,2],[3,4],[5,6]]
lst62 = [[1],[4],[5,6]]
lst7  = [10,[50],[250],["H"],100]
lst81 = [[1,2,3,4,5,6]]
lst82 = [1, 2, 3, 4, 5, 6]
lst83 = [[1],[2],[3],[4],[5],[6]]


print(f"{cp.ins_chr(n=80, unicode="-")}")
print(f"{cp.ins_chr(n=80, unicode="-")}")


print("original :", lst1)
trans_lst = pylo.transpose(data=lst1, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)


print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst2)
trans_lst = pylo.transpose(data=lst2, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst3)
trans_lst = pylo.transpose(data=lst3, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst4)
trans_lst = pylo.transpose(data=lst4, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst5)
trans_lst = pylo.transpose(data=lst5, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst61)
trans_lst = pylo.transpose(data=lst61, autofill=True, fill_value=15, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst62)
trans_lst = pylo.transpose(data=lst62, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst7)
trans_lst = pylo.transpose(data=lst7, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst81)
trans_lst = pylo.transpose(data=lst81, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst82)
trans_lst = pylo.transpose(data=lst82, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

print(f"{cp.ins_chr(n=80, unicode="-")}")

print("original :", lst83)
trans_lst = pylo.transpose(data=lst83, autofill=True, fill_value=0.5, update=False)
print("Transpose:",trans_lst)

tbl = cp.FancyFormat()
tbl.print_fancy_format(lst61)
pylo.transpose(data=lst61,update=True)
tbl.print_fancy_format(lst61)
```

<!-- ---------------------------------- -->
<!-- Merge Two List Method              -->
<!-- ---------------------------------- -->
## Merge
This method merge two lists with two options. <br>
It can be merge by ***ROWS*** or by ***COLUMNS***. It also,
provide the option to pick the specific ***position***
where to start the merge on ***list_1***.
```python
merge_list = merge(list_1, list_2, posi=0, merge_by=Appending.ROWS)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True
tbl.align_title  = cp.Align.LEFT

methods = [\
    ["Cursor",  "FontStyle"  ,    "FancyMessage"        ],
    ["jumpTo",  "start_style",    "print_fancy_message" ],
    ["jumpxy",  "stop_style" ,    "print_fancy_note"    ],
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

tbl.msg_title = " Merge List people to List methods as COLUMNS Posi=2 "
merge_cols = pylo.merge(list_1=methods, list_2=people, posi=2, merge_by=pylo.Appending.COLUMNS)
tbl.print_fancy_format(merge_cols)

tbl.msg_title = " Merge List people to List methods as ROWS Posi=4 "
merge_cols = pylo.merge(list_1=methods, list_2=people, posi=4, merge_by=pylo.Appending.ROWS)
tbl.print_fancy_format(merge_cols)
```

<!-- ---------------------------------- -->
<!-- Reverse Row Order Method               -->
<!-- ---------------------------------- -->
## Reversed Row Order 
This method reverse the order of the list keeping the headers in the same positon.

```python
new_list = reversed_row_order(data, update=False)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()
tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True
tbl.align_title = cp.Align.CENTER


methods = [\
    ["Header 0","Header 1"   ,    "Header 2"           ,    "Header 3",],
    ["Cursor",  "FontStyle"  ,    "FancyMessage"       ,    "FancyFormat"        ],
    ["jumpTo",  "start_style",    "print_fancy_message",    "print_fancy_format" ],
    ["jumpxy",  "stop_style" ,    "print_fancy_note"   ,    "reset_fancy_format" ],
    ["moveTo",  "print_style"],
    ["movexy"]]

result = pylo.reversed_row_order(methods, False)
tbl.msg_title = " Reversed_ROW_Order "
tbl.print_fancy_format(result)

tbl.msg_title = " Original Values "
tbl.print_fancy_format(methods)

tmp = []
reversed_list = []
for row in reversed(methods):
    reversed_list.append(row)
tbl.print_fancy_format(reversed_list)
```

<!-- ---------------------------------- -->
<!-- Sort Rows by Columns Method        -->
<!-- ---------------------------------- -->
## Sort Rows by Columns
***sort_by_col*** won't sort the first row because it is considered the Header of the list.
If a column is mixed with string type and another type, like integer or float, it will
cause an error. This method is intended to be used with all cells filled with the same
type of data per column except the header; any empty cells will be filled automatically.
If you want to fill those spots with a specific type, then use the ***autofill_data*** method.

```python
sort_rows_by_col(data, ref_col=0, reversed_order=False, update=False)       
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

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

result = pylo.sort_rows_by_col(data=lst, ref_col=0, reversed_order=False, update=False)
tbl.msg_title = " Sort_by Col 0 "
tbl.print_fancy_format(result)

tbl.msg_title = " Original "
tbl.print_fancy_format(lst)

tbl.msg_title = " Sort_by Col 4 "
result = pylo.sort_rows_by_col(data=lst, ref_col=4, reversed_order=False, update=False)
tbl.print_fancy_format(result)

tbl.msg_title = " Sort_by Col 0. reverse_order=True, update=True "
result = pylo.sort_rows_by_col(data=lst, ref_col=0, reversed_order=True, update=True)
tbl.print_fancy_format(result)

tbl.msg_title = " New Original "
tbl.print_fancy_format(lst)

tbl.msg_title = ""
lst_2 = [5,1,9,5]
result2 = pylo.sort_rows_by_col(data=lst_2, ref_col=10, reversed_order=False, update=False)
print("\n\nResult  : reverse_order=False, update=False")
tbl.print_fancy_format(result2)
print("Original:");  tbl.print_fancy_format(lst_2)

result2 = pylo.sort_rows_by_col(data=lst_2, ref_col=0, reversed_order=True, update=True)
print("Result  : reverse_order=True, update=True ")
tbl.print_fancy_format(result2)
print("Original:");  tbl.print_fancy_format(lst_2)
```

<!-- ---------------------------------- -->
<!-- Sort Columns Method                -->
<!-- ---------------------------------- -->
## Sort Columns
If the option provided is different than ***ascending*** or ***descending*** or a ***list***, it will sort as ***ascending***. If the list contains numbers not in the range of the data list, it will sort as ***ascending***. If the list contains a length different than the length of the data, it will sort as ***ascending***. If the list is ***NOT*** in the form of mXn it will return an empty list as a result.

```python
 new_list = sort_cols(data, sort_type=Order.ASCENDING, update=False)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()

tbl  = cp.FancyFormat()
tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True
tbl.align_title = cp.Align.CENTER

#         0           1          2            3         4
l1 = [["Names",    "Lasts",    "Ages",  "Department", "AWeb"    ],
      ["Miguel",   "AC",       40,         "EE",      "uno"     ],
      ["Tyler",    "Hig",      35,         "ECE",     "dos"     ],
      ["Alex",     "Call",     38,         "EE",      "tres"    ],
      ["Matt",     "Armaci",   40,         "CS",      "cuatro"  ]]



new_list = pylo.sort_cols(l1, "ascending", False)
tbl.msg_title = " Ascending Order ";    tbl.print_fancy_format(new_list)
tbl.msg_title = " Original List ";      tbl.print_fancy_format(l1)


new_list = pylo.sort_cols(l1, "descending", False)
tbl.msg_title = " Descending Order ";     tbl.print_fancy_format(new_list)
tbl.msg_title = " Original List ";        tbl.print_fancy_format(l1)

new_list = pylo.sort_cols(data=l1, sort_type=[4,0,1,3,2], update=True)
tbl.msg_title = " Order by List Reference [4,0,1,3,2] update=True "
tbl.print_fancy_format(new_list)
tbl.msg_title = " Original List "
tbl.print_fancy_format(l1)


new_list = pylo.sort_cols(data=l1, sort_type=pylo.Order.ASCENDING, update=False)
new_list = pylo.sort_cols(data=l1, sort_type=pylo.Order.DESCENDING, update=True)

tbl.msg_title = ""
l1 = ["NaMeS",    "LaStS",    "AgeS",  "DeparTmenT", "AWeB"]
l = sorted(l1, reverse=False)
tbl.print_fancy_format(l)

new_list = pylo.sort_cols(data=l1, sort_type=pylo.Order.ASCENDING, update=False)
tbl.print_fancy_format(new_list)
```


<!-- ---------------------------------- -->
<!-- Find Duplicate Method              -->
<!-- ---------------------------------- -->
## Find Duplicate
This method find all duplicate values into a list and returns all duplicate values into a list.

```python
find_duplicate(data, case_sensitive=True)
```

[**Top**](#pylo-class) <span style="color:red"> <strong> Example: </strong> </span>

```python
import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

tbl.bg_title  = 90
tbl.bold_title = True
tbl.italic_title = True
tbl.align_title  = cp.Align.LEFT
tbl.bg_header = 90
tbl.bold_header = True

result = pylo.find_duplicate(data=COLOR_NAMES, case_sensitive=True)
tbl.print_fancy_format(result)

NEW_LIST = ["HELLO","HI","BYE","hellO","Hola","Hi","HELLO"]
rst = pylo.find_duplicate(data=NEW_LIST, case_sensitive=True)
tbl.print_fancy_format(rst)

rst = pylo.find_duplicate(data=NEW_LIST, case_sensitive=False)
tbl.print_fancy_format(rst)
```



#### [Back](README.md)

https://github.com/acma82/custom_print

## Report bugs at	→	acma.mex@hotmail.com