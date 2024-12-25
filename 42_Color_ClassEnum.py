import custom_print as cp

fs = cp.FontStyle()

# USING COLOR AS NUMBER:
# Classes  -> FancyFormat, FonstStyle, FancyMessage, 
# Function -> set_font()  
fs.bg = cp.No.SCORPION_GRAY
fs.fg = cp.No.AO_GREEN
fs.print_style(" Hello World...! ")
print()
print(f"{cp.set_font(True, cp.No.CRYSTAL_BLUE, cp.No.YELLOW)}\
    Hello There...! {cp.reset_font()}")

cp.ins_newline(2)
# USING COLOR AS NAME
print(f"{cp.Bg.WHITE+cp.Fg.BLUEBERRY_PURPLE}\
Background and Foreground {cp.Bg.OFF} Only Foreground {cp.Fg.OFF} Normal....! ")
print()

bg = cp.Bg
fg = cp.Fg
st = cp.Style

print(f"{st.UNDERLINE_ON} Hello World {st.UNDERLINE_OFF} ...!\n")

print(F"{bg.LIME+fg.BLACK+st.ITALIC_ON+st.BOLD_ON} Combination of all {st.RESET_ALL} Normal\n")

my_style = bg.BLAZE_ORANGE + fg.EERIE_BLACK + st.UNDERLINE_ON + st.ITALIC_ON +st.BOLD_ON
print(f"{my_style} Hello There...! {bg.OFF+fg.OFF+st.BOLD_OFF}")

print("\nAnother line keeping underline and italic.\n")
print(f"{st.UNDERLINE_OFF+st.ITALIC_OFF} Normal Again...!\n")

print(f"{st.BOLD_ON+st.ITALIC_ON+st.UNDERLINE_ON} Hello {st.OFF} Normal\n")

print(F"{my_style} Combination of all {st.OFF} Only BG and FG still active. {st.RESET_ALL} Normal")