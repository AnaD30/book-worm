from django.db import models
from django.contrib.auth.models import User
from .models import Book,Genre

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')
    list_filter = ('genre',)
    search_fields = ('title', 'author')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
def genre_books(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)
    books = Book.objects.filter(genre=genre)
    return render(request, 'books/genre_books.html', {'genre': genre, 'books': books})        