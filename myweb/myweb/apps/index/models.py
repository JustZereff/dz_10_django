from django.db import models

# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=100, unique=True)
    born_date = models.CharField(max_length=50, blank=True, null=True)
    born_location = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    message_sent = models.BooleanField(default=False)
    
    class Meta:
        app_label = 'index'  # Указываем принадлежность модели к приложению index

    def __str__(self):
        return f'{self.fullname}'

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.quote},{self.author}, {self.tag}"