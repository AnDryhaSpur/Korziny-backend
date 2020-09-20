from django.shortcuts import render
from django.http import HttpResponse
from bitrix24 import Bitrix24


bx24 = Bitrix24('https://alteka.bitrix24.ru/rest/1/lerb5yxddj5fxgpz')
# Create your views here.
def index(request):
    return render(request, 'index.html')

def send(request):
    name = request.POST.get('name')
    tel = request.POST.get('tel')
    bx24.callMethod('crm.lead.add', fields={'TITLE': 'Корзины заявка - {}'.format(name), 'NAME': name, 'PHONE': [{'VALUE': tel, 'VALUE_TYPE': 'MOBILE'}]})
    return HttpResponse(name, tel)

def handler404(request):
    return render(request, 'base/404.html', status=404)
def handler500(request):
    return render(request, 'base/500.html', status=500)
