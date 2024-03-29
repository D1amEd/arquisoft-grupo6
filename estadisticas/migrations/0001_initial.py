# Generated by Django 3.2.6 on 2022-09-27 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=50)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('reporte', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='reportes.reporte')),
            ],
        ),
    ]
