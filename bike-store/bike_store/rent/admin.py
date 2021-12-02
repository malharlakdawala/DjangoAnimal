from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Vehicle_type)
admin.site.register(Vehicle_size)
admin.site.register(Vehicle)
admin.site.register(Rental)
admin.site.register(Rental_rate)
