# Generated by Django 5.0.6 on 2024-06-13 22:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_pergunta', models.CharField(max_length=200)),
                ('data_publicacao', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Escolha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_escolha', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquetes.pergunta')),
            ],
        ),
    ]