from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
#from django.http import HttpResponse, HttpResponseNotFound
#from . import views

def home(request):
    rooms = Room.objects.all()
    #return HttpResponse("Hello, world. You're at the pr index.")
    return render(request, 'base/home.html', {'rooms' : rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            # request.POST.get('name')
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj': room}
    return render(request, 'base/delete.html', context)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
    #return HttpResponseNotFound("Oops! Page not found. Please check the URL.")