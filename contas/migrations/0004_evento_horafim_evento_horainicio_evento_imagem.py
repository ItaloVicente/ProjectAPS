# Generated by Django 5.1.4 on 2024-12-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_evento_tipodehora_coordenador_certificado_inscricao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='horaFim',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='evento',
            name='horaInicio',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='evento',
            name='imagem',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='fotos/'),
        ),
    ]
