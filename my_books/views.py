from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404
from .book_sorting import sort_books_alphabetically
from .models import Book

def index(request):
    context = {}
    return render(request, 'my_books/index.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to the homepage after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'my_books/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to the homepage after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'my_books/login.html', {'form': form})
    

def order_books(request):
    # Retrieve the queryset of books from your database
    books = Book.objects.all()

    # Sort the books alphabetically by title
    sorted_books = sort_books_alphabetically(books)

    # Pass the sorted queryset to the template context
    return render(request, 'my_books/order_books.html', {'books': sorted_books})
