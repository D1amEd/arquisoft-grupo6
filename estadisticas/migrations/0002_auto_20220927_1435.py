# Generated by Django 3.2.6 on 2022-09-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadistica',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='estadistica',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]