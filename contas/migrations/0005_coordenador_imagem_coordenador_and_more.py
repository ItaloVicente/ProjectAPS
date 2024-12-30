# Generated by Django 5.1.4 on 2024-12-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_evento_horafim_evento_horainicio_evento_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordenador',
            name='imagem_coordenador',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='perfil_coordenador/'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='qr_code',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='qr_code/'),
        ),
    ]