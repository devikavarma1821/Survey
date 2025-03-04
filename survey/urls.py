from django.urls import path
from survey import views  # Make sure this line exists
from .views import user_login


urlpatterns = [
    path('register/', views.register, name='register'),  # Must match views.py function name
    path('', views.survey_home, name='survey_home'),  # Home page
    path('login/', user_login, name='login'),

    path('demographic/', views.demographic_information_view, name='demographic_information'),
    path('transportation/', views.transportation_view, name='transportation'),
    path('environmental_awareness/', views.environmental_awareness_view, name='environmental_awareness'),
    path('occupation/', views.occupation_view, name='occupation'),
    path('food_consumption/', views.food_consumption_view, name='food_consumption'),
    path('energy_consumption/', views.energy_consumption_view, name='energy_consumption'),
    path('consumer_choices/', views.consumer_choices_view, name='consumer_choices'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
]
