from django.shortcuts import render, HttpResponse
from django.db import models
from .models import Url
from django.shortcuts import render
from django.http import HttpRequest
from .forms import UrlForm


def start_page(request):
    return render(request, 'stream/start_page.html')


def demo_url(request):
     return render(request, 'stream/demo.html')


def saving_url(request):
    form = UrlForm(request.POST)

    #if form.is_valid():
     #   form.save()
    url=form.cleaned_data['url']
    Url.objects.create(url = form.cleaned_data['url'])
        #return HttpResponse('/thanks/')
    #else:
     #   url = UrlForm()
    return render(request, 'stream/name.html',{"url":url})
