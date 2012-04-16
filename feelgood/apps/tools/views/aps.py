
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from feelgood.apps.tools.forms.aps import AntiProcrastinationSheetEntryFormSet
from feelgood.apps.tools.models import AntiProcrastinationSheetEntry,AntiProcrastinationSheet
from feelgood.util.shortcuts import render_response
from feelgood.util.dates import daterange

from datetime import date

@login_required
def index(request):

    sheets = AntiProcrastinationSheet.objects.filter(user=request.user).order_by('-date')
    dates = daterange(date.today(),-1,4)
    return render_response(request, 'tools/aps/index.html', {
        'sheets' : sheets,
        'dates'  : dates,
    })    
    
@login_required
def view(request, year, month, day):

    sheet, created = AntiProcrastinationSheet.objects.get_or_create(user=request.user, date=date(year=int(year), month=int(month), day=int(day)))

    if request.method == 'POST':
        formset = AntiProcrastinationSheetEntryFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.sheet = sheet
                instance.save()
            return HttpResponseRedirect(reverse('tools:aps-view', args=[year,month,day]))
    else:
        formset = AntiProcrastinationSheetEntryFormSet(queryset=sheet.entries.all())

    return render_response(request, 'tools/aps/view.html', {
        'sheet'   : sheet,
        'formset' : formset,
    })
    
@login_required
def delete(request, year, month, day):

    sheet = get_object_or_404(AntiProcrastinationSheet, user=request.user, date=date(year=int(year), month=int(month), day=int(day)))

    if request.method == 'POST':
        for entry in sheet.entries.all():
            entry.delete()
        sheet.delete()

    return HttpResponseRedirect(reverse('tools:aps-index'))

@login_required
def delete_entry(request, id):

    entry = get_object_or_404(AntiProcrastinationSheetEntry, user=request.user, pk=id)
    date = entry.sheet.date

    if request.method == 'POST':
        entry.delete()

    return HttpResponseRedirect(reverse('tools:aps-view', args=[date.year,date.month,date.day]))
