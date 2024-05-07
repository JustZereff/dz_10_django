from django.db import models

# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=100, unique=True)
    born_date = models.CharField(max_length=50, blank=True, null=True)
    born_location = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.fullname}'

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.quote},{self.author}, {self.tag}"