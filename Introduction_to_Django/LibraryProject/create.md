## Create Book



```python

from bookshelf.models import Book



book = Book.objects.create(

&nbsp;   title="1984",

&nbsp;   author="George Orwell",

&nbsp;   publication\_year=1949

)



book
```

# Output:

#<QuerySet [<Book: 1984 by George Orwell (1949)>]>
