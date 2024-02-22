from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request,'core/frontpage.html')

def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('frontpage')
    else:
        form = SignUpForm()
            
    return render(request,'core/signup.html',{'form':form})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/login/')
    return render(request,'core/login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')
