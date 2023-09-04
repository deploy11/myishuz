from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('category/',cate,name='categ'),
    path('about/',about,name='about'),
    path('new/',new.as_view(),name='new'),
]