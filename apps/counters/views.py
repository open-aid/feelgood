
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from feelgood.apps.counters.forms import CounterForm
from feelgood.apps.counters.models import Counter
from feelgood.util.shortcuts import render_response

from datetime import datetime

@login_required
def create(request):
     
    if request.method == 'POST':
        form = CounterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.last_update = datetime.now()
            instance.save()
            return HttpResponseRedirect(reverse('counters:view', args=[instance.id]))
    else:
        form = CounterForm()

    return render_response(request, 'counters/create.html', {
        'form' : form,
    })

@login_required
def index(request):

    counters = Counter.objects.filter(user=request.user).order_by('name')

    return render_response(request, 'counters/index.html', {
        'counters' : counters,
    })    
    
@login_required
def view(request, id):

    counter = get_object_or_404(Counter, pk=id, user=request.user)

    return render_response(request, 'counters/view.html', {
        'counter' : counter,
    })
    
@login_required
def delete(request, id):

    counter = get_object_or_404(Counter, pk=id, user=request.user)
    if request.method == 'POST':
        counter.delete()

    return HttpResponseRedirect(reverse('counters:index'))

@login_required
def count(request, id):

    counter = get_object_or_404(Counter, pk=id, user=request.user)
    if request.method == 'POST':
        counter.increment_and_save()

    return HttpResponseRedirect(reverse('counters:view',args=[counter.id]))

@login_required
def reset(request, id):

    counter = get_object_or_404(Counter, pk=id, user=request.user)
    if request.method == 'POST':
        counter.reset_and_save()

    return HttpResponseRedirect(reverse('counters:view',args=[counter.id]))
