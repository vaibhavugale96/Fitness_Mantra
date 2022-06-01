from django.http import HttpResponse
from django.shortcuts import render
from .models import Fitness
# Create your views here.
def index(req):
    #testing home page
    return HttpResponse("<h2>Welcome to Fitness Mantra App<h2>")

def fitness(req):
    pass
    # write code of get post put delete here