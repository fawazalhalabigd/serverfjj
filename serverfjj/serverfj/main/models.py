from django.db import models

# Create your models here.

class ips(models.Model):
    ip = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    red_card = models.BooleanField(null=True,blank=True) 

    def __str__(self) -> str:
        return self.ip
    

class montag(models.Model): # منتج
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    s3r = models.CharField(max_length=255)
    nshr = models.BooleanField(null=True) # انشر المنتج

    def __str__(self) -> str:
        return self.name
    
class place(models.Model):
    place_name = models.TextField()

    def __str__(self) -> str:
        return self.place_name

class Mony(models.Model):
    monyToGet = models.CharField(max_length=255,blank=True,null=True)
    Name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.Name

class employee(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    mony = models.ManyToManyField(Mony,null=True,blank=True)
    places = models.ManyToManyField(place,null=True,blank=True)


    def __str__(self) -> str:
        return self.name

class notificate(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.title

class montagOrder(models.Model): # منتج
    name = models.CharField(max_length=255)
    s3r = models.CharField(max_length=255)
    kmwahed_number = models.CharField(max_length=255)
    ip = models.OneToOneField(ips,on_delete=models.CASCADE)
    place_to_get = models.OneToOneField(place,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    