# Tutorial: The Local Library Website

## Designing the LocalLibrary models

Have separate models for every *object*, i.e., a group of related information. Here objects are authors, books, and book instances.

Use models to represent selection-list options (drop-down list of choices) rather than hard coding the choices into website when options are not know up front or may change. Here models include book genre and language.

Define models that are one-to-one (`OneToOneField`), one-to-many (`ForeignKey`), and many-to-many (`ManyToManyField`).

[diagram](https://raw.githubusercontent.com/mdn/django-locallibrary-tutorial/master/catalog/static/images/local_library_model_uml.png)

Note: in `BookInstance:status`, the values `LOAN_STATUS` are hard-coded as it is not expected to change.

## Model primer

### Model definition

Define models in the application's **`models.py`** file. Implement subclasses of `django.db.models.Model`. Include fields, methods and metadata.

**Fields** represents a column of data in database tables. Each database record or row consists of one of each field value.
```
class MyModelName(models.Model):
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
```
A field called `my_field_name` of type `models.Charfield` contains strings of alphanumeric characters.

Common arguments:
- help_text: a text label for HTML forms
- verbose_name: a human-readable name for the field
- default, null, blank, choices - see [documentation](https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-options)
- primary_key: if `True` then set the current field to unique identifier

**Metadata** is declared as a class.
```
    class Meta:
        ordering = ['-my_field_name']
```
List of attributes in [documentation](https://docs.djangoproject.com/en/3.1/ref/models/options/)

**Method** - minimally, in every model, `__str__()` returns a human-readable string for each object.
```
    def __str__(self):
        return self.field_name
```

### Model management

Create a record
```
# Create a new record using the model's constructor.
record = MyModelName(my_field_name="Instance #1")

# Save the object into the database.
record.save()
```

Access a record
```
# Access model field values using Python attributes.
print(record.id) # should return 1 for the first record.
print(record.my_field_name) # should print 'Instance #1'
```

Modify a record
```
# Change record by modifying the fields, then calling save().
record.my_field_name = "New Instance Name"
record.save()
```

Search for records as a `QuerySet`, which is an iterable object. Use `objects.all()` or `filter()` method to match a speficied text or numeric field with criteria.
```
all_books = Book.objects.all()
wild_books = Book.objects.filter(title__contains='wild')
books_containing_genre = Book.objects.filter(genre__name__icontains='fiction')
```
Note: field to match and type of match are defined as `field_name__match_type` with *double underscore* in-between. To filter on a field that defines a relationship to another model, "index" to fields within the related model with additional *double underscores*.
Full list of the types of match in [documentation](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#field-lookups)

## Defining the LocalLibrary Models

Define models in the application's **`locallibrary/catalog/models.py`** - see the [code](https://github.com/mdn/django-locallibrary-tutorial/blob/master/catalog/models.py)
- Genre (and Language)
- Book
	- `isbn = models.CharField('ISBN', max_length=13, unique=True, ...)`: the field `isbn` is explicitly labeled as "ISBN", `unique=True` ensures that the parameter is globally unique.
	- `author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)`: the 'Author' is string because it has not been declared, `null=True` allows the database to store `Null` value, `on_delete=models.SET_NULL` set the value of the author to `Null` when/if the associated author is deleted.
	- `genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')`: the pre-defined `Genre` class is referred.
- BookInstance
	- `id = models.UUIDField(primary_key=True, default=uuid.uuid4, ...)`: set the `id` field to be a `primary_key` for this model.
	- `LOAN_STATUS` is a tuple of choices whereas `status = models.CharField(max_length=1, choices=LOAN_STATUS, ...)` is a tuple containing tuples of key-value pairs.
- Author

### Running database migrations

Run database migrations after models are created
```
$ python3 manage.py makemigrations
Migrations for 'catalog':
  catalog/migrations/0001_initial.py
    - Create model Author
    - Create model Book
    - Create model Genre
    - Create model BookInstance
    - Add field genre to book
$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, catalog, contenttypes, sessions
Running migrations:
  Applying catalog.0001_initial... OK
```

Re-run database migrations as changes are made
```
$ python3 manage.py makemigrations
Migrations for 'catalog':
  catalog/migrations/0002_language.py
    - Create model Language
$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, catalog, contenttypes, sessions
Running migrations:
  Applying catalog.0002_language... OK
```

