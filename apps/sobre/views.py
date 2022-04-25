from django.shortcuts import render
from django.http import HttpResponse


def sobre_view(request):
    return render(request, 'sobre.html')