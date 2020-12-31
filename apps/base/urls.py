from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.base.views import Hometemplateview

urlpatterns = [
    path('', login_required(Hometemplateview.as_view()), name = 'home'),
]
