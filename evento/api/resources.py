from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields, utils
from evento.models import *
from django.contrib.auth.models import User


class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        filtering = {
            "descricao": ('exact', 'startswith')
        }
        authorization= Authorization()


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']


class PessoaFisicaResource(ModelResource):
    class Meta:
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class EventoResource(ModelResource):
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class EventoCientificoResource(ModelResource):
    class Meta:
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class PessoaJuridicaResource(ModelResource):
    class Meta:
        queryset = PessoaJuridica.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class ArtigoCientificoResource(ModelResource):
    evento = fields.ToOneField(EventoCientificoResource , 'evento')
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class ArtigoAutorResource(ModelResource):
    artigoCientifico = fields.ToOneField(ArtigoCientificoResource, 'artigoCientifico')
    autor = fields.ToOneField(AutorResource, 'autor')
    class Meta:
        queryset = ArtigoAutor.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class InscricaoResource(ModelResource):
    pessoa = fields.ToOneField(PessoaFisicaResource, 'pessoa')
    evento = fields.ToOneField(Evento, 'evento')
    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }
