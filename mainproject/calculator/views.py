from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render , redirect
from calculator.forms import KruppForm, OdermattForm
import math

# Create your views here.
class HomePage(TemplateView):
    template_name = 'templatesviews/home.html'
    ''' '''
    def get(self, request, nazwisko):
        if 'k' in nazwisko:
            form = KruppForm()
        else:
            form = OdermattForm()
        return render(request,self.template_name, {'form':form, 'nazwisko': nazwisko})

    def post(self,request, nazwisko):

        """ jesli nazwisko z URL to Krupp"""
        if 'k' in nazwisko:
            form = KruppForm(request.POST)
            if form.is_valid():
                D = form.cleaned_data['Srednica']
                L = form.cleaned_data['Dlugosc']
                V = form.cleaned_data['Predkosc']
                if D == None:
                    D = 2
                if L == None:
                    L = 2
                if V == None:
                    V = 2
            if 'oblicz' in request.POST:
                vol = ((D/2)*(D/2))*3.14*L
                masa = (0.9*vol)*0.000008
                result = 100 * (V * math.sqrt(masa)) / (240 * (math.sqrt(D)))

            """ jesli nazwisko z URL to Odermatt"""
        else:

            form = OdermattForm(request.POST)
            if form.is_valid():
                D = form.cleaned_data['Srednica']
                L = form.cleaned_data['Dlugosc']
                LP = form.cleaned_data['Dlugosc_czubka']
                V = form.cleaned_data['Predkosc'] / 1000
                try:
                    if 'oblicz' in request.POST:
                        s = ((138 + (-0.1 * 240)) * 240) / 17200
                        seg1 = math.sqrt(17200 / 240)
                        seg2 = math.exp((-s) / (V * V))
                        result = 0.921 * (1 / math.tanh(0.283 + (0.0656 * ((L - (0.7 * LP)) / D)))) * seg1 * seg2
                        result = 0.18 * (L - (0.7 * LP)) * result

                except ZeroDivisionError:
                        result = "Wpisywanie 0 moze wywolac blad! Prosze sprobowac ponownie"

        args = {'form': form , 'result': result,'nazwisko': nazwisko}
        return render(request, self.template_name, args)
