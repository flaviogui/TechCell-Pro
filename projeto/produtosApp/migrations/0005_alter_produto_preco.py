# Generated by Django 4.2.11 on 2024-08-19 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtosApp', '0004_alter_produto_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.FloatField(),
        ),
    ]
