from datetime import datetime

from django.db import models


class Partner(models.Model):

  def upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/partners/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename

  name = models.CharField(max_length=255, verbose_name="Имя партнёра")
  image = models.ImageField(upload_to=upload_to, verbose_name="Фотография партнёра")
  url = models.URLField(max_length=255, null=True, verbose_name="Ссылка на партнёра")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Партнёр'
    verbose_name_plural = 'Партнёры'