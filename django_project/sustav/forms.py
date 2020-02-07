from django import forms
from sustav.models import Predmeti, Korisnici, Upisi
from django.contrib.auth.forms import UserCreationForm

class PredmetForm(forms.ModelForm):
    ime = forms.CharField()
    kod = forms.CharField()
    program = forms.CharField()
    bodovi = forms.IntegerField()
    sem_redovni = forms.IntegerField()
    sem_izvanredni = forms.IntegerField()
    izborni = forms.ChoiceField(choices=(('da', ("da")),('ne', ("ne"))), widget=forms.Select())
    
    class Meta:
        model= Predmeti
        fields=["ime", "kod", "program", "bodovi", "sem_redovni", "sem_izvanredni", "izborni"]

