from django.contrib import admin
from .models import Cliente, Produto, Endereco

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Produto)