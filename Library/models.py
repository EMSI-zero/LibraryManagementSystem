from django.db import models
from django.db.models.deletion import CASCADE



# Model Representing Author
class Author:
    
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    country = models.CharField
    
    
    #to add later
        #awards  
        #languages 



# Model Representing Genre
class Genre:
    title= models.CharField(max_length=100)
    
    #to add later
        #relatedGenre 



# Model Representing books
class Book:
    title= models.TextField()
    author= models.ForeignKey(Author , on_delete=models.CASCADE)
    publishDate= models.DateField()
    genre = models.ManyToManyField(Genre , blank=True , null=True)

    #to add later
        #publisher
        #publishCode
