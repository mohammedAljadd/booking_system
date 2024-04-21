from django import forms
from .models import Booking



class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['room', 'start_date', 'start_hour', 'end_hour']