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
        token = 'EAAEze9xMBS0BAMCQy0xL4gwXsmnZCGfReBpvTQdvORR1EG0MpKo28c427jHY2OYWoWX4ItZBZAhKsnVNGx85fNikQgjHV3rAelYSaRHctXfmZAR1ni1ZCAxEbSIpHGSyBZCamvZCGiZCKBNaWMnFu4IOEZCj6E4r9wVQU3YXj8lZAUjhb4gLVMkxmEdyxcbMD9RwQdQklrBed2ugZDZD'

        graph = facebook.GraphAPI(token)
        fields = ['link', 'created_time']
        fields = ','.join(fields)
        print(fields)
        url = url.split('/')[-2] + '/posts'
        page = graph.get_object(url, fields=fields)
        for posts in page['data']:
            a.append([posts['created_time'], posts['link']])
    a.sort(reverse=True)
    b = list(map(lambda x: x[2], a))
    context = {'l_post': b}
    return render(request, 'stream/stream.html', context)
