from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import DemographicInformation, Transportation, EnvironmentalAwareness, FoodConsumption, Miscellaneous, Occupation

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "date_joined", "is_active", "is_staff")  # Show in admin panel
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),  # Add if applicable
        ("Permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_superuser")}
        ),
    )
    search_fields = ("email",)
    list_filter = ("is_staff", "is_superuser", "is_active")

admin.site.register(CustomUser, CustomUserAdmin)

# Registering other models
admin.site.register(DemographicInformation)
admin.site.register(Transportation)
admin.site.register(EnvironmentalAwareness)
admin.site.register(FoodConsumption)
admin.site.register(Miscellaneous)
admin.site.register(Occupation)
