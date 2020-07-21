from django.shortcuts import render, get_object_or_404, reverse,redirect
from django.forms.models import modelformset_factory,formset_factory,inlineformset_factory
from django.utils import timezone
from django.http.response import HttpResponse
from django.http import JsonResponse,HttpResponseRedirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,UpdateView,ListView,CreateView,DeleteView,FormView
from .models import *
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import BodegasForm
# Create your views here.

class Bodegas_ListView(ListView):
    model = Bodegas
    template_name = "bodegas/listaproductos.html"
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Bodegas.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Repuestos'
        context['create_url'] = reverse_lazy('crear_bodega')
        context['list_url'] = reverse_lazy('lista_repuestos')
        context['entity'] = 'REPUESTOS'
        return context


class BodegaCreateView(CreateView):
    model = Bodegas
    form_class=BodegasForm
    template_name = "bodegas/crearbodega.html"
    sucess_url=reverse_lazy('lista_repuestos')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action=request.POST['action']
            if action == 'add':
                form = self.get_form()
                data=form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de Reouestos'
        context['entity'] = 'REPUESTOS'
        context['list_url'] = reverse_lazy('lista_repuestos')
        context['action']='add'
        return context


class BodegaUpdateView(UpdateView):
    model = Bodegas
    form_class = BodegasForm
    template_name = 'bodegas/crearbodega.html'
    success_url = reverse_lazy('lista_repuestos')
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición De Repuesto'
        context['entity'] = 'Repuestos'
        context['list_url'] = reverse_lazy('lista_repuestos')
        context['action'] = 'edit'
        return context


class BodegaDeleteView(DeleteView):
    model = Bodegas
    template_name = 'bodegas/borrarproducto.html'
    success_url = reverse_lazy('lista_repuestos')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Producto'
        context['entity'] = 'REPUESTOS'
        context['list_url'] = reverse_lazy('lista_repuestos')
        return context