# Set up django

## Installation

Follow the instruction at https://docs.djangoproject.com/en/3.1/topics/install/#installing-official-release
```
$ python -m pip install Django
Collecting Django
  Downloading Django-3.1.4-py3-none-any.whl (7.8 MB)
     |████████████████████████████████| 7.8 MB 2.8 MB/s 
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 1.3 MB/s 
Collecting asgiref<4,>=3.2.10
  Downloading asgiref-3.3.1-py3-none-any.whl (19 kB)
Requirement already satisfied: pytz in ./anaconda3/lib/python3.7/site-packages (from Django) (2019.3)
Installing collected packages: sqlparse, asgiref, Django
Successfully installed Django-3.1.4 asgiref-3.3.1 sqlparse-0.4.1
```

Check the installation
```
$ python -m django --version
3.1.4
```

## Testing the installation

Create a new skeleton site called "mytestsite" using `django-admin tool` then navigate into the folder. Main script `manage.py` is automaticially created.
```
$ django-admin startproject mytestsite
$ cd mytestsite
```

Run the development web server
```
$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
December 28, 2020 - 23:50:26
Django version 3.1.4, using settings 'mytestsite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

