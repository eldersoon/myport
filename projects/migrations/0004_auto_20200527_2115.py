# Generated by Django 3.0.6 on 2020-05-28 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200527_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects_img'),
        ),
    ]
