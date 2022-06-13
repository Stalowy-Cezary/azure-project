from django import forms
from django.core.validators import *
''' forma pobierana zaleznie od tego ktory kalkulator wybrany'''
class KruppForm(forms.Form):
    Srednica = forms.IntegerField(required=True, min_value=1)
    Dlugosc = forms.IntegerField(required=True, min_value=1)
    Predkosc = forms.IntegerField(required=True, min_value=1)

class OdermattForm(forms.Form):
    Dlugosc = forms.IntegerField(required=True, min_value=1)
    Srednica = forms.IntegerField(required=True, min_value=1)
    Dlugosc_czubka = forms.IntegerField(required=False)
    Srednica_czubka = forms.IntegerField(required=False)
    Predkosc = forms.IntegerField(required=True, min_value=1)