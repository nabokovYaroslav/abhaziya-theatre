# Generated by Django 3.2.8 on 2021-10-20 06:33

from django.db import migrations, models
import django.db.models.deletion
import tours.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название гастроли')),
                ('year', models.PositiveIntegerField(verbose_name='Год')),
                ('image', models.ImageField(upload_to=tours.models.Tour.upload_to, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Гастроль',
                'verbose_name_plural': 'Гастроли',
            },
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=tours.models.TourImage.upload_to, verbose_name='Изображение')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tour', verbose_name='Гастроль')),
            ],
            options={
                'verbose_name': 'Изображение гастроли',
                'verbose_name_plural': 'Изображения гастролей',
            },
        ),
    ]
