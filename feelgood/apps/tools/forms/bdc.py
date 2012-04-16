
from form_utils import forms
from feelgood.apps.tools.models import BDC
from django.utils.translation import ugettext as _

class BDCForm(forms.BetterModelForm):
    class Meta:
        model = BDC
        fieldsets = (('thoughts_and_feelings', {
                          'fields': ('q_1', 'q_2', 'q_3', 'q_4', 'q_5',
                                     'q_6', 'q_7', 'q_8', 'q_9', 'q_10',),
                          'legend': _("Thoughts and feelings"),}),
                     ('activities_and_relationships', {
                          'fields': ('q_11','q_12','q_13','q_14','q_15',
                                     'q_16','q_17',),
                          'legend': _("Activities and personal relationships"),}),
                     ('physical_symptoms', {
                          'fields': ('q_18','q_19','q_20','q_21','q_22',),
                          'legend': _("Physical symptoms"),}),
                     ('suicidal_urges', {
                          'fields': ('q_23','q_24','q_25',),
                          'legend': _("Suicidal urges"),}),)
