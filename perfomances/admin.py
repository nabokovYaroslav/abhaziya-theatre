import json
import os

from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404

from config.settings import MEDIA_ROOT
from perfomances.models import Producer, Perfomance, PerfomanceImage, Poster, Ticket, Map

class TicketAdminForm(forms.ModelForm):
   def clean_reservation(self):   
      if self.instance.reservation == True and self.cleaned_data['reservation'] == True:
        raise forms.ValidationError(_("Билет уже занят"))
      return self.cleaned_data['reservation']

class TicketAdmin(admin.ModelAdmin):
  list_filter = ('reservation', 'poster', 'row_number', 'seat_number', 'sector')
  exclude = ('seat_id',)
  form = TicketAdminForm

class PosterAdmin(admin.ModelAdmin):
  def save_model(self, request, obj, form, change):
    super().save_model(request, obj, form, change)
    if change == False:
      tickets = []
      path = os.path.join(
                          MEDIA_ROOT, 
                          str(get_object_or_404(Perfomance.objects, id=request.POST["perfomance"]).map.seats_json)
                          )
      with open(path, encoding="utf-8") as json_file:
        data = json.load(json_file)
        for seats in data:
          sector = seats["sector"]
          for seat in seats["seats"]:
            ticket = Ticket(poster_id=obj.id,
                            seat_id=seat["id"],
                            row_number=seat["row_number"],
                            seat_number=seat["seat_number"], 
                            price=seat["price"], 
                            sector=sector
                            )
            tickets.append(ticket)
      Ticket.objects.bulk_create(tickets)

admin.site.register(Producer)
admin.site.register(Perfomance)
admin.site.register(PerfomanceImage)
admin.site.register(Poster, PosterAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Map)
