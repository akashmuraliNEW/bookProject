from django.db import models

# Create your models here.
class Author(models.Model):
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.author
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(default='default_image.png', upload_to='book_images')
    def __str__(self):
        return self.title