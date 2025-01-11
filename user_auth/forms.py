from django import forms
from .models import Profile

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']

