from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.

def home(request):

    HtmlFile = open('boards/front_page/page.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read() 

    return HttpResponse(source_code)


