
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Count

from feelgood.apps.tools.models import TripleColumnEntry, BDC

from feelgood.util.shortcuts import render_response

@login_required
def index(request):

    distortion_statistics = TripleColumnEntry.objects.filter(triplecolumn__user=request.user).distortion_statistics()
    bdcs = BDC.objects.filter(user=request.user).order_by('timestamp')

    return render_response(request, 'statistics/index.html', {
        'distortion_statistics' : distortion_statistics,
        'bdcs' : bdcs,
    })
