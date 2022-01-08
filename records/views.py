from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from records.forms import ClientForm
from records.models import Client


class BaseListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'INATEL'
        return context


class ClientList(BaseListView):
    queryset = Client.objects.all().order_by('name')
    context_object_name = 'client'
    template_name = 'records/list_clients.html'


class ClientDetail(DetailView):
    queryset = Client.objects.all()
    context_object_name = 'client'
    template_name = 'records/detail_clients.html'


class ClientDelete(DeleteView):
    model = Client
    context_object_name = 'client'
    template_name = 'records/delete_clients.html'
    success_url = reverse_lazy('client-list')


class ClientCreate(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'records/create_clients.html'
    success_url = reverse_lazy('client-list')


class ClientUpdate(UpdateView, SuccessMessageMixin):
    model = Client
    form_class = ClientForm
    template_name = 'records/update_clients.html'
    success_url = reverse_lazy('client-list')
    success_message = '!Cadastro Atualizado com Sucesso!'
