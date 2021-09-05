from django.urls import path


from . import views #import views file to use views in url patterns


urlpatterns = [
    path('api/' , views.apiOverview), #domain/api
    path('author-list/' , views.authorList , name="author-list"),
    path('book-list/' , views.bookList , name="book-list"),
    path('genre-list/' , views.genreList , name="genre-list"),
    path('author-list/<str:pk>/' , views.authorDetail , name="author"),
    path('book-list/<str:pk>/' , views.bookDetail , name="book"),

]