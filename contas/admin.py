
from django.contrib import admin

from .models import Conta, Transacoes

admin.site.register(Conta)
admin.site.register(Transacoes)
