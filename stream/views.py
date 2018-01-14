from django.shortcuts import render, HttpResponse
from django.db import models
from .models import Url
from django.shortcuts import render
from django.http import HttpRequest
from .forms import UrlForm
from .models import Url
from .forms import UrlForm
import facebook


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

    a = []
    for url in Url.objects.all():
        token = 'EAAEze9xMBS0BAFwhmYrdWFmjP4tZCX9di843oTZCHuEKt3o8zSy9Mk88dcKfhH1AQF9UP5v5Wz1ZAQYov6Kd8SuWsgZCWyXVJR5yBmXBocpG7vtD8WakkWFlxRKXzRQ6mIK2hyj8lO7lIL5JdXe7GJ1ZBhdfnpA3T51A6RIl454UPtIbbz6WfeV7xRbNCFLkzeMsgTNL6sgZDZD'

        graph = facebook.GraphAPI(token)
        fields = ['link', 'created_time']
        fields = ','.join(fields)
        print(fields)
        url = str(url).split('/')[-2] + '/posts'
        page = graph.get_object(url, fields=fields)
        for posts in page['data'][:5]:
            a.append([posts['created_time'], posts['link']])
    a.sort(reverse=True)
    b = list(map(lambda x: x[1], a))
    context = {'l_post': b}
    return render(request, 'stream/stream.html', context)
