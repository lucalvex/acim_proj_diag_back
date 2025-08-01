# Generated by Django 5.1.6 on 2025-07-21 19:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0006_alter_respostadimensao_resposta_modulo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RepostaModuloIncompleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respotas', models.JSONField(default=dict)),
                ('dataResposta', models.DateTimeField(auto_now=True)),
                ('modulo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='respostas_incompletas', to='questionario.modulo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Respostas Incompletas dos Módulos',
            },
        ),
    ]
