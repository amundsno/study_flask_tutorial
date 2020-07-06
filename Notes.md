## Using code blocks
Use code blocks in .html files to access python functionality.
`{% code goes here %}` is used to insert a codeblock, for instance: `{% for post in posts %}{% endfor %}`
`{{ access posted content }}` is used to access elements

## Using layouts/templates
Use layouts and content blocks for HTML-pages to avoid repetative code. See for instance ./templates/layout.html.   
In the layout file, the following block `{% block nameofblock %}{% endblock %}` will be replaced by the content inside the same block in the other file.

## Div
- Static files (CSS) must be in a folder named *static*
- Use url_for(decorated_function_name) to redirect. Lets flask keep track of paths.


## Forms and User-Input
Use extension: *wtf-forms* (flask-wtf)
