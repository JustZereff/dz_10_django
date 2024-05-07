from django import forms
from .models import Quote, Author


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    agree_to_rules = forms.BooleanField(label='Agree to the rules', required=True)

class QuoteForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tag']
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']