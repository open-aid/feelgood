
from form_utils import forms
from feelgood.apps.counters.models import Counter
from django.utils.translation import ugettext as _

class CounterForm(forms.BetterModelForm):
    class Meta:
        model = Counter
        fieldsets = (('counter_info', {
                          'fields': ('name','daily_reset',),
                          'legend': _("Counter information"),}),)
