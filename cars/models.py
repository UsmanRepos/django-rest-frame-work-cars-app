from django.db import models

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

class CarPlan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()

class Car(BaseModel):
    plan = models.ForeignKey(CarPlan, on_delete=models.SET_NULL, null=True, blank=True, related_name='plan')
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    production_year = models.DateField()
    engine_type = models.CharField(max_length=100)
    car_body = models.CharField(max_length=100)



