from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import BookForm, ReviewForm


def index(request):
    """Home page"""
    return render(request, 'reading_log/index.html')


def books(request):
    """Show all topics"""
    books = Book.objects.order_by('date_added')
    context = {'books': books}
    return render(request, 'reading_log/books.html', context)


def book(request, book_id):
    """Show a single topic and all of its entries"""
    book = Book.objects.get(id=book_id)
    reviews = book.review_set.order_by('-date_added')
    context = {'book': book, 'reviews': reviews}
    return render(request, 'reading_log/book.html', context)


def new_book(request):
    """Create and add a new book"""
    if request.method != 'POST':
        # No data was submitted, create a blank form
        form = BookForm()
    else:
        # POST data was submitted, process the submitted data
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('reading_log:books')

    # Display a blank or invalid form
    context = {'form': form}

    return render(request, 'reading_log/new_book.html', context)


def new_review(request, book_id):
    """Add a new review for a particular book"""
    book = Book.objects.get(id=book_id)

    if request.method != 'POST':
        # No data was submitted, create a blank form
        form = ReviewForm()
    else:
        # POST data was submitted, process the submitted data
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.book = book
            new_review.save()
            return redirect('reading_log:book', book_id=book_id)

    # Display a blank or invalid form
    context = {'book': book, 'form': form}

    return render(request, 'reading_log/new_review.html', context)


def edit_review(request, review_id):
    """Edit an existing review"""
    review = Review.objects.get(id=review_id)
    book = review.book

    if request.method != 'POST':
        # Initial request, fill the form with the current review
        form = ReviewForm(instance=review)
    else:
        # POST data submitted, process the submitted data
        form = ReviewForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('reading_log:book', book_id=book.id)

    # Display a blank or invalid form
    context = {'review': review, 'book': book, 'form': form}

    return render(request, 'reading_log/edit_review.html', context)
