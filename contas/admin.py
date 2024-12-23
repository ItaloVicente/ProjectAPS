from django.contrib import admin
from .models import *

# Register your models here.
models = [Aluno, Curso, Professor, TipoDeHora, Evento, HoraComplementar,
          Certificado, Inscricao, Presenca, Coordenador]

for model in models:
    admin.site.register(model)
