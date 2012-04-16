
from form_utils import forms
from django.forms.formsets import formset_factory
from feelgood.apps.tools.models import TripleColumnEntry
from django.utils.translation import ugettext as _

class TripleColumnEntryForm(forms.BetterModelForm):
    class Meta:
        model = TripleColumnEntry
        fields = ('automatic_thought','cognitive_distortions','rational_response')

TripleColumnEntryFormset = formset_factory(TripleColumnEntryForm, extra=2)
