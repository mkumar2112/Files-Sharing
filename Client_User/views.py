from django.shortcuts import get_object_or_404, HttpResponse, render, redirect
from Operation_User.models import Files
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.mail import send_mail
import random



# Mk@12345
# Create your views here.

def download_file(request, file_id):
    uploaded_file = get_object_or_404(Files, pk=file_id)
    response = HttpResponse(uploaded_file.File, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename={uploaded_file.File.name.split("/")[-1]}'
    return response

def Home(request):
    Doc = Files.objects.all() # Take all object from our model.\
    return render(request, 'App.html', {'file': Doc})



class home(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('Client:login')  

def signup(request):
    if request.method == 'GET':
        form = RegisterForm() # A registration Form is creating.
        return render(request, 'SignUp.html', { 'form': form}) 
    if request.method == 'POST':
        form = RegisterForm(request.POST) # A registration Form is creating.
        if form.is_valid(): # if form is valid.
            user = form.save(commit=True) 
            user.email = user.email.lower()
            # print(self.user.email)
            I_otp = random.randint(100001,999999)
            send_mail(
                "Testing Email",
                f"Here is the message.{I_otp}",
                "mkumar321568@gmail.com",
                [user.email],
                fail_silently=False,
                )
            
            user.save() # Form save
            login(request, user)
            return redirect('/Client/Home/')  
        else:
            return render(request, 'SignUp.html', {'form': form})  # Return to User creation Form
 