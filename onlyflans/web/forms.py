from django import forms
from . import models


class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label="Correo")
    customer_name = forms.CharField(max_length=64, label="Nombre")
    message = forms.CharField(label="Mensaje")


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = models.ContactForm
        fields = ["customer_email", "customer_name", "message"]
        labels = {
            "customer_email": "Correo",
            "customer_name": "Nombre",
            "message": "Mensaje",
        }
