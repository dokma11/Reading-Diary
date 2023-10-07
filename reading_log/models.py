from django.db import models


class Book(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

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
