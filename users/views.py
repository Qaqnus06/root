from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import  LoginRequiredMixin

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request,'users/register.html', context={'form':form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            form.save()
            return redirect('landing_page')

        else:
            return render(request,'users/register.html',context={'form':form})

class LoginView(View):
    def get(self, request):
        form=LoginForm()
        return render(request,'users/login.html',context={'form':form})
    
    def post(self, request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('landing_page')
            else:
                return render(request,'users/login.html',context={'form':form})
        else:
            return render(request,'users/login.html',context={'form':form})

class LogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        return redirect('landing_page')

class ProfileUpdateView(LoginRequiredMixin,View):
    def get(self, request):
        form=ProfileUpdateView(isinstance=request.user) 

        return render(request, 'users/profile.html',context={'form':form})   
                        
    def post(self,request):
        form=ProfileUpdateView(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
        else:
            return render(request, 'users/profile.html',context={'form':form})
        
