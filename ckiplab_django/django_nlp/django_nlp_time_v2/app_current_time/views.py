from django.shortcuts import render

# Create your views here.
from datetime import datetime

def home(request):

    dt_now = str(datetime.now())

    return render(request, 'app_current_time/home.html',
    {'current_time' : dt_now})