# Generated by Django 4.0.1 on 2022-04-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_interests'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.TextField(blank=True),
        ),
    ]