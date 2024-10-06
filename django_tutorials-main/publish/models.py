from django.db import models
from django.core.validators import MaxValueValidator


class Author(models.Model):
    name= models.CharField(max_length= 255, null= False, blank= False)
    published_books= models.IntegerField(validators= [MaxValueValidator(10)])

    def __str__(self):
        return self.name
        

class Books(models.Model):
    title= models.CharField(max_length= 255, null= False, blank= False)
    author= models.ForeignKey(Author, on_delete= models.CASCADE)
    pages= models.IntegerField()
    published_date= models.DateField()
    
    ordering= ['-published_date']

    def __str__(self):
        return f'{self.title} by  {self.author}'
    
    
    class Meta:
        verbose_name= 'Book'
        verbose_name_plural= 'Books'
        

class Review(models.Model):
    book= models.ForeignKey(Books, on_delete= models.CASCADE)
    review= models.TextField()
    
    def __str__(self):
        return f'{self.book}  {self.review}'
        
# Create your models here.
