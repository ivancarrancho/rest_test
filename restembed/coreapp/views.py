# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from coreapp.models import SavedEmbeds

import requests


from .forms import SubmitEmbed
from .serializer import EmbedSerializer


def save_embed(request):

    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            r = requests.get('http://api.embed.ly/1/oembed?key=' + settings.EMBEDLY_KEY + '&url=' + url)
            json = r.json()
            serializer = EmbedSerializer(data=json)
            if serializer.is_valid():

                embed = serializer.save()
                return render(request, 'embed.html', {'embed': embed})
    else:
        form = SubmitEmbed()

    return render(request, 'index.html', {'form': form})


def video_all(self, **kwargs):
    videos = SavedEmbeds.objects.all()

    return render(self, 'new.html', {'videos': videos})
