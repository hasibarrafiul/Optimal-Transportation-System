# Generated by Django 3.2.6 on 2021-08-23 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_balaka_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balaka',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]
