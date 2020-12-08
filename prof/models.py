from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='images/',null=True, blank=True,default='images/smiley-4832482_1920.png')
    bio=models.CharField(max_length =100,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username 
        

    @classmethod
    def get_profile(cls,user_id):
        userd=cls.objects.get(user=user_id)
        # print (userd)
        return userd;
    @classmethod
    def update(cls,user_id):
        pass

class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=50)
    image_caption=models.CharField(max_length=50,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['-pub_time']

    @classmethod
    def get_all(cls):
        images=cls.objects.all()
        return images

    @classmethod
    def get_specific(cls,user_id):
        image=cls.objects.filter(user=user_id)
        return image
    @classmethod
    def get_followed_image(cls,followers_array):
        images=cls.objects.filter(user__in=followers_array)
        return images

class comment(models.Model):
    comment=HTMLField()
    user=models.ForeignKey(User)
    image=models.ForeignKey(Image)

    def __str__(self):
        return self.comment
    
    @classmethod
    def get_comments(cls,image_id):
        comments=cls.objects.filter(image=image_id)
        return comments
class Follow(models.Model):
    follower_id=models.IntegerField(blank=True)
    user_id=models.ForeignKey(User,blank=True)
    
    def __str__(self):
        return self.user_id.username  
    
    