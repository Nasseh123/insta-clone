from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile,User,Image,comment,Follow
from .forms import ProfileForm,ImageForm,CommentForm
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your views here..

@login_required(login_url='/accounts/login/')
def index(request):
    user=request.user
    
    # print(user.id)
    profilepic=Profile.objects.filter(user=user)
    print(profilepic)
    pr=User.objects.filter(profile__user_id=1)
    print(pr)
    # image=Image.get_all()
    # image=Image.get_specific(user.id)
   
    # if 'name' request.method
    
    followers=Follow.objects.filter(user_id=user.id)
    # print(followers)
    followers_id=followers.values('follower_id')
    # print(followers_id)
    followers_array=[user.id]
    
    for one in followers_id:
        followers_array.append(one['follower_id'])
    # print(followers_array)
    imagefollowed=Image.get_followed_image(followers_array)
    
    # ***********************************************************COMMENTS**********************************************************************8
    comentdsd=[]
    
    # if('comments' in request.GET):
    idd= request.GET.get("comments_image_id")
    # print(idd)
    comments=comment.get_comments(idd)
    # print(comments)
    for commentss in comments.values('comment'):
        # print(commentss)
        comentds=commentss['comment']
        # print(comentds)
        comentdsd.append(comentds)
        # print(comentdsd)
       
        


    return render(request,'index.html',{"user":user,'image':imagefollowed,'profilepic':profilepic,'comentdsd':comentdsd,'pr':pr})

@login_required(login_url='/accounts/login/')
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
        # ********************************************************8
    

    return render(request,'profile.html',{'profile':profile,'form':ProfileForm})

def success(request):
    return HttpResponse('successfully uploaded')

@login_required(login_url='/accounts/login/')    
def new_image(request):
    current_user=request.user
    profileid=Profile.objects.get(user=current_user.id)
    print(profileid)
    if request.method=='POST':
        form =ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.profile=profileid
            image.save()
        return redirect('index')
        
    else:
        form=ImageForm()
    return render(request,'new_image.html',{'form':form})

@login_required(login_url='/accounts/login/')
def searchuser(request):

    if 'searchuser' in request.GET and request.GET["searchuser"]:
        search_term = request.GET.get("searchuser")
        # print(search_term)
        
        searched_user = User.objects.filter(username__icontains=search_term).all()
        # print(searched_user.values('id'))
        
        users_id=searched_user.values('id')
        usersarray=[]
        
        for one in users_id:
            usersarray.append(one['id'])
        # print(usersarray)
         
        searched_image=Profile.objects.filter(user__in=usersarray).all()
        # print(searched_image)
        # print(users_id)
        # listuser=list(users_id.values())
        # print(listuser)
        # current_user=request.user
        # for users in users_id:
        #     idS=listuser[:1]
        #     print(id)
            # 
            # print(searched_image)s
        # print(searched_user)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"users": searched_user,'image':searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def new_comment(request,images_id):
    current_user=request.user
    print(images_id)
    imageds=Image.objects.get(id=images_id)
    print(imageds.id)
    ima=imageds.id
    # imageds_id=imageds.values('user_id')
    # print(imageds_id)
        
    # for one in imageds_id:
    #     imageds_value=one['user_id']
    #     print( imageds_value)
    # ids=imageds_value

    if request.method=='POST':
        form =CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=current_user
            comment.image=Image.objects.get(id=ima)
            
            comment.save()
        return redirect('index')
        
    else:
        form=CommentForm()
    return render(request,'new_comment.html',{'form':form})

@login_required(login_url='/accounts/login/')
def usersimages(request):
    current_user_id=request.user
    
    print(current_user_id)
    if(request.GET.get('mybtn')):
        follow= request.GET.get("mytextbox")
        print(follow)
        checkfollow=Follow.objects.filter(follower_id=follow,user_id=current_user_id)
        if checkfollow:
            message="You have already followed this person"
            return render(request, 'search.html',{'message':message})
        else:
            followupdate=Follow.objects.create(follower_id = follow,user_id =current_user_id )
            followupdate.save()
    return redirect( 'index.html')
def userspublicprofile(request,user_id):
    print(user_id)
    images=Image.objects.filter(user=user_id)
    
    return render(request, 'usersprofile.html',{'image':images})
