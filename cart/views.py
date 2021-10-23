import json
from decimal import Decimal
from datetime import date, datetime

from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from cart.cart import Cart
from perfomances.models import Ticket


def add_to_cart(request):
  try:
    ticket = Ticket.objects.select_related('poster').get(id = request.POST.get("ticket_id",9))
  except ObjectDoesNotExist:
    return HttpResponse(json.dumps({'error': "Билет не найден"}), content_type='application/json', status=404)
  if ticket.poster.close_date <=timezone.now():
    return HttpResponse(json.dumps({'error': "Афиша была закрыта, добавление невозможно"}), content_type='application/json', status=403)
  if ticket.reservation == True:
    return HttpResponse(json.dumps({'error': 'Билет уже занят'}), content_type='application/json', status=403)
  ticket.reservation = True
  ticket.save()
  cart = Cart(request.COOKIES)
  cart.add(ticket)
  response = HttpResponse(json.dumps({'text': "Билет успешно добавлен"}), content_type='application/json' ,status=201)
  if(request.COOKIES.get("CART_ID", '') != cart.cart.id):
    response.set_cookie(key="CART_ID", value=cart.cart.id, httponly=True)
  return response

def remove_from_cart(request):
  try:
    ticket = Ticket.objects.select_related('poster').get(id = request.POST.get("ticket_id",0))
  except ObjectDoesNotExist:
    return HttpResponse(json.dumps({'error': "Билет не найден"}), content_type="application/json", status=404)
  ticket.reservation = False
  ticket.save()
  cart = Cart(request.COOKIES)
  try:
    cart.remove(ticket)
  except ObjectDoesNotExist:
    return HttpResponse(json.dumps({'error': "Билет не найден в корзине."}), content_type='application/json', status=404)
  response = HttpResponse(json.dumps({'text':"Билет успешно удалён"}), content_type='application/json', status=200)
  if(request.COOKIES.get("CART_ID") != cart.cart.id):
    response.set_cookie(key="CART_ID", value=cart.cart.id, httponly=True)
  return response

def get_cart(request): 
  cart = Cart(request.COOKIES)
  queryset = cart.cart.ticket_set.select_related('ticket', 'ticket__poster', 'ticket__poster__perfomance')
  tickets = []
  for item in queryset:
    ticket = {}
    ticket["id"] = item.id
    ticket["ticket_id"] = item.ticket.id
    ticket["title"] = item.ticket.poster.perfomance.title
    ticket["start_date"] = item.ticket.poster.formatted_start_date
    ticket["seat_id"] = item.ticket.seat_id
    ticket["sector"] = item.ticket.sector
    ticket["row_number"] = item.ticket.row_number
    ticket["seat_number"] = item.ticket.seat_number
    ticket["price"] = item.ticket.price
    tickets.append(ticket)
  data = json.dumps({'timeout':cart.cart.timeout, 'tickets': tickets, 'count': cart.count(), 'total': cart.summary()}, cls=DecimalEncoder)
  response = HttpResponse(data, content_type="application/json", status=200)
  if(request.COOKIES.get("CART_ID", '') != cart.cart.id):
    response.set_cookie(key="CART_ID", value=cart.cart.id, httponly=True)
  return response

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, (datetime, date)):
          return obj.isoformat()
        return json.JSONEncoder.default(self, obj)
