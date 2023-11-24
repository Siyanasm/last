from django.contrib import auth, messages
from django.shortcuts import render, redirect




# Create your views here.
def demo(request):
     return render(request,"index.html")

def login(request):
    if request.method =='POST':
       #username=request.POST['username']
      # password=request.POST['password']
       #user=auth.authenticate(username=username,password=password)
       return redirect('http://127.0.0.1:8000/newpage')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        return redirect('http://127.0.0.1:8000/login')
    return render(request, 'register.html')

def newpage(request):
    if request.method == 'POST':
       return redirect('http://127.0.0.1:8000/form')
    return render(request,'newpage.html')

def form(request):
    if request.method =='POST':
        return redirect('http://127.0.0.1:8000/home')
    return render(request,'form.html')

def home(request):
    return render(request,'home.html')

