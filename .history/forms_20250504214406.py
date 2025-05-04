from django import forms
from .models import Book, Genre

class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'select2'}),
    )  
    
    
def add_book(request):
    if request.method == 'POST':
        form = BookAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books:book_list')
    else:
        form = BookAdminForm()
    return render(request, 'books/add_book.html', {'form': form})

