from py4htmlpc import *

image("rubarion_logo.png","logo")
heading("Rubarion Inc",1,style={"color":"red"})
line_break()
line_break()
paragraph("Rubarion is a data company that aims to make dealing with data as easy as possibble",style={"color":"blue"})
line_break()
paragraph("This site is under construction and will be updated very soon")
line_break()
paragraph("""The first product from Rubarion is a an open source Python library py4html\n which was used to 
          create this webpage entirely using only Python in under 2 minutes\n.More info
          about this python package is available in these urls
          """,style={'color':"green"})
line_break()
add_link("Pythons offical pypi link","https://pypi.org/project/py4html/")
add_link("Github repo link","https://github.com/Rubarion/py4html")