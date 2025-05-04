from django.urls import path
from . import views

urlpatterns = [
     path('book/', views.book_detail, name='book_detail'),
]    