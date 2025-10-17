from py4htmlpc import *

# In this file I am simple testing out all available feautures
title("sreeharis acrobatics")
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

add_link("www.facebook.com","https://www.google.com")
add_link("www.google.com","https://www.facebook.com/", style = {"color":"red"})

#Now working with Tables

country_table=[ ("heading1","heading2","heading3"),
        ["first","second","third"],
       
        ["India","Japan","Germany"],
       
        ["New Delhi","Tokyo","Berlin"]]

country_table_without_headings=[ ["first","second","third"],
       
                                 ["India","Japan","Germany"],
       

                                 ["New Delhi","Tokyo","Berlin"]]

#nested table with a division for a table cell
division_in_cell=division_begins("inside_cell##",{"background-color":"red","width":"100px","height":"50px"},"sreehari loves python")

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
           [("sruthi",),"28","Alapuzha"]]  

table(new_table)

big_heading("Table with spanning rows columns")
line_break()

newest_table=[("name","age","place"),["sreehari",{"rowspan":"2"},"30","Kannur"],
              ["22","VAdakara"],
              ["nandan","33","talassery"],
              ["Vasudevan","26","Trivandrum"],
              [("sruthi",),"28","Alapuzha"],
              ["Vimal","31","Aluva"],
              ["sanjay","41","Calicut"]]

table(newest_table)

line_break()

f=form()
f.label("name","Sreehari")
line_break()
line_break()
f.input("text","one","one","Enter Sreehari\'s age")
line_break()
line_break()
f.label("second_name","Sruthi")
line_break()
line_break()
f.input("text","second","second","Enter Sruthi\'s age")
line_break()
line_break()
f.input("submit",value="submit to database")
f.close()
division_begins(class_name="simply")
biggest_heading('simply')
division_ends()
all_styles({"body":{"background-color":"#ffffcc"}})
all_styles({".simply":{"background-color":"red","width":"2000px","height":"700px"}})
line_break()
nf=form(action="winner.js",method="POST")
nf.input("text")
line_break()
line_break()
nf.input("submit",value="submit to loser")
nf.close()
line_break()
sf=form(action="getlost javscript", method="GET", style={'width':"500px","height":"500px","background-color":"violet"})
sf.label("SecondStyled Form")
line_break()
sf.input("text")
line_break()
line_break()
sf.input("submit",value="submit to winner")
sf.close()
line_break()
#form with attributes
af=form(action="love.js",method="GET",attr_list=["autocapitalize",'autocomplete="on"'],
        style={'width':"500px","height":"500px","background-color":"blue"})
af.label("everything will be capitalized")
line_break()
af.input("text")
line_break()
line_break()
af.label("second text field",style={"color":"green"})
line_break()
af.input("text")
line_break()
line_break()
af.input("submit",value="submit to antartica")
af.close()
line_break()

le=form()
le.label("Enter address:",attr_list=[])
line_break()
line_break()
le.input("text",style={"width":"100px","height":"100px"},attr_list=["required","placeholder=\"enter your address\""])
line_break()
line_break()
le.label("Enter place",id="place",style={"color":"yellow"})
line_break()
line_break()
le.input("text",id="place",value="Default is Kannur kerala",style={"width":"100px","height":"200px"})
line_break()
line_break()
le.input("submit",value="Submit to place register",style={"width":"100px","height":"200px","color":"red"})
le.close()
line_break()


radio=form()
radio.input("radio",radio_button_list=["html##","css","python"])
radio.close()
line_break()
line_break()
line_break()
#styled from
styled_radio=form()
division_begins(class_name="container")
styled_radio.input("radio",radio_button_list=["option1","option2","option3"])
division_ends()
styled_radio.close()
label1=style_copier("""padding: 10px 20px;border: 2px solid #ff5733;background-color: #ffe6e1;color: #ff5733;border-radius: 8px;cursor: pointer;font-size: 14px;transition: 0.3s;""")

label2=style_copier("""padding: 12px 22px;
            border: 2px solid #28a745;
            background-color: #e8f5e9; 
            color: #28a745; 
            border-radius: 12px;
            cursor: pointer;
            font-size: 16px;
            transition: 0.3s;""")
label3=style_copier(""" padding: 14px 24px;
            border: 2px solid #007bff; /* Blue border */
            background-color: #e1f0ff; /* Light blue background */
            color: #007bff; /* Blue text */
            border-radius: 16px;
            cursor: pointer;
            font-size: 18px;
            transition: 0.3s;""")
all_styles({".container":{"display":"flex","gap":"20px","align-items": "center",
                                              "margin-top":"20px"},
                        "input[type=\"radio\"]":{"display":"none"},"#option10 + label":label1,
                        "#option21 + label":label2,
            "#option32 + label":label3,
            "#option10:checked + label":{"background-color":"#ff5733","color": "white"},
            "#option21:checked + label":{"background-color":"#28a745","color": "white"},
            "#option32:checked + label":{"background-color":"#007bff","color": "white"}})

line_break()
checkbox=form()
checkbox.input("checkbox",checkbox_list=["html##","css##","java"])
checkbox.close()
line_break()
#new styled form
nstf=form()
nstf.label("Eneter your favourite team",style=style_copier("color:red;font-size:50px"))
line_break()
line_break()
nstf.input("text",style=style_copier("width:100px; height:300px;background-color:pink;"))
line_break()
line_break()
nstf.input("submit",value="forward",style=style_copier("width:200px;height:200px;color:green;"))
nstf.close()
line_break()
field=form()
field.fieldset(legend="Chose your favourite monster",radio_button_list=["Kraken##","Sasquatch##","Mothman##"])
field.close()
line_break()
field_check=form()
field_check.fieldset(legend="Chose your favourite monster",checkbox_list=["Kraken##","Sasquatch##","Mothman##"])
field_check.close()
#video
biggest_heading("Lets play a beautiful video")
line_break()
video(source={"ReelBe.mp4":"video/mp4"},no_video_text="No video to show",
      attr_list=['width="320"','height="240"',"controls"])