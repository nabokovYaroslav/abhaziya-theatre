from django.http.response import HttpResponse, JsonResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core import serializers

from perfomances.models import Poster


class PosterList(View):

  def get(self, request):
    posters = (
              Poster
              .objects
              .select_related('perfomance', 'perfomance__producer')
              .filter(close_date__gte=timezone.now())
              .order_by('start_date')
              )
    months = {
      1: 'января',
      2: 'февравля',
      3: 'марта',
      4: 'апреля',
      5: 'мая',
      6: 'инюня',
      7: 'илюля',
      8: 'августа',
      9: 'сентября',
      10: 'октября',
      11: 'ноября',
      12: 'декабря'
    }
    posters_group = []
    for poster in posters:
      isExit = False
      for poster_group in posters_group:
        if poster_group['day'] == poster.start_date.day and posters_group['month'] == posters_group.start_date.month:
          isExit == True
          poster_group['posters'].append(poster)
          break
      if not isExit:
        posters_group.append({'day': poster.start_date.day, 'month': months[poster.start_date.month], 'posters': [poster]})
    print(posters_group)
    return render(request, 'posters/poster_list.html', context={'posters_group':posters_group})

class PosterDetail(View):
  
  def get(self, request, pk=None):
    poster = (
              Poster
              .objects
              .select_related('perfomance', 'perfomance__producer')
              .prefetch_related('perfomance__perfomanceimage_set', 'perfomance__actors')
              .filter(close_date__gte=timezone.now())
              .get(id=pk)
              )
    return render(request,
                 'posters/poster_detail.html', 
                  context={
                          'poster':poster, 
                          'poster_images': poster.perfomance.perfomanceimage_set.all(), 
                          'actors': poster.perfomance.actors.all()
                          }
                  )

class Place(View):
  def get(self, request, pk=None):
    poster = get_object_or_404(
              Poster
              .objects
              .filter(close_date__gte=timezone.now())
              .select_related('perfomance'),
              id=pk
              )
    return render(request, 'posters/place.html', context={'poster': poster})

class Map(View):
  def get(self, request, pk=None):
    poster = Poster.objects.select_related('perfomance', 'perfomance__map').get(id=pk)
    map_svg = poster.perfomance.map.map_svg.url
    return HttpResponse(map_svg)

class Ticket(View):
  def get(self, request, pk=None):
    poster = Poster.objects.prefetch_related('ticket_set').filter(close_date__gte=timezone.now()).get(id=pk)
    tickets = poster.ticket_set.all().filter(reservation=False)
    data = serializers.serialize('json', tickets)
    return HttpResponse(data, content_type='application/json')

