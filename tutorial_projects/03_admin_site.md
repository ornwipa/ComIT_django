# Tutorial: The Local Library Website

Note: all the results created in this section can be viewed in the [figures](https://github.com/ornwipa/ComIT_django/tree/master/tutorial_projects/figures) folder

## Admin application for internal data management

### Registering models (to add models into admin application)

Open **`/locallibrary/catalog/admin.py`** to add codes that import the models and call `admin.site.register()` to register each of the models.

### Creating superusers

In the directory containing **manage.py**, run the command:
```
$ python3 manage.py createsuperuser
Username (leave blank to use 'ornwipa'): 
Email address: fahornwipa@gmail.com
Password: 
Password (again): 
Superuser created successfully.
```

### Logging in and using the site

Restart the development server, run `python3 manage.py runserver`. Open the URL http://127.0.0.1:8000/admin, enter new superuser's id and password credentials, then use the site.

## Advanced configurations

### Registering a ModelAdmin class

Define a [ModelAdmin](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#modeladmin-objects) class that describes the layout, and register the admin class with the associated model.
```
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)
```
Or, use the decorator
```
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
```

### Configuring list views

Use [list_display](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display) to add additional fields to the view.
```
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
```

### Adding list filters

Use `list_filter` attribute.
```
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
```

### Controlling which fields to be displayed and laid out

Use `fields` attribure.
```
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
```

### Sectioning the detailed view

Use [fieldsets](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets) to organize or group information into different sections.
```
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
```

### In-line editing associated records

Declare [inlines](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.inlines), of type TabularInline (horizonal layout) or StackedInline (vertical layout, just like the default model layout).
```
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
```
