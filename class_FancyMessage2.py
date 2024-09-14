import fancyprint as fp
msg = fp.FancyMessage()
crs = fp.Cursor()

#---------------------------------------------------------------------------------------
# Start the Script                                                                     -
#---------------------------------------------------------------------------------------
fp.ins_newline(2)
title = " Love Poem "
footnote = " FootNote "
#        0         0         0         0         0         0         0        80_space_available
body = f'''
"What is love?" is a question that has been asked in many novels, poems, plays,
and songs. The answer to the question may vary and could change within a lifet-
ime for each individual. Love is often considered complex, and many philosophe-
rs and scientists have hypothesized about what it means.

https://www.betterhelp.com/advice/love/how-to-last-through-the-5-stages-of-love'''

#        0         0         0         0         0         0         0         0         01234
biography1 = '''
Jean Toomer was born on December 26, 1894, in Washington, D.C., the son of Nathan Toomer, a 
Georgian farmer, and Nina Pinchback. His grandfather, Pinckney Benton Stewart Pinchback, was
the first African American governor in the United States, serving in Louisiana during 
Reconstruction from 1872-73. Toomer began college at the University of Wisconsin in 1914, but
transferred to the College of the City of New York and studied there until 1917. Toomer spent
the next four years writing and publishing poetry and prose in Broom, The Liberator, The 
Little Review, and other journals.
He actively participated in literary society and was acquainted with such prominent figures as
the critic Kenneth Burke, the photographer Alfred Steiglitz, and the poet Hart Crane. 

In 1921, Toomer took a teaching job in Georgia and remained there for four months. The trip 
represented his journey back to his Southern roots. His experience inspired his book Cane 
(Boni & Liveright, 1923), which describes the Georgian people and landscape and is regarded
as an influential work in Modernist literature. About the book, Rudolph P. Byrd and Henry 
Louis Gates Jr. wrote,'''

biography2 = '''
Cane, a compelling, haunting amalgam of fiction, poetry, and drama  unified formally and 
thematically and replete with leitmotifs, would elevate Toomer, virtually overnight, to the
status of a canonical writer in two branches of American modernism: the writers and critics
who compose the New Critics and the “Lost Generation” and those who compose the New Negro 
movement or the Harlem Renaissance.
'''

biography3 = '''
In the early 1920s, Toomer became interested in Unitism, a religion founded by the Armenian guru George Ivanovich Gurdjieff. The doctrine taught unity, transcendence,
and mastery of self through yoga, all of which appealed to Toomer. After studying with Gurdjieff in France, Toomer began to preach his teachings in Harlem and to offer
workshops in other parts of the country. In 1936, Toomer moved to Doylestown, Pennsylvania and eventually distanced himself from Gurdjieff, taking up, instead, a 
new interest in Quakerism.

Toomer, devoted to seeking spiritual enlightenment, also questioned theboundaries of race. His longing for a national identity free from 
divisions by race or class, as illustrated by his Whitmanesque long poem“Blue Meridian.” About his quest, Elizabeth Alexander wrote, in her poem,
“Toomer”: “I did not wish to \'rise above\' / or \'move beyond\' my race. I wished / to contemplate who I was beyond / my body, this container of flesh.”
Toomer died after numerous ailments in Doylestown, Pennsylvania, on March 30, 1967.'''


# msg.bottom_lines = 0
# msg.top_lines = 0

msg.align_title = fp.Align.LEFT
# msg.align_footnote = fp.Align.LEFT

# msg.align_title = fp.Align.RIGHT
msg.align_footnote = fp.Align.RIGHT

# msg.align_title = fp.Align.CENTER
# msg.align_footnote = fp.Align.CENTER



# msg.adj_bg_lines_to_right_indent = False
# msg.adj_bg_msg_to_space_available = None # True # False    # False, True or None

msg.left_indent = 3; msg.right_indent = 3
# msg.length = fp.Length_bg.ONLY_WORD
# msg.inverse_title = True
msg.print_fancy_header(title_msg=title, body_msg=biography1, footnote_msg=None)
msg.print_fancy_header(title_msg=None, body_msg=biography2, footnote_msg=None)
msg.help_lines = True
msg.print_fancy_letter(title_msg=None, body_msg=biography3, footnote_msg=footnote)
fp.ins_newline(3)

msg.left_indent = 10; msg.right_indent = 10
msg.help_lines = False
msg.lines_title_body = 0
msg.lines_body_footnote = 0
msg.align_title = fp.Align.JUSTIFY;     msg.title_indent = 20
msg.align_footnote = fp.Align.JUSTIFY;  msg.footnote_indent = 70
msg.print_fancy_header(title_msg=title, body_msg=body, footnote_msg=None)
fp.ins_newline(2)
msg.print_fancy_header(title_msg=None, body_msg=body, footnote_msg=footnote)
fp.ins_newline(2)
msg.print_fancy_header(title_msg=None, body_msg=body, footnote_msg=None)
fp.ins_newline(2)
msg.help_lines = True
msg.print_fancy_header(title_msg="", body_msg=body, footnote_msg="")
