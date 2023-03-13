from datetime import datetime
import pyttsx3
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms import models
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact, Booking, Flight
from .forms import SetPasswordForm



# Create your views here.

def index(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'index.html', param)
    else:
        return redirect('login')
    return render(request, 'login.html')

# def index(request):
#     return render(request, 'index.html')
    # return HttpResponse("This Is My Home Page")

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def about(request):
    return render(request, 'about.html')

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def services(request):
    return render(request, 'services.html')

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def terms(request):
    return render(request, 'terms.html')

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def privacy(request):
    return render(request, 'privacy-policy.html')

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def destination(request):
    allFlights = Flight.objects.all()
    context = {'allFlights': allFlights}
    return render(request, 'destination.html', context)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        location=request.POST.get('location')
        desc=request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, location=location, desc=desc, date=datetime.today())
        contact.save()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        if len(str(phone)) != 10:
            engine.say('Please enter your valid Mobile No. Must be 10 digit')
            engine.runAndWait()
            messages.warning(request, 'Mobile number must be 10 digits long')
            return redirect("contact")
        else:
            messages.success(request, 'Your Message Has Been Sent Successfully')
    return render(request, 'contact.html')

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# @login_required(login_url='login')
# @user_passes_test(User)
def booking(request):
    if request.method == "POST":
        p_name=request.POST.get('p_name')
        mobile=request.POST.get('mobile')
        email_id=request.POST.get('email_id')
        address=request.POST.get('address')
        t_date=request.POST.get('t_date')
        dep_from=request.POST.get('dep_from')
        des_from=request.POST.get('des_from')
        booking = Booking(p_name=p_name, mobile=mobile, email_id=email_id, address=address,
                          t_date=t_date, dep_from=dep_from, des_from=des_from, date=datetime.today())
        booking.save()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        if len(str(mobile)) != 10:
            engine.say('Please enter your valid Mobile No. Must be 10 digit')
            engine.runAndWait()
            messages.warning(request, 'Mobile number must be 10 digits long')
            return redirect("booking")
        else:
            messages.success(request, 'Your Flight Booking Form Has Been Successfully Submitted')
    return render(request, 'booking.html')

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def search(request):
    if request.method == 'GET':
        query = request.GET['query']
    if len(query) > 78:
        allFlights = Flight.objects.none()
    else:
        allFlightsflight_name = Flight.objects.filter(flight_name__icontains=query)
        allFlightsdestination = Flight.objects.filter(destination__icontains=query)
        allFlights = allFlightsflight_name.union(allFlightsdestination)

    if allFlights.count() == 0:
        messages.warning(request, "No Search Result Found, Please Try With Different Query")
    params = {'allFlights': allFlights, 'query': query}
    return render(request, 'search.html', params)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'password_change.html', {'form': form})


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def signup(request):
    if request.method == 'POST':

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")


        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already registered")
            return redirect("signup")

        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = first_name
            myuser.last_name = last_name
            myuser.save()
            messages.success(request, "Your Account has been successfully created, Please Login")
            return redirect("login")

    return render(request, "signup.html")

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def login(request):
    if request.method == 'POST':

        loginusername = request.POST.get("loginusername")
        loginpassword = request.POST.get("loginpassword")

        user = authenticate(username=loginusername, password=loginpassword)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        if user is not None:
            request.session['user'] = loginusername
            messages.success(request, "You are Successfully Logged In")
            return redirect("index")
        else:
            engine.say('Invalid Login Details, Please enter Correct Username & Password')
            engine.runAndWait()
            messages.warning(request, "Invalid Login Details, Please Try Again")

    return render(request, "login.html")

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def logout_view(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return render(request, 'index.html')

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@













