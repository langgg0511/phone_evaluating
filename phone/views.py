from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template


# Create your views here.

def index(requset):
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)


def phone(request, phone_id):
    template = get_template('phone.html')
    html = template.render(locals())
    return HttpResponse(html)
