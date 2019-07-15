from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.default, name='default'), #/hello_world girdiğinde beni default fonksiyonuna yönlendir.
    re_path('index/(?P<page>[0-9]*)', views.index, name='index'),
    #path('monitoring', views.monitoring, name='monitoring') 
    re_path('monitoring/(?P<page>[0-9]*)', views.monitoring, name='monitoring'), #pagination için bu sayfaları eklememiz gerekiyor. 
    re_path('suphelihareketler/', views.suphelihareketler, name='suphelihareketler'),
    path('raporcikar/', views.raporcikar, name='raporcikar'),
    path('raporpdf/', views.Pdf, name="raporpdf" )
]