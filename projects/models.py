from datetime import datetime

from django.utils import timezone
from django.db import models


class Project(models.Model):
  name = models.CharField(max_length=255, verbose_name="Название проекта")
  description = models.TextField(verbose_name="Описание проекта")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Проект'
    verbose_name_plural = 'Проекты'

class ProjectImage(models.Model):

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

  project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Проект")
  name = models.CharField(max_length=255, verbose_name="Название изображения")
  published_date = models.DateField(verbose_name="Дата публикации", default=timezone.now)
  image = models.ImageField(upload_to=upload_to, verbose_name="Изображение")

  def __str__(self):
    return self.project

  class Meta:
    verbose_name = 'Изображение проекта'
    verbose_name_plural = 'Изображении проекта'

class ProjectVideo(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Проект")
  name = models.CharField(max_length=255, verbose_name="Название видео")
  published_date = models.DateField(verbose_name="Дата публикации", default=timezone.now)
  video = models.CharField(max_length=255, verbose_name="Идентификатор видео ютуб")

  def __str__(self):
    return self.project

  class Meta:
    verbose_name = 'Видеозапись проекта'
    verbose_name_plural = 'Видеозаписи проекта'
