from __future__ import division
from django.shortcuts import render, redirect
import json as simplejson
from subprocess import Popen, PIPE, STDOUT
import random

def home_view(request):
    msg = ""
    return render(request, 'home.html')