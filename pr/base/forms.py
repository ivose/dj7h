from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User
#from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        #fields = ['name', 'topic', 'description']
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'email', 'bio']
        #fields = '__all__'
        #exclude = ['host', 'participants', 'groups', 'user_permissions', 'status', 'last_login', 'date_joined', 'password']
