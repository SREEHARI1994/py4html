=====
Lists
=====

Lists are one of the easiest to make in py4html. We just pass the entries to be included in the list as a 
touple or in other words as arguments to the function, separated by commas

There are 3 types of lists

First and a very common type is **unordered lists** in which the **list entries will be rendered on the web page
as bullet points** (dot followed by text).i.e there is no numbering for the list entries or list items
Example-

* Harry
* Ron
* Hermione

Second and another very common type is **ordered_list** in which the **list items begin with a number starting from
1 for the first item and 10 for the tenth item**
Example-

1. Harry
2. Ron
3. Hermione

Third and a very less kind of list is **Description lists** where we have **essentially a list item followed 
by its explanation on the next line and so on.** This is easy to understand by looking at the example given below
which is about Harry Potter characters and a short description of whether they are good or bad.
Example-

Harry
   He is the hero and therefore obviously a good lad

Ron
   He is harry's friend who is mostly good

Voldemort
   He is the most kind gentle and humble out of all Harry Potter characters


**Ordered Lists**

*python function documentation*

.. py:function:: ordered_list(items)

   The entries to be included in the list are passed as a touple separated by commas to 'items' the only 
   argument of this function

.. py:function:: unordered_list(items)

   The entries to be included in the list are passed as a touple separated by commas to 'items' the only 
   argument of this function


Example code::
   
   ordered_list("sreehari","sruthi","rahul")
   if "sree":
      print("yes")