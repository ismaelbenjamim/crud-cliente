from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Hometemplateview (TemplateView):
    template_name = 'base/home.html'

class MenuView (TemplateView):
    template_name = 'base/menu.html'