from django.shortcuts import render, redirect
from .forms import  DemographicInformationForm, TransportationForm, EnvironmentalAwarenessForm, OccupationForm, FoodConsumptionForm,EnergyConsumptionForm, WasteManagementForm ,ConsumerChoicesForm , MiscellaneousForm

from .utils import save_to_csv





# Home View
def survey_home(request):
    return render(request, 'survey/survey_home.html')

# Demographic Information View
# Import the save_to_excel function from utils


# Demographic Information View
def demographic_information_view(request):
    if request.method == 'POST':
        form = DemographicInformationForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            instance = form.save()

            # Save data to CSV
            save_to_csv('Demographic Information', instance)  # Save the form data to CSV

            return redirect('transportation')  # Redirect to transportation form
    else:
        form = DemographicInformationForm()

    return render(request, 'survey/demographic_information.html', {'form': form})

# Transportation View
 # Import the save_to_excel function

def transportation_view(request):
    if request.method == 'POST':
        form = TransportationForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            instance = form.save()

            # Save data to CSV (instead of Excel)
            save_to_csv('Transportation Information', instance)  # Updated to save to CSV

            # Redirect to environmental awareness page
            return redirect('environmental_awareness')
        else:
            print(form.errors)  # Print any form validation errors to check why it's failing
    else:
        form = TransportationForm()

    return render(request, 'survey/transportation.html', {'form': form})
# Environmental Awareness View
  # Import the save_to_excel function

def environmental_awareness_view(request):
    if request.method == 'POST':
        form = EnvironmentalAwarenessForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            instance = form.save()

            # Save data to CSV (instead of Excel)
            save_to_csv('Environmental Awareness Information', instance)  # Updated to save to CSV

            # Redirect to occupation form
            return redirect('occupation')
    else:
        form = EnvironmentalAwarenessForm()

    return render(request, 'survey/environmental_awareness.html', {'form': form})
# Occupation View
# Import the save_to_excel function

def occupation_view(request):
    if request.method == 'POST':
        form = OccupationForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            instance = form.save()

            # Save data to CSV (instead of Excel)
            save_to_csv('Occupation Information', instance)  # Updated to save to CSV

            # Redirect to food consumption form
            return redirect('food_consumption')
    else:
        form = OccupationForm()

    return render(request, 'survey/occupation.html', {'form': form})
# Food Consumption View
# Adjust this import if necessary
  # Import the save_to_excel function

def food_consumption_view(request):
    if request.method == 'POST':
        form = FoodConsumptionForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            instance = form.save()

            # Save data to CSV (instead of Excel)
            save_to_csv('Food Consumption Information', instance)  # Updated to save to CSV

            # Redirect to the next form (energy consumption)
            return redirect('energy_consumption')  # Adjust the redirect to your actual view
        else:
            # Print form errors to the console for debugging
            print(form.errors)
    else:
        form = FoodConsumptionForm()

    return render(request, 'survey/food_consumption.html', {'form': form})
# Energy Consumption View
 # Import the save_to_excel function

def energy_consumption_view(request):
    if request.method == 'POST':
        form = EnergyConsumptionForm(request.POST)
        if form.is_valid():
            print("Energy Consumption form is valid!")

            # Save form data to the database
            instance = form.save()

            # Save data to CSV (instead of Excel)
            save_to_csv('Energy Consumption Information', instance)  # Updated to save to CSV

            # Redirect to the next form (consumer choices)
            return redirect('consumer_choices')
        else:
            print(form.errors)

    else:
        form = EnergyConsumptionForm()

    return render(request, 'survey/energy_consumption.html', {'form': form})
#waste_management





#consumer_choices_view
# Import the save_to_excel function

def consumer_choices_view(request):
    if request.method == 'POST':
        form = ConsumerChoicesForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            instance = form.save()

            # Save data to CSV (instead of Excel)
            save_to_csv('Consumer Choices Information', instance)  # Updated to save to CSV

            # Redirect to the 'thank_you' page after form submission
            return redirect('thank_you')  # Ensure 'thank_you' is correctly mapped in your URLs
    else:
        form = ConsumerChoicesForm()

    return render(request, 'survey/consumer_choices.html', {'form': form})
# Miscellaneous View

# Thank You View (End of Survey)
def thank_you_view(request):
    return render(request, 'survey/thank_you.html')
