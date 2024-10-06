from rest_framework import serializers
from .models import Author, Books, Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields= "__all__"
    
class BookSerializer(serializers.ModelSerializer):
    author= AuthorSerializer()
    class Meta:
        model= Books
        fields= "__all__"

    def create(self, validated_data):
        author_data= validated_data.pop('author')
        author, _ = Author.objects.get_or_create(**author_data)
        book= Books.objects.create(author= author, **validated_data)
        return book
    
    def delete(self, request, id):
        book = Books.object.get(id=id)
        
        book.delete()    
    
    def validate(self, data):
        if data['published_date'] > 12/12/2024:
            return serializers.ValidationError('Publish date not set right!')
        return data

class ReviewSerializers(serializers.ModelSerializer):
    book= BookSerializer()

    def create(self, validated_data):
        books_data= validated_data.pop('book')
        book, _ = Books.objects.get_or_create(**books_data)
        review= Review.objects.create(book=book, **validated_data)
        return review
    class Meta:
        model= Review
        fields= "__all__"
        