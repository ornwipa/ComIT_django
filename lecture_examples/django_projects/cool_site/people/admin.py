from django.contrib import admin

# Register your models here.

from people.models import Person

# @register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

admin.site.register(Person, PersonAdmin)
