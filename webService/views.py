from django.shortcuts import render
import random
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from relatorios.models import Vistoria

# Create your views here.

@csrf_exempt
def sorteio(request):
	limitValue = request.POST.get('value', False)
	data = {'value':random.randint(0, int(limitValue))}
	return JsonResponse(data)

@csrf_exempt
def porcentagem(request):
	porcentagemBusca = int(request.POST.get('busca', False))
	valorTotal = int(request.POST.get('total', False))
	resultado = (valorTotal*porcentagemBusca)/100
	data = {'result':resultado}
	return JsonResponse(data)

@csrf_exempt
def getVistoriaMaisRescente(request):

	vistoria = Vistoria.objects.latest('pk')
	data = serializers.serialize("json", [vistoria, ])
	return JsonResponse(data, safe = False)

