from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria', 'destaque')
    list_filter = ('categoria', 'destaque')
    search_fields = ('nome', 'descricao')