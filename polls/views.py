from django.shortcuts import render
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     template = loader.get_template('polls/index.html')
#     return HttpResponse("Hello, world. You're at the polls index.")
#
@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")

from django.template.context_processors import csrf

from polls.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


@csrf_protect
def register(request, template_name="register.html"):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = c['RegistrationForm'] = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],

            )
            return HttpResponseRedirect('/success/')
    else:
        form = c['RegistrationForm'] = RegistrationForm()

    # return render_to_response(template_name, {'form': c['RegistrationForm']} ,  RequestContext(request))
    return render(request,template_name, {'form':c['RegistrationForm']}, c)


# def register_success(request):
#     return render_to_response(
#         'success.html',
#     )
def register_success(request):
    return render(request,"home.html")


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


# @login_required
# def home(request):
#     return render_to_response(
#         'home.html',
#         {'user': request.user}
#     )