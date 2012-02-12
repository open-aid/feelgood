
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from feelgood.apps.tools.forms.bdc import BDCForm
from feelgood.apps.tools.models import BDC
from feelgood.util.shortcuts import render_response

from datetime import datetime

@login_required
def create(request):
     
    if request.method == 'POST':
        form = BDCForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.timestamp = datetime.now()
            instance.save()
            return HttpResponseRedirect(reverse('tools:bdc-view', args=[instance.id]))
    else:
        form = BDCForm()

    return render_response(request, 'tools/bdc/create.html', {
        'form' : form,
    })

@login_required
def index(request):

    bdcs = BDC.objects.filter(user=request.user).order_by('-timestamp')

    return render_response(request, 'tools/bdc/index.html', {
        'bdcs' : bdcs,
    })    
    
@login_required
def view(request, id):

    bdc = get_object_or_404(BDC, pk=id, user=request.user)

    return render_response(request, 'tools/bdc/view.html', {
        'bdc' : bdc,
    })
    
@login_required
def delete(request, id):

    bdc = get_object_or_404(BDC, pk=id, user=request.user)
    if request.method == 'POST':
        bdc.delete()

    return HttpResponseRedirect(reverse('tools:bdc-index'))
