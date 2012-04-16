
from form_utils import forms
from feelgood.apps.tools.models import NovacoAngerScale
from django.utils.translation import ugettext as _

class NovacoAngerScaleForm(forms.BetterModelForm):
    class Meta:
        model = NovacoAngerScale
        fieldsets = (('statements', {
                          'fields': NovacoAngerScale.STATEMENT_FIELDS,
                          'legend': _("Statements"),}),)
