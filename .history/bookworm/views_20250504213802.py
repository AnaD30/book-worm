def add_book(request):
    if request.method == 'POST':
        form = BookAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books:book_list')
    else:
        form = BookAdminForm()
    return render(request, 'books/add_book.html', {'form': form})s