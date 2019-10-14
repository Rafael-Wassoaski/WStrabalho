from django.conf import settings
from django.db import models
from django.utils import timezone


class Vistoria(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #tem como fazer com choice
    cobrad = models.CharField(max_length=200)
    municipio = models.CharField(max_length=200)
    #tem como fazer com choice

    descricao = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    endereco = models.TextField()

    #latitude e longitude com FloatField ou DecimalField?
    #Danos humanos:

    danos_humanos_desalojados = models.IntegerField(default=0)
    danos_humanos_desabrigados = models.IntegerField(default=0)
    danos_humanos_desaparecidos = models.IntegerField(default=0)
    danos_humanos_feridos = models.IntegerField(default=0)
    danos_humanos_enfermos = models.IntegerField(default=0)
    danos_humanos_mortos = models.IntegerField(default=0)
    danos_humanos_isolados = models.IntegerField(default=0)
    danos_humanos_atingidos = models.IntegerField(default=0)
    danos_humanos_afetados = models.IntegerField(default=0)

    danos_humanos_observacoes = models.TextField()

    #Danos materiais:

    unidades_habitacionais_atingidas = models.IntegerField(default=0)
    unidades_habitacionais_danificads = models.IntegerField(default=0)
    unidades_habitacionais_interditadas = models.IntegerField(default=0)
    unidades_habitacionais_destruidas = models.IntegerField(default=0)
    instalacoes_publicas_saude_atingidas = models.IntegerField(default=0)
    instalacoes_publicas_ensino_atingidas = models.IntegerField(default=0)
    instalacoes_comunitarias_atingidas = models.IntegerField(default=0)
    obras_atingidas = models.IntegerField(default=0)
    interrupcoes_servicos_essenciais = models.IntegerField(default=0)

    danos_materiais_observacoes = models.TextField()

    #Danos ambientais:

    contaminacao_solo = models.IntegerField(default=0)
    contaminacao_agua = models.IntegerField(default=0)
    contaminacao_ar = models.IntegerField(default=0)

    danos_ambientais_observacoes = models.TextField()

    #Danos econômicos:

    danos_agricultura = models.IntegerField(default=0)
    danos_pecuaria = models.IntegerField(default=0)
    danos_industria = models.IntegerField(default=0)
    danos_comercio = models.IntegerField(default=0)
    danos_prestacao_de_servicos = models.IntegerField(default=0)

    danos_economicos_observacoes = models.TextField()

    #IAH

    iah_cestas_de_alimentos = models.IntegerField(default=0)
    iah_agua_potavel = models.IntegerField(default=0)
    iah_colchoes = models.IntegerField(default=0)
    iah_kit_higiene_pessoal = models.IntegerField(default=0)
    iah_kit_limpeza = models.IntegerField(default=0)
    iah_telhas = models.IntegerField(default=0)
    iah_lona_plastica = models.IntegerField(default=0)
    iah_outros = models.IntegerField(default=0)

    iah_fornecidos_outros_observacoes = models.TextField()
    iah_vias_publicas_totalmente_desobistruidas = models.BooleanField(default=False)
    iah_reestabelecimento_servicos_essenciais = models.BooleanField(default=False)

    def publish(self):
        self.save()

