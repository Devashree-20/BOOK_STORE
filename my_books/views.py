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



########

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Book  # Assuming you have a Book model
from .cart import Cart

cart = Cart()


def add_to_cart(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        book_id = request.POST.get('book_id')
        quantity = int(request.POST.get('quantity'))
        
        try:
            book = Book.objects.get(pk=book_id)
            cart.add_item({'book_id': book_id, 'title': book.title, 'price': book.price, 'quantity': quantity})
            return JsonResponse({'status': 'success'})
        except Book.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Book not found'})
    
    return redirect('my_books/cart.html')

def remove_from_cart(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        book_id = request.POST.get('book_id')
        
        try:
            book = Book.objects.get(pk=book_id)
            cart.remove_item({'book_id': book_id, 'title': book.title, 'price': book.price, 'quantity': 1})
            return JsonResponse({'status': 'success'})
        except Book.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Book not found'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def update_cart(request):
    if request.method == 'POST' and request.is_ajax():
        book_id = request.POST.get('book_id')
        quantity = int(request.POST.get('quantity'))
        
        try:
            book = Book.objects.get(pk=book_id)
            cart.update_item_quantity({'book_id': book_id, 'title': book.title, 'price': book.price}, quantity)
            return JsonResponse({'status': 'success'})
        except Book.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Book not found'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def view_cart(request):
    items = cart.list_items()
    total_price = sum(item['price'] * item['quantity'] for item in items)
    return render(request, 'my_books/cart.html', {'items': items, 'total_price': total_price})

def clear_cart(request):
    cart.clear_cart()
    return redirect('my_books/cart.html')
