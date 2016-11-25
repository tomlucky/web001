from django.contrib import admin
from web001.models import *


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ['name', 'age']


class TitleAdmin(admin.ModelAdmin):
    list_display = ('enName', 'cnName')
    search_fields = ['enName', 'cnName']


admin.site.register(Person, PersonAdmin)
admin.site.register(Titles, TitleAdmin)
