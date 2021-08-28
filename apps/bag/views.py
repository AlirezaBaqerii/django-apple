from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

def bag(request):
    return render(request, 'bag/bag.html', )
