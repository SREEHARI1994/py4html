from py4html import *

division_begins("first",{"background-color":"#ff6600","margin":"auto","width":"1250px"})
biggest_heading("This is a web page", style = {"color":"white","font-size":"100px"})
paragraph("This contains more details about page",style={"color":"white","text-align":"center"})
ordered_list("google","microsoft","apple")
division_ends()
common_style={"float":"left","padding":"55px"}
centering_division={"display":"flex",
                    "justify-content":"center",
                    "align-items": "center",
                    "flex-direction":"row",
                    "height":"60vh",
                    "width":"60%",
                    "margin":"0 auto",
                    "background-color": "lightblue"}
division_begins("main",centering_division)
division_begins("sub1",common_style|{"background":"red"},"div1")
division_ends()
division_begins("sub2",common_style|{"background":"yellow"},"div2")
division_ends()
division_begins("sub3",common_style|{"background":"green"},"div3")
division_ends()
division_ends()
                
