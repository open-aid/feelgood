
from django.forms.models import ModelForm
from django.forms.models import modelformset_factory
from feelgood.apps.tools.models import DailyActivityScheduleEntry
from django.utils.translation import ugettext as _


class DailyActivityScheduleEntryForm(ModelForm):
    class Meta:
        model = DailyActivityScheduleEntry
        fields = ('prospective','retrospective')

DailyActivityScheduleEntryFormSet = modelformset_factory(DailyActivityScheduleEntry, exclude=('schedule','start','end',), extra=0)
