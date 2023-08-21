from django import forms
from .models import Advertisement
from django.core.exceptions import ValidationError


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-lg'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control form-control-lg'
            }),
            'auction': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control form-control-lg'
            }),
        }

    def clean_title(self):
        import re
        title = self.cleaned_data['title']
        reg = r"\A[\w\d\s]+[\w\d\s\?%\$№!\(\):;\.,><=]*"
        if not re.fullmatch(reg, title):
            raise ValidationError(
                "Заголовок не может содержать такие спец. символы как: ^@#^&*_+=/\|`~ и может начинатся только с буквы или цифры."
            )
        return title



