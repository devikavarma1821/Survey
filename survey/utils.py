import csv
import os
from django.conf import settings
from django.utils import timezone

def save_to_csv(sheet_name, data_instance):
    """
    Saves form data from a Django model instance to a single CSV file.
    """

    try:
        print(f"Saving data to CSV: {sheet_name}")  # Debugging line

        # Define file path
        file_path = os.path.join(settings.BASE_DIR, 'survey_data', 'all_survey_responses.csv')

        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Determine user identifier
        user_identifier = getattr(data_instance, 'email', "Anonymous")

        # Prepare data dictionary
        data_dict = {
            "User Identifier": user_identifier,
            "Form Name": sheet_name,
            "Timestamp": timezone.now(),
        }

        # Loop through model fields (excluding password)
        for field in data_instance._meta.fields:
            if field.name != "password":
                data_dict[field.verbose_name] = getattr(data_instance, field.name, "")

        # Open the CSV file in append mode
        file_exists = os.path.isfile(file_path)
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data_dict.keys())

            # Write headers if file is new
            if not file_exists:
                writer.writeheader()

            # Write data row
            writer.writerow(data_dict)

        print(f"Data successfully saved to {file_path}")

    except Exception as e:
        print(f"Error saving data to CSV: {e}")
