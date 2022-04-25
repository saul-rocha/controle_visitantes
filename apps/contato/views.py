from django.shortcuts import render
from django.http import HttpResponse


def contato_view(request):
    return render(request, 'Fale_Conosco.html')