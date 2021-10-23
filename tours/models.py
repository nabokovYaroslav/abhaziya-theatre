from datetime import datetime

from django.db import models


class Tour(models.Model):

  def upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/tours/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename

  name = models.CharField(max_length=255, verbose_name="Название гастроли")
  year = models.PositiveIntegerField(verbose_name="Год")
  image = models.ImageField(upload_to=upload_to, verbose_name="Изображение")
  
  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Гастроль'
    verbose_name_plural = 'Гастроли'

class TourImage(models.Model):

  def upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/tours/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename
  
  tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name="Гастроль")
  image = models.ImageField(upload_to=upload_to, verbose_name="Изображение")

  def __str__(self):
    return self.tour

  class Meta:
    verbose_name = 'Изображение гастроли'
    verbose_name_plural = 'Изображения гастролей'