# Tutorial: The Local Library Website

This tutorial illustrates how to work with HTML forms in Django; it extends the website to allow librarians (with permission) to renew books with the following steps:
- create a form that allows users to enter a date
- seed the date field with initial value of 3 weeks from the current date
- add validation to ensure that dates are not in the past or too far in the future
- write the validated date to the current record's `BookInstance.due_back` field

### Form

The `Form` **class** specifies the fields in the form, their layout, display widgets, labels, initial values, valid values, and error messages associated with invalid fields. The *class* also provides *methods* for rendering itself in templates using predefined formats, e.g. tables, lists, or getting value from an element.

The declaration syntax for a `Form` is very similar to which for declaring a `Model`, and shares the same field types and some similar parameters. To create a `Form`, create a file **locallibrary/catalog/forms.py** and add the following code:

```
from django import forms

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

```

The `DateField` is for entering the renewal date that will render in HTML with a blank value.

To validate a single field, override the method `clean_<fieldname>()`; in this case, `clean_renewal_date()` as follow:

```
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data
```

In this method, first get data from `self.cleaned_data['renewal_date']`, then perform logical check, and always return the cleaned data, i.e. date in this case.

### URL configuration

In **locallibrary/catalog/urls.py**, add URL for the _renew-book_ page by adding the `path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian')` to the `urlpatterns`.

The URL configuration will redirect URLs with the format **/catalog/book/<bookinstance_id>/renew/** to the function named `renew_book_librarian()` in **views.py**, and send the `BookInstance` id as the parameter named `pk` (primary key). The pattern only matches if `pk` is a correctly formatted `uuid`.

### View

The view render the default form when it is first called, then either re-render it with error messages or process the data and redirect to a new page.

The code `get_object_or_404(BookInstance, pk=pk)` will get the current `BookInstance`. If it does not exist, the view will immediately exit and the page will display a "not found" error.

Test against the POST request type (`if request.method == 'POST':`) to identify form validation requests then process data.

Otherwise, `GET` (under an `else` condition) to identify the initial form creation request, i.e. pass an `initial` value for the `renewal_date` field.

If this is a POST request, create a form object and populate it with data from the request. This process is called "binding". Then use `form.is_valid()` to check all the fields including newly-created `clean_renewal_date()` function to check date range.

If the form is not valid, call `render()`. If the form is valid, start to use data, accessed through `form.clean_data`. For instance, `book_instance.due_back = form.cleaned_data['renewal_date']` is to save the data as `due_back` value of `BookInstance` object.

Note that `HttpResponseRedirect()` creates a redirection to a specified URL and `reverse()` generates a URL from a URL configuration name and a set of arguments.

```
import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import RenewBookForm

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)
```

### Template

Create the template referenced in the view (**/catalog/templates/catalog/book_renew_librarian.html**) with the following code:

```
{% extends "base_generic.html" %}

{% block content %}
  <h1>Renew: {{ book_instance.book.title }}</h1>
  <p>Borrower: {{ book_instance.borrower }}</p>
  <p>{% if book_instance.is_overdue %} class="text-danger"{% endif %}>Due date: {{ book_instance.due_back }}</p>
  
  <form action="" method="post">
    {% csrf_token %}
    <table>
    {{ form.as_table }}
    </table>
    <input type="submit" value="Submit">
  </form>
{% endblock %}
```

The template references `{{ book_instance }}` as it is passed into the context object in the `render()` function.

The `<form>` tag is to specify where the form is to be submitted, i.e. `action`, and the `method`, i.e. HTTP POST. Inside the tag, define `<input type="submit">` so that users can press to submit the data. The `{% csrf_token %}` is for forgery protection.

### Testing the page

Add `{% if perms.catalog.can_mark_returned %}- <a href="{% url 'renew-book-librarian' bookinst.id %}">Renew</a>  {% endif %}` to the page showing book instance visible for staffs only.

