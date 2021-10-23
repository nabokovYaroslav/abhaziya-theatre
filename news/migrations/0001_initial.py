# Generated by Django 3.2.8 on 2021-10-20 06:33

from django.db import migrations, models
import django.db.models.deletion
import news.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название новости')),
                ('text', models.TextField(verbose_name='Текст новости')),
                ('image', models.ImageField(upload_to=news.models.News.upload_to, verbose_name='Изображение новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=news.models.NewsImage.upload_to, verbose_name='Изображение')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Изображение новости',
                'verbose_name_plural': 'Изображения новостей',
            },
        ),
    ]