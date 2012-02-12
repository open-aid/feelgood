
from form_utils import forms
from django.forms.models import modelformset_factory
from feelgood.apps.tools.models import AntiProcrastinationSheetEntry
from django.utils.translation import ugettext as _

class AntiProcrastinationSheetEntryForm(forms.BetterModelForm):
    class Meta:
        model = AntiProcrastinationSheetEntry
        fields = ('activity',
                  'predicted_difficulty','predicted_satisfaction',
                  'actual_difficulty','actual_satisfaction',)



AntiProcrastinationSheetEntryFormSet = modelformset_factory(AntiProcrastinationSheetEntry, 
    exclude=('sheet',), extra=1, can_delete=True)
