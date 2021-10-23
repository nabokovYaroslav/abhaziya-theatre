from uuid import uuid4

from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _

from perfomances.models import Ticket


class Cart(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  creation_date = models.DateTimeField(verbose_name=_('creation date'))
  last_updated = models.DateTimeField(default=timezone.now)
  timeout = models.DateTimeField(null=True)

  class Meta:
    verbose_name = _('cart')
    verbose_name_plural = _('carts')
    ordering = ('-creation_date',)

  def __str__(self):
    return str(self.creation_date)


class Ticket(models.Model):
  cart = models.ForeignKey(Cart, verbose_name=_('cart'), on_delete=models.CASCADE)
  ticket = models.OneToOneField(Ticket, verbose_name="Билет", on_delete=models.CASCADE)

  class Meta:
    verbose_name = _('item')
    verbose_name_plural = _('items')
    ordering = ('cart',)

  def __unicode__(self):
    return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)