
# Django Car Project
A comprehensive Django project that includes two models, Car and CarPlan, and serializers for each model with field-level validators. The CarPlan model represents a plan for a car, including information about the car's features and price, while the Car model represents a specific car instance with a foreign key referencing the CarPlan model.

## Requirements
* Python 3.x
* Django 3.x
* Django Rest Framework
## Installation
1. Clone the repository <br>
``` git clone https://github.com/<username>/django-car-project.git ``` <br><br>
2. Install the required packages <br>
``` pip install -r requirements.txt ``` <br><br>
3. Run migrations <br>
``` python manage.py migrate ``` <br><br>
4. Run the development server  
``` python manage.py runserver ``` <br><br>
# Models
## CarPlan
A CarPlan represents a plan for a car and includes the following fields:
* name (CharField) - the name of the plan
* description (TextField) - a detailed description of the plan
* price (DecimalField) - the price of the plan
* features (TextField) - a list of features included in the plan
## Car
A Car represents a specific car instance and includes the following fields:
* plan (ForeignKey to CarPlan) - the plan the car belongs to
* brand (CharField) - the brand of the car
* model (CharField) - the model of the car
* production_year (DateField) - the year the car was produced
* engine_type (CharField) - the type of engine the car has
* car_body (CharField) - the body type of the car  
# Serializers
## CarPlanSerializer
The CarPlanSerializer is the serializer for the CarPlan model and includes the following fields:
* id (AutoField) - a unique identifier for the plan
* name (CharField) - the name of the plan
* description (TextField) - a detailed description of the plan
* price (DecimalField) - the price of the plan
* features (TextField) - a list of features included in the plan
## CarSerializer
The CarSerializer is the serializer for the Car model and includes the following fields:
* id (AutoField) - a unique identifier for the car
* plan (CarPlanSerializer) - the plan the car belongs to
* brand (CharField) - the brand of the car
* model (CharField) - the model of the car
* production_year (DateField) - the year the car was produced
* engine_type (CharField) - the type of engine the car has
* car_body (CharField) - the body type of the car
## Field-level validators
The project includes field-level validators to ensure that the data entered is valid. These validators check the length of the brand and model fields to ensure that they do not exceed a specified length.
## Contributing
Contributions are welcome! If you would like to contribute to this project, you can start by forking the repository



