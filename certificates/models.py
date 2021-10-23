from django.db import models


class Certificate(models.Model):
  price = models.PositiveIntegerField(verbose_name="Цена")

  def __str__(self):
    return self.price

  class Meta:
    verbose_name = 'Сертификат'
    verbose_name_plural = 'Сертификаты'
