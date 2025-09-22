import custom_print as cp

def print_items():
    info_items = [["Topis:","Languages:","Specialities:"],
                  ["Arithmetics", "Geometry","Calculous"],
                  ["Spanish", "English","Japanese","Portuguese","Korean"],
                  ["EE", "CS","ME"]]
    row_I = 1
    for title in info_items[0]:
        print(f"\n  {cp.set_font(True,90,231)} {title} {cp.reset_font()}\n")
        for info in info_items[row_I]:
            print(f"    {cp.set_font(True, -1, 22)} {info} {cp.reset_font()}")
        row_I += 1
    

print_items()
cp.ins_newline(1)