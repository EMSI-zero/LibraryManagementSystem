from django.db import models
from rest_framework import serializers
from .models import Author, Genre , Book


#serializer class for Author data model        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

#serializer class for Genre data model        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        
#serializer class for Book data model        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
