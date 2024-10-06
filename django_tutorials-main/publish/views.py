from rest_framework import generics
from .models import Author, Books, Review
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializers
from django.db.models import Count, Avg, Case, When, BooleanField, Sum
from django.db.models import Q, F
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# List of all authors with their book count
class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.annotate(book_count=Count('books'))
    serializer_class = AuthorSerializer

# List of all books with authors using select_related for optimization
class BookListView(generics.ListAPIView):
    queryset = Books.objects.select_related('author').all()
    serializer_class = BookSerializer

# List of all reviews with books and authors using prefetch_related for optimization
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.prefetch_related('book__author').all()
    serializer_class = ReviewSerializers

# List of authors who have written more than 1 book
class AuthorsWithMultipleBooksView(generics.ListAPIView):
    queryset = Author.objects.annotate(book_count=Count('books')).filter(book_count__gt=1)
    serializer_class = AuthorSerializer

# List of books with a boolean field 'has_reviews' to indicate if a book has reviews
class BookWithReviewsView(generics.ListAPIView):
    queryset = Books.objects.annotate(
        has_reviews=Case(
            When(review__isnull=False, then=True),
            default=False,
            output_field=BooleanField()
        )
    )
    serializer_class = BookSerializer

# Top 3 authors based on the number of books
class TopAuthorsView(generics.ListAPIView):
    queryset = Author.objects.annotate(book_count=Count('books')).order_by('-book_count')[:3]
    serializer_class = AuthorSerializer


class AuthorCreateView(generics.CreateAPIView):
    queryset= Author.objects.all()
    serializer_class= AuthorSerializer

class BookCreateView(generics.CreateAPIView):
    queryset= Books.objects.all()
    serializer_class= BookSerializer
    
class ReviewCreateView(generics.CreateAPIView):
    queryset= Review.objects.all()
    serializer_class= ReviewSerializers

# ASSIGNMENT
# 1. create an endpoint to delete a book  
# 2. create an endpoint to delete a review 
# 3. create an endpoint to update a book 
# 4. create an endpoint to update a review 

# 1. an endpoint to delete a book  
class BookDeleteView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def delete(self, request, *args, **kwargs):
            book = self.get_object()
            book.delete() 
            return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# 2. an endpoint to delete a review 
class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def delete(self, request, *args, **kwargs):
            review = self.get_object()
            review.delete() 
            return Response({"message": "Review deleted"}, status=status.HTTP_204_NO_CONTENT)

# 3. an endpoint to update a book 
class BookUpdateView(generics.UpdateAPIView):
    queryset = Books.objects.all()  
    serializer_class = BookSerializer  

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  
        book = self.get_object()  

        serializer = self.get_serializer(book, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()  

# 4. an endpoint to update a review 
class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()  
    serializer_class = ReviewSerializers  

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  
        book = self.get_object()  

        serializer = self.get_serializer(book, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()  




#Advanced filtering:
#books where the title starts with 'A' or 'B' and published after 2000
book= Books.objects.filter(
    Q(title__startswith= 'A') | Q(title__startswith= 'B'),
    published_date__year__gt=2000
    
)

#Books where the number of pages is greater than the number of reviews
books= Books.objects.annotate(review_count= Count('review')).filter(pages__gt= F('review_count'))

#this would return books greater than 2010
books_greater_than_2010= Books.objects.filter(published_date__year__gt= 2010)

books= Books.objects.filter(title__icontains= 'Django')