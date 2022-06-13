from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render , redirect
from .forms import KruppForm, OdermattForm
import math

# Create your views here.
class HomePage(TemplateView):
    template_name = 'templatesviews/home.html'

    def get(self, request, nazwisko):
        if 'd' in nazwisko:
            form = OdermattForm()
        else:
            form = KruppForm()
        return render(request,self.template_name, {'form':form, 'nazwisko': nazwisko})

    def post(self,request, nazwisko):

        """ jesli nazwisko z URL to Krupp"""
        if 'k' in nazwisko:
            form = KruppForm(request.POST)
            if form.is_valid():
                D = form.cleaned_data['Srednica']
                L = form.cleaned_data['Dlugosc']
                V = form.cleaned_data['Predkosc']
            if 'oblicz' in request.POST:

                vol = ((D/2)*(D/2))*3.14*L
                masa = (0.9*vol)*0.000008
                result = 100 * (V * math.sqrt(masa)) / (240 * (math.sqrt(D)))

            """ jesli nazwisko z URL to OdermattL"""
        else:

            form = OdermattForm(request.POST)
            if form.is_valid():
                D = form.cleaned_data['Srednica']
                L = form.cleaned_data['Dlugosc']
                DP = form.cleaned_data['Srednica_czubka']
                LP = form.cleaned_data['Dlugosc_czubka']
                V = form.cleaned_data['Predkosc'] / 1000
                if 'oblicz' in request.POST:
                    if DP == None:

                        Wrk = L
                        s = ((138 + (-0.1 * 240)) * 240) / 17200
                        seg1 = math.sqrt(17200 / 240)
                        seg2 = math.exp((-s) / (V * V))
                        result = 0.921 * (1 / math.tanh(0.283 + (0.0656 * (Wrk / D)))) * seg1 * seg2
                        result = 0.18 * (Wrk) * result
                    elif DP > D or LP > L:
                        result  = 'Srednica i dlugosc czubka nie moze byc wieksza niz lugosc i srednica calego penetratora'
                    else:
                        Wrk = L-(LP*(1-1/3*(1+DP/D+(DP**2/D**2))))
                        s = ((138 + (-0.1 * 240)) * 240) / 17200
                        seg1 = math.sqrt(17200 / 240)
                        seg2 = math.exp((-s) / (V * V))
                        result = 0.921 * (1 / math.tanh(0.283 + (0.0656 * (Wrk / D)))) * seg1 * seg2
                        result = 0.18 * (Wrk) * result

        args = {'form': form , 'result': result,'nazwisko': nazwisko}
        return render(request, self.template_name, args)