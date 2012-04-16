
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from feelgood.apps.tools.forms.das import DailyActivityScheduleEntryFormSet
from feelgood.apps.tools.models import DailyActivitySchedule
from feelgood.util.shortcuts import render_response
from feelgood.util.dates import daterange
from django.utils.translation import ugettext as _


from datetime import date, timedelta


@login_required
def index(request):

    schedules = DailyActivitySchedule.objects.filter(user=request.user).order_by('-date')

    dates = daterange(date.today(),-1,4)

    return render_response(request, 'tools/das/index.html', {
        'schedules' : schedules,
        'dates'     : dates,
    }) 

@login_required
def create(request):
     
    if request.method == 'POST':
        form = DailyActivityScheduleEntryFormSet(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('tools:das-view', args=[instance.id]))
    else:
        form = DailyActivityScheduleEntryFormSet(queryset=Author.objects.none())

    return HttpResponseRedirect(reverse('tools:das-view', args=[instance.id]))  
    
@login_required
def view(request, year, month, day):

    schedule_date = date(int(year),int(month),int(day))
    das, created = DailyActivitySchedule.objects.get_or_create(user=request.user, date=schedule_date)

    if created:
        das.create_entries()

    if request.method == 'POST':
        formset = DailyActivityScheduleEntryFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.schedule = das
                instance.save()
            return HttpResponseRedirect(reverse('tools:das-view', args=[year,month,day]))
    else:
        formset = DailyActivityScheduleEntryFormSet(queryset=das.entries.all().order_by('start'))

    return render_response(request, 'tools/das/view.html', {
        'das' : das,
        'formset' : formset,
    })
    
@login_required
def delete(request, id):

    das = get_object_or_404(DailyActivitySchedule, pk=id, user=request.user)
    if request.method == 'POST':
        for entry in das.entries.all():
            entry.delete()
        das.delete()

    return HttpResponseRedirect(reverse('tools:das-index'))
