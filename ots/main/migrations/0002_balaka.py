# Generated by Django 3.2.6 on 2021-08-23 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='balaka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, max_length=3000)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, '1 - Trash'), (2, '2- Horrible'), (3, '3- Terrible'), (4, '4- Bad'), (5, '5- OK'), (6, '6- Rideable'), (7, '7- Good'), (8, '8- Very good'), (9, '9- Perfect'), (10, '10- Best')])),
                ('likes', models.PositiveIntegerField(default=0)),
                ('unlikes', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
