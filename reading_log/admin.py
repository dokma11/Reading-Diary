from django.contrib import admin
from .models import Topic, Entry, Book, Review

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Book)
admin.site.register(Review)
