from django.db import models

# Create your models here.

class Property(models.Model):

    type = models.CharField(max_length=100)
    address = models.CharField(max_length=150, unique=True)
    value = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class Client(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

class Rent(models.Model):

    start = models.DateField()
    end = models.DateField()
    finished = models.BooleanField(default=False, help_text='Check')

    client = models.ForeignKey(Client, on_delete=models.PROTECT, null=True, blank=False)
    property = models.OneToOneField(Property, on_delete=models.PROTECT, null=True, blank=False)

    def __str__(self):
        return  'Contrato ' + str(self._get_pk_val()) + ': ' + self.property.type + ' - ' + self.client.name + ' | ' + self.finished


