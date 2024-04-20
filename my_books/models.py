from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='books/')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title