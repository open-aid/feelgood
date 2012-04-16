
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from feelgood.apps.tools.forms.nas import NovacoAngerScaleForm
from feelgood.apps.tools.models import NovacoAngerScale
from feelgood.util.shortcuts import render_response

from datetime import datetime

@login_required
def create(request):
     
    if request.method == 'POST':
        form = NovacoAngerScaleForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.timestamp = datetime.now()
            instance.save()
            return HttpResponseRedirect(reverse('tools:nas-view', args=[instance.id]))
    else:
        form = NovacoAngerScaleForm()

    return render_response(request, 'tools/nas/create.html', {
        "current_page" : "anger",
        'form' : form,
    })

@login_required
def index(request):

    nass = NovacoAngerScale.objects.filter(user=request.user).order_by('-timestamp')

    return render_response(request, 'tools/nas/index.html', {
        "current_page" : "anger",
        'nass' : nass,
    })    
    
@login_required
def view(request, id):

    nas = get_object_or_404(NovacoAngerScale, pk=id, user=request.user)

    return render_response(request, 'tools/nas/view.html', {
        "current_page" : "anger",
        'nas' : nas,
    })
    
@login_required
def delete(request, id):

    nas = get_object_or_404(NovacoAngerScale, pk=id, user=request.user)
    if request.method == 'POST':
        nas.delete()

    return HttpResponseRedirect(reverse('tools:nas-index'))
