from django.db import models


# Author Model
# This model represents an author who can have multiple books.
class Author(models.Model):
    # Stores the name of the author
    name = models.CharField(max_length=100)

    def __str__(self):
        # This makes the author name readable in Django admin
        return self.name


# Book Model
# This model represents a book written by an author.
class Book(models.Model):
    # Stores the book title
    title = models.CharField(max_length=200)

    # Stores the year the book was published
    publication_year = models.IntegerField()

    # ForeignKey creates a one-to-many relationship:
    # One Author can have many Books.
    author = models.ForeignKey(
        Author,
        related_name='books',  # Allows access via author.books
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title