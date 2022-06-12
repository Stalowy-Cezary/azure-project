from django import forms

''' forma pobierana zaleznie od tego ktory kalkulator wybrany'''
class KruppForm(forms.Form):
    Srednica = forms.IntegerField(required=True)
    Dlugosc = forms.IntegerField(required=True)
    Predkosc = forms.IntegerField(required=True)

class OdermattForm(forms.Form):
    Dlugosc = forms.IntegerField(required=True)
    Srednica = forms.IntegerField(required=True)
    Dlugosc_czubka = forms.IntegerField(required=True)
    Predkosc = forms.IntegerField(required=True)

