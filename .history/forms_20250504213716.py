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