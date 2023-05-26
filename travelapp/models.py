from django.db import models
from authentication.models import User
from multiselectfield import MultiSelectField



class City(models.Model):
    Countries = (
        ('Pakistan', 'Pakistan'),
        ('England', 'England'),
         ('India', 'India'),
        ('America', 'America'),
        # .. etc
    )
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200,choices=Countries)
    image = models.ImageField(blank=True, upload_to='images/')


    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = "Cities"



class Location(models.Model):
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.address


class Hotels(models.Model):
    hotel = models.CharField(max_length=200)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    address = models.ForeignKey(Location,on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/')


    def __str__(self):
        return self.hotel

    class Meta:
        verbose_name_plural = "Hotels"



class Destination(models.Model):
    Items = (
        ('Private Transport', 'Private Transport'),
        ('Entrance Fees', 'Entrance Fees'),
        ('Box Lunch', 'Box Lunch'),
        ('Additional Services', ' Additional Services'),
        ('Insurance', 'Insurance'),
        ('Drink', 'Drink'),
        ('Tickets', 'Tickets'),
        # .. etc
    )
    name = models.CharField(max_length=200, verbose_name=('Name'))
    slug = models.SlugField(max_length=250,verbose_name=('Slug'))
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    address = models.ForeignKey(Location,on_delete=models.CASCADE)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True, upload_to='images/')
    duration = models.IntegerField()
    tour_type = models.IntegerField()
    group = models.IntegerField()
    languages = models.CharField(max_length=200)
    overview = models.CharField(max_length=700, verbose_name=('OverView'))
    departure_time = models.DateField()
    return_time = models.DateField()
    included = MultiSelectField(max_length=200,choices=Items)
    excluded = MultiSelectField(max_length=200,choices=Items)
        
    

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)




class Book(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()


class Package(models.Model):
    Items = (
        ('Private Transport', 'Private Transport'),
        ('Entrance Fees', 'Entrance Fees'),
        ('Box Lunch', 'Box Lunch'),
        ('Additional Services', ' Additional Services'),
        ('Insurance', 'Insurance'),
        ('Drink', 'Drink'),
        ('Tickets', 'Tickets'),
        # .. etc
    )
    name = models.CharField(max_length=200, verbose_name=('Name'))
    slug = models.SlugField(max_length=250,verbose_name=('Slug'))
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    address = models.ForeignKey(Location,on_delete=models.CASCADE)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(blank=True, upload_to='images/')
    duration = models.IntegerField()
    tour_type = models.IntegerField()
    group = models.IntegerField()
    languages = models.CharField(max_length=200)
    overview = models.CharField(max_length=700, verbose_name=('OverView'))
    departure_time = models.DateField()
    return_time = models.DateField()
    included = MultiSelectField(max_length=200,choices=Items)
    excluded = MultiSelectField(max_length=200,choices=Items)


class Guides(models.Model):
    name = models.CharField(max_length=200, verbose_name=('Name'))
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    image = models.FileField(blank=True, upload_to='guide-images/')
    fb = models.CharField(max_length=400, verbose_name=(
        'Facebook Link'), blank=True,)
    insta = models.CharField(
        max_length=400, verbose_name=('Instagram Link'), blank=True,)
    twiter = models.CharField(
        max_length=400, verbose_name=('Twiter Link'), blank=True,)
    whatsapp = models.CharField(
        max_length=400, verbose_name=('Whatsapp Number'), blank=True,)


class Gallery(models.Model):
    image = models.FileField(blank=True, upload_to='gallery-images/')


class Reviews(models.Model):
    image = models.FileField(blank=True, upload_to='review-images/')
    name = models.CharField(max_length=200, verbose_name=('Name'))
    quote = models.CharField(max_length=500, verbose_name=('Quote'))
