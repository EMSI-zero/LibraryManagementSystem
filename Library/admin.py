from django.contrib import admin
from .models.Author import Author
from .models.Genre import Genre
from .models.Book import Book

#Register Models

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name' , 'last_name', 'country')
    list_filter = ('last_name', 'country' ,)

admin.site.register(Author, AuthorAdmin)



admin.site.register(Genre)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author')
    list_filter = ('author',)

admin.site.register(Book , BookAdmin)



