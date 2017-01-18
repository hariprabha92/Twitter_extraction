from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from app.twitter import tweets
import json

def home(request):
    return render(request, 'app/index.html')
def results(request):
    git=None
    a=request.POST.get(str('twittername'))
    git=tweets(a)
    return render(request, 'app/results.html',{'datas':git})

