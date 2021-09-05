from django.contrib import admin
from .models import Author, Genre, Book


#Register Models

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name' , 'last_name', 'country')
    list_filter = ('last_name',)

admin.site.register(Author, AuthorAdmin)



admin.site.register(Genre)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author')
    list_filter = ('author',)

admin.site.register(Book , BookAdmin)



