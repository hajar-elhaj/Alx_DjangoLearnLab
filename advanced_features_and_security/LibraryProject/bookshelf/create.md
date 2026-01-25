## Create Book

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

book


# Output:

<QuerySet [<Book: 1984 by George Orwell (1949)>]>
