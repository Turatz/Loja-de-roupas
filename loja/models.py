from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True)
    categoria = models.CharField(max_length=100)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.nome