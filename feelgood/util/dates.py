
from django.utils.translation import ugettext as _
from datetime import timedelta

def daterange(basedate,start,stop):

    ds = []    
    for day_offset in range(start,stop):
        note = None
        if day_offset is -1:
            note = _("yesterday")
        if day_offset is 0:
            note = _("today")
        if day_offset is 1:
            note = _("tomorrow")
        ds.append((basedate + timedelta(days=day_offset), note))

    return ds
