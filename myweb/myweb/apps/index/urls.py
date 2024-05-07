from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('authors/', views.authors, name='authors'),
    path('add_author/', views.add_author, name='add_author'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout_view'),
    path('custom_login/', LoginView.as_view(template_name='registration/login.html'), name='custom_login'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    
]