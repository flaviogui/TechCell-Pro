# Generated by Django 4.2.11 on 2024-08-14 00:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=16, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=18, null=True)),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=25)),
                ('bairro', models.CharField(max_length=25)),
                ('cidade', models.CharField(max_length=25)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9)),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
                'ordering': ['nome'],
            },
        ),
    ]
