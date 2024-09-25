from django.shortcuts import render
#from django.http import HttpResponse, HttpResponseNotFound
#from . import views

rooms = [
    {'id':1, 'name':'Lets learn python'},
    {'id':2, 'name':'Design with me'},
    {'id':3, 'name':'Blaa-blaa-blaa'},
]

def home(request):
    #return HttpResponse("Hello, world. You're at the pr index.")
    return render(request, 'base/home.html', {'rooms' : rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
            break
    context = {'room' : room}
    return render(request, 'room.html', context)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
    #return HttpResponseNotFound("Oops! Page not found. Please check the URL.")