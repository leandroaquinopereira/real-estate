from django.contrib.auth.decorators import login_required
from django.urls import include, path

from records.views import ClientList, ClientDetail, ClientDelete, ClientCreate, ClientUpdate, PropertyList, \
    PropertyDetail, PropertyDelete, PropertyCreate, PropertyUpdate

urlpatterns = [
    path('client/', ClientList.as_view(), name='client-list'),
    path('client/detail/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
    path('client/delete/<int:pk>/', login_required(ClientDelete.as_view()), name='client-delete'),
    path('client/create/', login_required(ClientCreate.as_view()), name='client-create'),
    path('client/update/<int:pk>/', login_required(ClientUpdate.as_view()), name='client-update'),

    path('property/', PropertyList.as_view(), name='property-list'),
    path('property/detail/<int:pk>/', PropertyDetail.as_view(), name='property-detail'),
    path('property/delete/<int:pk>/', login_required(PropertyDelete.as_view()), name='property-delete'),
    path('property/create/', login_required(PropertyCreate.as_view()), name='property-create'),
    path('property/update/<int:pk>/', login_required(PropertyUpdate.as_view()), name='property-update')
]
