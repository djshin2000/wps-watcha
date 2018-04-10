# Generated by Django 2.0.3 on 2018-04-10 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('real_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='본명')),
                ('img_profile', models.ImageField(blank=True, upload_to='members')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
            ],
        ),
    ]
