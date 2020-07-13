from django.contrib import admin
from . import models


class EdiAdmin(admin.ModelAdmin):
    list_display = ('Id_Ed', 'Nome', 'Telefone')


class LivAdmin(admin.ModelAdmin):
    list_display = ('Id_Li', 'Nome', 'Autor', 'Editora')


class ResAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Nome_liv', 'Devolver')


admin.site.register(models.Editora, EdiAdmin)
admin.site.register(models.Livro, LivAdmin)
admin.site.register(models.Reservar, ResAdmin)
# Register your models here.

# Register your models here.
