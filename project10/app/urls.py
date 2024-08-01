from django.urls import path
from .views import *
urlpatterns = [
    path('insert_skool', insert_skool, name='insert_skool'),

]
