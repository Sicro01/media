from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ClientForm, PlanForm, PhaseForm, StrategyForm
from .models import *

# messages.warning(request, 'Watch Out!!!')

def homepage(request):

    clients = Client.objects.all()
    plans = Plan.objects.all()
    phases = Phase.objects.all()
    strategies = Strategy.objects.all()

    context = {'clients': clients,
        'plans': plans,
        'phases': phases,
        'strategies': strategies
        }

    return render(request, 'main/dashboard.html', context)

def deleteClient(request, pk):

    client = Client.objects.get(id=pk)

    if request.method == 'POST':
        client.delete()
        return redirect('/')

    context = {'item': client}
    
    return render(request, 'main/delete_form.html', context)

def createClient(request):

    client_form = ClientForm()
    plan_form = PlanForm()
    phase_form = PhaseForm()
    strategy_form = StrategyForm()

    if request.method == 'POST':
        client_form = ClientForm(request.POST, instance=Client())
        plan_form = PlanForm(request.POST, instance=Plan())
        phase_form = PhaseForm(request.POST, instance=Phase())
        strategy_form = StrategyForm(request.POST, instance=Strategy())

        if client_form.is_valid() and plan_form.is_valid():
            _client = client_form.save()
            _plan = plan_form.save(commit=False)
            _phase = phase_form.save(commit=False)
            _strategy = strategy_form.save(commit=False)
            _plan.client = _client
            _plan.save()
            _phase.plan = _plan
            _phase.save()
            _strategy.phase = _phase
            _strategy.save()

        return redirect('/')

    context = {
        'client_form': client_form,
        'plan_form': plan_form,
        'phase_form': phase_form,
        'strategy_form': strategy_form,
        }
    return render(request, 'main/client_form.html', context)

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

        

