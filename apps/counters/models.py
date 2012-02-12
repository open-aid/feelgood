
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from datetime import datetime

class Counter(models.Model):
    
    user = models.ForeignKey(User, related_name='counters')

    name = models.CharField(_('Name'), max_length=140)
    count = models.IntegerField(_('Count'), default=0,max_length=10)

    daily_reset = models.BooleanField(_('Reset daily'), default=True)

    last_update = models.DateTimeField()

    def increment_and_save(self):
        self.last_update = datetime.now()
        self.count = self.count + 1
        self.save()

    def reset_and_save(self):
        self.count = 0
        self.save()

    def __unicode__(self):
        return self.name

class CounterDataPoint(models.Model):
    
    counter = models.ForeignKey(Counter)

    timestamp = models.DateTimeField()

    value = models.IntegerField(_('Value'), max_length=10)
