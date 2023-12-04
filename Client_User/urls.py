from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required



app_name = 'Client_User'



urlpatterns = [
    
    path('signup/',  views.signup , name='Sign Up'),
    path('email/', include('verify_email.urls')),
    path('Home/',  login_required(views.Home) , name='Home'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/Client/signup/'), name='logout'), # Login Page Where user log out from applicaiton


    


]


