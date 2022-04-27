from django.shortcuts import render
from django.http import HttpResponse


def ajuda_view(request):
    return render(request, 'ajuda.html')