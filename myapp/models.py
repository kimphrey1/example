

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    description = models.TextField(max_length=600, default='')

    def __str__(self):
        return self.title
