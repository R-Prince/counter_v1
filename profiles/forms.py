from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name',
                    'email', 'phone_number', 'company_name',
                    'company_street_address1', 'company_street_address2',
                    'company_city', 'company_county',
                    'company_postcode')


def __init__(self, *args, **kwargs):
    """ Add placeholders and classes, remove auto-generated
    labels and set autofocus on first field"""

    super().__init__(*args, **kwargs)
    placeholders = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'email': 'Email',
        'phone_number': 'Phone Number',
        'company_name': 'Company Name',
        'company_street_address1': 'Street Address 1',
        'company_street_address2': 'Street Address 2',
        'company_city': 'City',
        'company_county': 'County',
        'company_postcode': 'Postcode'
    }

    self.fields['first_name'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if self.fields[field].required:
            placeholder = f'{placeholders[field]} *'
        else:
            placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'form-input-field'
        self.fields[field].label = False
