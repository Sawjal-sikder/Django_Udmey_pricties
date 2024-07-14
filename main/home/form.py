from django.forms import ModelForm, TextInput, Textarea
from .models import personModel
from django.utils.translation import gettext_lazy as _

# Create the form class.
class person(ModelForm):
    class Meta:
        model = personModel
        fields = "__all__"
        # exclude = ['last_name']
        labels = {
            "first_name": _(""),
            "last_name": _(""),
        }
        help_texts = {
            "first_name": _(""),
        }
        error_messages = {
            "first_name": {
                "max_length": _("This writer's name is too long."),
            },
            "last_name": {
                "max_length": _("This writer's name is too long."),
            },
        }
        widgets = {
            "first_name": TextInput(attrs={"class": "form-control", "placeholder": "Enter your first name" }),
            "last_name": TextInput(attrs={"class": "form-control","placeholder": "Enter your last name" }),
        }

