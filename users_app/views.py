from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    context = {
        'all_users': User.objects.all(),
    }
    return render(request, 'index.html', context)

def add_user(request):
    print(request.POST)
# add_user function first create a new user in the db
# HTML will show the user to the webpage
    User.objects.create( 
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email_address=request.POST['email'],
        age=request.POST['age'],
    )
#first first_name is from models.py
#second first_name is from index.html name field
    return redirect('/')