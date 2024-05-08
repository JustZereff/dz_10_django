from mongoengine import connect
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")
django.setup()

from index.models import Author as DjangoAuthor, Quote as DjangoQuote
from models_from_mongodb import Author, Quotes


with open('password.txt', 'r') as file_pass:
    password = file_pass.read()
    # print(password)

URL = f'mongodb+srv://tapxyh1445:{password}@nosqlbase.zekqidk.mongodb.net/'
connect(host=URL)

# Получение данных из MongoDB
authors = Author.objects.all()
quotes = Quotes.objects.all()

# print("MongoDB authors:", authors)
# print("MongoDB quotes:", quotes)
# for i in quotes:
#     print(i.author)


# Перенос данных в PostgreSQL
django_authors = []
for author in authors:
    django_authors.append(DjangoAuthor(fullname=author.fullname,
                                       born_date=author.born_date,
                                       born_location=author.born_location,
                                       description=author.description,
                                       message_sent=author.message_sent))
DjangoAuthor.objects.bulk_create(django_authors)

django_quotes = []
for quote in quotes:
    author, created = DjangoAuthor.objects.get_or_create(fullname=quote.author)
    # Преобразование списка тегов в строку
    tags_string = ", ".join(quote.tags)
    
    # Создание объекта модели DjangoQuote с преобразованной строкой тегов
    django_quotes.append(DjangoQuote(quote=quote.quote,
                                     author=author,
                                     tag=tags_string))
DjangoQuote.objects.bulk_create(django_quotes)



print("Successfully transferred data to PostgreSQL.")