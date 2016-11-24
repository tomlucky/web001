from django.contrib import admin
from web001.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

    search_fields = ['name', 'age']


admin.site.register(Person, PersonAdmin)
