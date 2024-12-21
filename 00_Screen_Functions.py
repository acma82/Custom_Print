'''
Screen Functions Available:
    clean()
    clear()
    erase()         
    ncols, nrows = dimensions()
    resize(rows=25, cols=80)
'''
import time
from custom_print import clean
from custom_print import clear
from custom_print import erase
from custom_print import dimensions

print("fp.clear() -> clear function")
print("Clear the terminal and restore to home the cursor")
print("It uses the system cmd to clear all the screen")
time.sleep(6)
clear()


# It returns the dimensions of the terminal
cols, rows = dimensions()
print("fp.dimensions() -> It returns the dimensions of the screen")
print("cols: ", cols, "  rows: ", rows)
time.sleep(6)


for n in range(5):
    print("keep going... with erase() function")

print("erase() function cleans the terminal and the cursor remain in the same position")
print("erase uses the ansi system")
erase()
time.sleep(6)


print("keep going... with clean")
print("clean uses the ansi system")
print("Clear the terminal and restore to home the cursor")
time.sleep(5)
clean()
# This is the end of Screen_Functions
