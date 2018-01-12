from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def start_page(request):
    return render(request, 'stream/start_page.html')