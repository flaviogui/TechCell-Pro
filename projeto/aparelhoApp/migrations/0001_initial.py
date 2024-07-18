# Generated by Django 4.2.11 on 2024-07-17 18:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparelho',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('imei', models.CharField(max_length=15, unique=True)),
                ('numero_serie', models.CharField(max_length=50, unique=True)),
                ('descricao_problema', models.TextField()),
                ('ordem_servico', models.CharField(blank=True, max_length=36, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Aparelho',
                'verbose_name_plural': 'Aparelhos',
                'ordering': ['marca', 'modelo'],
            },
        ),
    ]