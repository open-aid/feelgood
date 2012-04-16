
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as dj_login, logout as dj_logout, authenticate
from django.http import HttpResponseRedirect
from django import forms

from django.utils.translation import ugettext as _

from feelgood.apps.landing.forms import RegistrationForm, LoginForm
from feelgood.util.shortcuts import render_response

from feelgood.apps.tools.models import BDC, NovacoAngerScale

def index(request):
    register = RegistrationForm()
    login = LoginForm()

    if request.user.is_authenticated():
        bdcs = BDC.objects.filter(user=request.user).order_by('-timestamp')[:50]
        nass = NovacoAngerScale.objects.filter(user=request.user).order_by('-timestamp')[:50]
        
        return render_response(request, 'landing/dashboard.html', {
            "current_page" : "dashboard",
            "bdcs"         : bdcs,
            "nass"         : nass,
        })

    return render_response(request, 'landing/index.html', {
        "current_page" : "dashboard",
        "registration_form" : register,
        "login_form" : login,
    })


def registration(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(form.cleaned_data['username'], 
                                     form.cleaned_data['email'],
                                     form.cleaned_data['password'])
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            dj_login(request, user)

            return HttpResponseRedirect(reverse('landing:index'))
    else:
        form = RegistrationForm()

    return render_response(request, 'landing/registration.html', {
        "form" : form,
    })


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    dj_login(request, user)
                    return HttpResponseRedirect(reverse('landing:index'))
                else:
                    error = _("This account has been disabled.")
            else: 
                error = _("Invalid username and/or password.")
            
            errors = form._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.util.ErrorList())
            errors.append(error)
    else:
        form = LoginForm()

    return render_response(request, 'landing/login.html', {
        "form" : form,
    })

@login_required
def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('landing:index'))
