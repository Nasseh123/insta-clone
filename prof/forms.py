from django import forms
from .models import Profile,Image,comment

class ProfileForm(forms.ModelForm):

    class Meta:
        model =Profile
        fields=['profile_pic','bio']

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['user','profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model=comment
        exclude=['user','image']
        