from Library.Serializers import AuthorSerializer
from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response

#Model imports
from .models import Author, Genre, Book


@api_view(['GET'])
def apiOverview(request):
    return Response("Hello!")


@api_view(['GET'])
def authorList(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors , many=True)
    return Response(serializer.data)


