# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator


class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):

    CAR_TYPE = [
        ('SEDAN', "Sedan"),
        ('SUV', "SUV"),
        ('WAGON', "Wagon"),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30)
    car_type = models.CharField(max_length=5, choices=CAR_TYPE)
    year = models.IntegerField(
        default=2024,
        validators=[MaxValueValidator(2024)]
    )
    dealer_id = models.IntegerField(default=1)

    def __str__(self):
        return self.name
