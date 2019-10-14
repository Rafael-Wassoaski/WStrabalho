from django.contrib.auth.models import User, Group
from rest_framework import serializers
from relatorios.models import Vistoria

from django.conf import settings
from django.utils import timezone


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class LoginSerializer(serializers.Serializer):
	#email = serializers.EmailField(max_length=None, min_length=None)
	passWord = serializers.CharField()





class VistoriaSerializer(serializers.Serializer):
	
	autor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

	#tem como fazer com choice
	cobrad = serializers.CharField(max_length=200)
	municipio = serializers.CharField(max_length=200)
	#tem como fazer com choice

	descricao = serializers.CharField(max_length=None, min_length=None)
	data = serializers.DateTimeField(default=timezone.now)
	endereco = serializers.CharField(max_length=None, min_length=None)

	#latitude e longitude com FloatField ou DecimalField?
	#Danos humanos:

	danos_humanos_desalojados = serializers.IntegerField(default=0)
	danos_humanos_desabrigados = serializers.IntegerField(default=0)
	danos_humanos_desaparecidos = serializers.IntegerField(default=0)
	danos_humanos_feridos = serializers.IntegerField(default=0)
	danos_humanos_enfermos = serializers.IntegerField(default=0)
	danos_humanos_mortos = serializers.IntegerField(default=0)
	danos_humanos_isolados = serializers.IntegerField(default=0)
	danos_humanos_atingidos = serializers.IntegerField(default=0)
	danos_humanos_afetados = serializers.IntegerField(default=0)

	danos_humanos_observacoes = serializers.CharField(max_length=None, min_length=None)

	#Danos materiais:

	unidades_habitacionais_atingidas = serializers.IntegerField(default=0)
	unidades_habitacionais_danificads = serializers.IntegerField(default=0)
	unidades_habitacionais_interditadas = serializers.IntegerField(default=0)
	unidades_habitacionais_destruidas = serializers.IntegerField(default=0)
	instalacoes_publicas_saude_atingidas = serializers.IntegerField(default=0)
	instalacoes_publicas_ensino_atingidas = serializers.IntegerField(default=0)
	instalacoes_comunitarias_atingidas = serializers.IntegerField(default=0)
	obras_atingidas = serializers.IntegerField(default=0)
	interrupcoes_servicos_essenciais = serializers.IntegerField(default=0)

	danos_materiais_observacoes = serializers.CharField(max_length=None, min_length=None)

	#Danos ambientais:

	contaminacao_solo = serializers.IntegerField(default=0)
	contaminacao_agua = serializers.IntegerField(default=0)
	contaminacao_ar = serializers.IntegerField(default=0)

	danos_ambientais_observacoes = serializers.CharField(max_length=None, min_length=None)

	#Danos econômicos:

	danos_agricultura = serializers.IntegerField(default=0)
	danos_pecuaria = serializers.IntegerField(default=0)
	danos_industria = serializers.IntegerField(default=0)
	danos_comercio = serializers.IntegerField(default=0)
	danos_prestacao_de_servicos = serializers.IntegerField(default=0)

	danos_economicos_observacoes = serializers.CharField(max_length=None, min_length=None)

	#IAH

	iah_cestas_de_alimentos = serializers.IntegerField(default=0)
	iah_agua_potavel = serializers.IntegerField(default=0)
	iah_colchoes = serializers.IntegerField(default=0)
	iah_kit_higiene_pessoal = serializers.IntegerField(default=0)
	iah_kit_limpeza = serializers.IntegerField(default=0)
	iah_telhas = serializers.IntegerField(default=0)
	iah_lona_plastica = serializers.IntegerField(default=0)
	iah_outros = serializers.IntegerField(default=0)

	iah_fornecidos_outros_observacoes = serializers.CharField(max_length=None, min_length=None)
	iah_vias_publicas_totalmente_desobistruidas = serializers.BooleanField(default=False)
	iah_reestabelecimento_servicos_essenciais = serializers.BooleanField(default=False)

	def create(self, validated_data):
		return Vistoria.objects.create(**validated_data)

