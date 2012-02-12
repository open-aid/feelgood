
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as dj_login, logout as dj_logout, authenticate
from django.http import HttpResponseRedirect

from feelgood.apps.landing.forms import RegistrationForm, LoginForm
from feelgood.util.shortcuts import render_response

def index(request):
    register = RegistrationForm()
    login = LoginForm()

    user = request.user
    print user
    return render_response(request, 'landing/index.html', {
        "registration_form" : register,
        "login_form" : login,
    })


def registration(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], 
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            dj_login(request, user)

            return HttpResponseRedirect(reverse('tools'))
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
            dj_login(request, user)

            return HttpResponseRedirect(reverse('tools:index'))
    else:
        form = LoginForm()

    return render_response(request, 'landing/login.html', {
        "form" : form,
    })

@login_required
def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('landing:index'))
