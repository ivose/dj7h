from django.forms import ModelForm
from .models import Room, Topic, Message
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        #fields = ['name', 'topic', 'description']
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        #fields = '__all__'
        #exclude = ['host', 'participants', 'groups', 'user_permissions', 'status', 'last_login', 'date_joined', 'password']
