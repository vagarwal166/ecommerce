from django.forms import ModelForm
from .models import Address

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ('mobile','address','zip_code','state','city')