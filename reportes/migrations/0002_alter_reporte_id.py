# Generated by Django 3.2.6 on 2022-10-01 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
