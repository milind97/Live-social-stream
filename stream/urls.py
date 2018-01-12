from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.start_page, name='start_page'),
]