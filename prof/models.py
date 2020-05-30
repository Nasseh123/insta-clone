from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='articles/', blank=True)
    bio=models.CharField(max_length =100,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.bio

    @classmethod
    def get_profile(cls,user_id):
        userd=cls.objects.get(user=user_id)
        # print (userd)
        return userd;
    @classmethod
    def update(cls,user_id):
        pass