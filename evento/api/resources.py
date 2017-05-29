from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields, utils
from evento.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from tastypie.exceptions import Unauthorized
class TipoInscricaoResource(ModelResource):
    def obj_create(self, bundle, **kwargs):
        if not(TipoInscricao.objects.filter(descricao = bundle.data['descricao'].upper())):
            tipo = TipoInscricao()
            tipo.descricao = bundle.data['descricao'].upper()
            tipo.save()
            bundle.obj = tipo
            return bundle
        else:
            raise Unauthorized('Já existe tipo com esse nome')
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized("Não é possivel apagar toda a lista! ")

    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
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
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }
class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }
class EventoResource(ModelResource):

    realizador = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods =['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class EventoCientificoResource(ModelResource):
    class Meta:
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }



class PessoaJuridicaResource(ModelResource):
    class Meta:
        queryset = PessoaJuridica.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class ArtigoCientificoResource(ModelResource):
    evento = fields.ToOneField(EventoCientificoResource , 'evento')
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class ArtigoAutorResource(ModelResource):
    artigoCientifico = fields.ToOneField(ArtigoCientificoResource, 'artigoCientifico')
    autor = fields.ToOneField(AutorResource, 'autor')
    class Meta:
        queryset = ArtigoAutor.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class InscricaoResource(ModelResource):
    def obj_create(self, bundle, **kwargs):
        x = bundle.data['pessoa'].split("/")
        e = bundle.data['evento'].split("/")

        if not(Inscricoes.objects.filter(pessoa = x[4], evento = e[4]):
            e = bundle.data['evento'].split("/")
            t = bundle.data['tipo'].split("/")

            inscricao = Inscricoes()

            inscricao.pessoa = PessoaFisica.objects.get(pk = int(x[4]) )
            inscricao.evento = Evento.objects.get(pk = int(e[4]) )
            inscricao.tipoInscricao = TipoInscricao.objects.get(pk = int(t[4]) )

            inscricao.dataEHoraDaInscricao = bundle.data["dataEHoraDaInscricao"]
            inscricao.save()
            bundle.obj = inscricao
            return bundle
        else:
            raise Unauthorized("Pessoa ja cadastrada no evento!")

    evento = fields.ToOneField(EventoResource, 'evento')
    pessoa = fields.ToOneField(PessoaFisicaResource, 'pessoa')
    tipoInscricao = fields.ToOneField(TipoInscricaoResource, 'tipoInscricao')
    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
	    	"descricao": ('exact', 'startswith')
            }
