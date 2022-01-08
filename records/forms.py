from django import forms

from records.models import Client, Property, Rent


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'
