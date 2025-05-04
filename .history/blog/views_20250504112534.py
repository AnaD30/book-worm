from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_blog(request):
    return HttpResponse("Hello, blog!")
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})