from django.shortcuts import render
from django.views.generic.base import View

from radio.models import Audio


class AudioList(View):

  def get(self, request):
    audiotapes = Audio.objects.all()
    return render(request, 'radio/audio_list.html', context={'audiotapes': audiotapes})
