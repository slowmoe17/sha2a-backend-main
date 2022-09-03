from django.db import models
from users.models import CustomUser




"""class PropertyImage(models.Model):
    image = models.ImageField(upload_to='property_images')
"""
class Property(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    property_types = (
        ("villa", "villa"),
        ("apartment", "apartment"),
        ("house", "house"),
        ("office", "office"),
        ("shop", "shop"),
    )

    Ad_types = (
        ("rent", "rent"),
        ("sell", "sell"),
        ("student_house", "student_house")
    )
    title = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100 ,choices=property_types, default="apartment")
    ad_type = models.CharField(max_length=50, choices=Ad_types, default="rent")
    description = models.TextField(blank=True, null=True)
    space = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    number_of_rooms = models.IntegerField(blank=True, null=True)
    # location = models.CharField(max_length=100)
    location_long = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    location_lat = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)


    def __str__(self):
        return self.title
"""    image = models.ForeignKey(PropertyImage, on_delete=models.CASCADE)
"""
    
    





class Favorite(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fav_property = models.ForeignKey(Property, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email + " " + self.property.name


  


        
