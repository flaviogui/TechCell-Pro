# Generated by Django 4.2.11 on 2024-08-14 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('codigo_barras', models.CharField(max_length=13, unique=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.CharField(max_length=100)),
            ],
        ),
    ]