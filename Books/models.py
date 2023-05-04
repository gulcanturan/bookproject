from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    overall_rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.title