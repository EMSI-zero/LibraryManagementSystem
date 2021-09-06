from django.db import models


# Model Representing Genre
class Genre(models.Model):
    title= models.CharField(max_length=100)
    
    #to add later
        #relatedGenre 

    def __str__(self) -> str:
       return self.title

