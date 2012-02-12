
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from feelgood.apps.tools.forms.triplecolumn import TripleColumnEntryForm
from feelgood.apps.tools.models import TripleColumnEntry,TripleColumn
from feelgood.util.shortcuts import render_response

@login_required
def create(request):
     
    if request.method == 'POST':
        form = TripleColumnEntryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            triplecolumn, created = TripleColumn.objects.get_or_create(user=request.user)
            instance.triplecolumn = triplecolumn
            instance.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('tools:triplecolumn-index'))
    else:
        form = TripleColumnEntryForm()

    return render_response(request, 'tools/triplecolumn/create.html', {
        'form' : form,
    })

@login_required
def index(request):

    entries = TripleColumnEntry.objects.filter(triplecolumn__user=request.user).order_by('-timestamp')
    form = TripleColumnEntryForm()

    return render_response(request, 'tools/triplecolumn/index.html', {
        'entries' : entries,
        'form'    : form,
    })    
    
@login_required
def view(request, id):

    entry = get_object_or_404(TripleColumnEntry, pk=id, triplecolumn__user=request.user)

    return render_response(request, 'tools/triplecolumn/view.html', {
        'entry' : entry,
    })
    
@login_required
def delete(request, id):

    entry = get_object_or_404(TripleColumnEntry, pk=id, triplecolumn__user=request.user)
    if request.method == 'POST':
        entry.delete()

    return HttpResponseRedirect(reverse('tools:triplecolumn-index'))
