from django.urls import path, include
from . import views
from rest_framework import routers
from .views import FileViewSet  , UserView, home
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required



router =routers.DefaultRouter()
router.register(r'Files', FileViewSet, basename="Files CRUD Operation") 

from django.urls import path, reverse
app_name = 'Operation_User'

urlpatterns = [
    path('',include(router.urls)),
    path('login/',home.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/Operation/login/'), name='logout'), # Login Page Where user log out from applicaiton
    path('accounts/profile/',  login_required(views.Home), name='profile'), #Application
    




]


