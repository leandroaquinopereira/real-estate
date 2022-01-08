from django.contrib.auth.decorators import login_required
from django.urls import include, path

from records.views import ClientList, ClientDetail, ClientDelete, ClientCreate, ClientUpdate

urlpatterns = [
    path('', ClientList.as_view(), name='client-list'),
    path('detail/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
    path('delete/<int:pk>/', login_required(ClientDelete.as_view()), name='client-delete'),
    path('create/', login_required(ClientCreate.as_view()), name='client-create'),
    path('update/<int:pk>/', login_required(ClientUpdate.as_view()), name='client-update')
]
