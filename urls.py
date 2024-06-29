from django.urls import path
from .views import *
urlpatterns = [
    path("crud/",first,name="first")
]

