# Generated by Django 4.2.11 on 2024-08-19 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtosApp', '0003_rename_preco_produto_preco_alter_produto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.IntegerField(),
        ),
    ]
