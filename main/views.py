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

class ClientCreate(CreateView):
    template_name = 'main/client_create.html'
    model = Client
    form_class = ClientForm
    context_object_name = 'client'
    success_url= reverse_lazy('main:dashboard')

    def get_form_kwargs(self):
        """ inject the extra data """
        kwargs = super().get_form_kwargs()
        return kwargs 

class ClientDelete(DeleteView):
    template_name = 'main/client_delete.html'
    model = Client
    context_object_name = 'client'
    success_url= reverse_lazy('main:dashboard')

class ClientUpdate(UpdateView):
    template_name = 'main/client_update.html'
    model = Client
    context_object_name = 'client'
    fields = [
        'client_name'
    ]
    success_url= reverse_lazy('main:dashboard')

class PlanCreate(CreateView):
    template_name = 'main/plan_create.html'
    model = Plan
    context_object_name = 'plan'
    fields = [
        'plan_name',
        'client'
    ]
    success_url= reverse_lazy('main:dashboard')

def createPlan(request):

    form = PlanForm()

    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/plan_form.html', context)

def createPhase(request):

    form = PhaseForm()

    if request.method == 'POST':
        form = PhaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/phase_form.html', context)

def createStrategy(request):

    form = StrategyForm()

    if request.method == 'POST':
        form = StrategyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/strategy_form.html', context)

def createPlan(request):

    form = PlanForm()

    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/plan_form.html', context)

def deletePlan(request, pk):

    plan = Plan.objects.get(id=pk)

    if request.method == 'POST':
        plan.delete()
        return redirect('/')
        
    context = {'item': plan}
    
    return render(request, 'main/delete_form.html', context)

        

