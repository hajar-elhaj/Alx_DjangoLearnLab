from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# BookSerializer
# This serializer converts Book model instances into JSON
# and handles validation logic.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'  # Serialize all model fields

    # Custom validation to ensure publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# AuthorSerializer
# This serializer includes nested BookSerializer
# to display all books related to an author.
class AuthorSerializer(serializers.ModelSerializer):

    # Nested serializer
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']