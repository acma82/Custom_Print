'''
Cursor Class
Method Available:
    jumpTo(self,qty=0, direction=Move.DOWN)
    moveTo(self,qty=0, direction=Move.DOWN)

    jumpxy(self,x=0,y=0)
    movexy(self,x=0, y=0)
'''

from custom_print import Cursor # Class
from custom_print import clear  # Function
from custom_print import Move   # Class
crs = Cursor()

clear()
#+-----------------------------------------------------------------------------------+
#|    jumpTo Method                                                                  |
#+-----------------------------------------------------------------------------------+
crs.jumpTo(qty=2, direction = Move.DOWN)
print("I am down")

crs.jumpTo(qty=20, direction= "right")
print("I am right")

crs.jumpTo(1,Move.UP)
print("I am up")
crs.jumpTo(5,"down")


#+-----------------------------------------------------------------------------------+
#|    moveTo Method                                                                  |
#+-----------------------------------------------------------------------------------+
print(f"{crs.moveTo(15,"right")} First One",  end="")
print(f"{crs.moveTo(15,"right")} Second One", end="")
print(f"{crs.moveTo(qty=20,direction="left")}Hello")


#+-----------------------------------------------------------------------------------+
#|    jumpxy Method                                                                  |
#+-----------------------------------------------------------------------------------+
crs.jumpxy(0,0)
print("Start Here*")


#+-----------------------------------------------------------------------------------+
#|    movexy Method                                                                  |
#+-----------------------------------------------------------------------------------+
print(f"{crs.movexy(15,40)}hello again")


#+-----------------------------------------------------------------------------------+
#|    combination                                                                    |
#+-----------------------------------------------------------------------------------+
crs.jumpTo(8,"down")
crs.jumpxy(-1,-1)
print("adios",end="")
print(f"{crs.moveTo(qty=20,direction=Move.RIGHT)}BYE")
