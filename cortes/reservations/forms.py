from django import forms
from .models import TableReservation


class TableReservationForm(forms.ModelForm):
    class Meta:
        model = TableReservation
        fields = ['name', 'email', 'phone', 'date', 'time', 'people', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'date': forms.DateInput(format='%d-%m-%Y',
                                    attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Date'}),
            'time': forms.TimeInput(format='%H:%M',
                                    attrs={'type': 'time', 'class': 'form-control', 'placeholder': 'Time'}),
            'people': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'People', 'min': 1, 'max': 20}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }
