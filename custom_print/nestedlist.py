from custom_print.fancy_functions import set_font
from custom_print.fancy_functions import reset_font
from custom_print.fancy_functions import ins_chr
from custom_print.fancy_functions import get_list_type
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Table List To Vector List                                                                                                                      -
#-------------------------------------------------------------------------------------------------------------------------------------------------
def make_to_vector(data:list):

    '''  This function makes any list in a form as a vector. [1,2,3,4,5,etc.],
            up to 4 brackets.
    '''

    vector_lista = []
    for item in data:
        if isinstance(item, list):
            for i in item:
                if isinstance(i, list):
                    for n in i:
                        if isinstance(n, list):
                            for m in n:
                                vector_lista.append(m)
                        else:
                            vector_lista.append(n)
                else:
                    vector_lista.append(i)
        else:
            vector_lista.append(item)
    return vector_lista
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Convert a List From Any Type to String                                                                                                         -
#-------------------------------------------------------------------------------------------------------------------------------------------------
def data_to_str(data:list, update=False):

    '''  Converts all the elements of a list to string type  '''

    new_list = []
    for value in data:
        if isinstance(value, list):
            new_list.append(data_to_str(value))
        else:
            new_list.append(str(value))


    if update == True:
        data.clear()
        for n in new_list: data.append(n)

    return new_list
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Transpose list                                                                                                                                 -
#-------------------------------------------------------------------------------------------------------------------------------------------------
def get_transpose(nested_list):
    transpose_list = []
    tempo = []
    for col in range(len(nested_list[0])):
        for row in range(len(nested_list)):
            tempo.append(nested_list[row][col])

        transpose_list.append(tempo)
        tempo=[]
    return transpose_list
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Number a List                                                                                                                                  -
#-------------------------------------------------------------------------------------------------------------------------------------------------
def add_col_id(nested_list:list, start_number:int=0, id_label:str="ID", renumber:bool=False, update:bool=False):

    '''  This method set the number of rows by adding a column to the left side.  '''

    original = nested_list

    list_type = "multiple_items_multiple_rows" #get_list_type(original)
    if list_type == "multiple_items_multiple_rows":

        result = [];                    tempo = []
        header = original.pop(0);       header.insert(0,id_label)

        for row in original:
            tempo = row
            tempo.insert(0,start_number)
            start_number += 1
            result.append(tempo)
            tempo = []
        result.insert(0,header)

    if update == True:
        tempo_rows = []
        nested_list.clear()
        for row in result:
            for col in row:
                tempo_rows.append(col)
            nested_list.append(tempo_rows)
            tempo_rows = []
    else:
        tempo_rows = []
        nested_list.clear()
        for row in result:
            for col in row[1:]:
                tempo_rows.append(col)
            nested_list.append(tempo_rows)
            tempo_rows = []
    return result
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Find the shortes element in a NestedList                                                                                                       -
#-------------------------------------------------------------------------------------------------------------------------------------------------
def find_longest_item(data:list, display=False):
    longest_len  = 0
    longest_item = ""
    longest_row  = 0
    longest_col  = 0

    # Calculating Longest: Item, len, row, col
    for row in range(len(data)):
        for col in range(len(data[row])):
            item_length = (len(str(data[row][col])))
            if item_length > longest_len:
                longest_len  = item_length
                longest_item = data[row][col]
                longest_row  = row
                longest_col  = col
            else: pass

    result = [["Item", "Len", "Row", "Col"],
            [longest_item, longest_len, longest_row, longest_col]]

    return result



