from datetime import datetime

from django.db import models


class Position(models.Model):
  position = models.CharField(max_length=255, verbose_name="Должность")
  has_self_page = models.BooleanField(default=True, verbose_name="Есть собственная страница")

  def __str__(self):
    return self.position

  class Meta:
    verbose_name = "Должность"
    verbose_name_plural = "Должности"


class Person(models.Model):

  def upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/people/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename
  
  name = models.CharField(max_length=100, verbose_name="Имя")
  surname = models.CharField(max_length=100, verbose_name="Фамилия")
  middlename = models.CharField(max_length=100, verbose_name="Отчество")
  biography = models.TextField(verbose_name="Биография")
  position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Должность")
  image = models.ImageField(upload_to=upload_to,verbose_name="Основное фото")
  banner_image = models.ImageField(upload_to=upload_to,verbose_name="Банер фото", null=True)
  banner_video = models.CharField(max_length=255, verbose_name="Баннер идентификатор ютуб видео", null=True)

  def __str__(self):
    return self.name

  @property
  def full_name(self):
    return '{} {} {}'.format(self.name, self.surname, self.middlename)
  
  class Meta:
    verbose_name = "Человек"
    verbose_name_plural = "Люди"


class PersonImage(models.Model):

  def upload_to(self, file):
    arr = file.split('.')
    ext = arr[-1]
    name = ''
    for i in range(len(arr)-1):
      name+=arr[i]
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    path = 'images/people/'
    filename = '{}{}-{}.{}'.format(path, name, time, ext)
    return filename
  
  person = models.ForeignKey(Person, verbose_name="Актёр", on_delete=models.CASCADE)
  image = models.ImageField(upload_to=upload_to, verbose_name="Фото")

  def __str__(self):
    return str(self.person)

  class Meta:
    verbose_name = "Изображение человека"
    verbose_name_plural = "Изображения людей"