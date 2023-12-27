from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib import messages

# Create your views here.
def user_login(request):
     return render(request,'form.html')

def user_signup(request):
        if request.method=='POST':
              form=UserForm(request.POST)
              if form.is_valid():
                    messages.success(request,'user created successfully !!')
                    form.save(commit=False)
                    return redirect('user_login')
              
        else:
              form=UserForm()
              return render(request,'form.html',{'form': form, 'type': 'Signup'})