from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    """
    User e'lon qo'shishi uchun form.
    """

    class Meta:
        model = Listing
        fields = [
            'category',
            'region',
            'district',
            'title',
            'price',
            'short_description',
            'description',
            'phone',
            'telegram_username',
            'google_maps_link',
            'main_image',
        ]