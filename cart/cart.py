from datetime import timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.db.models import Sum

from cart import models

CART_ID = 'CART_ID'


class TicketAlreadyExists(Exception):
  pass


class TicketDoesNotExist(Exception):
  pass


class Cart:
  def __init__(self, cookies):
    cart_id = cookies.get(CART_ID)
    if cart_id:
      cart = models.Cart.objects.prefetch_related('ticket_set').filter(id=cart_id).first()
      if cart is None:
        cart = self.new()
    else:
      cart = self.new()
    self.cart = cart

  def __iter__(self):
    for item in self.cart.ticket_set.all():
      yield item

  def new(self):
    cart = models.Cart.objects.create(creation_date=timezone.now(), timeout=timezone.now() + timedelta(minutes=10))
    return cart

  def add(self, ticket):
    models.Ticket.objects.create(cart=self.cart, ticket=ticket)
    self.cart.last_updated = timezone.now()
    self.cart.save()

  def remove(self, ticket):
    try:
      ticket = models.Ticket.objects.get(cart=self.cart, ticket=ticket)
    except ObjectDoesNotExist:
      raise ObjectDoesNotExist
    ticket.delete()

  def count(self):
    return self.cart.ticket_set.count()

  def summary(self):
    total = self.cart.ticket_set.select_related('ticket').aggregate(total=Sum('ticket__price')).get('total', 0)
    return 0 if total == None else total

  def clear(self):
    self.cart.item_set.all().delete()
