from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request, "home.html")

def login(request):
    if request.method == 'POST':
        return redirect('course')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        return redirect('login') 
    else:
        print("g")
        return render(request, 'register.html')

def course(request):
    return render(request, 'course.html')

