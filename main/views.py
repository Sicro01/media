from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ClientForm, PlanForm, PhaseForm, StrategyForm
from .models import *
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# messages.warning(request, 'Watch Out!!!')

class Dashboard(ListView):
    model = Client
    template_name = 'main/dashboard.html'
    context_object_name = 'clients'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plans'] = Plan.objects.all()
        context['phases'] = Phase.objects.all()
        context['strategies'] = Strategy.objects.all()
        return context
# Client
class ClientCreate(CreateView):
    template_name = 'main/client_create.html'
    model = Client
    form_class = ClientForm
    context_object_name = 'client'
    success_url= reverse_lazy('main:dashboard')

class ClientDelete(DeleteView):
    template_name = 'main/client_delete.html'
    model = Client
    context_object_name = 'client'
    success_url= reverse_lazy('main:dashboard')

class ClientUpdate(UpdateView):
    template_name = 'main/client_update.html'
    model = Client
    form_class = ClientForm
    context_object_name = 'client'
    success_url= reverse_lazy('main:dashboard')

# Plan
class PlanCreate(CreateView):
    template_name = 'main/plan_create.html'
    model = Plan
    form_class = PlanForm
    context_object_name = 'plan'
    success_url= reverse_lazy('main:dashboard')

class PlanDelete(DeleteView):
    template_name = 'main/plan_delete.html'
    model = Plan
    context_object_name = 'plan'
    success_url= reverse_lazy('main:dashboard')

class PlanUpdate(UpdateView):
    template_name = 'main/plan_update.html'
    model = Plan
    form_class = PlanForm
    context_object_name = 'plan'
    success_url= reverse_lazy('main:dashboard')

# Phase
class PhaseCreate(CreateView):
    template_name = 'main/phase_create.html'
    model = Phase
    form_class = PhaseForm
    context_object_name = 'phase'
    success_url= reverse_lazy('main:dashboard')

class PhaseDelete(DeleteView):
    template_name = 'main/phase_delete.html'
    model = Phase
    context_object_name = 'phase'
    success_url= reverse_lazy('main:dashboard')

class PhaseUpdate(UpdateView):
    template_name = 'main/phase_update.html'
    model = Phase
    form_class = PhaseForm
    context_object_name = 'phase'
    success_url= reverse_lazy('main:dashboard')

# Strategy
class StrategyCreate(CreateView):
    template_name = 'main/strategy_create.html'
    model = Strategy
    form_class = StrategyForm
    context_object_name = 'strategy'
    success_url= reverse_lazy('main:dashboard')

class StrategyDelete(DeleteView):
    template_name = 'main/strategy_delete.html'
    model = Strategy
    context_object_name = 'strategy'
    success_url= reverse_lazy('main:dashboard')

class StrategyUpdate(UpdateView):
    template_name = 'main/strategy_update.html'
    model = Strategy
    form_class = StrategyForm
    context_object_name = 'strategy'
    success_url= reverse_lazy('main:dashboard')



        

