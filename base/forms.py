from django.forms import ModelForm
from .models import Room, Message
from django import forms


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'style': 'width:100%;'})
        }
