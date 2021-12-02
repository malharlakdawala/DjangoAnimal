from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Vehicle_type(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Vehicle_size(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_type=models.ForeignKey(Vehicle_type,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True, blank=True)
    real_cost=models.IntegerField(default=1000)
    vehicle_size=models.ForeignKey(Vehicle_size,on_delete=models.CASCADE)

    def __str__(self):
        vehicle_name_size = f'{self.vehicle_type.name} {self.vehicle_size.name}'

        return vehicle_name_size


class Rental(models.Model):
    rental_date=models.DateTimeField(blank=True, null=True)
    return_date=models.DateTimeField(blank=True, null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Rental_rate(models.Model):
    daily_rate=models.IntegerField(default=100)
    vehicle_type=models.ForeignKey(Vehicle_type,on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(Vehicle_size,on_delete=models.CASCADE)

    def __int__(self):
        return self.daily_rate

