"""This file contains forms, which define the fields used to represent an object for uploading to a databse, or simply enabling a user to input data to a page without a database."""

from django import forms


class SlurmForm(forms.Form):
    email = forms.EmailField()

    class Meta:
        fields = ('email')