#-------------------------------------------------------------------------------------------------------------------------------------------------
# Padding the list                                                                                                                               -
#-------------------------------------------------------------------------------------------------------------------------------------------------
def padding_list(self, nested_list):
    # I want to print the nested list in a nice way.
    # For Normal Order:
    #       1. convert this list to string in all the elements
    #       2. add the headers
    #       3. add the id row and col if it is set to TRUE
    #       4. get the transpose list
    #       5. convert all the nested_list to string again if the id was added
    #       6. pad the column 0 and the others as well put condition if necessary
    #       7. get transpose to get the finall list
    #       8. get ready all the colors
    #       9. print the final list
    # For Reversed Order:
    #       1., 2., and 3. from this step jump to step 6, and then jump to step 8 and then step 9.
    check_list = get_list_type(nested_list)
    new_list = []

    if check_list == "incorrect_variable_type":
        new_list.append(["No a List Type"])

    elif check_list == "empty_list":
        new_list = [["Custom_Print"]]

    elif check_list == "multiple_items_no_row":
        new_list.append(nested_list)

    elif check_list == "mix_items":
        print("inside")
        tempo = make_to_vector(nested_list)
        new_list.append(tempo)

    elif check_list == "one_item_no_row":
        new_list.append(nested_list)

    else:
        new_list = nested_list


    string_nested_list = data_to_str(new_list)                        # step 1

    if self.id_on == True:
        col_list = []
        for n in range(len(string_nested_list[0])):
            col_list.append(f"Col_{str(n)}")
        string_nested_list.insert(0, col_list)                        # step 2

        if self.transpose_list == False: header_on_nested_list = add_col_id(nested_list=string_nested_list, id_label = "Rows \u2193")   # Step 3 (longest 8)
        else:                           header_on_nested_list = add_col_id(nested_list=string_nested_list, id_label = "Rows \u2192")   # Step 3 (longest 8)
        transpose_nested_list = get_transpose(header_on_nested_list)  # step 4
        new_nested_list = data_to_str(transpose_nested_list)          # step 5
    else:
        transpose_nested_list = get_transpose(string_nested_list)     # step 4
        new_nested_list = data_to_str (transpose_nested_list)

    # ---------------------------------------------------------------------------------------------
    # this is for printing normally
    # ---------------------------------------------------------------------------------------------
    padding_list = []
    if self.transpose_list == False:
        for row in range(len(new_nested_list)):                       # step 6 (padding)
            longest = find_longest_item([new_nested_list[row]])
            if row == 0:
                if self.id_on == True:  padded_matrix = [cell.center(longest[1][1]) for cell in new_nested_list[row]]
                else:                   padded_matrix = [cell.ljust(longest[1][1]) for cell in new_nested_list[row]]

            else:
                padded_matrix = [cell.ljust(longest[1][1]) for cell in new_nested_list[row]]

            padding_list.append(padded_matrix)
        formatted_nested_list = get_transpose(padding_list)             # step 7 (transpose final list)
    else:
        # ---------------------------------------------------------------------------------------------
        # Reversed Order     Step 6 # here is missing the colors
        # ------------------l_id_space  ---------------------------------------------------------------------------
        nested_list_str = get_transpose(new_nested_list)
        for row in range(len(nested_list_str)):
            longest = find_longest_item([nested_list_str[row]])
            padded_matrix = [word.ljust(longest[1][1]) for word in nested_list_str[row]] # step 6 (padding)
            padding_list.append(padded_matrix)

        formatted_nested_list = get_transpose(padding_list)                              # step 7 (transpose final list)

    return formatted_nested_list



