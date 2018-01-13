'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.start_page, name='start_page'),
    url('saving_url/', views.saving_url, name='saving_url'),
    url('demo_url/', views.demo_url, name='demo_url'),
]
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('clear/', views.clear_urls, name='clear_urls'),
    path('saving_url/', views.saving_url, name='saving_url'),
    path('stream/', views.stream, name='stream'),
    #path('demo_url/', views.demo_url, name='demo_url'),
]
