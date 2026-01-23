# CRUD Operations for Book Model

## Create Book

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

book

# Output:
<Book: 1984 by George Orwell (1949)>



## Retrieve Book

Book.objects.get(title='1984', author='George Orwell')

# Output:
<QuerySet \[<Book: 1984 by George Orwell (1949)>]>



## Update Book

book.title = "Nineteen Eighty-Four"
book.save()
book

# Output:
<Book: Nineteen Eighty-Four by George Orwell (1949)>



## Delete Book

book.delete()
Book.objects.all()

# Output:

<QuerySet \[]>





