from django.db import models
from django.contrib.auth.models import User
class Hotel(models.Model):
    name=models.CharField(max_length=50,blank=True)
    location=models.CharField(max_length=100,blank=True)
    image=models.ImageField(max_length=500,blank=True,upload_to="image")
    rating=models.IntegerField()
    def __str__(self):
        return self.name
class Food(models.Model):
    food_name=models.CharField(max_length=50,blank=True)
    food_image=models.ImageField(max_length=50,upload_to="image")
    hotel_name=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    price=models.IntegerField()
    comments=models.TextField(max_length=500,blank=True)
    def __str__(self):
        return self.food_name
class Fooditem(models.Model):
    fooditem=models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    def __str__(self):
        return str(self.fooditem)
class Detail(models.Model):
    name=models.CharField(max_length=25,blank=None)
    address=models.TextField(max_length=100,blank=None)
    phone=models.IntegerField()
    email=models.EmailField()
def __str__(self):
    return self.name(str) 