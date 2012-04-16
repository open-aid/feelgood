
from form_utils import forms
from django.forms.models import modelformset_factory
from feelgood.apps.tools.models import TwoColumn, TwoColumnEntry
from django.utils.translation import ugettext as _

class TwoColumnForm(forms.BetterModelForm):
    class Meta:
        model = TwoColumn
        fields = ('name','column_one_title','column_two_title',)

TwoColumnEntryFormSet = modelformset_factory(TwoColumnEntry, exclude=('sheet','timestamp',), extra=2, can_delete=True)
