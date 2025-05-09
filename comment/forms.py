from django import forms
from .models import User , Comment

class CommentForm(forms.ModelForm):
    def __init_subclass__(self , *args ,**kwargs):
        super(CommentForm , self ).__init__(*args ,**kwargs)
        for item in self.visible_fields():
            item.field.widget.attrs['class'] = "form-control"

    username = forms.CharField(required=True , label='username'  , widget=forms.TextInput(attrs={'placeholder': 'Enter your username...'}))
    email = forms.EmailField( required=True , label='email' , widget=forms.EmailInput(attrs={'placeholder': 'Enter your email...'}))
    text = forms.CharField(required=True , label='text' , widget=forms.Textarea(attrs={'placeholder': 'Enter your comment...'}))
    class Meta:
        model = Comment
        fields = ['username', 'email' , "text"]
