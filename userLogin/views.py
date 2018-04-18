from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import profile_form, user_form
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'userLogin/index.html',{})

def user_register(request):
    registered = False
    if request.method == 'POST':
        userfrm = user_form(data=request.POST)
        profilefrm = profile_form(data=request.POST)

        if userfrm.is_valid() and profilefrm.is_valid():
            user = userfrm.save()
            user.set_password(user.password)
            user.save()

            profile = profilefrm.save(commit=False)
            profile.user = user
            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
            profile.save()
            registered = True
        else:
            return render(request,'userLogin/register.html',context={'userfrm':userfrm,'profilefrm':profilefrm})
    else:
        userfrm = user_form()
        profilefrm = profile_form()
        return render(request,'userLogin/register.html',context={'userfrm':userfrm,'profilefrm':profilefrm})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('user not active')
        else:
            return HttpResponse('invalid login')
    else:
        return render(request, 'userLogin/login.html', context={})