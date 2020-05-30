from django import forms
from .models import Profile,Image

class ProfileForm(forms.ModelForm):

    class Meta:
        model =Profile
        fields=['profile_pic','bio']

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['user']
        