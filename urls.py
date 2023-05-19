"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app01 import views
from app01.views import publish_content,article_detail




urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('user/list',views.user_list),
    path('login/',views.login),
    path('orm/',views.orm),
    path('info/list/',views.info_list),
    path('info/add/',views.info_add),
    path('info/delete/',views.info_delete),
    
   
    path('home/',views.home),
   
    path('home/sign_in',views.sign_in),
    path('home/publish_content',views.publish_content,name='publish_content'),
    path('administrator/',views.administrator),
    path('article_detail/<int:id>/',views.article_detail,name='article_detail')
  
]
