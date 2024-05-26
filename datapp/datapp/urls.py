"""
URL configuration for datapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import (
    AccountListCreateView, AccountDetailView,
    DestinationListCreateView, DestinationDetailView,
    AccountDestinationsView, IncomingDataView,
    home
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),  # Root path
    path('', AccountListCreateView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('destinations/', DestinationListCreateView.as_view(), name='destination-list'),
    path('destinations/<int:pk>/', DestinationDetailView.as_view(), name='destination-detail'),
    path('accounts/<uuid:account_id>/destinations/', AccountDestinationsView.as_view(), name='account-destinations'),
    path('server/incoming_data/', IncomingDataView.as_view(), name='incoming-data'),
]

