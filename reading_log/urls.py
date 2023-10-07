"""Defines URL patterns for reading_log"""
from django.urls import path
from . import views

app_name = 'reading_log'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Books page
    path('books/', views.books, name='books'),
    # Review page for a single book
    path('books/<int:book_id>/', views.book, name='book'),
]