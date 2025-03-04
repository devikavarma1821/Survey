from django import forms
from .models import  RegistrationForm, DemographicInformation, Transportation, Occupation ,EnvironmentalAwareness, FoodConsumption,EnergyConsumption,ConsumerChoices, Miscellaneous
from .models import CustomUser
import re
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

CustomUser = get_user_model()  # Ensure this fetches the correct user model

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser  # Use CustomUser instead of User
        fields = ["email", "password"]  # No username field
        widgets = {
            "password": forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")

        # Regex to enforce strong password requirements
        if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            raise ValidationError(
                "Password must contain at least 8 characters, including one uppercase, one lowercase, one number, and one special character (@$!%*?&)."
            )
        return password


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



class DemographicInformationForm(forms.ModelForm):
    class Meta:
        model = DemographicInformation
        fields = '__all__'

class TransportationForm(forms.ModelForm):
    class Meta:
        model = Transportation
        fields = ['primary_mode', 'owns_electric_vehicle', 'frequency_private_transport',
                  'driving_pattern', 'avg_distance_per_day', 'carpool']


# forms.py
class OccupationForm(forms.ModelForm):
    class Meta:
        model = Occupation
        fields = ['owns_business', 'promotes_awareness', 'attends_seminars', 'seminar_location', 'seminar_frequency']
        widgets = {
            'owns_business': forms.Select(attrs={'class': 'form-select'}),
            'promotes_awareness': forms.Select(attrs={'class': 'form-select'}),
            'attends_seminars': forms.Select(attrs={'class': 'form-select'}),
            'seminar_location': forms.Select(attrs={'class': 'form-select'}),
            'seminar_frequency': forms.Select(attrs={'class': 'form-select'}),
        }



class EnvironmentalAwarenessForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalAwareness
        fields = '__all__'

class FoodConsumptionForm(forms.ModelForm):
    class Meta:
        model = FoodConsumption
        fields = '__all__'

    # Optional fields: set required=False if needed
    wheat_consumption = forms.CharField(max_length=25, required=False)
    nuts_consumption = forms.CharField(max_length=25, required=False)

class EnergyConsumptionForm(forms.ModelForm):
    class Meta:
        model = EnergyConsumption
        fields = ['primary_source', 'energy_efficient_usage', 'monthly_consumption', 'other_source']
        widgets = {
            'primary_source': forms.Select(choices=EnergyConsumption.ENERGY_SOURCE_CHOICES),
            'energy_efficient_usage': forms.Select(choices=EnergyConsumption.EFFICIENT_USAGE_CHOICES),
            'monthly_consumption': forms.Select(choices=EnergyConsumption.MONTHLY_CONSUMPTION_CHOICES),
        }



class ConsumerChoicesForm(forms.ModelForm):
    class Meta:
        model = ConsumerChoices
        fields = ['buy_locally', 'reduce_plastic', 'carbon_conscious']

        widgets = {
            'buy_locally': forms.Select(choices=ConsumerChoices.LOCALLY_CHOICES),
            'reduce_plastic': forms.Select(choices=ConsumerChoices.PLASTIC_CHOICES),
            'carbon_conscious': forms.Select(choices=ConsumerChoices.CARBON_CHOICES),
        }

class MiscellaneousForm(forms.ModelForm):
    class Meta:
        model = Miscellaneous
        fields = ['international_flights', 'carbon_offset', 'additional_comments']
        widgets = {
            'additional_comments': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Share your comments here...'}),
        }
