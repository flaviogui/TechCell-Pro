# Generated by Django 4.2.11 on 2024-08-19 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pecaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peca',
            name='quantidade',
            field=models.IntegerField(),
        ),
    ]
