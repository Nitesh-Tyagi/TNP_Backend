"""TNP_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Backend import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('getForms/', views.getForms, name='get_forms'),
    path('getForm/<int:formId>/', views.getForm, name='get_form'),
    path('postForm/', views.postForm, name='post_form'),
    path('putForm/<int:formId>/', views.putForm, name='put_form'),
    path('delForm/<int:formId>/', views.delForm, name='del_form'),
    path('getSettings/<int:userId>/', views.getSettings, name='get_settings'),
    path('putSettings/<int:userId>/', views.putSettings, name='put_settings'),
    path('getRooms/', views.getRooms, name='get_rooms'),
    path('getRoom/<int:roomId>/', views.getRoom, name='get_room'),
    path('putRoom/<int:roomId>/', views.putRoom, name='put_room'),
    path('sendBack/<int:formId>/<int:userId>/', views.send_back),
]
