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
mysite/			<- project folder
	manage.py		<- utility script
	mysite/		<- actual project package
		settings.py	<- define how the website runs
		urls.py	<- declare URL, map views to URL
		asgi.py	<- server entry point
		wsgi.py	<- server entry point
	polls/			<- directory containing "polls" app
		admin.py	<- define admin site
		apps.py	<- define app config
		models.py	<- define models
		tests.py	<- define unit tests
		views.py	<- define views
```

