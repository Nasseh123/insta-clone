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
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Add a comment...',"rows":3, "cols":20,"style": "resize: none;padding-top:0;margin-top:0"}), label='')
    class Meta:
        model=comment
        exclude=['user','image']
        