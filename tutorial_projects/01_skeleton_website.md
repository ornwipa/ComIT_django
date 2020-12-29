# Tutorial: The Local Library Website

Instruction from Mozilla, MDN Web Docs, https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website

Codes in the fully developed version on GitHub, https://github.com/mdn/django-locallibrary-tutorial

## Creating a skeleton website

### Creating the project
```
django-admin startproject locallibrary
cd locallibrary
```

### Creating the catalog application
```
python3 manage.py startapp catalog
```

### Registering the catalog application
Add a new line in **`settings.py`** under the definition of `INSTALLED_APPS` to specify application configuration object.
```
INSTALLED_APPS = [
    'catalog.apps.CatalogConfig', # This object was created in /catalog/apps.py
]
```

### Specifying the database
Use the default SQLite in **`settings.py`** under the definition of `DATABASES`.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
For different options, see https://docs.djangoproject.com/en/3.1/ref/settings/#databases

### Hooking up the URL mapper
Open **`locallibrary/locallibrary/urls.py`**, the `urlpatterns` list initially mpas all URLs with the pattern `admin/` to the module `admin.site.urls`.
Add a new list item to include a `path()` that forwards request with the pattern `catalog/` to the module `catalog.urls`, i.e. the file with `catalog/urls.py`.
```
from django.urls import include
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
```
Redirect the root URL to `127.0.0.1:8000/catalog/`.
```
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]
```
Enable static files like CSS, JavaScript and images.
```
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

Create a file called **`locallibrary/catalog/urls.py`**, and define the empty imported `urlpatterns`.

