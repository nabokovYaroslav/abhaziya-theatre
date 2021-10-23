from django.utils import timezone

from django.shortcuts import render
from django.views.generic.base import View

from perfomances.models import Poster
from people.models import Person


class Index(View):

  def get(self, request):
    posters = (
               Poster
               .objects
               .select_related('perfomance', 'perfomance__producer')
               .filter(close_date__gte=timezone.now())
               )
    persons = Person.objects.only('name', 'surname', 'middlename', 'biography', 'image')
    return render(request, 'main/main.html', context={'poster_list': posters, 'person_list': persons})
