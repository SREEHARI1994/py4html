from py4html import *

# In this file I am simple testing out all available feautures

heading("Biggest heading unstyled unformatted")
heading("biggest heading unstyled unformatted with heading number given",1)
heading("Biggest heading with text formatting",1,"bold")
heading("once again same biggest heading in italics",1,"italics")
heading("biggest heading with style and text formatting",1,"italics",style={"color":"red"})
heading("biggest heading with style and text formattting multiple styles center align",1,
        style={"text-align":"center","color":"blue"})
line_break()

heading("Biggest heading unstyled unformatted")
heading("biggest heading unstyled unformatted with heading number given",1)
heading("Biggest heading with text formatting",1,"bold")
heading("once again same biggest heading in italics",1,"italics")
heading("biggest heading with style and text formatting",1,"italics",style={"color":"red"})
heading("biggest heading with style and text formattting multiple styles center align",1,
        style={"text-align":"center","color":"blue"})
line_break()

heading("Bigger heading unstyled unformatted",2)
heading("Bigger heading with text formatting",2,"bold")
heading("once again same bigger heading in italics",2,"italics")
heading("bigger heading with style and text formatting",2,"italics",style={"color":"red"})
heading("bigger heading with style and text formattting multiple styles center align",2,
        style={"text-align":"center","color":"blue"})
line_break()

heading("Big heading unstyled unformatted",3)
heading("Big heading with text formatting",3,"bold")
heading("once again same big heading in italics",3,"italics")
heading("big heading with style and text formatting",3,"italics",style={"color":"red"})
heading("big heading with style and text formattting multiple styles center align",3,
        style={"text-align":"center","color":"blue"})
line_break()

heading("Small heading unstyled unformatted",4)
heading("Small heading with text formatting",4,"bold")
heading("once again same small heading in italics",4,"italics")
heading("Small heading with style and text formatting",4,"italics",style={"color":"red"})
heading("Small heading with style and text formattting multiple styles center align",4,
        style={"text-align":"center","color":"blue"})
line_break()

heading("smaller heading unstyled unformatted",5)
heading("smaller heading with text formatting",5,"bold")
heading("once again same smaller heading in italics",5,"italics")
heading("smaller heading with style and text formatting",5,"italics",style={"color":"red"})
heading("smaller heading with style and text formattting multiple styles center align",5,
        style={"text-align":"center","color":"blue"})
line_break()

heading("smallest heading unstyled unformatted",6)
heading("smallest heading with text formatting",6,"bold")
heading("once again same smallest heading in italics",6,"italics")
heading("smallest heading with style and text formatting",6,"italics",style={"color":"red"})
heading("smallest heading with style and text formattting multiple styles center align",6,
        style={"text-align":"center","color":"blue"})
line_break()
#Now working with Tables

country_table=[ ("heading1","heading2","heading3"),
        ["first","second","third"],
       
        ["India","Japan","Germany"],
       
        ["New Delhi","Tokyo","Berlin"]]

country_table_without_headings=[ ["first","second","third"],
       
                                 ["India","Japan","Germany"],
       

                                 ["New Delhi","Tokyo","Berlin"]]

#nested table with a division for a table cell
division_in_cell=division_begins("inside_cell",{"background-color":"red","width":"100px","height":"50px"},"sreehari loves python",type="nested")

nested_table=[ ["first","second","third"],
               ["India",
                division_in_cell,{"width":"100px","height":"50px"},
                "Germany"],
               ["New Delhi","Tokyo","Berlin"]]

table(country_table)
line_break()
table(country_table_without_headings)

line_break()
table(nested_table)

line_break()
#setting width of entire table first and then changing widths of columns and rows
biggest_heading("Setting the first column to be 70% of the table width")

new_table=[("name","age","place"),
           ["sreehari",{"width":"70%"},"30","Kannur"],
           ["Rahul","22","Vadakara"],
           ["sruthi","28","Alapuzha"]]

table(new_table,{"width":"100%"})
line_break()

bigger_heading("Same table with Border")

common_table_style={"border":"1px solid black","border-collapse":"collapse"}
table(new_table,common_table_style|{"width":"100%"})
#applying border to inner columns and rows too
line_break()
big_heading("Applying border to column and row")
new_table=[("name","age","place"),
           ["sreehari",{"width":"70%"},"30","Kannur"],
           ["Rahul","22","Vadakara"],
           ["sruthi",{"common_style":{("table","th","td"):common_table_style}},"28","Alapuzha"]]
#table(new_table,common_table_style|{"width":"100%"})
table(new_table)

#table with first rows as headings
big_heading("Table with first row entry as headings")
line_break()

new_table= [("name","age","place"),
           [("sreehari",),"30","Kannur"],
           [("Rahul",),"22","Vadakara"],
           [("sruthi",),{"common_style":{("table","th","td"):common_table_style}},"28","Alapuzha"]]         
           
table(new_table)