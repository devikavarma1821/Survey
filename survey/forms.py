from django import forms
from .models import DemographicInformation, Transportation, Occupation ,EnvironmentalAwareness, FoodConsumption,EnergyConsumption,WasteManagement,ConsumerChoices, Miscellaneous



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

'''class WasteManagementForm(forms.ModelForm):
    class Meta:
        model = WasteManagement
        fields = ['recycles', 'organic_waste', 'other_waste_method'] '''
from django import forms
from .models import WasteManagement

class WasteManagementForm(forms.ModelForm):
    class Meta:
        model = WasteManagement
        fields = ['recycles', 'organic_waste', 'other_waste_method']

    def clean(self):
        cleaned_data = super().clean()
        organic_waste = cleaned_data.get('organic_waste')
        other_waste_method = cleaned_data.get('other_waste_method')

        # Validation for "Other" option in organic_waste
        if organic_waste == "Other" and not other_waste_method:
            self.add_error('other_waste_method', 'Please specify the waste management method.')

        return cleaned_data

    def clean_other_waste_method(self):
        other_waste_method = self.cleaned_data.get('other_waste_method')
        # Strip leading/trailing spaces from the input
        if other_waste_method:
            return other_waste_method.strip()
        return other_waste_method


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
