from django import forms
from .models import Blog

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['writer', 'body', 'image']
        widgets = {
            'created_at' : forms.DateInput(
                attrs = {
                    'class' : 'from-control',
                    'type' : 'date'
                }
            )
        }