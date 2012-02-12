
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from feelgood.apps.tools.forms.bdc import BDCForm
from feelgood.util.shortcuts import render_response

@login_required
def index(request):

    return render_response(request, 'tools/index.html', {
        
    })

@login_required
def create(request):
     
    if request.method == 'POST':
        form = BDCForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('tools:bdc-view', id=instance.id))
    else:
        form = BDCForm()

    return render_response(request, 'tools/bdc/create.html', {
        'form' : form,
    })
