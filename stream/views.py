from django.shortcuts import render, HttpResponse
from django.db import models
from .models import Url
from django.shortcuts import render
from django.http import HttpRequest
from .forms import UrlForm
from .models import Url
from .forms import UrlForm


def start_page(request):
    return render(request, 'stream/start_page.html')


def clear_urls(request):
    Url.objects.all().delete()
    context = {"cleared": "done", "Merge": "Not Merged"}
    return render(request, 'stream/start_page.html', context)


def saving_url(request):
   # form = UrlForm(request.POST)

    #if form.is_valid():
     #   form.save()
    #url=form.cleaned_data['url']
    Url.objects.create(url = request.POST.get("url"))
        #return HttpResponse('/thanks/')
    #else:
     #   url = UrlForm()
    context = {"Merge": "Url Merged"}
    return render(request, 'stream/start_page.html', context)


def stream(request):
    for x in Url.objects.all():
