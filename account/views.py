from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form= self.form_class(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            User.objects.create_user(cd['username'],cd['email'], cd['password1'])
            messages.success(request,'you, registration','success')
            return redirect('home:home')
            # because if our form contains an error , we render the form again with error messages so that the messages comes
        return render(request, self.template_name, {'form': form})
    
    
    
class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    
    def get(self, request):
        form= self.form_class
        return render(request,self.template_name, {'form': form})
    
    def post(self, request):
        # etelaati ke az tariq method post miado be form midim
        form= self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'you logged in successfully', 'success')
                return redirect('home:home')
            messages.error(request,'username or password is incorrect','warning')
            # because if our form contains an error , we render the form again with error messages so that the messages comes
        return render(request,self.template_name, {'form':form})
