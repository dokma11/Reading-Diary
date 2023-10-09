"""Defines URL patterns for reading_log"""
from django.urls import path
from . import views

app_name = 'reading_log'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Books page
    path('books/', views.books, name='books'),
    # Review page for a single book
    path('books/<int:book_id>/', views.book, name='book'),
    # Page for adding a new book
    path('new_book/', views.new_book, name='new_book'),
    # Page for adding a new review
    path('new_review/<int:book_id>', views.new_review, name='new_review'),
    # Page for editing a review
    path('edit_review/<int:review_id>', views.edit_review, name='edit_review'),
    # Bucket list page
    path('bucket_list/', views.books_in_bucket_list, name='bucket_list'),
    # Bucket list item page
    path('bucket_list/<int:book_id>/', views.bucket_list_item, name='bucket_list_item'),
    # Page for adding a new bucket list item
    path('new_bucket_list_item/', views.new_bucket_list_item, name='new_bucket_list_item'),
]