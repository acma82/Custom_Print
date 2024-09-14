import time
import fancyprint as fp

print("fp.clear() -> clear function")
print("Clear the terminal and restore to home the cursor")
print("It uses the system cmd to clear all the screen")
time.sleep(6)
fp.clear()


# It returns the dimensions of the terminal
cols, rows = fp.dimensions()
print("fp.dimensions() -> It returns the dimensions of the screen")
print("cols: ", cols, "  rows: ", rows); time.sleep(6)


for n in range(5):
   print("keep going... with erase() function")

print("erase() function cleans the terminal and the cursor remain in the same position")
print("erase uses the ansi system")
fp.erase()
time.sleep(6)


print("keep going... with clean")
print("clean uses the ansi system")
print("Clear the terminal and restore to home the cursor")
time.sleep(5)
fp.clean()



