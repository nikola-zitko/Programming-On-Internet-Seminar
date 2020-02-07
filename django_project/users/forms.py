from django import forms
from sustav.models import Korisnici
from django.contrib.auth.forms import UserCreationForm

class KorisniciForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=(('', ("")),('Student', ("Student")),('Mentor', ("Mentor"))), widget=forms.Select())
    status = forms.ChoiceField(choices=(('', ("")),('Redovni', ("Redovni")),('Izvanredni', ("Izvanredni"))), widget=forms.Select(), required=False)
    class Meta:
        model= Korisnici
        fields= ["username", "email", "password1","password2", "role", "status"]


