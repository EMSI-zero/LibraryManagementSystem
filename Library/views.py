from re import search
from Library.Serializers import AuthorSerializer, BookSerializer, GenreSerializer
from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response

#Model imports
from .models.Author import Author
from .models.Genre import Genre
from .models.Book import Book

@api_view(['GET'])
def apiOverview(request):
    return Response("Hello!")


#Author Views

#author list view. lists the author and responses using serializer.
@api_view(['GET'])
def authorList(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors , many=True)
    return Response(serializer.data)

#author details
@api_view(['GET'])
def authorDetail(request,pk):
    authors = Author.objects.get(id=pk)
    serializer = AuthorSerializer(authors , many=False)
    response = Response(serializer.data)
    return response



#Book Views

#Book list view. lists the Book and responses using serializer.
@api_view(['GET'])
def bookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books , many=True)
    return Response(serializer.data)


#book details
@api_view(['GET'])
def bookDetail(request,pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(books , many=False)
    return Response(serializer.data)


#Genre Views

#Genre list view. lists the Genre and responses using serializer.
@api_view(['GET'])
def genreList(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres , many=True)
    return Response(serializer.data)


