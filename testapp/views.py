from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hydjobs(request):
    s="<h1>here is your hyderabad jobs information</h1>"
    return HttpResponse(s)
def chennaijobs(request):
    s="<h1>here is your chennai  jobs information</h1>"
    return HttpResponse(s)
def rcrjobs(request):
    s="<h1>here is your raichur jobs information</h1>"
    return HttpResponse(s)