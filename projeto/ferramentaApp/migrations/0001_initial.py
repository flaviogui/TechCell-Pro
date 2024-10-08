# Generated by Django 4.2.11 on 2024-08-15 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ferramenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('quantidade_disponivel', models.PositiveIntegerField()),
                ('condicao', models.CharField(choices=[('novo', 'Novo'), ('usado', 'Usado'), ('danificado', 'Danificado')], max_length=20)),
                ('fornecedor', models.CharField(max_length=100)),
            ],
        ),
    ]
