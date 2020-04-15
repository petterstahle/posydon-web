"""This file contains forms, which define the fields used to represent an object for uploading to a databse."""

from django import forms
import datetime


class FlowForm(forms.ModelForm):
    title   = forms.CharField(
                    label='',
                    widget=forms.TextInput(
                        attrs={
                            "placeholder": "Flow Title"
                        }
                    )
                )

    content = forms.CharField(
                    widget=forms.Textarea(
                        attrs={
                            "placeholder": "flow content (as dictionary)",

                        }
                    )
                )

    comment = forms.CharField(
                    required=False,
                    widget=forms.Textarea(
                        attrs={
                            "placeholder": "comment"
                        }
                    )
                )

    date = forms.DateField(initial=datetime.date.today)
