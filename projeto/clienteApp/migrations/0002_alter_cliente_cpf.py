# Generated by Django 4.2.11 on 2024-07-12 05:29

import cpf_field.models # type: ignore
from django.db import migrations # type: ignore


class Migration(migrations.Migration):

    dependencies = [
        ('clienteApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=cpf_field.models.CPFField(max_length=14, verbose_name='cpf'),
        ),
    ]
