from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)

        # Check if the user already exists
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")


        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for admin access
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Use email instead of username
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class RegistrationForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DemographicInformation(models.Model):
    AGE_CHOICES = [
        ('18-24', '18-24'),
        ('25-34', '25-34'),
        ('35-44', '35-44'),
        ('45-54', '45-54'),
        ('55+', '55 and above'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Non-binary', 'Non-binary'),
        ('Other', 'Other (Specify)'),
    ]
    LOCATION_CHOICES = [
        ('Urban', 'Urban'),
        ('Suburban', 'Suburban'),
        ('Rural', 'Rural'),
    ]
    OCCUPATION_CHOICES = [
        ('Employed', 'Employed'),
        ('Student', 'Student'),
        ('Homemaker', 'Homemaker'),
        ('Unemployed', 'Unemployed'),
        ('Other', 'Other'),
    ]

    age = models.CharField(max_length=10, choices=AGE_CHOICES)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    occupation = models.CharField(max_length=15, choices=OCCUPATION_CHOICES)

    def __str__(self):
        return f"{self.age}, {self.gender}, {self.location}, {self.occupation}"


class Transportation(models.Model):
    TRANSPORT_CHOICES = [
        ('Private car', 'Private car'),
        ('Public transportation', 'Public transportation'),
        ('Bicycle', 'Bicycle'),
        ('Walking', 'Walking'),
        ('Motorcycle/scooter', 'Motorcycle/scooter'),
        ('Other', 'Other'),
    ]
    FREQUENCY_CHOICES = [
        ('Daily', 'Daily'),
        ('Several times a week', 'Several times a week'),
        ('Occasionally', 'Occasionally'),
        ('Rarely', 'Rarely'),
    ]
    DRIVING_PATTERN_CHOICES = [
        ('Steady and mature', 'Steady and mature'),
        ('Fast but safe', 'Fast but safe'),
        ('Rash', 'Rash'),
        ('No idea', 'No idea'),
    ]
    DISTANCE_CHOICES = [
        ('Less than 5 km', 'Less than 5 km'),
        ('5-10 km', '5-10 km'),
        ('10-20 km', '10-20 km'),
        ('More than 20 km', 'More than 20 km'),
    ]

    primary_mode = models.CharField(max_length=100, blank=True,   null=True, choices=TRANSPORT_CHOICES)
    owns_electric_vehicle = models.BooleanField()
    frequency_private_transport = models.CharField(max_length=100,blank=True, null=True, choices=FREQUENCY_CHOICES)
    driving_pattern = models.CharField(max_length=25, choices=DRIVING_PATTERN_CHOICES)
    avg_distance_per_day = models.CharField(max_length=25, blank=True,  null=True, choices=DISTANCE_CHOICES)
    carpool = models.BooleanField()

    def __str__(self):
        return self.primary_mode


#occupation


# models.py
class Occupation(models.Model):
    BUSINESS_OWNER_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    AWARENESS_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    SEMINAR_ATTENDANCE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    DISTANCE_CHOICES = [
        ('Within city limits', 'Within city limits'),
        ('Within state', 'Within state'),
        ('Within country', 'Within country'),
        ('International', 'International'),
    ]
    FREQUENCY_CHOICES = [
        ('Annually', 'Annually'),
        ('Monthly', 'Monthly'),
        ('Weekly', 'Weekly'),
    ]

    owns_business = models.CharField(max_length=3, choices=BUSINESS_OWNER_CHOICES, default='No')
    promotes_awareness = models.CharField(max_length=3, choices=AWARENESS_CHOICES, default='No')
    attends_seminars = models.CharField(max_length=3, choices=SEMINAR_ATTENDANCE_CHOICES, default='No')
    seminar_location = models.CharField(
        max_length=50, choices=DISTANCE_CHOICES, blank=True, null=True, default='Within city limits'
    )
    seminar_frequency = models.CharField(
        max_length=10, choices=FREQUENCY_CHOICES, blank=True, null=True, default='Annually'
    )

    def _str_(self):
        return f"Business: {self.owns_business}, Awareness: {self.promotes_awareness}"


class EnvironmentalAwareness(models.Model):
    does_gardening = models.BooleanField()
    attends_awareness_programs = models.BooleanField()
    aware_of_sustainable_features = models.BooleanField()

    def __str__(self):
        return f"Gardening: {self.does_gardening}, Programs: {self.attends_awareness_programs}"


class FoodConsumption(models.Model):
    DIET_CHOICES = [
        ('High meat', 'High meat'),
        ('Medium meat', 'Medium meat'),
        ('Low meat', 'Low meat'),
        ('Vegetarian', 'Vegetarian'),
        ('Vegan', 'Vegan'),
        ('Pescetarian', 'Pescetarian'),
        ('Other', 'Other'),
    ]
    diet_type = models.CharField(max_length=20, choices=DIET_CHOICES)
    beef_consumption = models.CharField(max_length=25)
    pork_consumption = models.CharField(max_length=25)
    mutton_consumption = models.CharField(max_length=25)
    milk_consumption = models.CharField(max_length=25)
    potato_consumption = models.CharField(max_length=25)
    vegetable_consumption = models.CharField(max_length=25)
    rice_consumption = models.CharField(max_length=25)
    wheat_consumption = models.CharField(max_length=25)
    nuts_consumption = models.CharField(max_length=25)

    def __str__(self):
        return self.diet_type


# EnergyConsumption

class EnergyConsumption(models.Model):
    # Choices for primary energy source
    ENERGY_SOURCE_CHOICES = [
        ('electricity', 'Electricity from the grid'),
        ('solar', 'Solar power'),
        ('wind', 'Wind power'),
        ('other', 'Other (please specify)'),
    ]
    # Choices for energy-efficient usage
    EFFICIENT_USAGE_CHOICES = [
        ('always', 'Always'),
        ('often', 'Often'),
        ('occasionally', 'Occasionally'),
        ('rarely', 'Rarely'),
        ('never', 'Never'),
    ]
    # Choices for monthly consumption
    MONTHLY_CONSUMPTION_CHOICES = [
        ('<100', 'Less than 100 kWh'),
        ('100-300', '100-300 kWh'),
        ('300-500', '300-500 kWh'),
        ('>500', 'More than 500 kWh'),
    ]

    primary_source = models.CharField(
        max_length=20,
        choices=ENERGY_SOURCE_CHOICES,
        default='electricity',
    )
    energy_efficient_usage = models.CharField(
        max_length=20,
        choices=EFFICIENT_USAGE_CHOICES,
        default='always',
    )
    monthly_consumption = models.CharField(
        max_length=20,
        choices=MONTHLY_CONSUMPTION_CHOICES,
        default='<100',
    )
    other_source = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Specify other energy source if selected."
    )

    def __str__(self):
        return f"Energy Source: {self.primary_source}, Efficiency: {self.energy_efficient_usage}"




