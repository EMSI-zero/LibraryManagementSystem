from django.db import models
from django_countries.fields import CountryField

# Model Representing Author
class Author(models.Model):
    
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    country = CountryField()
    
    
    #to add later
        #awards  
        #languages 


    def __str__(self) -> str:
        return self.name + ' ' + self.last_name
