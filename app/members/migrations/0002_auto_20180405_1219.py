# Generated by Django 2.0.3 on 2018-04-05 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20, unique=True, verbose_name='nickname'),
        ),
    ]