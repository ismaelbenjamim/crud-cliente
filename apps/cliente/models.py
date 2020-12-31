from django.db import models
from django.urls import reverse


class Cliente(models.Model):
    nome = models.CharField(max_length=64)
    endereco = models.TextField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list')