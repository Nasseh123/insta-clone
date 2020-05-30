from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from .models import Profile,User
from .forms import ProfileForm,ImageForm

# Create your views here..

# @login_required(login_url='/accounts/login/')
def index(request):
    user=request.user
    # print(user.username)
    
    return render(request,'index.html',{"user":user})

def profile(request,user_id):

    profile=Profile.get_profile(user_id)
    prof_pic=profile.profile_pic
    # print(prof_pic)
    # print(profile)
    if request.method=='POST':
        # instance=get_object_or_404(Profile,user_id=user_id)
        form=ProfileForm(request.POST, request.FILES,instance=profile)
        print(form)
        
        if form.is_valid():
            # formd=Profile.update()
            # print(formd)
            form.save()
            message='Success'
            return redirect('success')
        
    else:
        form=ProfileForm()
    return render(request,'profile.html',{'profile':profile,'form':ProfileForm})

def success(request):
    return HttpResponse('successfully uploaded')
    
def new_image(request):
    current_user=request.user
    if request.method=='POST':
        form =ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('success')
        
    else:
        form=ImageForm()
    return render(request,'new_image.html',{'form':form})