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

