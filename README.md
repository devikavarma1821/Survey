# Survey

This is a Django-based survey application deployed on Render.


🔗 **Live Demo:** [Click here to visit](https://survey-rpz3.onrender.com)


# Survey-Data-Collection-System
A Django-based web application to collect and store survey data across various categories, including demographics, transportation, environmental awareness, and more. The data is securely saved in CSV files for further analysis.
📌 Features
*Collect survey responses in an organized manner.
*Multi-step form for different survey categories:
*Demographics
*Transportation
*Environmental Awareness
*Occupation
*Food Consumption
*Energy Consumption
*Consumer Choices
*CSV export for easy data storage and analysis.
*User-friendly UI and efficient backend processing.

🛠️ Technologies Used
*Python
*Django
*HTML/CSS
*Bootstrap (for styling)
*CSV Module (for data storage)


⚙️ Installation and Setup
Follow these steps to set up and run the project on your local machine:

1.Clone the Repository
git clone https://github.com/your-username/survey-data-collection.git
cd survey-data-collection

2. Set Up Virtual Environment
python -m venv env
.\env\Scripts\activate   # Windows
source env/bin/activate  # macOS/Linux

3. Install Dependencies
pip install -r requirements.txt

4.Run Migrations
python manage.py migrate

5.Start the Server
python manage.py runserver


📊 Data Flow
1.Users fill out forms for different categories.
2.Form data is validated and stored in CSV files located in the data/ folder.
3.Data is ready for further processing or analysis.

💡 How to View Saved Data
1.Navigate to the data/ directory in your project folder.
2.Open the desired CSV file using:
   Any text editor (e.g., Notepad, VS Code).
   Spreadsheet software (e.g., Excel, Google Sheets).

