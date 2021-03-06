from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name',
                'email', 'phone_number', 'company_name',
                'company_street_address1', 'company_street_address2',
                'company_city', 'company_county',
                'company_postcode')

    list_display = ('first_name', 'last_name', 'email',
                    'phone_number', 'company_name')


admin.site.register(UserProfile, UserProfileAdmin)
