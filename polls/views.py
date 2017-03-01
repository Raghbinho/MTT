from django.shortcuts import render
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     template = loader.get_template('polls/index.html')
#     return HttpResponse("Hello, world. You're at the polls index.")

@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")
