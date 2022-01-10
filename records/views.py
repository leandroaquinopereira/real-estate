from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from records.forms import ClientForm, PropertyForm, RentForm
from records.models import Client, Property, Rent


# Property

class PropertyList(ListView):
    queryset = Property.objects.all().order_by('type')
    context_object_name = 'property'
    template_name = 'records/list_properties.html'

    def get_queryset(self):

        txt_type = self.request.GET.get('type')

        if txt_type:
            property = Property.objects.filter(type__icontains=txt_type)
        else:
            property = Property.objects.all()
        return property


class PropertyDetail(DetailView):
    queryset = Property.objects.all()
    context_object_name = 'property'
    template_name = 'records/detail_properties.html'


class PropertyDelete(DeleteView):
    model = Property
    context_object_name = 'property'
    template_name = 'records/delete_properties.html'
    success_url = reverse_lazy('property-list')


class PropertyCreate(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'records/create_properties.html'
    success_url = reverse_lazy('property-list')


class PropertyUpdate(UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = 'records/update_properties.html'
    success_url = reverse_lazy('property-list')


# Client

class ClientList(ListView):
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


class ClientUpdate(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'records/update_clients.html'
    success_url = reverse_lazy('client-list')


# Rent

class RentList(ListView):
    queryset = Rent.objects.all().order_by('id')
    context_object_name = 'rent'
    template_name = 'records/list_rents.html'


class RentDetail(DetailView):
    queryset = Rent.objects.all()
    context_object_name = 'rent'
    template_name = 'records/detail_rents.html'


class RentDelete(DeleteView):
    model = Rent
    context_object_name = 'rent'
    template_name = 'records/delete_rents.html'
    success_url = reverse_lazy('rent-list')


class RentCreate(CreateView):
    model = Rent
    form_class = RentForm
    template_name = 'records/create_rents.html'
    success_url = reverse_lazy('rent-list')


class RentUpdate(UpdateView):
    model = Rent
    form_class = RentForm
    template_name = 'records/update_rents.html'
    success_url = reverse_lazy('rent-list')
