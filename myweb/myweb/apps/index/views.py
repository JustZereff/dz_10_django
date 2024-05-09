from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, QuoteForm, AuthorForm
from django.views.generic.base import View
from .models import Author, Quote, Tag

def index(request):
    quote_list = Quote.objects.order_by('author')
    return render(request, 'index/quote.html', {'quote_list': quote_list})
def authors(request):
    author_list = Author.objects.all()
    return render(request, 'authors/authors.html', {'author_list': author_list})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})

    return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            agree_to_rules = form.cleaned_data['agree_to_rules']
            # Проверка на уникальность имени пользователя
            if not User.objects.filter(username=username).exists():
                # Создание пользователя, если имя уникально
                user = User.objects.create_user(username=username, password=password)
                # Логин пользователя
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('index')
            else:
                # Вывод ошибки, если имя пользователя уже используется
                return render(request, 'registration/register.html', {'form': form, 'error_message': 'Username already exists'})
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))
    
@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote_text = form.cleaned_data['quote']
            author = form.cleaned_data['author']
            tag_custom = form.cleaned_data['tag_custom']
            tags_input = tag_custom.split(',')
            tags_input = [tag.strip() for tag in tags_input if tag.strip()]
            # Создаем список объектов Tag для каждого тега
            tag_objects = [Tag.objects.get_or_create(tag=tag)[0] for tag in tags_input]
            new_quote = Quote.objects.create(quote=quote_text, author=author)
            # Привязываем теги к цитате
            new_quote.tag.add(*tag_objects)

            return redirect('index')
    else:
        form = QuoteForm()
    return render(request, 'index/add_quote.html', {'form': form})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm()
    return render(request, 'authors/add_author.html', {'form': form})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'authors/author_detail.html', {'author': author})