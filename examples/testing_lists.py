from py4htmlpc import *
biggest_heading("creating simple lists of 3 types",style={"color":"maroon"})
unordered_list("sree","sruthi",'Harry')
ordered_list("potter","ron","hermione")
description_list({"Harry":"hero","ron":"harry's friend","hermione":"harry and ron's friend"})

#Applying styles to ordered and unordered lists

#Common color to all list entries
line_break()
bigger_heading("common style to all list elements",style={"color":"maroon"})
unordered_list({"color":"red"},"gabriel","garcia","marquez")
line_break()
ordered_list({"color":"red"},"gabriel","garcia","marquez")

#different color for all entries
line_break()
bigger_heading("Indiviaul colors of red, blue, green for the 3 list elements",style={"color":"maroon"})
unordered_list("gabriel",{"color":"red"},"garcia",{"color":"blue"},"marquez",{"color":"green"})
line_break()
ordered_list("gabriel",{"color":"red"},"garcia",{"color":"blue"},"marquez",{"color":"green"})

#overriding common color with individual colors
line_break()
bigger_heading("overriding common color with individual colors",style={"color":"maroon"})
big_heading("common red is overrided with green for gabriel and blue for garcia",style={"color":"maroon"})
unordered_list({"color":"red"},"gabriel",{"color":"green"},"garcia",{"color":"blue"},"marquez")
big_heading("common red is overrided with blue for garcia and green for marquez",style={"color":"maroon"})
ordered_list({"color":"red"},"gabriel","garcia",{"color":"blue"},"marquez",{"color":"green"})

#list testing for ordered and unordered lists carried out succesfully
#applying common color to description list
big_heading("Applying common style of color green to all entries in description list",style={"color":"red"})
description_list({"harry":"hero","ron":"harry's friend","hermione":"harry and ron's friend"},style={"color":"green"})
#nesting paragraph as a list entry
line_break()
big_heading("Nesting paragraph as a list entry",style={"color":"red"})
para_string="""\
The paragraph function when called with a string that ends with ## returns the string surrounded by opening
and closing p tags including the style applied. These can be then inserted as such into the list by passing
this returned string to the list functions\
"""
heading_style={"color":"red"}
small_heading("A simple normal paragraph",style=heading_style)
paragraph(para_string,style={"color":"violet"})
#Now lets nest this paragraph inside list by passing a string ending with ## to paragraph function 
#and then the string returned by paragraph will be passed to list function
small_heading("Now lets nest this paragraph inside the list",style=heading_style)
new_para_string=para_string+"##"
retuned_para_string=paragraph(new_para_string,style={"color":"violet"})
ordered_list({"color":"red"},"first",retuned_para_string,"third")
biggest_heading("Testing attribute list feauture for ordered lists",style={"color":"red"},attr_list=['id="one"'])
ordered_list("Gandalf","Frodo","Bilbo",attr_list=['id="list1"','class="listclass"'])
bigger_heading("Apllying style to list entries and adding attributes",style={"color":"orange"},attr_list=['id="heading2"'])
ordered_list({"color":"blue"},"Gandalf",{"color":"red"},"Frodo","Bilbo",{"color":"green"},
             attr_list=['id="listtwo"','class="listclass2"'])