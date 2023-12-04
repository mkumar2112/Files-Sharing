from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from rest_framework import viewsets
from .Seriliazier import FileSerializer , SignUpForm
from .models import Files, USER
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.

class home(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('Operation:login')  


# @login_required
class UserView(DetailView):
    template_name = 'App.html'

    def get_object(self):
        return self.request.user


def Home(request):
    # Doc = Files.objects.all() # Take all object from our model.\
    return redirect('/Operation/Files/',)




class FileViewSet(viewsets.ModelViewSet):
    
    # Serialize the Our Files Model
    serializer_class = FileSerializer
    def get_queryset(self):
        return Files.objects.all()





