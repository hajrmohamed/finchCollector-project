# Generated by Django 4.1.7 on 2023-03-17 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_finch_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='toy',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]
