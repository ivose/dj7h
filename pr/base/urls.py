from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register_page'),
    path('logout/', views.logoutPage, name='logout_page'),
    
    path('', views.home, name='home'),
    path('room_page/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    
    path('create_room/', views.createRoom, name='create_room'),
    path('update_room/<str:pk>/', views.updateRoom, name='update_room'),
    path('delete_room/<str:pk>/', views.deleteRoom, name='delete_room'),
    path('delete_message/<str:pk>/', views.deleteMessage, name='delete_message'),

    path('update-user/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),
]