from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django import forms
from .models import *


class EmpForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = "__all__"

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']