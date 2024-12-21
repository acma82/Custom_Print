#### [Back](README.md)
# <span style="color:green"> <strong> Cursor </strong> </span>

This class contains 4 methods. The difference between ***jump*** and ***move*** is that jump executes the code while move returns the code.

+ ***jumpTo(qty=0, direction=cp.Move.DOWN)*** <br> 
This method jumps rows or columns for the cursor in the terminal.

+ ***jumpxy(x=0, y=0)*** <br>
This method jumps the cursor to specific coordinates in the terminal.

+ ***moveTo(qty=0, direction=cp.Move.DOWN)*** <br> 
This method moves rows or columns for the cursor in the terminal.

+ ***movexy(x=0, y=0)*** <br>
This method moves the cursor to specific coordinates in the terminal.

<span style="color:red"> <strong> Example: </strong> </span>

```python
    from custom_print import Cursor
    from custom_print import clear
    from custom_print import Move
    crs = Cursor()

    clear()
    # jumpTo
    crs.jumpTo(qty=2, direction = Move.DOWN)
    print("I am down")

    crs.jumpTo(qty=20, direction= "right")
    print("I am right")

    crs.jumpTo(1,Move.UP)
    print("I am up")
    crs.jumpTo(5,"down")

    # moveTo
    print(f"{crs.moveTo(15,"right")} First One",  end="")
    print(f"{crs.moveTo(15,"right")} Second One", end="")
    print(f"{crs.moveTo(qty=20,direction="left")}Hello")

    # jumpxy
    crs.jumpxy(0,0)
    print("Start Here*")

    # movexy
    print(f"{crs.movexy(15,40)}hello again")

    # combination
    crs.jumpTo(8,"down")
    crs.jumpxy(-1,-1)
    print("adios",end="")
    print(f"{crs.moveTo(qty=20,direction=Move.RIGHT)}BYE")
```

#### [Back](README.md)