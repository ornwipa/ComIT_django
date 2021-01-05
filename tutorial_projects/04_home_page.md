# Tutorial: The Local Library Website

**Overview** First, define the information to display to users and the URLs for returning those resources. Then, create a URL mapper, views, and templates to display the pages.
- URL mappers (`urls.py`) receive HTTP requests and forward the suppored URLs to the appropriate view functions.
- View functions (`views.py`) get the requested data from the models (`models.py`), create HTML pages (response) that dispaly the data, and return the page to the user to view in the browser.
- Templates (`<filename>.html`) are used when rendering data in the views.

## Defining the resource URLs

For read-only home page, URLs are:
- `catalog/` : home or index page
- `catalog/books` : list of all books
- `catalog/authors/` : list of all authors
- `catalog/book/<id>` : detail view of a particular book
- `catalog/author/<id>` : detail view for specific author

## Creating the index page

### URL mapping

Note that, in **`locallibrary/urls.py`**, the code `path('catalog/', include('catalog.urls'))` was already added to the `urlpatterns` to ensure that, when URl starting with `catalog/` is received, the *URLConf* module `catalog.urls` will process the remaining substring.

Create a placeholder file for the *URLConf* module, named **`catalog/urls.py`**, by adding `path('', views.index, name='index')` to the `urlpatterns`.
```
urlpatterns = [
    path('', views.index, name='index'),
]
```
A view function will be called if the URL pattern is detected. The `views.index` is a function, named `index()` in the `views.py` file.

The `path()` function speficies a `name` parameter, which is a unique identifier for this URL mapping. The `name` parameter can be used to "reverse" the mapper, i.e., to create a URL poiting the resource that the mapper is designed to handle. For example, it can refer or link to home page from any other page by adding `<a href="{% url 'index' %}">Home</a>` in a template.

### View (function-based)

> A view is a function that processes an HTTP request, fetches the required data from the database, renders the data in an HTML page using an HTML template, and then returns the generated HTML in an HTTP response to display the page to the user. 

The index view for this model fetches information about the `Book`, `BookInstance` and `Author` records in database, and passes that informatio to a template.

Open **`catalog/views.py`**, note that django already import the [render()](https://docs.djangoproject.com/en/3.1/topics/http/shortcuts/#django.shortcuts.render) shortcut function to generate an HTML file using a template and data.

Define the `index()` view as a function, i.e., `def index(request)` where the `request` object is an `HttpRequest`.

Within the definition, fetch the data such as the number of records using `objects` attribute on the model class; for example,
```
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
```

Create a `context` variable as a Python dictionary; for example,
```
    context = {
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
    }
```

At the end, call `render()` function to create an HTML page.
```
    return render(request, 'index.html', context=context)
```

### Templates

Django application created using **startapp** will look for templates in a subdirectory name "templates".

**Extending templates** - Specify the base template using `extends` template tag. Declare sections using `block`/`endblock`.
```
{% extends "base_generic.html" %}

{% block content %}
  <p>Welcome to LocalLibrary</p>
{% endblock %}
```

**LocalLibrary base template** - Create a new file `base_generic.html` in **`/locallibrary/catalog/templates/`** which defines blocks for `title`, `sidebar` and `content` within the `<html>` tags.

The template includes CSS from Bootstrap in `<link rel="stylesheet" href="https://.../bootstrap.min.css">` and refers to a local *styles.css*. Create a `style.css` file in **`/locallibrary/catalog/static/css/`**.
```
.sidebar-nav {
    margin-top: 20px;
    padding: 0;
    list-style: none;
}
```

**Index template** - Create an HTML file `index.html` in **`/locallibrary/catalog/templates/`** with the following sample code. This code extends the base template on the first line then replaces the default `content` block for the template. Variables are enclosed in double braces such as `{{ num_books }}`.
```
{% extends "base_generic.html" %}

{% block content %}
  <p>The library has the following record counts:</p>
  <ul>
    <li><strong>Copies:</strong> {{ num_instances }}</li>
    <li><strong>Copies available:</strong> {{ num_instances_available }}</li>
  </ul>
{% endblock %}
```

**Referencing static files in templates** - Call the `load` template tag specifying "static" to add the template library. THe default skeleton website sets the value of `STATIC_URL` to `/static/`.
```
{% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
```

**Configuring where to find the templates** - Django searches for templates in `TEMPLATES` object in the **`settings.py`** file. The `'APP_DIRS': True` tells Django to search for templates in a subdirectory of each application in the project.
