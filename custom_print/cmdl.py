import custom_print as cp
import help
# from help import*
import sys


def about_custom_print():
    
    '''  Description of custom_print project  '''

    lst = [["Module Name",         "custom_print"                                   ],
           ["Version",             "1.1.4"                                          ],
           ["Author",              "Miguel Angel Aguilar Cuesta"                    ],
           ["Author Email",        "acma.mex@gmail.com"                             ],
           ["Description",         "Customized Print"                               ],
           ["Requirement",         "Python 3.12 or greater"                         ],
           ["Long Description",    "README.md"                                      ],
           ["Content Type",        "MarkDown"                                       ],
           ["Find README.md at",   "https://github.com/acma82/Custom_Print"         ],
           ["Help on Terminal",    "custom_print help"                              ],
           ["Dependencies",        "None"                                           ],
           ["License",             "Everyone Can Use It At Their Own Risk"          ]]


    tbl = cp.FancyFormat()
    FACE = " (" + "0" + chr(0x25E1) + "0" + ") "
    tbl.title_msg = FACE + "  Project Description "
    tbl.title_align = "center"
    tbl.title_bg = 231
    tbl.title_fg = 234
    tbl.title_bold = True

    
    tbl.footnote_msg = "Released on Friday, December 27, 2024"
    tbl.adj_top_space = 1
    tbl.adj_bottom_space = 1


    tbl.header_bg = 54;             tbl.data_bg = 231
    tbl.header_fg = 231;            tbl.data_fg = 234
    tbl.header_bold = True;         tbl.bold_data = True
    tbl.adj_top_margin = 2;         tbl.adj_indent = 4

    tbl.print_fancy_format(lst, "design_10")
    cp.ins_newline(1)

if __name__ == "__main__":        
        # variabvles needed for the documentation
        main_topics        = ["screen_functions",  "internal_functions",  "help_classes",  "cursor",  "fontstyle",  "fancymessage",  "pen",  "divider",  "fancyformat",  "asciiart"]

        screen_functions   = ["clean", "clear","dimensions", "erase", "resize"]

        internal_functions = ["ansi_colors", "ins_chr", "ins_newline", "set_font & reset_font", "terminal_bell"]

        help_classes       = ["align", "length_bg", "ascii_letter", "line_style", "bg", "logo", "color_names", "move", "divider_style", "no", "fg", "style", "layout", "unicode"]

        cursor             = ["jumpto", "jumpxy", "moveto", "movexy"]

        fontstyle          = ["start_style", "stop_style", "print_style", "reset_style"]

        fancymessage       = ["print_fancy_message", "print_fancy_note"]

        pen                = ["draw_line", "draw_rectangle"]

        divider            = ["print_fancy_divider"]

        fancyformat        = ["fancyformat", "print_fancy_format", "reset_fancy_format"]

        asciiart           = ["print_ascii_art", "print_multi_ascii_art", "print_ascii_logo_art", "print_reversed_ascii_logo_art"]

        all_topic_together = ["screen_functions",  "internal_functions",  "help_classes",  "cursor",  "fontstyle",  "fancymessage",  "pen",  "divider",  "fancyformat",  "asciiart",
                             "clean", "clear","dimensions", "erase", "resize",
                             "ansi_colors", "ins_chr", "ins_newline", "set_font & reset_font", "terminal_bell",
                             "align", "length_bg", "ascii_letter", "line_style", "bg", "logo", "color_names", "move", "divider_style", "no", "fg", "style", "layout", "unicode",
                             "jumpto", "jumpxy", "moveto", "movexy",
                             "start_style", "stop_style", "print_style", "reset_style",
                             "print_fancy_message", "print_fancy_note",
                             "draw_line", "draw_rectangle",
                             "print_fancy_divider",
                             "fancyformat", "print_fancy_format", "reset_fancy_format",
                             "print_ascii_art", "print_multi_ascii_art", "print_ascii_logo_art", "print_reversed_ascii_logo_art"]
        

        # when only the first argument ,custom_print,  is being passed
        if (len(sys.argv)) <=1:
            about_custom_print()
            exit()

        # checking if the second argument exist when only 2 arguments are being passed
        elif (len(sys.argv)) == 2:            
            if sys.argv[1] == "help":
                help.documentation_help()
                exit()

            elif sys.argv[1] == "all":
                help.all_documentation()
                exit()

            else:
                if sys.argv[1] in all_topic_together:
                    sys.argv.pop(0) # remove the parameter 0 (custom_print)
                else:
                    print(f"\n  The option {cp.set_font(1,196,231)} \"{sys.argv[1]}\" {cp.reset_font()} is not recognize by custom_print Module  \n")
                    exit()

        # more than one parameter
        else:
            sys.argv.pop(0) # remove the parameter 0 (custom_print)
            # checking that all the arguments exist
            v_exist = 1
            for h in sys.argv:
                if h in all_topic_together:
                    pass
                else:
                    print(f"\n  The option {cp.set_font(1,196,231)} \"{h}\" {cp.reset_font()} is not recognize by custom_print Module")
                    v_exist = 0


            # if at least one item does not exist in the documentation then we leave
            if v_exist == 0: 
                exit()

        

        # converting all the items of the list in lowercase
        original_list = []
        for i in sys.argv:
            original_list.append(i.lower())

        # deleting duplicate items in the list
        unique_topic_list = list(dict.fromkeys(original_list))
        

        if "all" in unique_topic_list:
            help.all_documentation()
        else:
            # removing the functions being called when the group is being called.        
            # removing the methods being called when the class is bein called.
            for topic in main_topics:
                if topic in unique_topic_list:
                    for fun in (eval(topic)):
                        if fun in unique_topic_list:
                            unique_topic_list.remove(fun)
                        else:
                            pass

            

        
            # Calling all the functions or methods or group of functions or group of classes to be displayed
            # unique_topic_list contains all the topics the user wants to see
            for display in unique_topic_list:
                topic = eval("help."+display)
                topic()
