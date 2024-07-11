from django import forms

class person(forms.Form):
    first_name = forms.CharField(
        label="Your First Name",
        max_length=55,
        error_messages={
            "required": "First name must not be empty!",
            "max_length": "Please shorten your first name."
        }
    )
    last_name = forms.CharField(
        label="Your Last Name",
        max_length=55,
        error_messages={
            "required": "Last name must not be empty!",
            "max_length": "Please shorten your last name."
        }
    )
