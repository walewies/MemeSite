# Generated by Django 4.0.1 on 2022-04-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(max_length=256),
        ),
    ]
