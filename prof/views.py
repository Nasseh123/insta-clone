from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile,User
# Create your views here..

# @login_required(login_url='/accounts/login/')
def index(request):
    user=request.user
    # print(user.username)
    
    return render(request,'index.html',{"user":user})

def profile(request,user_id):

    profile=Profile.get_profile(user_id)
    print(profile)
    return render(request,'profile.html',{'profile':profile})

    