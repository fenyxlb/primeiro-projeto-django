from django.db.models import F
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Pergunta, Escolha
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

def index(request):
    ultimas_perguntas = Pergunta.objects.order_by('-data_publicacao')[:5]
    template = loader.get_template('enquetes/index.html')
    contexto = {
        'ultimas_perguntas': ultimas_perguntas
    }
    return HttpResponse(template.render(contexto, request))

def detalhes(request, pergunta_id):
    try:
        pergunta = Pergunta.objects.get(pk=pergunta_id)
    except:
        raise Http404("A pergunta não existe!")
    return render(request, 'enquetes/detalhes.html', {'pergunta': pergunta})

def resultados(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, "enquetes/resultados.html", {"pergunta": pergunta})

def votos(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        escolha_selecionada = pergunta.escolha_set.get(pk=request.POST["escolha"])
    except (KeyError, Escolha.DoesNotExist):
        return render(
            request,
            "enquetes/detalhes.html",
            {
                "question": pergunta,
                "error_message": "Você não selecionou uma escolha.",
            },
        )
    else:
        escolha_selecionada.votos = F("votos") + 1
        escolha_selecionada.save()
        return HttpResponseRedirect(reverse("enquetes:resultados", args=(pergunta.id,)))