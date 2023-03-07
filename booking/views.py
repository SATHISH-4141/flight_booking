

from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from booking.models import Enrollment
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    #return HttpResponse('home function')
    return render(request,'login.html')


def enrollment(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(username=username,password=password)
    if user is not None:
        #return HttpResponse('enrollment function')

        if user.is_superuser:
            print("username  :",username)
            print("password    :",password)
            login(request,user)
            
            
            return render(request,'home.html')
            # elif Enrollment.objects.filter(username = username,password = password).exists():
            #      return render(request,'welcome to admin from register page')
    else:
            #return HttpResponse("credential not correct")
        return render(request,'credential.html')
    # print("username",username)
    # print("number",password)  
    # return render(request,'admin.html')

    # print("username",username)
    # print("number",password)

def signpage(request):
    return render(request,"signup.html")
    #return HttpResponse("welcome")

def signup(request):
    #E = Enrollment()
    username = request.POST.get('username')
    mobile_number = request.POST.get('number')
    password = request.POST.get('password')
    comfirm_password = request.POST.get('confirmpassword')
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    dob = request.POST.get('dob')
    email = request.POST.get('email')
    #E.save()
    user = User.objects.create_superuser(username = username, password = password,email = email)
    user.save();
    #messages.success(request, 'your account have been successfully created!')
    print("username",username)
    print("number",mobile_number)
    #return redirect('enroll')
    #return HttpResponse('register successfully')
    return redirect('home')
