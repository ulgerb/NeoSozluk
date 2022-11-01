from django import forms
from .models import Comments


class CommenttForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ("name","text")
