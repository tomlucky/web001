from django.contrib import admin
from web001.models import *


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ['name', 'age']


class TitleAdmin(admin.ModelAdmin):
    list_display = ('enName', 'cnName')
    search_fields = ['enName', 'cnName']


class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_content')
    search_fields = ['post_title', 'post_content']


admin.site.register(Person, PersonAdmin)
admin.site.register(Titles, TitleAdmin)
admin.site.register(Posts, PostsAdmin)
