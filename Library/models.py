from django.db import models
from django.db.models.deletion import CASCADE



# Model Representing Author
class Author(models.Model):
    
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    country = models.CharField
    
    
    #to add later
        #awards  
        #languages 

        
    def __str__(self) -> str:
        return self.name + ' ' + self.last_name


# Model Representing Genre
class Genre(models.Model):
    title= models.CharField(max_length=100)
    
    #to add later
        #relatedGenre 

    def __str__(self) -> str:
       return self.title



# Model Representing books
class Book(models.Model):
    title= models.TextField()
    author= models.ForeignKey(Author , on_delete=models.CASCADE)
    publishDate= models.DateField()
    genre = models.ManyToManyField(Genre , blank=True , null=True)
    onLoan = models.BooleanField(default=False)

    
    #to add later
        #publisher
        #publishCode

    def __str__(self) -> str:
        return self.title
