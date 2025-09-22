import custom_print as cp
pylo = cp.PyLO()
tbl  = cp.FancyFormat()

tbl.title_bg  = 90
tbl.title_bold = True
tbl.title_italic = True
tbl.title_align  = cp.Align.LEFT
tbl.header_bg = 90
tbl.header_bold = True
# tbl.header_horizontal_line_on = True



COLOR_NAMES = [\
"LIGHT BLACK",          "RED",                   "LIGHT OFFICE GREEN",          #2
"LIGHT BROWN",          "EARLY NIGHT BLUE",      "MID PURPLE",                  #5
"CYAN",                 "LIGHT GRAY",            "DARK GRAY",                   #8
"PASTEL RED",           "ELECTRIC LIGHT GREEN",  "DARKISH YELLOW",              #11
"LIGHT BLUE",           "LIGHT PURPLE",          "VERY LIGHT BLUE",             #14
"WHITE",                "BLACK",                 "DARK BLUE",                   #17
"NAVY BLUE",            "MIDNIGHT BLUE",         "MEDDIUM BLUE",                #20
"BLUE",                 "SUMMER GREEN",          "VERY DARK CYAN",              #23
"SEA BLUE",             "ENDEAVOUR BLUE",        "SCIENCE BLUE",                #26
"BLUE RIBBON",          "AO GREEN",              "DEEP SEA GREEN",              #29
"TEAL",                 "DEEP CERULEAN BLUE",    "STRONG BLUE",                 #32
"AZURE BLUE",           "DARK LIME GREEN",       "GO GREEN",                    #35
"DARK CYAN",            "BONDI BLUE",            "CERULEAN BLUE",               #38
"BLUE BOLT",            "STRONG LIME GREEN",     "MALACHITE GREEN",             #41
"CARIBBEAN GREEN",      "STRONG CYAN",           "DARK TURQUOISE",              #44
"VIVID SKY BLUE",       "ELECTRIC GREEN",        "SPRING GREEN",                #47
"GUPPIE GREEN",         "MEDIUM SPRING GREEN",   "BRIGHT TURQUOISE",            #50
"AQUA",                 "BLOOD RED",             "VERY DARK MAGENTA",           #53
"INDIGO",               "DARK VIOLET",           "ELECTRIC VOILET",             #56
"ELECTRIC INDIGO",      "VERDUN GREEN",          "SCORPION GRAY",               #59
"UCLA BLUE",            "SCAMPI BLUE",           "SLATE BLUE",                  #62
"CORNFLOWER BLUE",      "AVOCADO GREEN",         "GLADE GREEN",                 #65
"STEEL TEAL CYAN",      "STEEL BLUE",            "HAVELOCK BLUE",               #68
"BLUEBERRY",            "KELLY GREEN",           "FOREST GREEN",                #71
"POLISHED PIN GREEN",   "CRYSTAL BLUE",          "AQUA PEARL",                  #74
"BLUE JEANS",           "HARLEQUIN GREEN",       "MODERATE LIME GREEN",         #77 
"CARIBBEAN GREEN PEARL","EUCALYPTUS GREEN",      "MEDDIUM TURQUOISE",           #80 
"MAYA BLUE",            "BRIGHT GREEN",          "LIGHT LIME GREEN",            #83 
"LIGHT MALACHITE GREEN","MEDDIUM AQUAMARINE",    "AQUAMARINE GREEN",            #86 
"AQUAMARINE CYAN",      "DEEP RED",              "FRENCH PLUM VIOLET",          #89 
"FRESH EGGPLANT VIOLET","VIOLET",                "STRONG VIOLET",               #92 
"ELECTRIC VIOLET",      "BROWN",                 "COPPER BROWN",                #95 
"MOSTLY VIOLET",        "ROYAL PURPLE",          "MEDDIUM PURPLE",              #98 
"BLUEBERRY PURPLE",     "DARK OLIVE GREEN",      "CLAY CREEK GREEN",            #101
"TAUPE GRAY",           "COOL GRAY",             "CHETWODE BLUE",               #104
"VIOLET BLUE",          "APPLE GREEN",           "ASPARAGUS GREEN",             #107
"LEAF GREEN",           "GRAYISH CYAN",          "COBALT BLUE",                 #110
"SKY BLUE",             "PISTACHIO GREEN",       "MANTIS GREEN",                #113
"PASTEL GREEN",         "PEARL AQUA",            "SLIGHTLY CYAN",               #116
"PALE CYAN",            "GREEN",                 "LIGHT GREEN",                 #119
"VERY LIGHT LIME GREEN","MINT GREEN",            "AQUA LIME GREEN",             #122
"LIGHT CYAN",           "DARK RED",              "DARK PINK",                   #125
"DARK MAGENTA",         "HELIOTROPE MAGENTA",    "VIVID PURPLE",                #128
"ELECTRIC PURPLE",      "DARK ORANGE BROWN",     "ELECTRIC BROWN",              #131
"DARK MODERATE PINK",   "DARK MODERATE MAGENTA", "RICH LILAC VIOLET",           #134
"LAVENDER INDIGO",      "PIRATE GOLD BROWN",     "BRONZE BROWN",                #137
"DARK GRAYISH RED",     "DARK GRAYISH MAGENTA",  "LAVENDER",                    #140
"BRIGHT LAVENDER",      "LIGHT GOLD BROWN",      "LIGHT OLIVE GREEN",           #143
"DARK GRAYISH YELLOW",  "SILVER FOIL",           "GRAYISH BLUE",                #146
"BLUE PURPLE",          "VIVID LIME GREEN",      "MODERATE GREEN",              #149
"YELLOW GREEN",         "GRAYISH LIME GREEN",    "CRYSTAL CYAN",                #152
"PALE BLUE",            "LIME",                  "GREEN YELLOW",                #155
"VERY LIGHT GREEN",     "MENTHOL GREEN",         "AEREO BLUE",                  #158
"CELESTE CYAN",         "STRONG RED",            "ROYAL RED",                   #161
"MEXICAN PINK",         "HOLLYWOOD PINK",        "STRONG MAGENTA",              #164
"PHLOX VIOLET",         "STRONG ORANGE",         "INDIAN RED",                  #167
"BLUSH RED",            "SUPER PINK",            "ORCHID MAGENTA",              #170
"LIGHT MAGENTA",        "CHOCOLATE BROWN",       "COPPERFIELD BROWN",           #173
"SLIGHTLY RED",         "SLIGHTLY PINK",         "LIGHT ORCHID PINK",           #176
"BRIGHT LILAC VIOLET",  "MUSTARD YELLOW",        "EARTH YELLOW",                #179
"TAN BROWN",            "GRAYISH RED",           "GRAYISH MAGENTA",             #182
"PALE VIOLET",          "STRONG YELLOW",         "MODERATE YELLOW",             #185
"DECO YELLOW",          "PASTEL GRAY",           "LIGHT SILVER",                #188
"PALE LAVENDER",        "YELLOW",                "LIGHT GREEN YELLOW",          #191
"MINDARO YELLOW",       "PALE GREEN",            "VERY PALE GREEN",             #194
"VERY LIGHT CYAN",      "LIGHT RED",             "RASBERRY RED",                #197
"BRIGHT PINK",          "PINK",                  "MAGENTA",                     #200
"FUCHSIA",              "BLAZE ORANGE",          "BITTERSWEET RED",             #203
"STRAWBERRY RED",       "HOT PINK",              "LIGHT PINK",                  #206
"PINK FLAMINGO",        "DARK ORANGE",           "SALMON ORANGE",               #209
"TANGERINE RED",        "PINK SALMON",           "LAVENDER ROSE",               #212
"FUCHSIA PINK",         "ORANGE",                "LIGHT ORANGE",                #215
"VERY LIGHT ORANGE",    "PALE RED",              "PALE PINK",                   #218
"PALE MAGENTA",         "GOLD",                  "DANDELION YELLOW",            #221
"JASMINE BROWN",        "PALE ORANGE",           "MISTY ROSE PINK",             #224
"PINK LACE",            "LIGHT YELLOW",          "LEMON YELLOW",                #227
"PASTEL YELLOW",        "PALE YELLOW",           "VERY PALE YELLOW",            #230
"LIGHT WHITE",          "VAMPIRE BLACK",         "GRAY BLACK",                  #233
"EERIE BLACK",          "RAISIN BLACK",          "DARK CHARCOAL",               #236
"BLACK OLIVE",          "OUTER SPACE GRAY",      "DARK LIVER GRAY",             #239
"DAVYS GRAY",           "GRANITE GRAY",          "DIM GRAY",                    #242
"SONIC SILVER",         "GRAY",                  "PHILIPPINE GRAY",             #245
"DUSTY GRAY",           "SPANISH GRAY",          "LIGHTISH GRAY",               #248
"PHILIPPINE SILVER",    "SILVER",                "SILVER SAND",                 #251
"AMERICAN SILVER",      "ALTO GRAY",             "MERCURY GRAY",                #254
"BRIGHT GRAY",          "DEFAULT",               "DEFAULT"]                     #-1


result = pylo.find_duplicate(data=COLOR_NAMES, case_sensitive=True)
tbl.print_fancy_format(result)

NEW_LIST = ["HELLO","HI","BYE","hellO","Hola","Hi","HELLO"]
print(f"{cp.Bg.AVOCADO_GREEN+cp.Fg.BLACK} case_sensitive=True {cp.Bg.OFF+cp.Fg.OFF}")
print(NEW_LIST)
rst = pylo.find_duplicate(data=NEW_LIST, case_sensitive=True)
tbl.print_fancy_format(rst)

print(f"{cp.Bg.AVOCADO_GREEN+cp.Fg.BLACK} case_sensitive=False {cp.Bg.OFF+cp.Fg.OFF}")
print(NEW_LIST)
rst = pylo.find_duplicate(data=NEW_LIST, case_sensitive=False)
tbl.print_fancy_format(rst)