from py4html import *

heading("This will default to biggest heading")
heading("This is second biggest heading",2)
heading("same heading but in bold",2,"bold")
line_break()
biggest_heading("Now moving to colored headings")
biggest_heading("Let this biggest heading be in bold","bold")
biggest_heading("Now let it be in italics","italics")
biggest_heading("styled but omitting text formatting",style={"color":"red"})
biggest_heading("styled and text formatted","italics",style={"font-size":"100px","color":"green"})