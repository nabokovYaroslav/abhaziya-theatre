from datetime import datetime

from django.db import models


class History(models.Model):

  def upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/histories/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename

  name = models.CharField(max_length=255, verbose_name="Название периода")
  start_period = models.PositiveIntegerField(verbose_name="Год начала периода")
  end_period = models.PositiveIntegerField(verbose_name="Год окончания периода")
  image = models.ImageField(upload_to=upload_to, verbose_name="Изображение")
  text = models.TextField(verbose_name="Описание периода")

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'История'
    verbose_name_plural = 'Истории'