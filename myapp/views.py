from dbus.decorators import method
from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
import random

from sqlalchemy.sql.functions import current_date

from .models import userForm
# Create your views here.

quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Do not wait to strike till the iron is hot; but make it hot by striking.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "The best way to predict the future is to create it.",
    "You miss 100% of the shots you don’t take."
]

def index(request):
    time = datetime.now()
    quote = random.choice(quotes)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user = userForm(name=name, email=email)
        user.save()
    return render(request, 'index.html', {'quote': quote,'time': time})

def submission(request):
    users = userForm.objects.all()
    return render(request, 'submission.html', {'users':users})