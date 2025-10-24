from py4html import *

#Table with Headings
state_capital=[("State","Capital"),["Kerala","Thiruvanathapuram"],["Tamil Nadu","Chennai"],
               ["Karnataka","Bangalore"],["West Bengal","Kolkata"]]

table(state_capital)

#table without headings and first row first column text styled with red color

state_capital=[["Kerala",{"color":"red"},"Thiruvanathapuram"],["Tamil Nadu","Chennai"],
               ["Karnataka","Bangalore"],["West Bengal","Kolkata"]]
line_break()
line_break()
table(state_capital)

#table with entire first row text styled with red color

state_capital=[["Kerala","Thiruvanathapuram"],{"color":"red"},["Tamil Nadu","Chennai"],
               ["Karnataka","Bangalore"],["West Bengal","Kolkata"]]
line_break()
line_break()
table(state_capital)