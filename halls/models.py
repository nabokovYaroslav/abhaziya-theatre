from datetime import datetime

from django.db import models


class Hall(models.Model):
  name = models.CharField(max_length=255, verbose_name="Название зала")
  descrpition = models.TextField(verbose_name="Описание зала")

  def __stf__(self):
    return self.name

  class Meta:
    verbose_name = 'Зал'
    verbose_name_plural = 'Залы'

class HallImage(models.Model):
  
  def upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/projects/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename

  hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name="Зал")
  image = models.ImageField(upload_to=upload_to, verbose_name="Изображение зала")

  def __stf__(self):
    return str(self.hall)

  class Meta:
    verbose_name = 'Изображение зала'
    verbose_name_plural = 'Изображения залов'
