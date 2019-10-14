from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, VistoriaSerializer, LoginSerializer
from relatorios.models import Vistoria

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class VistoriaViewSet(viewsets.ModelViewSet):
	queryset = Vistoria.objects.all()
	serializer_class = VistoriaSerializer

@csrf_exempt
def vistoria_list(request):
	
	if request.method == 'GET':
		vistorias = Vistoria.objects.all()
		serializer = VistoriaSerializer(vistorias, many = True, context = request)
		return JsonResponse(serializer.data, safe = False)
	elif request.method == 'POST':
		vistoria  = JSONParser().parse(request)
		serializer = VistoriaSerializer(data = vistoria)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = 201)
		return JsonResponse(serializer.errors, status = 400)

def LoginViewSet(request):
	user = User.objects.all()
	print(user)
	usuario = LoginSerializer(passWord = user.password)
	return JsonResponse(usuario.data, safe = False)