import custom_print as cp
import sys

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

        all_topics = ["screen_functions",  "internal_functions",  "help_classes",  "cursor",  "fontstyle",  "fancymessage",  "pen",  "divider",  "fancyformat",  "asciiart",
                      "clean", "clear","dimensions", "erase", "resize", 
                      "ansi_colors", "ins_chr", "ins_newline", "set_font_reset_font", "terminal_bell",
                      "align", "length_bg", "ascii_letter", "line_style", "bg", "logo", "color_names", "move", "divider_style", "no", "fg", "style", "layout", "unicode",
                      "jumpto", "jumpxy", "moveto", "movexy",
                      "start_style", "stop_style", "print_style", "reset_style",
                      "print_fancy_message", "print_fancy_note",
                      "draw_line", "draw_rectangle",
                      "print_fancy_divider",
                      "fancyformat", "print_fancy_format", "reset_fancy_format",
                      "print_ascii_art", "print_multi_ascii_art", "print_ascii_logo_art", "print_reversed_ascii_logo_art"]
        

        # converting all the items of the list in lowercase
        original_list = []
        for i in sys.argv:
            original_list.append(i.lower())

        # when only the first argument ,custom_print,  is being passed
        if (len(original_list)) <=1:
            cp.help.about_custom_print()
            exit()

        # checking if the second argument exist when only 2 arguments are being passed
        elif (len(original_list)) == 2:            
            if original_list[1] == "help":
                cp.help.help_documentation()
                exit()

            elif original_list[1] == "all" or original_list[1] == "documentation":
                cp.help.all_documentation()
                exit()

            else:
                if original_list[1] in all_topics:
                    original_list.pop(0) # remove the parameter 0 (custom_print)
                else:
                    print(f"\n  The topic {cp.set_font(1,196,231)} \"{original_list[1]}\" {cp.reset_font()} is not recognize by custom_print Module  \n")
                    exit()

        # more than one parameter
        else:
            if "all" in original_list or "documentation" in original_list:
                cp.help.all_documentation()
                exit()

            else:
                original_list.pop(0) # remove the parameter 0 (custom_print)
                # checking that all the arguments exist
                v_exist = 1
                for h in original_list:
                    if h in all_topics:
                        pass
                    else:
                        print(f"\n  The topic {cp.set_font(1,196,231)} \"{h}\" {cp.reset_font()} is not recognize by custom_print Module")
                        v_exist = 0


            # if at least one item does not exist in the documentation then we leave
            if v_exist == 0: 
                exit()

        



        # deleting duplicate items in the list
        unique_topic_list = list(dict.fromkeys(original_list))
        


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
            topic = eval("cp.help."+display+"_info")
            topic()
