from django.urls import path


from . import views #import views file to use views in url patterns


urlpatterns = [
    path('api/' , views.apiOverview), #domain/api
    path('author-list' , views.authorList , name="author-list")
]