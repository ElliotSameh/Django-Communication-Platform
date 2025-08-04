from django.forms import ModelForm
from .models import Room, Message
from django import forms
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'style': 'width:100%;'})
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
