# file_name = input("pass the name: ")
# key_word = input("pass the key word:") 
# heigh = int(input("pass the numbers of row: "))
# print(f"\u00D1") # Ñ
# print(f"\u00F1") # ñ
# print(f"\'")
# print(f"\"")
# print(f"\\")

# heighs
# Alpha  = 21          ANSI_Compact = 00    ANSI_Shadow = 6      Big = 5
# Big_Money_NE = 8     Big_Money_NW = 8     Big_Money_SE = 9     Big_Money_SW = 9 
# Blocks = 11          Bulbhead = 4         Classy = 00          Colossal = 8
# Doh = 16             Epic = 8             Font_Font = 00       Mono_12 = 00
# Roman = 7            Sweet = 9            Standard = 00
# https://budavariam.github.io/asciiart-text/

#------------------------------------------------------------------------------------------------
file_name = "Crazy_Letters"
key_word  = "Crazy"
heigh = 13
#------------------------------------------------------------------------------------------------
letters = [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
           
           ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
           
           ["backtick", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero", "minus", "equal", "backward_slash",
            "open_bracket", "close_bracket", "bemicolon", "apostrophe", "comma", "period", "forwad_slash"],

           ["tilde", "exclamation", "arroba", "pound", "dollar", "percent", "caret", "ampersand", "asterisk", "open_parenthesis",
            "close_parenthesis", "underscore", "plus", "pipe", "open_curly", "close_curly", "colon", "quotation","less_than",
             "greater_than", "question", "space", "NA"]]



with open(file_name+".py", "w") as file:

    file.write("# +-----------------------------------------------------------------------------------------------+\n")
    file.write(f"# |                                {file_name}                                                    |\n")
    file.write("# +-----------------------------------------------------------------------------------------------+\n")
    file.write("#    Uppercase :    A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z                          \n")
    file.write("#                                                                                                  \n")
    file.write("#    Lowercase :    a b c d e f g h i j k l m n ñ o p q r s t u v w x y z                          \n")
    file.write("#                                                                                                  \n")
    file.write("#    Shift_Off :    ` 1 2 3 4 5 6 7 8 9 0 - = \ [ ] ; ' , . /                                      \n")
    file.write("#                                                                                                  \n")
    file.write('#    Shift_On  :    ~ ! @ # $ % ^ & * ( ) _ + |  : " < > ?                                         \n')
    file.write("#\n")
    file.write("#\n")
    file.write("# +-----------------------------------------------------------------------------------------------+\n")
    file.write("# |                                   KeyBoard Symbol Names                                       |\n")
    file.write("# +-----------------------------------------------------------------------------------------------+\n")
    file.write("# |   ` : Backtick            - : Minus                = : Equal            \ : Backward_Slash    |\n")
    file.write("# |   [ : Open_Bracket        ] : Close_Bracket        ; : Semicolon        ' : Apostrophe        |\n")
    file.write("# |   , : Comma               . : Period               / : Forward_Slash    ~ : Tilde             |\n")
    file.write("# |   ! : Exclamation         @ : Arroba               # : Pound            $ : Dollar            |\n")
    file.write("# |   % : Percent             ^ : Caret                & : Ampersand        * : Asterisk          |\n")
    file.write("# |   ( : Open_Parenthesis    ) : Close_Parenthesis    _ : Underscore       + : Plus              |\n")
    file.write("# |   | : Pipe                { : Open_Curly           } : Close_Curly      : : Colon             |\n")
    file.write('# |   " : Quotation           < : Less_Than            > : Greater_Than     ? : Question          |\n')
    file.write("# +-----------------------------------------------------------------------------------------------+\n")

    heigh += 2  # letter_hight + top_line + bottom_line

# +--------------------------------+
# |  Doh_Close_Parenthesis Letter  |
# +--------------------------------+
    for row in range(len(letters)):
        for col in range(len(letters[row])):
            file.write(f"\n# +--------------------------------+\n")
            file.write(f"#   Letter {letters[row][col]} \n")
            file.write(f"# +--------------------------------+\n")

            file.write(f"{key_word}_{letters[row][col]} = []\n")
 
            for h in range(heigh):
                if h == 0: file.write(f"{key_word}_{letters[row][col]}.append(\"\") # Top, 0\n")
                elif h == (heigh-1): file.write(f"{key_word}_{letters[row][col]}.append(\"\") # Bottom, {heigh-1}\n")
                else:                file.write(f"{key_word}_{letters[row][col]}.append(\"\") # {h}\n")


print(f"\n\033[1;48;5;231;38;5;21m  All Done. File {file_name}.py was created  \033[0m\n")








