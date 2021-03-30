# ComIT Lecture on Django

Django is a data-driven web development framework.

Documentation: www.djangoproject.com/start/overview/

## Django Framework Layers

A Django project can be divided into layers, each with their own sets of responsibilities.

- Model layer: abstraction layer for structuring and manipulating data in application.

- View layer: encapsulates the logic responsible for processign a user's requests and for returning responses.

- Template layer: provides a designer-friendly syntax for rendering information to be presented to the user (HTML + other stuff).

## Structure of Django Project

A Django project can be divided into sub-modules known as "apps". Each "app" is best written as self-sufficient unit of functionality. An app should be able to be removed from a project and reused in another with minimal effort.

```
mysite/		<- project folder
  manage.py		<- utility script
  mysite/		<- actual project package
    settings.py	<- define how the website runs
    urls.py		<- declare URL, map views to URL
    asgi.py		<- server entry point
    wsgi.py		<- server entry point
  polls/		<- directory containing "polls" app
    admin.py		<- define admin site
    apps.py		<- define app config
    models.py		<- define models
    tests.py		<- define unit tests
    views.py		<- define views
```

To start a Django project, use the command `django-admin startproject <project name>`.

To start a Django app, within the project folder, use the command `django-admin startapp <app name>`.

### Django Model

A model represents a table in a (relational) database: columns ~ attributes; rows ~ instances.

*Schema* = general shape or architecture of database (columns or fields), not the data themselves.

### Django View

A view is responsible for taking a request and returning a response.

Views can be functions or classes. See the example folder.

```
from django.http import HttpResponse
def get_current_time(request):
	current_time = datetime.now()
	html = f"<html><body>It is now {current_time}.</body></html>"
	return HttpResponse(html)
```

In the `urls.py` file, add the following codes to map a view to a URL. Note that `first_app` is the name of the application.

```
from first_app.views import get_current_time # add this line
urlpatterns = [
    path('admin/', admin.site.urls),
    path('current_time/', get_current_time, name='current_time') # add this line
]
```

Note: see the `TemplateView`, `ListView` and `DetailView` use cases in examples. These base views allow to pass only the *context* to render on html. 

### Django Template

A template is a text document or Python using string. Django template languages are HTML, CSS, JavaScript.

There can be Python component in the .html file, using **{{ }}**.

The `views.py` should be changed to the following codes:

```
    the_data = {
        'current_time': current_time,
    }
    response = SimpleTemplateResponse('current_time.html', the_data)
    return response
```

In the `templates/current_time.html`, the html file contains "It is now {{current_time}}."

To add a style sheet, use `static` folder and add `<link rel = "stylesheet" href={% static people/mystyle.css %}>` to the head of the html file.

### Django Forms

A Python class, not HTML. A form has fields and each field has data validation.

```
from django import forms
class NameForm(forms.Form):
	your_name = forms.CharField(label="Your name", max_length=100)
```

Every form instance has an `is_valid()` method that runs validation routines and return `True` and place the form data in its `cleaned_data` attribute.

```
class PersonInfo(TemplateView):

    template_name = 'person.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        person = Person.objects.get(pk=pk)
        context['person'] = person
        return context 

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        person = context['person']
        form = FirstNameForm(data=request.POST)
        if form.is_valid():
            person.first_name = form.cleaned_data['first_name']
            person.save()
            return redirect('people-list')
        else:
            return render(request, self.template_name, context=context)
```

