from .forms import ContatoForm
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.contrib import messages

def contato_view(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(
                request,
                "Sua mensagem foi enviada, obrigado!"
            )

            return redirect("index")

    form = ContatoForm()
    context ={'form': form}
    return render(request, 'Fale_Conosco.html', context)