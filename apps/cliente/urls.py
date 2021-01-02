from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.cliente.views import ClienteListView, ClienteUpdateView, ClienteCreateView, ClienteDeleteView, ClienteListViewDelete

urlpatterns = [
    path('list', login_required(ClienteListView.as_view()), name='list'),
    path('update/<int:pk>', login_required(ClienteUpdateView.as_view()), name='update'),
    path('create', login_required(ClienteCreateView.as_view()), name='create'),
    path('delete/deletaruser=<int:pk>', login_required(ClienteDeleteView.as_view()), name='delete'),
    path('delete', login_required(ClienteListViewDelete.as_view()), name='deleteview'),
]
