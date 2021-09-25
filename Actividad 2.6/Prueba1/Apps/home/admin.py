from Apps.home.models import Administrador, Articulos, Comentario, Estudiante
from django.contrib import admin

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Administrador)
admin.site.register(Articulos)
admin.site.register(Comentario)