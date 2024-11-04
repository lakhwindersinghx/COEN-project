from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os
from django.conf import settings
from django.db import models


class Package(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE ,default=None)
    destination = models.CharField(max_length=100)
    activities = models.TextField(max_length=250, default=None)
    description= models.TextField(max_length=250,default=None)
    price= models.IntegerField(default=None)
    date= models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.destination + "|" + str(self.user)




class PackageImage(models.Model):
    package = models.ForeignKey(Package, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='package_images/')
    def __str__(self):
        # return self.destination + "|" + str(self.user)
        return f"Image for {self.package.destination}"
