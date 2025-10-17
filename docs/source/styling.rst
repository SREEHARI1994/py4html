Applying style or CSS
=====================

CSS gives beauty to web pages. Normally you apply styles or css to HTML files so as to change their appearnce
and make it appear beautiful in three different ways, the first is by adding a style attribute that contains 
key-value pairs of property and its value for that particular element or tag, or we can put the collection
of style information for various elements together under the <style> tag under head at the top of the html document
or the option is to put all the css code is put in a separate file whose name ends with .css and and a link 
to it is added to the html file. In py4html we are not going for this third option of a separate css file. Instead 
you can define the style information for each tag/element, as and when they are created by adding a style parameter 
in the form of a dictionary with the key-value pairs being the properties and its values for that particular tag.
Or you can call the all_styles() function at any point in the python file to add style information to the <style>
tag under head. Read on to find out how this way of adding css works. As a suggestion, if you never pass style 
parameter while calling any py4html tag creation functions and instead define all the style information for all
the tags together at the top of the page, then once py4html generates the html file, you only need to copy 
everything between that opening and closing style tags into a new .css file to get the external syle sheet for 
your webpage.  


Elements with a particular id can be styled by adding # to the begining of id text and class names can be styled 
by starting the class names with dot "." The difference between class and id is that id is unique or in other
words there will only be a single element with a particular id in a single html page.It is also possible to
combine classes by separating them with spaces for a particular element. For eg if a paragraph tag is defined as 
<p class="first second">, then the style information of both first and second class will be applied to the tag.