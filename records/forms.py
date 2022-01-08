from django import forms

from records.models import Client, Property, Rent


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        # fields = ['nome', 'capital']
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        # fields = ['nome', 'capital']
        fields = '__all__'


class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        # fields = ['nome', 'capital']
        fields = '__all__'
