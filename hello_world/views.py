from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import View


from . import helpers
from . import monitor
from . import filter
from . import pdfexport
from .render import Render

 #monitoring.py dosyasını ekledin.

def default(request):
    #return HttpResponseRedirect('index/1') # (request, 'hello_world/index.html')
    return HttpResponseRedirect('monitoring/1') #hello world diznine girdiğinde direk olarak monitoring/1 e yönlensin. 

def index(request, page=1):
    return render(request, 'hello_world/index.html', {'logs': helpers.get_logs(int(page, 10))})

#def monitoring(request):
#    return render(request, 'hello_world/monitoring.html', {'logs': helpers.get_logs()})

def monitoring(request, page=1):
    if request:
        return render(request, 'hello_world/monitoring.html', {'logs': monitor.get_logs(int(page, 10))})
    else:
        return HttpResponse("LOGLAR BU KADAR")

def suphelihareketler(request):
    return render(request, 'hello_world/suphelihareketler.html', {'logs': helpers.get_logs()})


def raporcikar(request):
    return render(request, 'hello_world/raporcikar.html', {'logsayisi1003': pdfexport.get_number_1003(), 'logsayisi1027': pdfexport.get_number_1027(), 'logsayisi1086': pdfexport.get_number_1086(), 'logs': pdfexport.get_logs(), 'logsayisi1136': pdfexport.get_number_1136()})


def Pdf(request, page=1):
        return Render.render('hello_world/raporpdf.html', {'logsayisi1003': pdfexport.get_number_1003(), 'logsayisi1027': pdfexport.get_number_1027(), 'logsayisi1086': pdfexport.get_number_1086(), 'logsayisi1136': pdfexport.get_number_1136(), 'logs': pdfexport.get_logs()})