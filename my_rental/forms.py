from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Renter, Property

class CustomSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    unit = forms.CharField(max_length=1, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    city = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    state = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    zip_code = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    country = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    property = forms.ModelChoiceField(
        queryset=Property.objects.filter(available=True),
        required=True,
        empty_label="Select a property",
        label="Select Property",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'property-select'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 
                  'property', 'address', 'unit', 'city', 'state', 'zip_code', 'country', 
                  'password1', 'password2')
