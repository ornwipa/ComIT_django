# Tutorial: The Local Library Website

This tutorial extends the website to allow users to log in and control what they can see and do based on whether or not they are logged in and their permissions.

## Authentication and Authorization

Django provides an authentication and authorization ("permission") system, built on top of the [session framework](https://github.com/ornwipa/ComIT_django/blob/master/tutorial_projects/06_session_framework.md). The framework includes built-in models for `Users` and `Groups` (a generic way of applying permissions to more than one user at a time).

## Enabling authentication

Authentication was enabled automatically when creating a [skeleton website](https://github.com/ornwipa/ComIT_django/blob/master/tutorial_projects/01_skeleton_website.md). The configuration in **locallibrary/locallibrary/settings.py** file is as shown:

```
INSTALLED_APPS = [
    ...
    'django.contrib.auth',  #Core authentication framework and its default models.
    'django.contrib.contenttypes',  #Django content type system (allows permissions to be associated with models).
    ....

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',  #Manages sessions across requests
    'django.contrib.auth.middleware.AuthenticationMiddleware',  #Associates users with requests using sessions.
    ....
```

## Creating users and groups

A superuser, created with the command `python manage.py createsuperuser`, is already authenticated and has all permissions.

To create a general user, i.e. "library member", start the development server and navigate to the admin site to **Add** a `Group` and a `User`.

## Setting up authentication views

### Project URLs

In the **locallibrary/locallibrary/urls.py)** file, add the following code to add the URL path for login, logout, and password management:

```
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
```

### Template directory and templates

In **/locallibrary/locallibrary/settings.py** file, import the `os` module and update `TEMPLATES`, `DIRS`, and add `LOGIN_REDIRECT_URL` as shown:

```
import os
...
TEMPLATES = [
      {
       ...
       'DIRS': [os.path.join(BASE_DIR, 'templates')],
       'APP_DIRS': True,
       ...

LOGIN_REDIRECT_URL = '/' # Redirect to home URL after login (Default redirects to /accounts/profile/)
```

Create a registration directory on the search path and add the login.html file:
- **locallibrary/templates/registration/login.html**, 
- locallibrary/templates/registration/**logged_out.html**, 
- locallibrary/templates/registration/**password_reset_form.html** and 
- locallibrary/templates/registration/**password_reset_done.html**, etc.

## Testing against authenticated users

### Testing in templates

Information about the currently logged in user is with the `{{ user }}` template variable. Typically, it is first tested against the `{{ user.is_authenticated }}`.

In the base template **/locallibrary/catalog/templates/base_generic.html**, add the following code to display the user with `{{ user.get_username }}` under the condition with `{% if user.is_authenticated %}`, `{% else %}` and `{% endif %}`.

Note that `url` template tags and the names of the respective URL configurations are created for login and logout link URLs. The `?next={{request.path}}` is appended to the end of the URLs, i.e. adding a URL parameter `next`, in order to redirect the user back to the page after the user successfully logged in or logged out.

```
  <ul class="sidebar-nav">
    ...
   {% if user.is_authenticated %}
     <li>User: {{ user.get_username }}</li>
     <li><a href="{% url 'logout'%}?next={{request.path}}">Logout</a></li>
   {% else %}
     <li><a href="{% url 'login'%}?next={{request.path}}">Login</a></li>
   {% endif %} 
  </ul>
```

### Testing in views

An access to function-based views can be restricted with `login_required` decorator to the view function.

```
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    pass
```

An access to class-based views can be restricted with `LoginRequiredMixin` superclass. Redirected location when the users are not authenticated is specified with `login_url`, and the URL parameter similar to `next` to insert current absolute path can be specified with `redirect_field_name`.

```
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
```

## Listing current user's book

### Models

To allow books to be on loan by users, import the `User` model: `from django.contrib.auth.models import User`; and add `borrower` filed to the `BookInstance` model with one-to-many relationship: `borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)`

Always update database when changing models

```
$ python manage.py makemigrations
Migrations for 'catalog':
  catalog/migrations/0003_bookinstance_borrower.py
    - Add field borrower to bookinstance
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, catalog, contenttypes, sessions
Running migrations:
  Applying catalog.0003_bookinstance_borrower... OK
```

### On loan view

### URL for on-loan books

### Template for on-loan books

## Permissions
