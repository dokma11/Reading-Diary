from django.shortcuts import render
from .models import Topic, Book


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


def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'reading_log/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all of its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'reading_log/topic.html', context)
