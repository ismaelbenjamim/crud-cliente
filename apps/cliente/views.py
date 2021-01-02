from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from apps.cliente.models import Cliente


class ClienteListView (ListView):
    model = Cliente

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('list')

class ClienteListViewDelete (ListView):
    model = Cliente
    template_name = 'cliente/cliente_delete.html'