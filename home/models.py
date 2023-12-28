from django.db import models
# Create your models here.


class CarBrand(models.Model):
     brand_name=models.CharField(max_length=100)
     quantity=models.PositiveIntegerField(default=0)

     def __str__(self):
         return self.brand_name
     

class Car(models.Model):
    brand=models.ForeignKey(CarBrand,on_delete=models.CASCADE)
    car_image=models.ImageField(upload_to='car_images/')
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()

    def __str__(self):
        return self.name