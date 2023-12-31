from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    in_bucket_list = models.BooleanField(default=False)

    def __str__(self):
        """Returns a string representation of the model"""
        return self.text


class Review(models.Model):
    """Review of the book"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'reviews'

    def __str__(self):
        """Returns a string representation of the model"""
        return f"{self.text[:50]}..."
