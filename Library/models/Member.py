from .Book import Book
from .Author import Author
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , BaseUserManager

class Member(AbstractBaseUser , PermissionsMixin ):
    username = models.CharField(max_length=64 , unique=True)
    email = models.EmailField(max_length=250,unique=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField()
    favorite_books = models.ManyToManyField(Book , related_name="favorite_books_of")
    favorite_authors = models.ManyToManyField(Author , related_name="favorite_authors_of" )


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username' , 'name' , 'last_name' , 'email']


    def get_full_name(self):
        return self.name + self.last_name
    
    def __str__(self) -> str:
        return self.email