# Generated by Django 4.2 on 2023-04-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_plannedleave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plannedleave',
            name='date',
            field=models.DateField(),
        ),
    ]
