from django.db import models

# Create your models here.

class Curso(models.Model):
    id = models.AutoField(primary_key = True)
    nome_curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_curso

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)  # ID com auto incremento
    nome = models.CharField(max_length=255)  # Nome com limite de 255 caracteres
    senha = models.CharField(max_length=255)  # Senha com limite de 255 caracteres
    email = models.EmailField(unique=True)  # Email único
    curso_id = models.ForeignKey('Curso', on_delete=models.CASCADE)  # Chave estrangeira para Curso
    imagem_aluno = models.ImageField(upload_to='perfil_aluno/', null=True, blank=True, default=None)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length= 255)
    desc_breve = models.CharField(max_length= 255)
    desc_detalhada = models.CharField(max_length= 511)
    data_ini = models.DateField()
    data_final = models.DateField()
    professorID = models.ForeignKey('Professor', on_delete=models.CASCADE)
    tipoId = models.ForeignKey("TipoDeHora", on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='fotos/', null=True, blank=True, default=None)
    horaInicio = models.TimeField(default=None)
    horaFim = models.TimeField(default=None)
    def __str__(self):
            return self.nome


class Professor(models.Model):
    id = models.AutoField(primary_key = True)
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    curso_id = models.ForeignKey('Curso', on_delete=models.CASCADE)
    imagem_professor = models.ImageField(upload_to='perfil_professor/', null=True, blank=True, default=None)


    def __str__(self):
        return self.nome


class TipoDeHora(models.Model):
    id = models.AutoField(primary_key=True)
    nome_hora = models.CharField(max_length=255)
    horas_max = models.IntegerField()
    horas_max_atv = models.IntegerField()

class HoraComplementar(models.Model):
    id = models.AutoField(primary_key=True)
    horas = models.IntegerField()
    tipoId = models.ForeignKey('TipoDeHora', on_delete=models.CASCADE)
    alunoId = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    certificadoId = models.ForeignKey('Certificado', on_delete=models.CASCADE)

class Certificado(models.Model):
    id = models.AutoField(primary_key=True)
    fs_path = models.CharField(max_length=511)
    alunoId = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    eventoId = models.ForeignKey('Evento', on_delete=models.CASCADE)

class Inscricao(models.Model):
    id = models.AutoField(primary_key=True)
    alunoId = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    eventoId = models.ForeignKey('Evento', on_delete=models.CASCADE)
    #Validar com o pessoal
    qr_code = models.ImageField(upload_to='qr_code/', null=True, blank=True, default=None)


class Presenca(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    falta = models.BooleanField(default=False)
    inscricaoId = models.ForeignKey('Inscricao', on_delete=models.CASCADE)
    eventoId = models.ForeignKey('Evento', on_delete=models.CASCADE)

class Coordenador(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    cursoId = models.ForeignKey('Curso', on_delete=models.CASCADE)
    imagem_coordenador = models.ImageField(upload_to='perfil_coordenador/', null=True, blank=True, default=None)
    def __str__(self):
        return self.nome



