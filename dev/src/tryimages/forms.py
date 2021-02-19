from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the Image Model"""

    """This will generate a form with fields title and image
    which will be rendered in the templates"""
    
    class Meta:
        model = Image
        fields = ('title', 'image')
