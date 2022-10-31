from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('new/',views.newuser,name='new'),
    path('login/',views.connect,name='login'),
    path('profile/',views.myprofile,name='profile'),
    path('logout/',views.deconect,name='logout'),
    path('newproject',views.newproject,name='newproject'),
    path('user/<int:id>',views.unprofile,name='user'),
    path('readproje/<int:id>',views.readprojet,name='readproje'),
    path('delete/<int:id>',views.efaseproje,name='delete'),
    path('all/',views.toutproje,name='all'),
    path('allprofil/',views.toutprofil,name='allprofil')
]

