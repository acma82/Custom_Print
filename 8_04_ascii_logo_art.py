import custom_print as cp

art_logo = cp.Art()

# Print the Logos Available
art_logo.description_ascii_logos()


# Printing the Logo_Unix
art_logo.bg = 231
art_logo.fg = 21
art_logo.delay_ms = 80
art_logo.bold = True
art_logo.ascii_type = cp.Logo_Unix
art_logo.set_layout = cp.Layout.HORIZONTAL
# art_logo.set_layout = cp.Layout.VERTICAL

art_logo.print_ascii_logo_art()

