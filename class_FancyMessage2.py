import os
import fancyprint as fp
msg = fp.FancyMessage()
crs = fp.Cursor()




#---------------------------------------------------------------------------------------   
def warning2(obj:fp.FancyMessage, body:str)->int:
   msg = str(body)
   
   tncols, tnrows = os.get_terminal_size()
   space_available = tncols - obj.left_indent - obj.right_indent
   msg_type = "single_line"; new_msg = ""
   longest_line = 0;  quotient = 0; residue = 0; letter_counter=0
   number_letter_line_list = []; quotient_number_letter_line_list = []
   adj_diff_space = []; carry_number_letter_line_list = []
   residue_number_letter_line_list = []; fit_number_letter_line_list = []
   result_multi_lines = []; 
   
   for l in msg:
      if (l=="\n"):
         number_letter_line_list.append(letter_counter)            
         letter_counter = 0
         msg_type="multiple_lines"
      
      else:
         new_msg += l
         letter_counter += 1

   if (msg_type == "single_line"):
      quotient = int(letter_counter/space_available)
      residue  = letter_counter%space_available
      while quotient>0:
         number_letter_line_list.append(space_available)
         quotient -= 1        
      number_letter_line_list.append(residue)
      
      for n in number_letter_line_list:
         adj_diff_space.append(space_available - n)



   else:   # multiple lines
      number_letter_line_list.append(letter_counter) # the last one not added
      longest_line = max(number_letter_line_list)
      # first item when only enter it's deleted
      if (number_letter_line_list[0] == 0):   number_letter_line_list.pop(0)
      # last item when only enter it's deleted
      if (number_letter_line_list[(len(number_letter_line_list))-1] == 0):
         number_letter_line_list.pop((len(number_letter_line_list))-1)
         
               
      if (space_available > longest_line):
         for n in number_letter_line_list:
            adj_diff_space.append(space_available-n)               

      else:
         for line in range(len(number_letter_line_list)):
            if (number_letter_line_list[line] <= space_available):
               fit_number_letter_line_list.append(number_letter_line_list[line])
               
            else:
               quotient = int(number_letter_line_list[line]/space_available)
               residue  = number_letter_line_list[line]%space_available                  
               n = quotient

               while n > 0:                     
                  quotient_number_letter_line_list.append(space_available)
                  n -= 1

               residue_number_letter_line_list.append(residue)
               carry_number_letter_line_list.append(quotient+1)

         ctrl = 0; first_time = 0
         for r in number_letter_line_list:
            if (r > space_available):                  
               last_one = carry_number_letter_line_list[ctrl] - 1

               for n in range(carry_number_letter_line_list[ctrl]):
                  if (last_one == n):                        
                     result_multi_lines.append(residue_number_letter_line_list[ctrl])
                     ctrl += 1
                  else:
                     result_multi_lines.append(space_available)
                  
            else:
               result_multi_lines.append(r)
         number_letter_line_list = result_multi_lines

         for n in number_letter_line_list:
            adj_diff_space.append(space_available - n)

   #------------------------------------------------------------------------------------------------------------------------------------------------
   longest_line = max(number_letter_line_list)
   # print("ncols                  :",tncols)
   # print("longes_line            :",longest_line)
   # print("space_available        :",space_available)
   # print("number_letter_line_list:",number_letter_line_list)
   # print("adj_diff_space         :", adj_diff_space)
   # print()
   # print(new_msg)
   return len(number_letter_line_list)






fp.ins_newline(3)
#---------------------------------------------------------------------------------------
# Another Way to Use FancyMessage Class with Some Manipulation                         -
#---------------------------------------------------------------------------------------
#                                                                                       #
warning_body = f'''
\"What is love?\" is a question that has been asked in many novels, poems, plays, and
songs. The answer to the question may vary and could change within a lifetime for    
each individual. Love is often considered complex, and many philosophers and         
scientists have hypothesized about what it means.

https://www.betterhelp.com/advice/love/how-to-last-through-the-5-stages-of-love'''

msg.fg = 0; msg.bold = True; msg.italic = True; msg.underline = True; msg.bg = 231
msg.left_indent = 35
msg.print_fancy_msg(" Love Poem ")
msg.top_lines = 0;   msg.bold = False;    msg.fg = 21
msg.left_indent = 4; msg.right_indent = 4
msg.italic = False; msg.underline = False
msg.left_indent = 2; msg.underline = False
msg.print_fancy_msg(warning_body)

fp.ins_newline(2)












note = " Warning: "
msg.top_lines = 1
msg.left_indent = 1+len(note)+1
#                                                                             #
warning_body = f'''
\"What is love?\" is a question that has been asked in many novels, poems,    
plays, and songs. The answer to the question may vary and could change within a
lifetime for each individual. Love is often considered complex, and many       
philosophers and scientists have hypothesized about what it means.            
                        
            Working with Python 3.12 and GNU/Linux/AlmaLinux 9.4

https://www.betterhelp.com/advice/love/how-to-last-through-the-5-stages-of-love'''

msg.bg = 23;  msg.fg = 231
msg.print_fancy_msg(warning_body)
# tncols, space_available, number_letter_line_list, adj_diff_space, new_msg, n_lines = msg.get_msg_attribute(warning_body)
n_lines = msg.get_msg_attribute(warning_body)
# print(f"{crs.move(qty=warning2(msg,warning_body)+msg.top_lines, direction=fp.Move.UP)}{fp.set_font(1,23,0)}{note}")
print(f"{crs.move(qty=n_lines+msg.top_lines, direction=fp.Move.UP)}{crs.move(qty=1,direction=fp.Move.RIGHT)}{fp.set_font(1,231,0)}{note}")
# print(f"{crs.move(qty=n_lines+msg.top_lines, direction=fp.Move.UP)}{fp.set_font(1,231,0)}{note}")
crs.jump(qty=7,direction=fp.Move.DOWN)
print(f"{fp.reset_font()}")
print()

print(f"{fp.ins_space(8)}{fp.set_font(1,90,231)}  Miguel Angel Aguilar Cuesta  {fp.reset_font()}")

print(n_lines)
