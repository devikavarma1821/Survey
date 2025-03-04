from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model  # Use this instead of User
from django.http import HttpResponse  # Fixed import
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import login

import os
import csv
from .forms import (
    DemographicInformationForm, TransportationForm, EnvironmentalAwarenessForm,
    OccupationForm, FoodConsumptionForm, EnergyConsumptionForm,
    ConsumerChoicesForm, MiscellaneousForm
)
from .utils import save_to_csv  # Ensure this function exists
CustomUser = get_user_model()  # Use CustomUser dynamically
from .forms import RegistrationForm  # Ensure this is at the top
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login




CustomUser = get_user_model()  # Ensure this fetches the correct user model

# Home View
def survey_home(request):
    return render(request, 'survey/survey_home.html')


def register(request):
    print("DEBUG: RegistrationForm import issue")  # Debugging print

    if request.method == 'POST':
        form = RegistrationForm(request.POST)  # Use the form for validation

        if form.is_valid():
            try:
                # Creating a new user using Django's create_user method
                user = CustomUser.objects.create_user(
                    email=form.cleaned_data["email"],
                    password=form.cleaned_data["password"]
                )

                # Automatically log in the user
                login(request, user)

                # -----------------------------
                # SAVE REGISTRATION DATA TO CSV in survey_data
                # -----------------------------
                survey_data_path = os.path.join(settings.BASE_DIR, "survey_data")
                os.makedirs(survey_data_path, exist_ok=True)

                file_path = os.path.join(survey_data_path, "registration_data.csv")
                file_exists = os.path.isfile(file_path)

                with open(file_path, mode="a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    if not file_exists:
                        writer.writerow(["Email", "Registration Time"])
                    writer.writerow([user.email, timezone.now()])

                return redirect('login')

            except Exception as e:
                print(f"DEBUG: Error during registration - {e}")
                return render(request, 'survey/register.html',
                              {'form': form, 'error': 'An error occurred. Please try again.'})

        # If the form is invalid, return errors
        return render(request, 'survey/register.html', {'form': form})

    else:
        form = RegistrationForm()
    return render(request, 'survey/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)

                # Save login data to CSV
                survey_data_path = os.path.join(settings.BASE_DIR, "survey_data")
                os.makedirs(survey_data_path, exist_ok=True)
                file_path = os.path.join(survey_data_path, "all_survey_responses.csv")
                with open(file_path, mode="a+", newline="", encoding="utf-8") as file:
                    file.seek(0, os.SEEK_END)
                    is_empty = file.tell() == 0
                    writer = csv.writer(file)
                    if is_empty:
                        writer.writerow(["Event Type", "Email", "Timestamp"])
                    writer.writerow(["Login", user.email, timezone.now()])

                return redirect('demographic_information')
            else:
                return render(request, 'survey/login.html', {'error': 'Your account is disabled. Please contact support.'})
        else:
            return render(request, 'survey/login.html', {'error': 'Invalid credentials. Please try again.'})

    return render(request, 'survey/login.html')


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
