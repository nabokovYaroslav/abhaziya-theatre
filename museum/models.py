from datetime import datetime

from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=255, verbose_name="Категория")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'

class Item(models.Model):

  def upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/museum/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename

  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
  name = models.CharField(max_length=255, verbose_name="Название")
  image = models.ImageField(upload_to=upload_to, verbose_name="Основное изображение")
  year = models.PositiveIntegerField(verbose_name="Год")
  description = models.TextField(verbose_name="Описание", null=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Предмет'
    verbose_name_plural = 'Предметы'

class ItemImage(models.Model):

  def upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/museum/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename
  
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  image = models.ImageField(upload_to=upload_to, verbose_name="Изображение")

  def __str__(self):
    return str(self.item)

  class Meta:
    verbose_name = 'Изображение предмета'
    verbose_name_plural = 'Изображение предметов'