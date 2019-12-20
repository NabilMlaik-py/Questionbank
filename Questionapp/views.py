from django.shortcuts import render
from .models import q_a
from django.http import *
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'


def index(request):
    Questionapp = q_a.objects.all()
    return render(request, 'nabil.html', {'Questionapp': Questionapp})
   # return HttpResponse('index.html')
  #  return HttpResponseRedirect('/Questionapp/')
