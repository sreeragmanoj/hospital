from django import forms

from .models import Booking

class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields='__all__'
        widgets = {
            'booking_date':DateInput
        }

        labels={
            'p_name':'Paitent Name',
            'p_phone':'Paitent Phone',
            'p_email':'Paitent Email',
            'doc_name':'Doctor Name',
            'booking_date':'Booking Date',
            
        }
        