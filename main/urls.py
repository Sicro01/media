"""media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('client_create/', views.ClientCreate.as_view(), name='client_create'),
    path('client_update/<str:pk>/', views.ClientUpdate.as_view(), name='client_update'),
    path('client_delete/<str:pk>/', views.ClientDelete.as_view(), name='client_delete'),

    path('plan_create/', views.PlanCreate.as_view(), name='plan_create'),
    path('plan_update/<str:pk>/', views.PlanUpdate.as_view(), name='plan_update'),
    path('plan_delete/<str:pk>/', views.PlanDelete.as_view(), name='plan_delete'),

    path('phase_create/', views.PhaseCreate.as_view(), name='phase_create'),
    path('phase_update/<str:pk>/', views.PhaseUpdate.as_view(), name='phase_update'),
    path('phase_delete/<str:pk>/', views.PhaseDelete.as_view(), name='phase_delete'),

    path('strategy_create/', views.StrategyCreate.as_view(), name='strategy_create'),
    path('strategy_update/<str:pk>/', views.StrategyUpdate.as_view(), name='strategy_update'),
    path('strategy_delete/<str:pk>/', views.StrategyDelete.as_view(), name='strategy_delete'),

    path('country_create/', views.CountryCreate.as_view(), name='country_create'),
    path('country_update/<str:pk>/', views.CountryUpdate.as_view(), name='country_update'),
    path('country_delete/<str:pk>/', views.CountryDelete.as_view(), name='country_delete'),

    path('channel_create/', views.ChannelCreate.as_view(), name='channel_create'),
    path('channel_update/<str:pk>/', views.ChannelUpdate.as_view(), name='channel_update'),
    path('channel_delete/<str:pk>/', views.ChannelDelete.as_view(), name='channel_delete'),

    path('ad_create/', views.AdCreate.as_view(), name='ad_create'),
    path('ad_update/<str:pk>/', views.AdUpdate.as_view(), name='ad_update'),
    path('ad_delete/<str:pk>/', views.AdDelete.as_view(), name='ad_delete'),

    path('targetcountry_create/', views.TargetCountryCreate.as_view(), name='targetcountry_create'),
    path('targetcountry_update/<str:pk>/', views.TargetCountryUpdate.as_view(), name='targetcountry_update'),
    path('targetcountry_delete/<str:pk>/', views.TargetCountryDelete.as_view(), name='targetcountry_delete'),

    path('targetchannel_create/', views.TargetChannelCreate.as_view(), name='targetchannel_create'),
    path('targetchannel_update/<str:pk>/', views.TargetChannelUpdate.as_view(), name='targetchannel_update'),
    path('targetchannel_delete/<str:pk>/', views.TargetChannelDelete.as_view(), name='targetchannel_delete'),

]
