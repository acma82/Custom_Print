import fancyprint as fp
crs = fp.Cursor()

crs.jump(2,"down");                   print("I am down")
crs.jump(20,"right");                 print("I am right")
crs.jump(qty=1,direction=fp.Move.UP); print("I am up")
crs.jump(5,"down")

print(f"{crs.move(15,"right")}First One",end="")
print(f"{crs.move(15,"right")}Second One",end="")
print(f"{crs.move(qty=20,direction="left")}Hello")

crs.jumpTo(0,0)
print("Start Here*")

print(f"{crs.moveTo(15,40)}hello again")

crs.jump(8,"down")

crs.jumpTo(-1,-1)
print("adios",end="")
print(f"{crs.move(qty=20,direction=fp.Move.RIGHT)}BYE")