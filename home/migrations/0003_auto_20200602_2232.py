# Generated by Django 3.0.6 on 2020-06-03 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200602_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='subtitle',
            field=models.TextField(max_length=255),
        ),
    ]
