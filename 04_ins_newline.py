import fancyprint as fp
msg = '''
----------------------------------------------------------------------------
   import fancyprint as fp

   fp.ins_newline(int)
   
   This function inserts x number of lines.    
   
   Example:
           print("Python 3")
           fp.ins_newline(3)
           print("is amazing...!")
----------------------------------------------------------------------------
'''
print(msg)
print("Python 3.12")
fp.ins_newline(4)
print("is amazing...!")