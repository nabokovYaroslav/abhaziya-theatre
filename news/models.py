from datetime import datetime

from django.db import models


class News(models.Model):

  def upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/news/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename

  name = models.CharField(max_length=255, verbose_name="Название новости")
  text = models.TextField(verbose_name="Текст новости")
  image = models.ImageField(upload_to=upload_to, verbose_name="Изображение новости")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'

class NewsImage(models.Model):

  def upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/news/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename

  news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name="Новость")
  image = models.ImageField(upload_to=upload_to, verbose_name="Изображение")

  def __str__(self):
    return str(self.news)

  class Meta:
    verbose_name = 'Изображение новости'
    verbose_name_plural = 'Изображения новостей'
