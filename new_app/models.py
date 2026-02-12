from django.db import models

class Library(models.Model):
    CATEGORY_CHOICES =[
        ('Fiction', 'Fiction'),
        ('Sci-Fi', 'Sci-Fi'),
        ('History', 'History'),
    ]
    Title = models.CharField(max_length=30)
    Author = models.CharField(max_length=20)
    Published_Date = models.DateTimeField()
    ISBN = models.CharField(max_length=20,unique=True)
    Category = models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    Is_available = models.BooleanField()
