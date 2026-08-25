import custom_print as cp

art_logo = cp.AsciiArt()

# Print the Logos Available
art_logo.description_ascii_logos()


# Printing the Logo_Unix
art_logo.bg = 16
art_logo.fg = 196
art_logo.delay_ms = 80
art_logo.bold = True
art_logo.set_layout = cp.Layout.HORIZONTAL
# art_logo.set_layout = cp.Layout.VERTICAL
art_logo.adj_indent = 4
art_logo.adj_right_space = 2
art_logo.adj_left_space = 2
art_logo.adj_middle_space = 6


ascii_logos = [cp.Logo_Unix, cp.Logo_Debian, cp.Logo_Centos, cp.Logo_RedHat, cp.Logo_Linux]#, cp.Logo_AlmaLinux]
bg_colors   = [16, 231, 22, 16, 4] 
ctrl = 0
for logo in ascii_logos:
    art_logo.ascii_type = logo
    art_logo.bg = bg_colors[ctrl]
    art_logo.print_ascii_logo_art()
    ctrl += 1

