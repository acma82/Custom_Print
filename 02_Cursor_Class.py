'''
Cursor Class
Method Available:
    jumpTo(self,qty=0, direction=Move.DOWN)
    moveTo(self,qty=0, direction=Move.DOWN)

    jumpxy(self,x=0,y=0)
    movexy(self,x=0, y=0)
'''

import fancyprint as fp
crs = fp.Cursor()

fp.clear()
# jumpTo method
crs.jumpTo(qty=2, direction = fp.Move.DOWN)
print("I am down")

crs.jumpTo(qty=20, direction= "right")
print("I am right")

crs.jumpTo(1,fp.Move.UP)
print("I am up")
crs.jumpTo(5,"down")


# moveTo method
print(f"{crs.moveTo(15,"right")} First One",  end="")
print(f"{crs.moveTo(15,"right")} Second One", end="")
print(f"{crs.moveTo(qty=20,direction="left")}Hello")


# jumpxy method
crs.jumpxy(0,0)
print("Start Here*")


# movexy
print(f"{crs.movexy(15,40)}hello again")


# combination
crs.jumpTo(8,"down")
crs.jumpxy(-1,-1)
print("adios",end="")
print(f"{crs.moveTo(qty=20,direction=fp.Move.RIGHT)}BYE")
