# Generated by Django 4.2.11 on 2024-08-19 05:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedorApp', '0003_remove_fornecedor_data_cadastro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=75)),
                ('descricao', models.CharField(max_length=250)),
                ('codigo', models.CharField(max_length=9)),
                ('quantidade', models.IntegerField(max_length=10)),
                ('preco_compra', models.IntegerField()),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedorApp.fornecedor')),
            ],
            options={
                'verbose_name': 'Peça',
                'verbose_name_plural': 'Peça',
                'ordering': ['nome'],
            },
        ),
    ]
