
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from feelgood.apps.tools.forms.twocolumn import TwoColumnForm, TwoColumnEntryFormSet
from feelgood.apps.tools.models import TwoColumnEntry,TwoColumn
from feelgood.util.shortcuts import render_response

@login_required
def index(request):

    sheets = TwoColumn.objects.filter(user=request.user).order_by('name')

    return render_response(request, 'tools/twocolumn/index.html', {
        "current_page" : "two_column_sheets",
        'sheets' : sheets,
    })    
    
@login_required
def view(request, id):

    sheet = get_object_or_404(TwoColumn, pk=id, user=request.user)

    if request.method == 'POST':
        formset = TwoColumnEntryFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.sheet = sheet
                instance.save()
            return HttpResponseRedirect(reverse('tools:twocolumn-view',args=[sheet.id]))
    else:
        formset = TwoColumnEntryFormSet(queryset=sheet.entries.all())

    return render_response(request, 'tools/twocolumn/view.html', {
        "current_page" : "two_column_sheets",
        'sheet' : sheet,
        'formset': formset,
    })

@login_required
def create(request):
     
    if request.method == 'POST':
        form = TwoColumnForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('tools:twocolumn-view',args=[instance.id]))
    else:
        form = TwoColumnForm()

    return render_response(request, 'tools/twocolumn/create.html', {
        "current_page" : "two_column_sheets",
        'form' : form,
    })

@login_required
def delete(request, id):

    sheet = get_object_or_404(TwoColumn, pk=id, user=request.user)
    if request.method == 'POST':
        for entry in sheet.entries.all():
            entry.delete()
        sheet.delete()

    return HttpResponseRedirect(reverse('tools:twocolumn-index'))