class ConsumerChoices(models.Model):
    LOCALLY_CHOICES = [
        ('Always', 'Always'),
        ('Often', 'Often'),
        ('Occasionally', 'Occasionally'),
        ('Rarely', 'Rarely'),
        ('Never', 'Never'),
    ]

    PLASTIC_CHOICES = [
        ('Always', 'Always'),
        ('Often', 'Often'),
        ('Occasionally', 'Occasionally'),
        ('Rarely', 'Rarely'),
        ('Never', 'Never'),
    ]

    CARBON_CHOICES = [
        ('Very conscious', 'Very conscious'),
        ('Somewhat conscious', 'Somewhat conscious'),
        ('Not very conscious', 'Not at all conscious'),
    ]

    buy_locally = models.CharField(max_length=20, choices=LOCALLY_CHOICES, null=True)
    reduce_plastic = models.CharField(max_length=20, choices=PLASTIC_CHOICES,null=True)
    carbon_conscious = models.CharField(max_length=20, choices=CARBON_CHOICES,null=True)

    def __str__(self):
        return f"Consumer Choices - {self.buy_locally}, {self.reduce_plastic}, {self.carbon_conscious}"



class Miscellaneous(models.Model):
    FLIGHT_CHOICES = [
        ('none', 'None'),
        ('1-2', '1-2 times'),
        ('3-5', '3-5 times'),
        ('5+', 'More than 5 times'),
    ]
    CARBON_OFFSET_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    international_flights = models.CharField(
        max_length=10,
        choices=FLIGHT_CHOICES,
        default='none',
        verbose_name="How often do you take international flights per year?"
    )
    carbon_offset = models.CharField(
        max_length=3,
        choices=CARBON_OFFSET_CHOICES,
        default='no',
        verbose_name="Do you participate in carbon offset programs or initiatives?"
    )
    additional_comments = models.TextField(
        blank=True,
        null=True,
        verbose_name="Any additional comments or practices you would like to share?"
    )