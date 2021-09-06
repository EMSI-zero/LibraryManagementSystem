from django.db import models
from .Author import Author
from .Genre import Genre
from django.db.models.deletion import CASCADE



# Model Representing books
class Book(models.Model):
    title= models.TextField()
    author= models.ForeignKey(Author , related_name='books', on_delete=models.CASCADE)
    publishDate= models.DateField()
    genre = models.ManyToManyField(Genre , related_name='genres', blank=True , null=True)
    onLoan = models.BooleanField(default=False)

    
    #to add later
        #publisher
        #publishCode

    def __str__(self) -> str:
        return self.title
