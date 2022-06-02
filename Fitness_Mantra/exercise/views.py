from django.http import HttpResponse
from django.shortcuts import render
from .models import Exercise
# Create your views here.
def index(req):
    #testing home pagez
    return HttpResponse("<h2>Welcome to myFitness Mantra App<h2>")

def exercise(req):
    pass
    # write code of get post put delete here