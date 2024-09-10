import atexit

f=open("index.html",'w')
start_string = """<!DOCTYPE html>
<html>
<body>
"""
end_string = """</body>
</html>
"""  

f.write(start_string)

def stylizer(element,style):
    styled_string= f'<{element}  style="'
    for item in style:
        styled_string=styled_string + f"{item}:{style[item]}; "
    styled_string=styled_string + '">'
    return styled_string

def transform_text(text,text_type):
    match text_type:
        case "bold":text="<b>"+text+"</b>"
        case "strong":text="<strong>"+text+"</strong>"
        case "italics":text="<i>"+text+"</i>"
        case "emphasized":text="<em>"+text+"</em"
        case "mark":text="<mark>"+text+"</mark>"
        case "small":text="<small>"+text+"</small>"
        case "deleted":text="<del>"+text+"</del>"
        case "inserted":text="<ins>"+text+"</ins>"
        case "sub":text="<sub>"+text+"</sub>"
        case "sup":text="<sup>"+text+"</sup>"
    return text


def heading(text,num=1,text_type="",style={}):
    if text_type:
        text=transform_text(text,text_type)
    if style:
        starting=stylizer(f"h{num}",style)
    else:
        starting=f"<h{num}>"
    f.write(f"{starting}\n{text}\n</h{num}>\n")

def biggest_heading(text,text_type="",style={}):
    if text_type:
        text=transform_text(text,text_type)
    if style:
        starting=stylizer("h1",style)
    else:
        starting="<h1>"
    f.write(f"{starting}\n{text}\n</h1>\n")


def bigger_heading(text,text_type="",style={}):
    if text_type:
        text=transform_text(text,text_type)
    if style:
        starting=stylizer("h2",style)
    else:
        starting="<h2>"
    f.write(f"{starting}\n{text}\n</h2>\n")


def big_heading(text,text_type="",style={}):
    if text_type:
        text=transform_text(text,text_type)
    if style:
        starting=stylizer("h3",style)
    else:
        starting="<h3>"
    f.write(f"{starting}\n{text}\n</h3>\n")


def small_heading(text,text_type="",style={}):
    if text_type:
        text=transform_text(text,text_type)
    if style:
        starting=stylizer("h4",style)
    else:
        starting="<h4>"
    f.write(f"{starting}\n{text}\n</h4>\n")

def smaller_heading(text,text_type="",style={}):
    if text_type:
        text=transform_text(text,text_type)
    if style:
        starting=stylizer("h5",style)
    else:
        starting="<h5>"
    f.write(f"{starting}\n{text}\n</h5>\n")

def smallest_heading(text,text_type="",style={}):
    if text_type:
        text=transform_text(text,text_type)
    if style:
        starting=stylizer("h6",style)
    else:
        starting="<h6>"
    f.write(f"{starting}\n{text}\n</h6>\n")

def paragraph(text,text_type="",style={}):
    if text_type:
        text=transform_text(text,text_type)
    if style:
        starting=stylizer("p",style)
    else:
        starting="<p>"
    f.write(f"{starting}\n{text}\n</p>\n")

def line_break():
    f.write("<br>\n")
    
def division_begins(class_name="",style={},text="",type="write"):
    div_string=""
    return_string=""
    if class_name:
        div_string=f'<div class ="{class_name}"'
    else:
        div_string="<div"
    if style:
        div_string=div_string + '  style="'
        style_string=""
        for item in style:
            style_string=style_string + f"{item}:{style[item]}; "
        div_string=div_string + style_string + '"'
    if type=="write":
        f.write(div_string + ">"+ "\n")
    else:
        return_string=div_string + ">"+ "\n"
    if text:
        if type=="write":
            f.write(text+'\n')
        else:
            return_string=return_string+text+"\n"
    return_string=return_string + "</div>"
    return return_string

def division_ends():
    f.write("</div>\n")

def add_link(link_text,url):
    f.write(f'<a href="{url}">{link_text}</a>\n')

def unordered_list(*items):
    f.write('<ul>\n')
    for item in items:
        f.write(f"<li>{item}</li>\n")
    f.write('</ul>\n')

def ordered_list(*items):
    f.write('<ol>\n')
    for item in items:
        f.write(f"<li>{item}</li>\n")
    f.write('</ol>\n')

def description_list(**items):
    f.write('<dl>\n')
    for item in items:
        f.write(f"<dt>{item}</dt>\n")
        f.write(f"<dd>{items[item]}</dd>\n")
    f.write('</dl>\n')  

def table(items_list,style={}):
    if style:
        start_string=stylizer("table",style)+'\n'
    else:
        start_string='<table>\n'
    f.write(start_string)
    skip=False
    if type(items_list[0]) is tuple:
        headings=items_list[0]
        skip=True
        f.write("<tr>\n")
        for heading in headings:
            f.write(f'<th>{heading}</th>\n')
        f.write("</tr>\n")

    row_list=[]
    element_list2d=[]
    content_list=[]
    for n,row in enumerate(items_list):
        if skip:
            skip=False
            n=n-1
            continue
        if type(row) is dict:
            row_list[n-1]=stylizer("tr",row)+"\n"
        else:
            row_list.append("<tr>\n")
            
        elements_in_one_row=[]
        content_in_one_row=[]
        n=0
        for element in row:
            if type(element) is dict:
                elements_in_one_row[n-1]=stylizer("td",element)+"\n"
            else:
                elements_in_one_row.append("<td>\n")
                content_in_one_row.append(element)
        element_list2d.append(elements_in_one_row)
        content_list.append(content_in_one_row)
    #writing to html file
    for ln,row in enumerate(row_list):
        f.write(row)
        for tag,content in zip(element_list2d[ln],content_list[ln]):
            f.write(tag)
            f.write(content+"\n")
            f.write('</td>\n')
        f.write("</tr>\n")

class Form():
    def __init__(self):
        f.write("<form action="">\n")
    def label(id,text):
        f.write(f"<label for=\"{id}\">{text}</label><br>\n")


    def input(type="",id="",name="",value=""):
        if type=="text":
            f.write(f"<input type=\"text\" id=\"{id}\" name=\"{name}\" value=\"{value}\"><br>\n")
        if type=="submit":
            f.write(f"<input type=\"submit\" value=\"{value}\">")
    def close():
        f.write("</form>\n")        
    

@atexit.register
def end():
        f.write(end_string)
        f.close()