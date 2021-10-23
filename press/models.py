from django.db import models


class Press(models.Model):
  name = models.CharField(max_length=255, verbose_name="Заголовок")
  text = models.TextField(verbose_name="Текст статьи")
  url = models.URLField(max_length=255,verbose_name="Ссылка на источник")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Пресса'
    verbose_name_plural = 'Пресса'
