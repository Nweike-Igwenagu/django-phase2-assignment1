from django.urls import path
from .views import (
    AuthorListView,
    BookListView,
    ReviewListView,
    AuthorsWithMultipleBooksView,
    BookWithReviewsView,
    TopAuthorsView,
    AuthorCreateView,
    BookCreateView,
    ReviewCreateView,
    
    BookDeleteView,
    ReviewDeleteView,
    
    BookUpdateView,
    ReviewUpdateView,
)

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('authors/multiple-books/', AuthorsWithMultipleBooksView.as_view(), name='authors-multiple-books'),
    path('books/with-reviews/', BookWithReviewsView.as_view(), name='books-with-reviews'),
    path('authors/top/', TopAuthorsView.as_view(), name='top-authors'),
    
    #create...
    path('author/create/', AuthorCreateView.as_view(), name= 'author-create'),
    path('book/create/', BookCreateView.as_view(), name= 'book-create'),
    path('review/create/', ReviewCreateView.as_view(), name= 'create-review'),
    
    #delete...
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('review/delete/<int:pk>/', ReviewDeleteView.as_view(), name='review-delete'),
    
    #update...
    path('book/update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('review/update/<int:pk>', ReviewUpdateView.as_view(), name='review-update'),
    
]
