from django.db import models


class Livro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
