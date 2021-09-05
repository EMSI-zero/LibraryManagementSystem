from django.db import models



# Model Representing Author
class Author:
    
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    country = models.CharField
    
    
    #to add later
    #awards  
    #languages 
