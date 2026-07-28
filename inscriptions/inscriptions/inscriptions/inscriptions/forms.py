from django import forms

from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            "nom",
            "email",
            "telephone",
            "categorie",
            "ville",
            "reference_paiement",
            "motivation",
        ]
        widgets = {
            "nom": forms.TextInput(attrs={"placeholder": "ex : Aïssatou Kora"}),
            "email": forms.EmailInput(attrs={"placeholder": "nom@exemple.com"}),
            "telephone": forms.TextInput(attrs={"placeholder": "+229 xx xx xx xx"}),
            "ville": forms.TextInput(attrs={"placeholder": "ex : Natitingou"}),
            "reference_paiement": forms.TextInput(
                attrs={"placeholder": "ex : MTN.240719.1234"}
            ),
            "motivation": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Une ligne sur votre motivation à participer…"}
            ),
        }
