# Generated by Django 2.2.2 on 2019-10-23 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takes',
            name='semester',
            field=models.CharField(choices=[('spring', 'spring'), ('fall', 'fall'), ('summer', 'summer')], max_length=20),
        ),
    ]
