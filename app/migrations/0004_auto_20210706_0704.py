# Generated by Django 3.2.5 on 2021-07-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210706_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, upload_to='staff_image'),
        ),
        migrations.AlterField(
            model_name='startapper',
            name='image',
            field=models.ImageField(blank=True, upload_to='startapper_file/startapp_image'),
        ),
    ]