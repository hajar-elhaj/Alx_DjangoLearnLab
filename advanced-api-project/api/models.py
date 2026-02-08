from django.db import models

class Author(models.Model):
    """
    Author model
    Stores basic information about a book author.
    One Author can be linked to many Book instances.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model
    Represents a book written by an Author.
    Each Book is linked to exactly one Author (ForeignKey).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