#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Nested List                                                                                                                                       -
#-----------------------------------------------------------------------------------------------------------------------------------------------------
class NestedList():
    def __init__(self):
        # print_simple_list;                       print_nested_list
        # header variables;                        id variables
        self.header_bg = 231;                      self.id_on = True
        self.header_fg = 16;                       self.id_bg = 234
        self.header_bold   = True;                 self.id_fg = 231
        self.header_dim    = False;                self.id_bold   = True
        self.header_italic = False;                self.id_dim    = False
        self.header_strike = False;                self.id_italic = True
        self.header_hidden = False;                self.id_strike = False
        self.header_inverse   = False;             self.id_hidden = False
        self.header_blinking  = False;             self.id_inverse   = False
        self.header_underline = False;             self.id_blinking  = False
        self.bullet = "\u2022";                      self.id_underline = False
        self.adj_int_indent = 4;                   self.adj_middle_space = 2
        self.force_all_col_same_width = True

        # data_variables
        self.data_bg = 202;                        self.data_bg_step = 1;
        self.data_fg = 231;                        self.data_bg_stop = 207;
        self.data_bold   = False;                  self.data_fg_step = 1;
        self.data_dim    = False;                  self.data_fg_stop = 232;
        self.data_italic = False
        self.data_strike = False;                  self.adj_left_space  = 2
        self.data_hidden = False;                  self.adj_right_space = 2
        self.data_inverse   = False
        self.data_blinking  = False;               self.transpose_list = False
        self.data_underline = False;               self.adj_indent    = 2


    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    # Print Nested List                                                                                                                                  -
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def print_nested_list(self, nested_list:list=[["Custom_print"]]):
        bg_step = self.data_bg;        fg_step = self.data_fg
        formatted_nested_list = padding_list(self, nested_list=nested_list)
        # step 8 (get the font settings)
        # id colors never change
        id_colors = set_font(bold=self.id_bold, bg=self.id_bg, fg=self.id_fg, italic=self.id_italic, underline=self.id_underline,
                    strike=self.id_strike, blinking=self.id_blinking, dim=self.id_dim, hidden=self.id_hidden, inverse=self.id_inverse)
        # data colors changes but this is the first one
        dt_colors = set_font(bold=self.data_bold, bg=self.data_bg, fg=self.data_fg, italic=self.data_italic, underline=self.data_underline,
                    strike=self.data_strike, blinking=self.data_blinking, dim=self.data_dim, hidden=self.data_hidden, inverse=self.data_inverse)


        # step 9 start the print and altering the colors for data if need it
        # calculating spaces
        indentation = ins_chr(self.adj_indent)
        lsp = ins_chr(self.adj_left_space)
        msp = ins_chr(self.adj_middle_space)
        rsp = ins_chr(self.adj_right_space)
        last_col = 0

        #-------------------------------------------------------------------------------------------------------------
        # print the first row id separately                                                                          -
        #-------------------------------------------------------------------------------------------------------------
        if self.id_on == True:
            id_rows_cols = formatted_nested_list.pop(0)
            print(f"{indentation}{id_colors}", end="", flush=True)

            for i in range(len(id_rows_cols)):
                if len(id_rows_cols)-1 == last_col:
                    if len(id_rows_cols) == 2: # only 1 item
                        print(f"{lsp}{id_rows_cols[i]}{rsp}",end="", flush=True)
                    else: # more than one
                        print(f"{msp}{id_rows_cols[i]}{rsp}",end="", flush=True)

                elif i == 0:
                    print(f"  {id_rows_cols[i]} ",end="", flush=True)
                elif i == 1:
                    print(f"{lsp}{id_rows_cols[i]}",end="", flush=True)
                else:
                    print(f"{msp}{id_rows_cols[i]}",end="", flush=True)
                last_col += 1

            print(reset_font())

            # printing the body now
            last_row = 0
            last_col = len(formatted_nested_list[0]) - 1
            for row in range(len(formatted_nested_list)):
                for col in range(len(formatted_nested_list[row])):
                    if len(formatted_nested_list)-1 == last_row:
                        if col == 0:
                            print(f"{indentation}{id_colors}  {formatted_nested_list[row][col]} ", end="", flush=True)
                        elif col == 1:
                            if len(formatted_nested_list) == 2: # only 2 rows
                                print(f"{dt_colors}{lsp}{formatted_nested_list[row][col]}{rsp}",end="", flush=True)
                            else:
                                if col == last_col:
                                    print(f"{dt_colors}{lsp}{formatted_nested_list[row][col]}{rsp}",end="", flush=True)
                                else:
                                    print(f"{dt_colors}{lsp}{formatted_nested_list[row][col]}",end="", flush=True)
                        else: # more than one
                            if col == last_col:
                                print(f"{dt_colors}{msp}{formatted_nested_list[row][col]}{rsp}",end="", flush=True)
                            else:
                                print(f"{dt_colors}{msp}{formatted_nested_list[row][col]}",end="", flush=True)
                    else:
                        if col == 0:
                            print(f"{indentation}{id_colors}  {formatted_nested_list[row][col]} ", end="", flush=True)

                        elif col == 1:
                            if col == last_col:
                                print(f"{dt_colors}{lsp}{formatted_nested_list[row][col]}{rsp}", end="", flush=True)
                            else:
                                print(f"{dt_colors}{lsp}{formatted_nested_list[row][col]}", end="", flush=True)
                        else:
                            if col == last_col:
                                print(f"{dt_colors}{msp}{formatted_nested_list[row][col]}{rsp}",end="", flush=True)
                            else:
                                print(f"{dt_colors}{msp}{formatted_nested_list[row][col]}",end="", flush=True)


                print(reset_font())

                if bg_step >= self.data_bg_stop: bg_step = self.data_bg
                else:                            bg_step += self.data_bg_step

                if fg_step >= self.data_fg_stop: fg_step = self.data_fg
                else:                            fg_step += self.data_fg_step
                last_row += 1

                dt_colors = set_font(bold=self.data_bold, bg=bg_step, fg=fg_step, italic=self.data_italic, underline=self.data_underline,
                            strike=self.data_strike, blinking=self.data_blinking, dim=self.data_dim, hidden=self.data_hidden, inverse=self.data_inverse)

            # all the table is data
        else:
            last_col = len(formatted_nested_list[0]) - 1
            for row in range(len(formatted_nested_list)):
                # print(f"")
                for col in range(len(formatted_nested_list[row])):
                    if col == 0:
                        if len(formatted_nested_list[row]) == 1: # 1 col
                            print(f"{indentation}{dt_colors}{lsp}{formatted_nested_list[row][col]}{rsp}", end="", flush=True)
                        else:
                            print(f"{indentation}{dt_colors}{lsp}{formatted_nested_list[row][col]}", end="", flush=True)

                    elif col == last_col:
                        print(f"{dt_colors}{msp}{formatted_nested_list[row][col]}{rsp}", end="", flush=True)

                    else:
                        print(f"{dt_colors}{msp}{formatted_nested_list[row][col]}", end="", flush=True)

                print(reset_font())

                if bg_step >= self.data_bg_stop: bg_step = self.data_bg
                else:                            bg_step += self.data_bg_step

                if fg_step >= self.data_fg_stop: fg_step = self.data_fg
                else:                            fg_step += self.data_fg_step


                dt_colors = set_font(bold=self.data_bold, bg=bg_step, fg=fg_step, italic=self.data_italic, underline=self.data_underline,
                            strike=self.data_strike, blinking=self.data_blinking, dim=self.data_dim, hidden=self.data_hidden, inverse=self.data_inverse)


    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    # Print Nested List                                                                                                                                  -
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def print_simple_list(self, nested_list):
        # bu id_on
        bu_id_on = self.id_on
        self.id_on = False
        #-------------------------------------------
        bg_step = self.data_bg;        fg_step = self.data_fg


        if self.force_all_col_same_width == True:
            formatted_nested_list = padding_list(self, nested_list=nested_list)
            longest = find_longest_item(nested_list)
            padded_matrix = [[cell.ljust(longest[1][1]) for cell in row] for row in formatted_nested_list]
            formatted_nested_list = padded_matrix
        else:
            formatted_nested_list = padding_list(self, nested_list=nested_list)


        # dt_colors = set_font(bold=self.data_bold, bg=self.data_bg, fg=self.data_fg, italic=self.data_italic, underline=self.data_underline,
        #             strike=self.data_strike, blinking=self.data_blinking, dim=self.data_dim, hidden=self.data_hidden, inverse=self.data_inverse)

        hd_colors = set_font(bold=self.header_bold, bg=self.header_bg, fg=self.header_fg, italic=self.header_italic, underline=self.header_underline,
                    strike=self.header_strike, blinking=self.header_blinking, dim=self.header_dim, hidden=self.header_hidden, inverse=self.header_inverse)


        counter = 0
        n_rows = len(formatted_nested_list)
        indentation = ins_chr(self.adj_indent)
        indent = ins_chr(self.adj_indent+self.adj_int_indent)
        rsp = ins_chr(self.adj_right_space)
        lsp = ins_chr(self.adj_left_space)


        mylist = get_transpose(formatted_nested_list)
        for row in range(len(mylist)):
            for col in range(len(mylist[row])):
                if col == 0:
                    if self.force_all_col_same_width == True:
                        adj_sp = ins_chr(len(str(n_rows))-len(str(counter)))
                        if len(str(self.bullet)) == 1:
                            print(f"{indentation}{hd_colors}{lsp}{adj_sp}{self.bullet}  {mylist[row][col]}{rsp}{reset_font()}")
                        elif len(str(self.bullet)) == 2:
                            print(f"{indentation}{hd_colors}{lsp}{adj_sp}{self.bullet} {mylist[row][col]}{rsp}{reset_font()}")
                        else:
                            print(f"{indentation}{hd_colors}{lsp}{adj_sp}{counter}. {mylist[row][col]}{rsp}{reset_font()}")
                    else:
                        adj_sp = ins_chr(len(str(n_rows))-len(str(counter)))
                        if len(str(self.bullet)) == 1:
                            print(f"{indentation}{hd_colors}{lsp}{adj_sp}{self.bullet}  {mylist[row][col]}{rsp}{reset_font()}")
                        elif len(str(self.bullet)) == 2:
                            print(f"{indentation}{hd_colors}{lsp}{adj_sp}{self.bullet} {mylist[row][col]}{rsp}{reset_font()}")
                        else:
                            print(f"{indentation}{hd_colors}{lsp}{adj_sp}{counter}. {mylist[row][col]}{rsp}{reset_font()}")

                else:
                    adj_sp = ins_chr(len(str(n_rows))-len(str(counter)))
                    print(f"{indent}{dt_colors}{lsp}{adj_sp}{counter}. {mylist[row][col]}{rsp}{reset_font()}")


                if counter == 0:
                    bg_step = self.data_bg;        fg_step = self.data_fg
                else:
                    if bg_step >= self.data_bg_stop: bg_step = self.data_bg
                    else:                            bg_step += self.data_bg_step

                    if fg_step >= self.data_fg_stop: fg_step = self.data_fg
                    else:                            fg_step += self.data_fg_step

                counter += 1
                dt_colors = set_font(bold=self.data_bold, bg=bg_step, fg=fg_step, italic=self.data_italic, underline=self.data_underline,
                            strike=self.data_strike, blinking=self.data_blinking, dim=self.data_dim, hidden=self.data_hidden, inverse=self.data_inverse)
            counter = 0
        # putting back id_on
        self.id_on = bu_id_on