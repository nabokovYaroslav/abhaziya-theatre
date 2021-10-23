from datetime import datetime

from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=255, verbose_name="Название категории")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Категория"
    verbose_name = "Категории"

class Audio(models.Model):

  def image_upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/radio/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename

  def audio_upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'audio/radio/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename  
  
  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
  name = models.CharField(max_length=255, verbose_name="Название")
  speaker = models.CharField(max_length=255, verbose_name="Спикер")
  image = models.ImageField(upload_to=image_upload_to, verbose_name="Изображение")
  audio = models.FileField(upload_to=audio_upload_to, verbose_name="Аудиозапись")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Аудиозапись'
    verbose_name_plural = 'Аудиозаписи'