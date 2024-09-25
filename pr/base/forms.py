from django.forms import ModelForm
from .models import Room, Topic, Message


class RoomForm(ModelForm):
    class Meta:
        model = Room
        #fields = ['name', 'topic', 'description']
        fields = '__all__'