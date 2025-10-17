Tables
======

.. function:: table(items_list, style={}, attr_list=[])

   Generates an HTML `<table>` element from a list of rows. Supports headers, inline styling, and advanced cell configurations such as `colspan`, `rowspan`, and `common_style`.

   :param items_list: A list of rows. Each row can be:
                      - A tuple: treated as a header row using `<th>`
                      - A list: treated as normal table rows
                      - A dict: contains styling or attributes for the row
   :type items_list: list

   :param style: Optional dictionary of CSS styles applied to the `<table>` element.
   :type style: dict

   :param attr_list: Optional list of HTML attributes (as raw strings) applied to the `<table>` tag.
   :type attr_list: list of str

   :returns: Writes HTML `<table>` code directly to the global file object `f`.

   **Row Behavior:**

   - If the first row is a tuple, it is considered a header and rendered using `<th>`.
   - Rows can have individual styles if passed as dictionaries with keys like `rowspan` or using `stylizer`.

   **Cell Behavior:**

   - Each cell can be:
     
     * A string: Rendered as `<td>value</td>`
     * A tuple (value,): Rendered as `<th>value</th>`
     * A dictionary with:
       - ``colspan``: Specifies how many columns the cell spans.
       - ``rowspan``: Specifies how many rows the cell spans.
       - ``common_style``: A style dictionary processed in a separate thread using ``edit_file_4style``.

   Examples
   --------

   **Simple Table with Header**

   .. code-block:: python

      table([
          ("Name", "Age", "City"),
          ["Alice", "25", "Mumbai"],
          ["Bob", "30", "Delhi"]
      ])

   **Table with `colspan` and `rowspan`**

   .. code-block:: python

      table([
          ("Name", "Details"),
          ["Alice", {"colspan": 2, "style": {"color": "red"}}],
          ["Bob", {"rowspan": 2}],
          ["Bob Again", "Still Bob"]
      ])

   **Styled Table with Attributes**

   .. code-block:: python

      table(
          [
              ("Fruit", "Color"),
              ["Apple", "Red"],
              ["Banana", "Yellow"]
          ],
          style={"border": "2px solid black", "width": "100%"},
          attr_list=["border=1", "align=center"]
      )

   Notes
   -----

   - `common_style` triggers a call to ``edit_file_4style`` in a separate thread.
   - Do not pass only `colspan`/`rowspan` without some meaningful content or styling — it may render as an empty cell.
   - Ensure that cell types are consistent to maintain proper table formatting.

   Related
   -------

   For more information on HTML tables, see:

   - https://www.w3schools.com/html/html_tables.asp
