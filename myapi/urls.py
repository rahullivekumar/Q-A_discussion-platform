"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.db import router
from django.urls import path, include
from rest_framework import routers
from . import  views

router=routers.DefaultRouter()
router.register(r'questions',views.QuestionViewSet)

urlpatterns = [
    path('data',include(router.urls)),
    path('login',views.login,name="login"),
    path('homes',views.home,name="home"),
    path('', views.home, name="home"),
    path('navv', views.navv, name="navv"),
    path('signup',views.signup,name="signup"),
    path('create',views.signup,name="signup"),
    path('logout',views.logout,name="logout"),
    path('newques',views.newques,name="newques"),
    path('ans/newans/<int:qid>',views.newans,name="newans"),
    path('search',views.search,name="search"),
    path('delques/<int:qid>',views.delques,name="delques"),
    path('ans/delans/<int:aid>',views.delans,name="delans"),
    path('updateques/<int:qid>',views.updateques,name="updateques"),
    path('editans/updateans/<int:aid>',views.updateans,name="updateans"),
    path('editques/<int:qid>', views.editques, name="editques"),
    path('editans/<int:aid>',views.editans,name="editans"),
    # path('editans/<int:aid>', views.editans, name="editans"),
    # path('delans/<int:qid>',views.delans,name="delans"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ans/<int:qid>', views.ans, name="ans"),
    path('viewcount/<int:qid>', views.viewcount, name="viewcount"),

    #path('path/to/my/view/', MySimpleView.as_view())
]
