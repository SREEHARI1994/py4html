from py4htmlpc import *

heading("py4html is awesome",text_type="italics") #no argument for num and hence it defaults to 1 or biggest size
heading("py4html is aweosme")
line_break()
line_break()
line_break()
heading("py4html is awesome",2,"italics",{"color":"red"})
heading("py4html is awesome",num=1)
heading("py4html is awesome",2)
heading("py4html is awesome",3)
heading("py4html is awesome",4)
heading("py4html is awesome",5)
heading("py4html is awesome",6)
heading("py4html is awesome",text_type="sub",style={"color":"blue"})
heading("py4html is awesome",text_type="sup",style={"color":"green"})
heading("py4html is awesome",style={"color":"yellow"})
heading("py4html is awesome",3,style={"color":"violet"})
#same result as previous
heading("py4html is awesome",num=3,style={"color":"violet"})

biggest_heading("py4html is very useful")
biggest_heading("py4html is very good",text_type="italics",style={"color":"green"})
bigger_heading("py4html is very useful")
bigger_heading("py4html is very good",text_type="italics",style={"color":"red"})
big_heading("py4html is very useful")
big_heading("py4html is very good",style={"color":"violet"})
small_heading("py4html is very good")
small_heading("py4html is very good",style={"color":"orange"})
smaller_heading("py4html is very good",text_type="italics")
smaller_heading("py4html is very good",style={"color":"orange"})
smallest_heading("py4html is very good")
smallest_heading("py4html is very good",style={"color":"blue"})

