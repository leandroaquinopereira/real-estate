from django.db import models

# Create your models here.

class Property(models.Model):

    type = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    value = models.CharField(max_length=15)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class Client(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Rent(models.Model):

    start = models.DateField()
    end = models.DateField()

    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    property = models.OneToOneField(Property, on_delete=models.PROTECT)

    def __str__(self):
        return self.property.type

