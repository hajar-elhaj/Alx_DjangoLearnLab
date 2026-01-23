\# CRUD Operations for Book Model



\## Create Book

```python

from bookshelf.models import Book



book = Book.objects.create(

&nbsp;   title="1984",

&nbsp;   author="George Orwell",

&nbsp;   publication\_year=1949

)



book

```

\# Output:

\# <Book: 1984 by George Orwell (1949)>



\## Retrieve Book

```python

Book.objects.all()

```

\# Output:

\# <QuerySet \[<Book: 1984 by George Orwell (1949)>]>



\## Update Book

```python

book = Book.objects.get(title="1984")

book.title = "Nineteen Eighty-Four"

book.save()



book

```

\# Output:

\# <Book: Nineteen Eighty-Four by George Orwell (1949)>



\## Delete Book

```python

book = Book.objects.get(title="Nineteen Eighty-Four")

book.delete()



Book.objects.all()

```

\# Output:

\# <QuerySet \[]>



