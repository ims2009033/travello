from django.conf import settings
from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class PC_stock(models.Model):
    serial = models.CharField(max_length=20)
    belongs_to = models.CharField(max_length=20)
    installed_at = models.CharField(max_length=15)
    dept = models.CharField(max_length=20)
    person_name = models.CharField(max_length=20)
    CC_number = models.IntegerField()
    
    
    def __str__(self):
        return self.serial


class Asset(models.Model):
    center = models.CharField(max_length=20)
    building = models.CharField(max_length=20)
    floor = models.IntegerField()
    dept = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    belongs = models.CharField(max_length=20)
    enduser = models.CharField(max_length=20)
    remarks = models.CharField(max_length=20)
    CC_number = models.IntegerField()

    def __str__(self):
        return self.center

class Infrastructure(models.Model):
    deviceName = models.CharField(max_length=20)
    hostName = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    serial = models.CharField(max_length=20)
    cpu = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)
    IPAdress = models.GenericIPAddressField(protocol='both', unique=True)
    warrantyEnd = models.DateField(auto_now=False, auto_now_add=False)
    other_comments = models.CharField(max_length=20)

    def __str__(self):
        return self.deviceName
        
#Post learninng of django girls

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title