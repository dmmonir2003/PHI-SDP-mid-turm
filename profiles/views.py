from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def user_login(request):
      if request.method=='POST':
              form=AuthenticationForm(request=request,data=request.POST)
              if form.is_valid():
                    name=form.cleaned_data['username']
                    user_pass=form.cleaned_data['password']
                    user=authenticate(username=name,password=user_pass)
                    if user is not None:
                           messages.success(request,'user login successfully !!')
                           login(request,user)
                           redirect('home_page')
                    else:
                        messages.error(request,'Invalid username or password')
              else:
                     form=AuthenticationForm()
                     return render(request,'form.html',{'form': form, 'type': 'Login'})      
      else:    
        form=AuthenticationForm()
        return render(request,'form.html',{'form': form, 'type': 'Login'})

def user_signup(request):
        if request.method=='POST':
              form=UserForm(request.POST)
              if form.is_valid():
                    messages.success(request,'user created successfully !!')
                    form.save()
                    return redirect('user_login')
              else:
                 messages.error(request, 'Please correct the field .')
             
                 return render(request, 'form.html', {'form': form, 'type':   'Signup'})
              
        else:
              form=UserForm()
              return render(request,'form.html',{'form': form, 'type': 'Signup'})