from re import T
from django.db import models
from rest_framework import serializers
from .models import Author, Genre , Book


#serializer class for Author data model        
class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)
    class Meta:
        model = Author
        fields = ['name' , 'last_name' , 'bio' , 'books']

#serializer class for Genre data model        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        
#serializer class for Book data model        
class BookSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(read_only=False , many=True)
    author = serializers.StringRelatedField(many=False)
    class Meta:
        model = Book
        fields = ['title' , 'author' , 'publishDate' , 'genre' , 'onLoan']
        
