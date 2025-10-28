# py4html
<b>py4html short for Python for HTML</b> is a simple Python library that makes it possible to develop websites entirely using python by writing HTML code in python or in other words you write your webpage
appearance in Python and the library generates the equivalent HTML code for you.

Write HTML in Python. No need to type a single word of HTML. Use Python to create web pages. Do web development only using Python. This is an ongoing project and will be updated frequently

Detailed documentation for using py4html are available [here](https://py4html.readthedocs.io/en/latest/)

(Documentation will be updated regularly in the coming days and it will be fully complete very soon)

py4html is a published [python package](https://pypi.org/project/py4html/) as such can be installed easily using the regualar pip command

```
pip install py4html
```

# 🐍 py4html  
### Write HTML with pure Python — no templates, no web frameworks, just Python code.  

---

## 📘 Overview  

`py4html` is a **Python library** that allows developers to create HTML files directly using Python functions — without writing any raw HTML manually.  
It automatically generates an HTML file corresponding to the Python file that imported it (for example, `my_page.py` creates `my_page_.html`).  

You can build complete web pages, including **headings, paragraphs, divs, lists, links, tables, and forms**, all from simple Python calls.  

---

## 🚀 Features  

✅ Automatically generates an HTML file when imported  
✅ Thread-safe file operations for simultaneous edits  
✅ Style elements directly using Python dictionaries  
✅ Add inline CSS or `<style>` blocks easily  
✅ Create all heading levels (`h1` to `h6`)  
✅ Add paragraphs, links, and text formatting (bold, italics, etc.)  
✅ Generate ordered, unordered, and description lists  
✅ Build HTML tables with rowspan, colspan, and styling support  
✅ Generate complete HTML forms — including text inputs, radio buttons, and checkboxes  

---

## 🧠 How It Works  

When you `import py4html` in your Python file, it:  

1. Detects the importing file’s name (e.g. `example.py`)  
2. Creates a corresponding HTML file named `example_.html`  
3. Starts writing HTML automatically from a basic structure:  

```html
<!DOCTYPE html>
<html>
<head>
<style>
</style>
</head>
<body>
```

Everything you generate via `py4html` functions is appended to this file until the Python interpreter exits.  

---

## ✨ Example Usage  

### 1️⃣ Basic Page with Headings and Paragraphs

```python
from py4html import *

title("My First py4html Page")

biggest_heading("Welcome to py4html!")
paragraph("This page was generated entirely using Python.")
line_break()

paragraph("You can add *styles*, **headings**, and even forms easily.")
```

Output HTML (`example_.html`):

```html
<!DOCTYPE html>
<html>
<head>
<title>My First py4html Page</title>
<style>
</style>
</head>
<body>
<h1>
Welcome to py4html!
</h1>
<p>
This page was generated entirely using Python.
</p>
<br>
<p>
You can add *styles*, **headings**, and even forms easily.
</p>
</body>
</html>
```

---

### 2️⃣ Styling Elements

```python
from py4html import *

all_styles({
    "body": {"background-color": "lightyellow", "font-family": "Arial"},
    "h1": {"color": "darkblue"},
})

biggest_heading("Styled Page Example", style={"text-align": "center"})
paragraph("This paragraph is normal.")
paragraph("This one is styled!", style={"color": "green", "font-size": "18px"})
```

---