import fancyprint as fp

print(f"Hello{fp.ins_space(40)}There")
print("Hello"+fp.ins_space(40)+"There")
mns = '''
----------------------------------------------------------------------------
   import fancyprint as fp

   fp.ins_space(int)
   
   This function inserts x number of spaces between words.
   
   Example:
           print(f"Hello{fp.ins_space(40)}There")
   
           print("Hello"+fp.ins_space(40)+"There")
----------------------------------------------------------------------------
'''
print(mns)