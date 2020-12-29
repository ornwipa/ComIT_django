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

According to the tutorial in https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment, the warning can be ignore. Otherwise, apply migrations:
```
$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

Then re-run the `manage.py` with the `runserver` command
```  
$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 28, 2020 - 23:51:24
Django version 3.1.4, using settings 'mytestsite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[28/Dec/2020 23:51:38] "GET / HTTP/1.1" 200 16351
[28/Dec/2020 23:51:39] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
Not Found: /favicon.ico
[28/Dec/2020 23:51:39] "GET /favicon.ico HTTP/1.1" 404 1976
[28/Dec/2020 23:51:39] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[28/Dec/2020 23:51:39] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[28/Dec/2020 23:51:39] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
```
