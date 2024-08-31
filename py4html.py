f=open("index.html",'w')
start_string = """<!DOCTYPE html>
<html>
<body>
"""
end_string = """</body>
</html>
"""  
def start():
    f.write(start_string)

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


def heading(text,num=1,text_type=""):
    if text_type:
        text=transform_text(text,text_type)
    f.write(f"<h{num}>{text}</h{num}>\n")

def biggest_heading(text):
    f.write(f"<h1>{text}</h1>\n")

def bigger_heading(text):
    f.write(f"<h2>{text}</h2>\n")

def big_heading(text):
    f.write(f"<h3>{text}</h3>\n")

def small_heading(text):
    f.write(f"<h4>{text}</h2>\n")

def smaller_heading(text):
    f.write(f"<h5>{text}</h5>\n")

def smallest_heading(text):
    f.write(f"<h6>{text}</h6>\n")

def paragraph(text):
    f.write(f"<p>{text}</p>\n")

def line_break():
    f.write("<br>\n")
    
def division_begins():
    f.write("<div>")

def division_ends():
    f.write("</div>\n")

def add_link(link_text,url):
    f.write(f'<a href="{url}">{link_text}</a>\n')
    
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
    
    
def end():
    f.write(end_string)
    f.close()