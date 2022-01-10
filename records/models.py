from django.db import models
from cpf_field.models import CPFField


# Create your models here.

class Property(models.Model):

    type_choice = (
        ('Apartment', 'Apartment'),
        ('Kitnet', 'Kitnet'),
        ('House', 'House'),
    )

    type = models.CharField(max_length=10, choices=type_choice)
    address = models.CharField(max_length=150, unique=True)
    value = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    rented = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return str(self._get_pk_val()) + ' - ' + self.type + ' | ' + self.address


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=35)

    cpf = CPFField('cpf', unique=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name


class Rent(models.Model):
    start = models.DateField()
    end = models.DateField()

    client = models.ForeignKey(Client, on_delete=models.PROTECT, null=True, blank=False)
    property = models.OneToOneField(Property, on_delete=models.PROTECT, null=True, blank=False)

    class Meta:
        verbose_name = 'Rent'
        verbose_name_plural = 'Rents'

    def __str__(self):
        return str(self._get_pk_val()) + ' - ' + self.property.type + ' | ' + self.client.name
