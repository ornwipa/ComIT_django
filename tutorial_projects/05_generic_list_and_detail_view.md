# Tutorial: The Local Library Website

## Book list page

The book list page displays a list of all the available book records, accessed using the URL `catalog/books/`. 

### URL mapping

In **`catalog/urls.py`**, add `path('books/', views.BookListView.as_view(), name='books')` to the `urlpatterns`. This `path()` function defines a pattern to match against the URL `books/`. A view fuction will be called if the URL matches `views.BookListView.as_view()` where `as_view()` is a class method.

### View (class-based)

In **`catalog/views.py`**, use a class-based generic `ListView`, inheriting from an existing view. 
```
class BookListView(generic.ListView):
    model = Book
```

### List View template

Create the HTML file `/locallibrary/catalog/templates/catalog/book_list.html`.
- Conditional execution
```
  {% if book_list %}
    <!-- code here to list the books -->
  {% else %}
    <p>There are no books in the library.</p>
  {% endif %} 
```
- For loops
```
    {% for book in book_list %}
      <!-- code here get information from each book item -->
    {% endfor %}
```
- Accessing variables
```
      <a href="{{ book.get_absolute_url }}">{{ book.title }}</a> ({{book.author}})
```
	- Access the _fields_ of the associated book record using the "dot notation" (e.g. `book.title` and `book.author`), where the text following the book item is the field name.
	- Call _functions_ in the model from within the template, i.e., call `Book.get_absolute_url()` to get a URL for displaying the associated detail record.

Update the base template in `locallibrary/catalog/templates/base_generic.html`. Insert `{% url 'books' %}` into the URL link: `<li><a href="{% url 'books' %}">All books</a></li>`.

## Book detail page

The book detail page displays information about a specific book, accessed using the URL `catalog/book/<id>`. In addition to fields in the Book model (author, summary, ISBN, language, and genre), list the details of the available copies (`BookInstances`) including the status, expected return date, imprint, and id. 

### URL mapping

In **`catalog/urls.py`**, add `path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail')` to the `urlpatterns`. This `path()` function defines a pattern, associated generic class-based detail view, and a name. The URL pattern uses a special syntax to capture the specific id of the book. `'<int:pk>'` capture the book id, which must be a specially formatted string and pass it to the view as a parameter named `pk` (short for primary key). 

### View (class-based)

In **`catalog/views.py`**, add the code:
```
class BookDetailView(generic.DetailView):
    model = Book
```

What if the reord does not exist... Implement the class-based view as a function.
```
def book_detail_view(request, primary_key):
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')
    return render(request, 'catalog/book_detail.html', context={'book': book})
```

### Detail View template

Create the HTML file `/locallibrary/catalog/templates/catalog/book_detail.html`. The view will pass specific `Book` record extracted by the URL mapper. Within the template, book's details can be accessed with the template variable, named `object` or `book`.

- In `{% for copy in book.bookinstance_set.all %}`, the function `book.bookinstance_set.all()` is needed because `ForeignKey` (one-to-many) field is declared. 

- Setting a class (`text-success`, `text-danger`, `text-warning`) to color-code the human readable status text for each book instance. Note that `BookInstance.get_status_display()` is automatically created by Django for every [choice fields](https://docs.djangoproject.com/en/3.1/ref/models/fields/#choices), e.g. `get_FOO_display()`.
```
 <p class="{% if copy.status == 'a' %}text-success{% elif copy.status == 'm' %}text-danger{% else %}text-warning{% endif %}">
 {{ copy.get_status_display }} </p>
```

## Pagination

In the **views.py**, add `paginate_by = 10` as a class attribute of the model.

In the **base_generic.html**, immediately after the `{% endblock %}` of the "content block", add the following code.
```
  {% block pagination %}
    {% if is_paginated %}
        <div class="pagination">
            <span class="page-links">
                {% if page_obj.has_previous %}
                    <a href="{{ request.path }}?page={{ page_obj.previous_page_number }}">previous</a>
                {% endif %}
                <span class="page-current">
                    Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
                </span>
                {% if page_obj.has_next %}
                    <a href="{{ request.path }}?page={{ page_obj.next_page_number }}">next</a>
                {% endif %}
            </span>
        </div>
    {% endif %}
  {% endblock %}
```
The `page_obj` is a [paginator](https://docs.djangoproject.com/en/3.1/topics/pagination/#paginator-objects) that will exist if pagination is being used on the current page. The `{{ request.path }}' is used to get the current page URL for creating the pagination links. 
