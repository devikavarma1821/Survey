import csv
import os

def save_to_csv(sheet_name, data_instance):
    """
    Saves data from a Django model instance to a CSV file.

    Parameters:
    - sheet_name: The name of the sheet to save the data to (optional, could be used as a file name).
    - data_instance: The Django model instance containing the data to save.
    """
    try:
        print(f"Saving data to CSV: {sheet_name}")  # Debugging line

        # Define the path to your CSV file
        file_path = os.path.join('data', 'survey_data.csv')

        # Create the 'data' directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Prepare the data row
        row = []
        for field in data_instance._meta.fields:
            value = getattr(data_instance, field.name)
            row.append(value)

        # Open the CSV file in append mode
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write the header if the file is empty
            if file.tell() == 0:  # Check if the file is empty
                headers = [field.name for field in data_instance._meta.fields]
                writer.writerow(headers)

            # Write the data row
            writer.writerow(row)

        print(f"Data saved to {file_path}")  # Debugging line

    except Exception as e:
        print(f"Error saving data to CSV: {e}")
